"""
g3
@Author : L.B.C.G.
"""
import MySQLdb
from datetime import datetime, timedelta
from flask import Flask, jsonify
import json
import requests


# we are using this variable to use the flask microframework
app = Flask(__name__)

# MySQL configurations
servername = "localhost"
username = "DBIndex_user"
passwordDB = "password_DBIndex_user"
databasename = "DBIndex"
db = MySQLdb.connect(user=username, password=passwordDB,
                     host=servername, db=databasename)


def execute_query(query):
    """
    input : query
    output : result of the query
    this function execute the query from the data base
    """
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def tf_idf_word(word):
    """
    input : word (String)
    output : 2 lists
    this function returns 2 lists: one of the word and one of the tf_idf
    we use it in other functions to give the tf_idf for one word
    """

    counter = execute_query("""SELECT count(mv_tf_idf.id_lemma) from word,
                            mv_tf_idf
                        where word.id_lemma = mv_tf_idf.id_lemma
                        and word = %s """ % ("'" + word + "'"))
    if (counter[0][0] != 0):
        date_min_res = execute_query("""SELECT DATE_ADD(CURRENT_DATE,
                                                        INTERVAL -14 DAY) """)
        date_max_res = execute_query("""SELECT CURRENT_DATE """)
        date_max_res = str(date_max_res[0][0])
        date_min_res = str(date_min_res[0][0])
        query_lemma_id = """SELECT id_lemma FROM word WHERE word = %s
        """ % ("'" + word + "'")
        lemma_id_res = execute_query(query_lemma_id)
        lemma_id_res = str(lemma_id_res[0][0])
        week_words_tf_idf = []
        list_week = []
        for day in range(14):
            day_query = datetime.strptime(date_min_res, "%Y-%m-%d") \
             + timedelta(days=day)
            list_article = []
            id_article = """SELECT mv.id_article
            FROM mv_tf_idf mv ,article a
            WHERE a.date_publication = %s AND a.id_article = mv.id_article
            AND id_lemma = %s ORDER BY id_article;
            """ % ("'" + str(day_query) + "'", lemma_id_res)
            id_article_res = execute_query(id_article)
            list_tf_idf = []
            for article in range(0, len(id_article_res)):
                list_article.append(id_article_res[article][0])
                query_tf_idf = """SELECT mv.tf_idf
                FROM mv_tf_idf mv, article a
                WHERE mv.id_lemma = %s AND mv.id_article = %s
                AND a.date_publication = %s AND mv.id_article = a.id_article;
                """ % (lemma_id_res, list_article[article],
                       "'" + str(day_query) + "'")
                tf_idf_res = execute_query(query_tf_idf)
                tf_idf = []
                for j in range(0, len(tf_idf_res)):
                    tf_idf.append(tf_idf_res[j][0])
                list_tf_idf.append(tf_idf[0])
            week_words_tf_idf.append(list_tf_idf)
            list_week.append(list_article)
        words = [str(word)]
        return words, week_words_tf_idf
    else:
        return None, None


@app.route("/link_by_label/<string:name_label>", methods=['GET', 'POST'])
def tf_idf_label(name_label):
    """ input : label name (string)
   output : dictionnary
   this function gives the tf_idf for each word of the label given
   """
    date_min_res = execute_query("""SELECT DATE_ADD(CURRENT_DATE,
                                                   INTERVAL -14 DAY) """)
    date_max_res = execute_query("""SELECT CURRENT_DATE """)
    date_max_res = str(date_max_res[0][0])
    date_min_res = str(date_min_res[0][0])
    query_word = """
        SELECT w.word
        FROM word w , position_word pw, article a, belong b, label l
        WHERE a.date_publication BETWEEN %s AND %s
        AND a.id_article = pw.id_article
        AND pw.id_word = w.id_word AND a.id_article = b.id_article
        AND b.id_label = l.id_label AND l.label = %s
        ORDER BY w.id_word;
        """ % ("'" + date_min_res + "'", "'" + date_max_res + "'",
               "'" + name_label + "'")
    word_res = execute_query(query_word)
    word_id_res = []
    for i in range(len(word_res)):
        word_id_res.append(str(word_res[i][0]))
    res = {}
    for word in word_id_res:
        words, tf_idf = tf_idf_word(word)
        res[words[0]] = tf_idf
    js = json.dumps(res)
    headers = {'Content-Type': 'application/json'}
    repo = requests.post('http://130.120.8.250:5002/dynamic_week_label/',
                         headers=headers, data=js)
    result = jsonify(repo.json())
    return result


