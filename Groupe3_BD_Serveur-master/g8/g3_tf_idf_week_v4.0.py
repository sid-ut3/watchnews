"""
g3
@Author : L.B.C.G.M.I
"""
import MySQLdb
from datetime import datetime, timedelta
import timestring
from flask import Flask, request, jsonify
import json
import requests
from flask_restful import Resource, Api
import mysql.connector
from flask_mysqldb import MySQL

# we are using this variable to use the flask microframework
app = Flask(__name__)
api = Api(app)
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
    input : /
    output : json data
    this function returns a json data formated the way Stats wanted it
    """
    #word = "décision"
    counter = execute_query("""SELECT count(mv_tf_idf.id_lemma) from word,
                            mv_tf_idf 
                        where word.id_lemma = mv_tf_idf.id_lemma 
                        and word = %s """  % ("'" + word + "'"))
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
                """ % (lemma_id_res, list_article[article], "'"
                 + str(day_query) + "'")
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
        return None
#json = jsonify(week)
#return json


@app.route("/link_by_source/", methods=['GET', 'POST'])
def tf_idf_label(name_label):
    date_min_res = execute_query("""SELECT DATE_ADD(CURRENT_DATE,
                                                   INTERVAL -14 DAY) """)
    date_max_res = execute_query("""SELECT CURRENT_DATE """)
    date_max_res = str(date_max_res[0][0])
    date_min_res = str(date_min_res[0][0])
    query_word = """SELECT w.word
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
        words,tf_idf =  tf_idf_word(word)
        res[words[0]] = tf_idf
    return res


def tf_idf_tagging(pos_tagging):
    date_min_res = execute_query("""SELECT DATE_ADD(CURRENT_DATE,
                                                   INTERVAL -14 DAY) """)
    date_max_res = execute_query("""SELECT CURRENT_DATE """)
    date_max_res = str(date_max_res[0][0])
    date_min_res = str(date_min_res[0][0])
    query_word = """SELECT w.word
    FROM word w , position_word pw, article a, pos_tagging pt
    WHERE a.date_publication BETWEEN %s AND %s
    AND a.id_article = pw.id_article
    AND pw.id_word = w.id_word AND pw.id_pos_tag = pt.id_pos_tag
    AND pt.pos_tag = %s
    ORDER BY w.id_word;
    """ % ("'" + date_min_res + "'", "'" + date_max_res + "'", 
    "'" + pos_tagging + "'")
    word_res = execute_query(query_word)
    word_id_res = []
    for i in range(len(word_res)):
        word_id_res.append(str(word_res[i][0]))
   # word_id_res = ["décision"]
    res = {}
    for word in word_id_res:
        words,tf_idf =  tf_idf_word(word)
        res[words[0] + "_type"] = pos_tagging
        res[words[0]] = tf_idf
    return res
    
def tf_idf_word_week():
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
        words,tf_idf =  tf_idf_word(word)
        res[words[0]] = tf_idf
    return res



