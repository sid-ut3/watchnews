#from flask_mysqldb import MySQL
import json
import pandas as pd
import mysql.connector
import MySQLdb
import glob
import  os


def tf_idf(data, cursor):
    for article in data :
        id_article = article['id_article']
        lemma = article['lemma']
        tf_idf = article['tf_idf']
    
    try:
        call_update_tf_idf (cursor, id_article, lemma, tf_idf)
    except: 
        print('Unable to update tf_idf')
          
    query = "COMMIT;"
    cursor.execute(query)

    

def call_update_tf_idf(cursor, id_article, lemma, tf_idf):
    query = "CALL update_mv_tf_idf ('" + id_article+ "','" + lemma + "', '" + tf_idf + "');"
    cursor.execute(query)


cwd = os.getcwd()

# MySQL configurations
servername = "localhost"
username = "root"
passwordDB = "sidiots"
databasename = "Index"

cnx = mysql.connector.connect(user=username, password=passwordDB,host= servername, database=databasename)

#db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
cursor = cnx.cursor()

cwd = os.getcwd()

for file in glob.glob(cwd + "/filtrage_json/*.json"):
    
    data = open(file).read()
    data = json.loads(data)
    tf_idf(data, cursor)





    