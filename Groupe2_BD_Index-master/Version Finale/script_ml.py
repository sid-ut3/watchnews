#from flask_mysqldb import MySQL
import json
import pandas as pd
import mysql.connector
import MySQLdb
import glob
import  os


def label(data, cursor):
	for article in data :
		
		id_article = article['id_article']

 
		list_label = article['label']
		list_strongest_label = article['strongest_label']

		for i in range(len(list_label)):
			strongest_label = list_strongest_label[i]
			label = list_label[i]
			
			try : 
				call_pbelong(cursor, id_article, label, strongest_label)
			except :
				print('Unable to insert label')

	query = "COMMIT;"
	cursor.execute(query)

def call_pbelong(cursor ,id_article, label, strongest_label):
	query = "CALL PBELONG('" + id_article +"','"+ label +"',"+ str(strongest_label) + ");"
	cursor.execute(query)


cwd = os.getcwd()

# MySQL configurations
servername = "localhost"
username = "root"
passwordDB = "sidiots"
databasename = "Index"

cnx = mysql.connector.connect(user=username, password=passwordDB,host= servername, database=databasename)

cursor = cnx.cursor()

cwd = os.getcwd()

for file in glob.glob(cwd + "/ml_json/*.json"):
	
	data = open(file).read()
	data = json.loads(data)
	label(data, cursor)