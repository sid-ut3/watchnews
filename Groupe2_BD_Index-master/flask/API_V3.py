##### GROUP 3 - Version 1.0 #####
from flask import Flask, request, jsonify
import json
import requests
from flask_restful import Resource, Api
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb
from flask_compress import Compress
import pandas as pd


#compress = Compress()
app = Flask(__name__) # we are using this variable to use the flask microframework
#compress.init_app(app)
api = Api(app)

# MySQL configurations
servername = "localhost"
username = "root"
passwordDB = "sidiots"
databasename = "index"

db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)

@app.route("/filtering/", strict_slashes = False, methods = ['POST'])
def filtering():
	data = request.get_json()

	#df = data, orient='records')
	#df.to_json(orient='table')
	df = pd.DataFrame(data[0]['position_word'])
	df['id_lemma'] = df['lemma'].apply(lambda x: query_id_lemma(x))
	df['id_word'] = df['word'].apply(lambda x: query_id_word(x))
	
	print(df)


	"""
	for article in data :
		date_publication = article['article']['date_publication']
		list_surname_author = article['article']['surname_author']
		name_newspaper = article['article']['name_newspaper']
		try : 
			id_article = call_pfiltering_article(date_publication, name_newspaper)
		except : 
			print('Unable to insert article')
			id_article = 0

		for surname_author in list_surname_author:
			try : 
				call_pauthor(id_article, surname_author)
			except : 
				print('Author alerady exist.')

		for position_word in article['position_word'] : 
			lemma = position_word['lemma']
			type_entity = position_word['type_entity']
			pos_tag = position_word['pos_tag']
			title = position_word['title']
			position = position_word['position']
			word = position_word['word']
			
			try : 
				call_pfiltering_position_word(position, word, lemma, title, pos_tag, type_entity, id_article)
			except: 
				print('Unable to insert word')
			

	result = json.dumps([[{"message":{"id_article" : id_article}}]])

	"""
	return 'ok'

def query_id_word(word, id_lemma):
	try :
		query = "select id_word from word where word = '" + word + "'"
		cursor = db.cursor()
		cursor.execute(query)
		id_word = cursor.fetchall()[0][0]
	except :
		query = "Insert into word (word, id_lemma) values ('" + word + "'," + str(id_lemma) + ");"
		cursor = db.cursor()
		cursor.execute(query)
		id_word = 0
	
	return id_word

def query_id_lemma(lemma):
	try :
		query = "select id_lemma from lemma where lemma = '" + lemma + "'"
		cursor = db.cursor()
		cursor.execute(query)
		id_lemma = cursor.fetchall()[0][0]
	
	except :
		
		id_lemma = 0
	
	return id_lemma



def call_pfiltering_article(date_publication, name_newspaper):
	query = "CALL FILTERING_PARTICLE('" + date_publication + "','" + name_newspaper + "',@vid_article);"
	cursor = db.cursor()
	cursor.execute(query)

	query = "SELECT @vid_article as id_article;"
	cursor = db.cursor()
	cursor.execute(query)
	id_article = cursor.fetchall()[0][0]

	return id_article



def call_pfiltering_position_word(position, word, lemma, title, pos_tag, type_entity, id_article):
	query = "CALL FILTERING_PPOSITION_WORD(" + str(position) + ",'" + word + "','" + lemma + "',"  + str(title) + ",'" + pos_tag + "','" + type_entity  + "'," + str(id_article) + ");"
	cursor = db.cursor()
	cursor.execute(query)

def call_pauthor(id_article, surname_author):
	query = "CALL FILTERING_PAUTHOR(" + str(id_article) + ",'" + surname_author + "');"
	cursor = db.cursor()
	cursor.execute(query)



@app.route("/semantic/", strict_slashes = False, methods = ['PATCH'])
def semantic():
	data = request.get_json()
	for article in data :
		
		id_article = str(article['article']['id_article'])
		
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
			call_psemantic_article(id_article,rate_positivity,rate_negativity, rate_joy, rate_fear, rate_sadness, rate_angry, rate_surprise, rate_disgust, rate_subjectivity, is_positive)
		except: 
			print('Article is missing.')

		for position_word in article['position_word'] : 
	
			position = str(position_word['position'])
			file_wiki = str(position_word['file_wiki'])
			word = str(position_word['word'])
			
			list_synonym = position_word['synonym']

			try :
				call_psemantic_pword(id_article, position, word, file_wiki)
			except : 
				print('Unable to update position word')

			#To do update if synonym needed :
			if isinstance(list_synonym, list):
				for synonym in list_synonym : 
					try : 
						call_psemantic_psynonym(id_article, position, synonym)
					except : 
						print(print("Unable to insert synonym {}".format(synonym)))
			else : 
				try : 
					call_psemantic_psynonym(id_article, position, list_synonym)
				except : 
					print("Unable to insert synonym {}".format(list_synonym))
	return '' 

def call_psemantic_article(id_article,rate_positivity,rate_negativity,rate_joy,rate_fear,rate_sadness,rate_angry,rate_surprise,rate_disgust,rate_subjectivity,is_positive):
	query = "CALL SEMANTIC_PARTICLE(" + id_article  + "," + rate_positivity  + "," + rate_negativity  + "," + rate_joy  + "," +  rate_fear  + "," +  rate_sadness  + "," + rate_angry  + "," + rate_surprise  + "," +  rate_disgust  + "," +  rate_subjectivity  + "," +  is_positive + ");"
	cursor = db.cursor()
	print(cursor.execute(query))


def call_psemantic_pword(id_article, position, word, file_wiki):
	query = "CALL SEMANTIC_PWORD(" + id_article + "," + position + ",'" + word + "','" + file_wiki + "');"
	print(query)
	cursor = db.cursor()
	print(cursor.execute(query))

def call_psemantic_psynonym(id_article, position, synonym):
	query = "CALL SEMANTIC_PSYNONYM(" + id_article + "," + position + ",'" + synonym +"');"
	print(query)
	cursor = db.cursor()
	print(cursor.execute(query))

@app.route("/label/", strict_slashes = False, methods = ['POST'])
def label():
	data = request.get_json()
	for article in data :
		id_article = str(article['id_article'])
		list_label = article['label']
		list_strongest_label = article['strongest_label']

		for i in range(len(list_label)):
			strongest_label = str(list_strongest_label[i])
			label = list_label[i]
			try : 
				call_pbelong(id_article, label, strongest_label)
			except :
				print('Unable to insert label')

	return ''


def call_pbelong(id_article, label, strongest_label):
	query = "CALL PBELONG(" + id_article +",'"+ label +"',"+ strongest_label + ");"
	print(query)
	cursor = db.cursor()
	print(cursor.execute(query))

if __name__ == '__main__':
	app.run(host="localhost", port = 5005, debug = True)
