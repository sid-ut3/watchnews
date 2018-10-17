#from flask_mysqldb import MySQL
import json
import pandas as pd
import mysql.connector
import MySQLdb
import glob
import  os


def filtering(data, cursor):
	for article in data :
		date_publication = article['article']['date_publication']
		list_surname_author = article['article']['surname_author']
		name_newspaper = article['article']['name_newspaper']
		id_article = article['id_art']

		try : 
			call_pfiltering_article(cursor, date_publication, name_newspaper, id_article)
		except : 
			print('Unable to insert article')

		for surname_author in list_surname_author:
			
			try : 
				call_pauthor(id_article, surname_author)
			except :  
				print('Unable to insert author')

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
			
	query = "COMMIT;"
	cursor.execute(query)



def call_pfiltering_article(cursor, date_publication, name_newspaper, id_article):
	query = "CALL FILTERING_PARTICLE('" + date_publication + "','" + name_newspaper + "','" + id_article + "');"
	cursor.execute(query)
	#print(query)
	
def call_pfiltering_position_word(position, word, lemma, title, pos_tag, type_entity, id_article):
	query = "CALL FILTERING_PPOSITION_WORD(" + str(position) + ",'" + word + "','" + lemma + "',"  + str(title) + ",'" + pos_tag + "','" + type_entity  + "','" + id_article + "');"
	cursor.execute(query)

def call_pauthor(id_article, surname_author):
	query = "CALL FILTERING_PAUTHOR('" + id_article+ "','" + surname_author + "');"
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
	filtering(data, cursor)





	