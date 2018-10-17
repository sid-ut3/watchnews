import json
import pandas as pd
import mysql.connector
import MySQLdb
import glob
import  os


def semantic(article, cursor):

	id_article = article['article']['id_art']
	
	rate_positivity = str(article['article']['rate_positivity'])
	
	rate_negativity = str(article['article']['rate_negativity'])

	rate_joy = str(article['article']['rate_joy'])

	rate_fear = str(article['article']['rate_fear'])

	rate_sadness = str(article['article']['rate_sadness'])

	rate_angry = str(article['article']['rate_angry'])

	rate_surprise = str(article['article']['rate_surprise'])

	rate_disgust = str(article['article']['rate_disgust'])

	rate_subjectivity = str(article['article']['rate_subjectivity'])

	is_positive = str(article['article']['is_positive'])
	try : 
		call_psemantic_article(cursor, id_article,rate_positivity,rate_negativity, rate_joy, rate_fear, rate_sadness, rate_angry, rate_surprise, rate_disgust, rate_subjectivity, is_positive)
	except: 
		print('Unable to update article')
	
	for position_word in article['position_word'] : 

		position = str(position_word['position'])
		file_wiki = str(position_word['file_wiki'])
		word = str(position_word['word'])
		
		list_synonym = position_word['synonym']

		try :
			call_psemantic_pword(cursor, id_article, position, word, file_wiki)
		except : 
			print('Unable to update position word')

	query = "COMMIT;"
	cursor.execute(query)

def call_psemantic_article(cursor, id_article,rate_positivity,rate_negativity,rate_joy,rate_fear,rate_sadness,rate_angry,rate_surprise,rate_disgust,rate_subjectivity,is_positive):
	query = "CALL SEMANTIC_PARTICLE('" + id_article  + "'," + rate_positivity  + "," + rate_negativity  + "," + rate_joy  + "," +  rate_fear  + "," +  rate_sadness  + "," + rate_angry  + "," + rate_surprise  + "," +  rate_disgust  + "," +  rate_subjectivity  + "," +  is_positive + ");"
	cursor.execute(query)
	


def call_psemantic_pword(cursor, id_article, position, word, file_wiki):
	query = "CALL SEMANTIC_PWORD('" + id_article + "'," + position + ",'" + word + "','" + file_wiki + "');"
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

for file in glob.glob(cwd + "/semantic_json/*.json"):
	
	data = open(file).read()
	data = json.loads(data)
	semantic(data, cursor)

	