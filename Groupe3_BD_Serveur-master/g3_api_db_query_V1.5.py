from flask import Flask, jsonify
import MySQLdb

"""
##### GROUP 3 - Version 1.0 - RY/RV/MC/CR/EM : Creation des requetes #####
##### GROUP 3 - Version 1.1 - MC/CR : modification des requetes #####
##### GROUP 3 - Version 1.2 - MC/CR : Ajout des commentaires #####
##### GROUP 3 - Version 1.3 - MC/CR/EM : Ajout de requetes #####
##### GROUP 3 - Version 1.4 - MC : Norme de codage pep8 #####
##### GROUP 3 - Version 1.5 - EM/CR : Création et modifications des requetes ##
"""
"""
from flask import Flask, request, jsonify
import json
import requests
from flask_restful import Resource, Api
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb
"""

app = Flask(__name__)

# MySQL configurations
servername = "localhost"
username = "DBIndex_user"
passwordDB = "password_DBIndex_user"
databasename = "DBIndex"

database_configuration = MySQLdb.connect(user=username, passwd=passwordDB,
                                         host=servername, db=databasename)


def to_json(keys, values):
    """
    input : keys = list of keys for the json file
            values = values related to the keys
    output : json file

    This function create a json file in a predefined format (for G9)
    """
    dictionary_final = dict()
    for i in range(len(values)):
        dictionary = dict()
        for j in range(len(values[i])):
            dictionary[keys[j]] = values[i][j]
            dictionary_final[str(i+1)] = dictionary
    json_file = jsonify(dictionary_final)
    return json_file


def execute_query(query):
    """
    input : the query
    output : dict object (we have to turn it into a json object with the
             "to_json" function)

    Task Automation (creating a cursor, execute the query, return the result)
    """
    cursor = database_configuration.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


