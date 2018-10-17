##### GROUP 3 - Version 1.0 - RY/RV/MC/CR/EM#####
from flask import Flask, request, jsonify
import json
import requests
from flask_restful import Resource, Api
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__) # we are using this variable to use the flask microframework
#api = Api(app)

# MySQL configurations
servername = "localhost"
username = "DBIndex_user"
passwordDB = "password_DBIndex_user"
databasename = "DBIndex"
 

@app.route("/connectDBjson/", methods = ['GET','POST'])
def api_connectDBjson():
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie")
	
	# with open("bla.txt", "rb") as fin:
		# j = json.load(fin)
	
	# query = """select * from lemma"""
	# cursor = db.cursor()
	# cursor.execute(query)
	# result = cursor.fetchall()
	# cursor.close()
	# db.close()
	
	res = (("mot1", 23), ("mot2", 17), ("mot3",9))
	
	result_json = jsonify(dict(res))
	print("ok")
	
	# headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	
	# repo = requests.post('http://130.120.8.250:5002/test_g3/', headers=headers, data=result_json)

	# url = "http://130.120.8.250:5002/static_day"
	# headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
	# r = requests.post(url, data=result_json)
	# print(jsonify(repo.json()))
	# res = jsonify(repo.json())
	# res.status_code = 200
	# res.headers.add('Access-Control-Allow-Origin','*')	# print(jsonify(repo.json()))
	# res = jsonify(repo.json())
	# res.status_code = 200
	# res.headers.add('Access-Control-Allow-Origin','*')
	return result_json
 
 
@app.route("/transfertJson/", methods = ['GET','POST'])
def api_transfertJson():
	try:
		# db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		# print("connexion reussie")
		# query = """select * from lemma"""
		# cursor = db.cursor()
		# cursor.execute(query)
		# result = cursor.fetchall()
		# cursor.close()
		# db.close()
		# result_json = jsonify(result)
		#print(result)
		
		
		headers = {'Content-Type': 'application/json'}
		data = '''{"period":"02/08/2017",
			  "Macron" : [[0.6],[0.3,0.4,0.5]],
			  "Tempete" : [[],[0.25,0.8,0.5]],
			  "Enfant" : [[0.5,0.6],[0.5,0.1,0.2]],
			  "Fleur" :  [[0.9,0.6],[0.5]],
			  "Jardin" :  [[0.3,0.6],[0.1,0.5]],
			  "Jouet" : [[0.5],[0.5,0.9,0.9]],
			  "Jeux" : [[0.6],[]],
			  "Magazine" : [[0.3,0.65],[0.1,0.5]],
			  "Noel" : [[0.5,0.6],[0.5]],
			  "Jour" : [[0.5],[0.1,0.2]],
			  "Test" : [[0.5,0.6],[0.5]]
			}'''
		repo = requests.post('http://130.120.8.250:5002/static_day/', headers=headers, data=data)
		#print(repo)
		# url = "http://130.120.8.250:5002/static_day"
		# headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
		# r = requests.post(url, data=result_json)
		print(repo.json())
		res = jsonify(repo.json())
		res.status_code = 200
		res.headers.add('Access-Control-Allow-Origin','*')
		return res
		
		


