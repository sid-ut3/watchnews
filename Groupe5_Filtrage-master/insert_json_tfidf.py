
#from flask_mysqldb import MySQL
import json
import pandas as pd
import mysql.connector
import MySQLdb
import glob
import  os

path_post_tf_target = '/var/www/html/projet2018/data/clean/temporary_filtering/post_tfidf'

def tf_idf(data, cursor):
    for article in data :
        
        id_article = article['id_hash']
        lemma = article['lemma']
        tf_idf = article['tf_idf']
    
        try:
            call_update_tf_idf (cursor, id_article, lemma, tf_idf)
        except: 
            print('Unable to update tf_idf')
              
        query = "COMMIT;"
        cursor.execute(query)

    

def call_update_tf_idf(cursor, id_article, lemma, tf_idf):
    query = "CALL update_mv_tf_idf ('" + id_article+ "','" + lemma + "'," + str(tf_idf) + ");"
    #print(query)
    cursor.execute(query)

# MySQL configurations
servername = "127.0.0.1"
username = "root"
passwordDB = "interpromo2018"
databasename = "DBIndex"

cnx = mysql.connector.connect(user=username, password=passwordDB,host= servername, database=databasename)
cursor = cnx.cursor()

try:
    for file in os.listdir(path_post_tf_target):
        data = open(path_post_tf_target + '/' + file).read()
        data = json.loads(data)
        tf_idf(data, cursor)
except:
    print('Insertion of data in tf-idf db stopped')


    
    