@app.route("/link_by_word/", methods=['GET', 'POST'])
def tf_idf_word_week():
    """input : /
   output : dictionnary
   this function gives thes words of the week and the tf_idf for each word
   """
    date_min_res = execute_query("""SELECT DATE_ADD(CURRENT_DATE,
                                                   INTERVAL -14 DAY) """)
    date_max_res = execute_query("""SELECT CURRENT_DATE """)
    date_max_res = str(date_max_res[0][0])
    date_min_res = str(date_min_res[0][0])
    query_word = """SELECT DISTINCT(w.word)
    FROM word w, article a, position_word pw
    WHERE w.id_word = pw.id_word AND pw.id_article = a.id_article
          AND a.date_publication BETWEEN %s AND %s
    """ % ("'" + date_min_res + "'", "'" + date_max_res + "'")
    word_week_res = execute_query(query_word)
    word_week_id_res = []
    for i in range(len(word_week_res)):
        word_week_id_res.append(str(word_week_res[i][0]))
    res = {}
    for word in word_week_id_res:
        words, tf_idf = tf_idf_word(word)
        if (words is not None):
            res[words[0]] = tf_idf
    js = json.dumps(res)
    print(res)
    headers = {'Content-Type': 'application/json'}
    repo = requests.post('http://130.120.8.250:5002/static_week/',
                         headers=headers, data=js)
    res = jsonify(repo.json())
    return res
    

@app.route("/link_by_tagging/", methods=['GET', 'POST'])
def tf_idf_tagging_all():
    date_min_res = execute_query("""SELECT DATE_ADD(CURRENT_DATE,
                                                   INTERVAL -14 DAY) """)
    date_max_res = execute_query("""SELECT CURRENT_DATE """)
    date_max_res = str(date_max_res[0][0])
    date_min_res = str(date_min_res[0][0])
    query_word = """SELECT w.word, pt.pos_tag
    FROM word w, article a, position_word pw, pos_tagging pt
    WHERE w.id_word = pw.id_word AND pw.id_article = a.id_article
          AND pt.id_pos_tag = pw.id_pos_tag
          AND a.date_publication BETWEEN %s AND %s
    """ % ("'" + date_min_res + "'", "'" + date_max_res + "'")
    pos_tag_week_res = execute_query(query_word)
    pos_tag_week_id_res = []
    for i in range(len(pos_tag_week_res)):
        pos_tag_week_id_res.append(str(pos_tag_week_res[i][0]))
    res = {}
    for word, pos_tag in pos_tag_week_res:
        words, tf_idf = tf_idf_word(word)
        if (words is not None):
            res[words[0] + "_type"] = pos_tag
            res[words[0]] = tf_idf
    # res = {"tweeter_type": "ADJ", "tweeter": [[], [0.8], [], [], [], [], [], [], [], [], [], [], [], []], "decision_type": "VERB", "decision": [[], [], [], [], [], [], [0.55], [], [], [], [], [], [], []], "elu_type": "PROPER_NOUN", "elu": [[], [], [], [], [], [], [0.23], [], [], [], [], [], [], []]}
    # res = {"oto": "toto"}
    js = json.dumps(res)
    print(res)
    headers = {'Content-Type': 'application/json'}
    repo = requests.post('http://130.120.8.250:5002/dynamic_week_label/',
                         headers=headers, data=js)
    res = jsonify(repo.json())
    return res


if __name__ == '__main__':
    app.run(host="130.120.8.250", port=5003, debug=True)