# Accueil
# query 1
# query 2
@app.route("/best_label_week/", strict_slashes=False, methods=['GET', 'POST'])
def api_best_label_week():
    """
    input :
    output : json_file

    Topic of the week label : percentage + label treated
    """
    query = """
        SELECT la.label, ((count(a.id_article) / (SELECT count(id_article)
        FROM article))*100)
        FROM article a, belong b, label la
        WHERE b.id_label = la.id_label
        AND b.id_article = a.id_article
        AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
        ORDER BY 2 DESC LIMIT 1;"""
    result = execute_query(query)
    floatify = [(row[0], float(row[1])) for row in result]
    result = tuple(floatify)
    print(result)
    keys = ['label', 'ratio_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# query 3
@app.route("/top_3_rate_feeling/", strict_slashes=False,
           methods=['GET', 'POST'])
def api_top_3_rate_feeling():
    """
    input :
    output : return a json file

    Top 3 most represented feelings: percentage + feelings
    """
    query = """
        SELECT feeling, rate
        FROM (
            SELECT 'joy' AS feeling,AVG(rate_joy) AS rate
            FROM article
            WHERE date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
            UNION
            SELECT 'fear' AS feeling,AVG(rate_fear) AS rate
            FROM article
            WHERE date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
            UNION
            SELECT 'sadness' AS feeling,AVG(rate_sadness) AS rate
            FROM article
            WHERE date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
            UNION
            SELECT 'angry' AS feeling,AVG(rate_angry) AS rate
            FROM article
            WHERE date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
            UNION
            SELECT 'surprise' AS feeling,AVG(rate_joy) AS rate
            FROM article
            WHERE date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
            UNION
            SELECT 'disgust' AS feeling,AVG(rate_disgust) AS rate
            FROM article
            WHERE date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
            UNION
            SELECT 'subjectivity' AS feeling,AVG(rate_subjectivity) AS rate
            FROM article
            WHERE date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
            ) as feels
        ORDER BY 2 DESC LIMIT 3;"""
    result = execute_query(query)
    keys = ['feeling', 'rate']
    json_return = to_json(keys, result)

    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# query 4
@app.route("/newspaper_by_article/", strict_slashes=False,
           methods=['GET', 'POST'])
def api_newspaper_by_article():
    """
    input :
    output : json_file

    All newspapers ordered in the descending order by number of items
    """
    query = """
        SELECT n.name_newspaper, count(a.id_article) AS number_article
        FROM article a, newspaper n
        WHERE a.id_newspaper = n.id_newspaper
        AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
        GROUP BY n.name_newspaper
        ORDER BY number_article DESC;"""
    result = execute_query(query)
    keys = ['newspaper', 'number_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# Theme
# query 1
@app.route("/newspaper_by_label/", strict_slashes=False,
           methods=['GET', 'POST'])
def api_newspaper_by_label():
    """
    input :
    output : json_file

    Numbers of items sorted by ascending order-monolabel
    """
    query = """
        SELECT l.label, count(a.id_article) as number_article
        FROM article a, label l, belong b
        WHERE a.id_article = b.id_article
        AND b.id_label = l.id_label
        AND b.strongest_label = 1
        AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
        ORDER BY number_article ASC;"""
    result = execute_query(query)
    keys = ['label', 'number_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# Recherche
# query 1
@app.route(
    "/article_per_day/<string:vWord>/<string:vDateStart>/<string:vDateEnd>/",
    strict_slashes=False, methods=['GET', 'POST'])
def api_article_per_day(vWord, vDateStart, vDateEnd):
    """
    input :
    output : json_file

    number of items for a specified keyword
    """
    query = """
        SELECT a.date_publication, count(a.id_article)
        FROM article a, word w, position_word pw
        WHERE w.id_word = pw.id_word
        AND pw.id_article = a.id_article
        AND w.word = '"""+vWord+"""'
        AND a.date_publication BETWEEN '"""+vDateStart+"""' AND '"""+vDateEnd+"""'
        GROUP BY a.date_publication;"""
    result = execute_query(query)
    keys = ['date', 'number_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# query 2
@app.route("/article_per_day_source/<string:vWord>/<string:vDateStart>/"
           + "<string:vDateEnd>/",
           strict_slashes=False, methods=['GET', 'POST'])
def api_article_per_day_source(vWord, vDateStart, vDateEnd):
    """
    input :
    output : json_file

    Number of article by newspaper for a specified keyword
    """
    query = """
       SELECT a.date_publication, n.name_newspaper, count(DISTINCT(a.id_article))
       FROM article a, word w, position_word pw, newspaper n
       WHERE w.id_word = pw.id_word
       AND pw.id_article = a.id_article
       AND w.word = '"""+vWord+"""'
       AND a.date_publication BETWEEN '"""+vDateStart+"""' AND '"""+vDateEnd+"""'
       AND a.id_newspaper = n.id_newspaper
       GROUP BY a.date_publication, n.name_newspaper;"""
    result = execute_query(query)
    keys = ['date', 'newspaper', 'number_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# query 3
@app.route("/article_per_source/<string:vWord>/<string:vDateStart>/"
           + "<string:vDateEnd>/",
           strict_slashes=False, methods=['GET', 'POST'])
def api_article_per_source(vWord, vDateStart, vDateEnd):
    """
    input :
    output : json_file

    By newspaper, the number of article for a specified keyword
    """
    query = """
       SELECT n.name_newspaper, count(DISTINCT (a.id_article))
       FROM article a, word w, position_word pw, newspaper n
       WHERE w.id_word = pw.id_word
       AND pw.id_article = a.id_article
       AND a.id_newspaper = n.id_newspaper
       AND w.word = '"""+vWord+"""'
       AND a.date_publication BETWEEN '"""+vDateStart+"""' AND '"""+vDateEnd+"""'
       GROUP BY n.name_newspaper;"""
    result = execute_query(query)
    keys = ['newspaper', 'number_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# query 4
@app.route("/article_per_day_label/<string:vWord>/<string:vDateStart>/"
           + "<string:vDateEnd>/",
           strict_slashes=False, methods=['GET', 'POST'])
def api_article_per_day_label(vWord, vDateStart, vDateEnd):
    """
    input :
    output : json_file

    Number of article by label for a specified keyword
    """
    query = """
       SELECT a.date_publication, l.label, count(DISTINCT(a.id_article))
       FROM article a, word w, position_word pw, label l, belong b
       WHERE w.id_word = pw.id_word
       AND pw.id_article = a.id_article
       AND w.word = '"""+vWord+"""'
       AND a.date_publication BETWEEN '"""+vDateStart+"""' AND '"""+vDateEnd+"""'
       AND a.id_article = b.id_article
       AND b.id_label = l.id_label
       GROUP BY 1, 2;"""
    result = execute_query(query)
    keys = ['date', 'label', 'number_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# query 5  #  /2014-01-01/2019-01-01
@app.route("/article_per_label/<string:vWord>/<string:vDateStart>/"
           + "<string:vDateEnd>/",
           strict_slashes=False, methods=['GET', 'POST'])
def api_article_per_label(vWord, vDateStart, vDateEnd):
    """
    input :
    output : json_file

    By label, the number of article for a specified keyword
    """
    query = """
       SELECT l.label, count(DISTINCT(a.id_article))
       FROM article a, word w, position_word pw, label l, belong b
       WHERE w.id_word = pw.id_word
       AND pw.id_article = a.id_article
       AND w.word = '"""+vWord+"""'
       AND a.date_publication BETWEEN '"""+vDateStart+"""' AND '"""+vDateEnd+"""'
       AND a.id_article = b.id_article
       AND b.id_label = l.id_label
       GROUP BY 1;"""
    result = execute_query(query)
    keys = ['label', 'number_article']
    json_return = to_json(keys, result)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


# query 6
@app.route("/found_word/<string:vWord>",
           strict_slashes=False, methods=['GET', 'POST'])
def api_found_word(vWord):
    """
    input :
    output : json file

    Return a wiki link if the word is an entity, otherwise return a synonym
    """
    json_return = {}
    query_word = """
        SELECT w.id_word
        FROM position_word pw, word w
        WHERE w.id_word = pw.id_word
        AND w.word = '"""+str(vWord)+"""';"""
    vId_word = execute_query(query_word)

    if vId_word == ():
        json_return = {}
        json_return = jsonify(json_return)
        json_return.status_code = 200
        json_return.headers.add('Access-Control-Allow-Origin', '*')
        json_return.headers.add('allow_redirects', True)
        return json_return

    query_entity = """
        SELECT id_entity
        FROM position_word
        WHERE id_word = """+str(vId_word[0][0])+""";
        """

    query_wiki_link = """
        SELECT file_wiki
        FROM wiki wk, position_word pw, word w
        WHERE pw.id_word = """+str(vId_word[0][0])+"""
        AND pw.id_wiki = wk.id_wiki;
      """

    # query_synonym = """
    # SELECT s.synonym
    # FROM synonym s, common c, position_word pw
    # WHERE pw.id_word = '"""+str(vId_word[0][0])+"""'
    # AND c.position = pw.position
    # AND s.id_synonym = c.id_synonym;
    # """

    vId_entity = execute_query(query_entity)

    if vId_entity[0][0] is not None:
        json_return['wiki'] = execute_query(query_wiki_link)
    else:
        json_return['wiki'] = None
    json_return = jsonify(json_return)
    json_return.status_code = 200
    json_return.headers.add('Access-Control-Allow-Origin', '*')
    json_return.headers.add('allow_redirects', True)
    return json_return


if __name__ == '__main__':
    app.run(host="130.120.8.250", port=5007, debug=True)