@app.route("/selectweb/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_selectweb():
	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	print("connexion reussie")
	query = """select * from lemma"""
	cursor = db.cursor()
	cursor.execute(query)
	result = cursor.fetchall()
	cursor.close()
	print(result)
	db.close()
	return "select ok"

	

@app.route("/insertweb/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_insertweb():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """insert into lemma (lemma) values ('tata');"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		


	
if __name__ == '__main__':
	app.run(host="130.120.8.250", port = 5000, debug = True)
	

##query 1 Web : View the most common keywords of the week
@app.route("/frequency_word_week/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_frequency_word_week():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """SELECT w.word, count(w.word)
				   FROM article a, word w,lemma l, position_word pw 
				   WHERE w.id_lemma = l.id_lemma
				   AND w.id_word = pw.id_word
				   AND pw.id_article = a.id_article
				   AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
				   GROUP BY w.word 
				   ORDER BY 2 DESC LIMIT 5;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 2 Web :Show theme + percentage of number of articles 
##of this theme for the week
@app.route("/percent_Theme/<String:vTheme>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_percent_Theme(vTheme):
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """CREATE PROCEDURE percent_Theme (INOUT vTheme varchar(25), OUT vPercent FLOAT) 
					BEGIN 
						SELECT la.label, ((count(a.id_article)/(SELECT count(id_article) FROM article))*100) 
						INTO vTheme, vPercent
						FROM article a, belong b, label la 
						WHERE la.label = 'vTheme' 
						AND b.id_label = la.id_label 
						AND b.id_article = a.id_article
						AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE; 
					END;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 3 Web : Top 10 sources with the most articles per week 
##(name of the source and number of articles)
@app.route("/Top_10_source/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_Top_10_source():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """SELECT n.name_newspaper, count(a.id_article)
				   FROM article a , newspaper n
				   WHERE n.id_newspaper = a.id_newspaper
				   AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
				   GROUP BY n.name_newspaper
				   ORDER BY 2 DESC LIMIT 10;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 4 Web : For each source, retrieve the link + the link of the image
@app.route("/link_by_source/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_link_by_source():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """SELECT DISTINCT n.name_newspaper, n.link_newspaper, n.link_logo
				   FROM newspaper n;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 5 Web : Most answered words / week for the selected theme
@app.route("/frequency_Theme/<String:vTheme>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_frequency_Theme(vTheme):
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """CREATE PROCEDURE frequency_Theme (INOUT vTheme VARCHAR(50)) 
					BEGIN
						SELECT la.label, w.word, count(w.word)
						FROM article a, label la, word w, lemma l, position_word pw,
						belong b 
						WHERE w.id_lemma = l.id_lemma
						AND w.id_word = pw.id_word
						AND pw.id_article = a.id_article
						AND a.id_article = b.id_article
						AND la.id_label = b.id_label
						AND la.label = vTheme
						AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
						ORDER BY 3 DESC LIMIT 5;
					END;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
		
##query 7 Web : Frequency of appearance of the word per week
@app.route("/count_word_Theme/<String:vTheme>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_count_word_Theme(vTheme):
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """CREATE PROCEDURE count_word_Theme (INOUT vTheme VARCHAR(50)) 
					BEGIN
						SELECT la.label, w.word, count(w.word)
						FROM article a, label la, word w, lemma l, position_word pw,
						belong b 
						WHERE w.id_lemma = l.id_lemma
						AND w.id_word = pw.id_word
						AND pw.id_article = a.id_article
						AND a.id_article = b.id_article
						AND la.id_label = b.id_label
						AND la.label = vTheme
						AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
						ORDER BY 3 DESC LIMIT 5;
					END;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 8 Web : Frequency of the word by source
@app.route("/frequency_per_Word/<String:vSource>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_frequency_per_Word(vSource):
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """CREATE PROCEDURE frequency_word_per_source  (INOUT vSource varchar(50), OUT vPercent FLOAT, OUT vWord varchar(50))
					BEGIN
					   SELECT w.word, count(pw.id_word) INTO vWord, vPercent
					   FROM word w, lemma l, position_word pw, article a, newspaper n
					   WHERE w.id_lemma = l.id_lemma
					   AND w.id_word = pw.id_word
					   AND pw.id_article = a.id_article
					   AND n.id_newspaper = a.id_newspaper
					   AND n.name_newspaper=vSource;
					END;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"

		

##query 9 Web : List of words associated with the keyword
@app.route("/list_Key_Word/<String:vWord>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_list_Key_Word(vWord):
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """CREATE PROCEDURE list_Key_Word (INOUT vWord varchar(50), OUT vSynonym varchar(50)) 
					BEGIN
						SELECT s.synonym INTO vSynonym
						FROM   word w, lemma l, synonym s
						WHERE w.id_lemma = l.id_lemma
						AND w.id_synonyme = s.id_synonyme
						AND w.word = vWord;
					END;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 10 Web : Frequency of appearance of the word by theme		
@app.route("/frequency_Word_Theme/<String:vWord>", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_frequency_Word_Theme(vWord):
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """CREATE PROCEDURE frequency_Word_Theme (INOUT vWord varchar(50), OUT vfrequency FLOAT, OUT vlabel varchar(25))
					BEGIN
						SELECT la.label, w.word, count(pw.id_word) INTO vlabel, vWord, vfrequency
						FROM article a, belong b, label la, word w, lemma l, position_word pw   
						WHERE w.id_lemma = l.id_lemma
						AND w.id_word = pw.id_word
						AND pw.id_article = a.id_article
						AND la.id_label = b.id_label
						AND b.id_article = a.id_article
						AND w.word = vWord
						GROUP BY la.label, w.word;
					END;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		

##query 11 Web : count the number of newspapers
@app.route("/number_newspaper/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_number_newspaper():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """SELECT count(n.id_newspaper)
				   FROM newspaper n;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		

##query 12 Web: bring out all the newspaper names
@app.route("/title_newspaper/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_title_newspaper():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """SELECT DISTINCT n.name_newspaper
				   FROM newspaper n;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 13 Web : number of items
@app.route("/number_items/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_number_items():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """SELECT number_article 
				   FROM mv_number_article_week ;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 14 Web : number of items/labels	
@app.route("/number_items_per_label/", methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])	
def api_number_items_per_label():
	try:
		db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
		print("connexion reussie iw")
		query = """SELECT id_label,number_article
				   FROM mv_number_article_week_label ;"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"