##### GROUP 3 - Version 1.0 - RY/RV/MC/CR/EM : Creation des requetes #####
##### GROUP 3 - Version 1.1 - MC/CR : modification des requetes #####
##### GROUP 3 - Version 1.2 - MC/CR : Rajout des commentaires #####

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

db = MySQLdb.connect(user=username, passwd=passwordDB, host=servername, db=databasename)

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
			dictionary[keys[j]]=values[i][j]
		dictionary_final[str(i+1)]=dictionary

	json = jsonify(dictionary_final)
	return json

def execute_query(query) :
	"""
	input : the query
	output : dict object (we have to turn it into a json object with the "to_json" function)
	
	Task Automation (creating a cursor, execute the query, return the result)
	"""
	
	cursor = db.cursor()
	cursor.execute(query)
	result = cursor.fetchall()
	cursor.close()
	return result	
	
##query 1 Web
@app.route("/frequency_word_week/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_frequency_word_week():
	"""
	input : 
	output : return a json file
	
	View the most common keywords of the week
	"""
	query = """SELECT w.word, count(w.word)
			   FROM article a, word w,lemma l, position_word pw 
			   WHERE w.id_lemma = l.id_lemma
			   AND w.id_word = pw.id_word
			   AND pw.id_article = a.id_article
			   AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
			   GROUP BY w.word 
			   ORDER BY 2 DESC LIMIT 10;"""
	result = execute_query(query)
	keys = ['text','weight']
	json_return = to_json(keys,result)
	
	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return
		
##query 2 Web 
@app.route("/percent_Theme/<string:vTheme>", strict_slashes = False, methods = ['GET', 'POST'])
def api_percent_Theme(vTheme):
	"""
	input :
	output : json file
	
	Show theme and percentage of number of articles
	of this theme for the week
	"""
	#SELECT la.label, FORMAT(((count(a.id_article)/(SELECT count(id_article) FROM article))*100),2)
	query = """ SELECT la.label, ((count(a.id_article)/(SELECT count(id_article) FROM article))*100)
				FROM article a, belong b, label la 
				WHERE la.label = '"""+vTheme+"""'
				AND b.id_label = la.id_label
				AND b.id_article = a.id_article
				AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE; 
				"""
	result = execute_query(query)
	floatify = [(row[0],float(row[1])) for row in result]
	result = tuple(floatify)
	
	keys = ['name','pourcentage']
	json_return = to_json(keys,result)

	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return
		
##query 3 Web : 
@app.route("/Top_10_source/", methods = ['GET', 'POST'])	
def api_Top_10_source():
	"""
	input :
	output : json file
	
	Top 10 sources with the most articles per week 
	(name of the source and number of articles)
	"""
	query = """SELECT n.name_newspaper, count(a.id_article)
			   FROM article a , newspaper n
			   WHERE n.id_newspaper = a.id_newspaper
			   AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
			   GROUP BY n.name_newspaper
			   ORDER BY 2 DESC;"""
	result = execute_query(query)
	keys = ['source','nombre']
	json_return = to_json(keys,result)

	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return

		
##query 4 Web ### Fonction à vérifier
@app.route("/link_by_source/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_link_by_source():
	"""
	input :
	output : json file
	
	For each source, retrieve the link + the link of the image
	"""
	query = """SELECT DISTINCT n.name_newspaper, n.link_newspaper, n.link_logo
			   FROM newspaper n;
			"""
	result = execute_query(query)
	keys = ['source','lien_source','lien_logo']
	json_return = to_json(keys,result)

	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return
		
##query 5 Web 
@app.route("/frequency_Theme/<string:vTheme>", strict_slashes = False, methods = ['GET', 'POST'])	
def api_frequency_Theme(vTheme):
	"""
	input :
	output : json file
	
	Most requested words per week for the selected theme
	"""
	query = """
				SELECT la.label, w.word, count(w.word)
				FROM article a, label la, word w, lemma l, position_word pw,
				belong b 
				WHERE w.id_lemma = l.id_lemma
				AND w.id_word = pw.id_word
				AND pw.id_article = a.id_article
				AND a.id_article = b.id_article
				AND la.id_label = b.id_label
				AND la.label = '"""+vTheme+"""'
				AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
				ORDER BY 3 DESC LIMIT 5;
			"""
	
	result = execute_query(query)
	keys = ['name', 'word', 'nombre']
	json_return = to_json(keys,result)
	db.close()
	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return

##query 6 Web :

##query 7 Web :

##query 8 Web : 

##query 9 Web :	


##query 10 Web : 
@app.route("/count_word_label/<string:vTheme>", strict_slashes = False, methods = ['GET', 'POST'])	
def api_count_word_label(vTheme):
	"""
	input :
	output :
	
	Frequency of appearance of the word per week
	"""
	query = """
				SELECT la.label, w.word, count(w.word)
				FROM article a, label la, word w, lemma l, position_word pw,
				belong b 
				WHERE w.id_lemma = l.id_lemma
				AND w.id_word = pw.id_word
				AND pw.id_article = a.id_article
				AND a.id_article = b.id_article
				AND la.id_label = b.id_label
				AND la.label = '"""+vTheme+"""'
				AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
				ORDER BY 3 DESC LIMIT 5;
			"""
	result = execute_query(query)
	keys = ['theme','word','somme']
	json_return = to_json(keys, result)
	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return
	
##query 11 Web : 
@app.route("/frequency_per_Word/<string:vSource>", strict_slashes = False, methods = ['GET', 'POST'])	
def api_frequency_per_Word(vSource):
	"""
	input :
	output : json_file
	
	Frequency of the word by source
	"""
	db = MySQLdb.connect(user=username, passwd=passwordDB, host=servername, db=databasename)
	query = """
			   SELECT w.word, count(pw.id_word)
			   FROM word w, lemma l, position_word pw, article a, newspaper n
			   WHERE w.id_lemma = l.id_lemma
			   AND w.id_word = pw.id_word
			   AND pw.id_article = a.id_article
			   AND n.id_newspaper = a.id_newspaper
			   AND n.name_newspaper='"""+vSource+"""';
			"""
	result = execute_query(query)
	keys = ['word','somme']
	json_return = to_json(keys, result)
	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return

		

##query Web : List of words associated with the keyword
@app.route("/list_Key_Word/<string:vWord>", strict_slashes = False, methods = ['GET', 'POST'])	
def api_list_Key_Word(vWord):
	"""
	input :
	output :
	
	
	"""
	db = MySQLdb.connect(user=username, passwd=passwordDB, host=servername, db=databasename)
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
		
##query 13 Web : 		
@app.route("/frequency_Word_Label/<string:vWord>", strict_slashes = False, methods = ['GET', 'POST'])	
def api_frequency_Word_Label(vWord):
	"""
	input :
	output :
	
	Frequency of appearance of the word by theme
	"""
	query = """ SELECT la.label, w.word, count(pw.id_word) 
				FROM article a, belong b, label la, word w, lemma l, position_word pw   
				WHERE w.id_lemma = l.id_lemma
				AND w.id_word = pw.id_word
				AND pw.id_article = a.id_article
				AND la.id_label = b.id_label
				AND b.id_article = a.id_article
				AND w.word = '"""+vWord+"""'
				GROUP BY la.label, w.word;
			"""
			
	result = execute_query(query)
	keys = ['theme','word','somme']
	json_return = to_json(keys, result)
	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return
		

##query 14 Web : 
@app.route("/number_newspaper/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_number_newspaper():
	"""
	input :
	output :
	
	count the number of newspapers
	"""
	db = MySQLdb.connect(user=username, passwd=passwordDB, host=servername, db=databasename)
	query = """SELECT count(n.id_newspaper)
			   FROM newspaper n;"""
	result = execute_query(query)
	keys = ['nombre']
	json_return = to_json(keys, result)
	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return
		

##query 15 Web: 
@app.route("/title_newspaper/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_title_newspaper():
	"""
	input :
	output :
	
	bring out all the newspaper names
	"""
	db = MySQLdb.connect(user=username, passwd=passwordDB, host=servername, db=databasename)
	query = """
				SELECT DISTINCT n.name_newspaper
				FROM newspaper n;
			"""
	result = execute_query(query)
	keys = ['name_newspaper']
	json_return = to_json(keys, result)
	json_return.status_code = 200
	json_return.headers.add('Access-Control-Allow-Origin','*')
	json_return.headers.add('allow_redirects',True)
	return json_return	


	
if __name__ == '__main__':
	app.run(host="130.120.8.250", port = 5007, debug = True)
	

#########

##Requêtes page recherche :
##query 1
@app.route("/word/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_word():
		"""
		input :
		output :
		
		all words in alphabetical order
		"""
		query = """
					SELECT word FROM word ORDER BY word;
				"""
		result = execute_query(query)
		keys = ['name_newspaper']
		json_return = to_json(keys, result)
		json_return.status_code = 200
		json_return.headers.add('Access-Control-Allow-Origin','*')
		json_return.headers.add('allow_redirects',True)
		return json_return	


##query 4
@app.route("/frequency_word_label_Periode/<String:vWord><Date:vDateDebut><Date:vDateFin><String:vLabel>", strict_slashes = False, methods = ['GET', 'POST'])	
def api_frequency_word_label_Periode(vWord, vDateDebut, vDateFin, vLabel):
		"""
		input :
		output :
		
		Frequency of appearance of the word by theme
		"""
		query = """
					SELECT la.label, w.word, count(pw.id_word)
					FROM article a, belong b, label la, word w, lemma l, position_word pw   
					WHERE w.id_lemma = l.id_lemma
					AND w.id_word = pw.id_word
					AND pw.id_article = a.id_article
					AND la.id_label = b.id_label
					AND b.id_article = a.id_article
					AND w.word = '"""vWord"""'
					AND la.label = '"""vLabel"""'
					AND a.date_publication BETWEEN '"""vDateDebut"""' AND '"""vDateFin"""'
					GROUP BY la.label, w.word;"""
		result = execute_query(query)
		keys = ['name_newspaper']
		json_return = to_json(keys, result)
		json_return.status_code = 200
		json_return.headers.add('Access-Control-Allow-Origin','*')
		json_return.headers.add('allow_redirects',True)
		return json_return
		
		
##query 5
@app.route("/frequency_word_newspaper_Periode/<String:vWord><Date:vDateDebut><Date:vDateFin><String:vName_newspaper>", strict_slashes = False, methods = ['GET', 'POST'])	
def api_frequency_word_newspaper_Periode(vWord, vDateDebut, vDateFin,vName_newspaper):
		"""
		input :
		output :
		
		Frequency of appearance of the word by source
		"""
		query = """
					SELECT n.name_newspaper, w.word, count(pw.id_word) 
					FROM article a, belong b, newspaper n, word w, lemma l, position_word pw 
					WHERE w.id_lemma = l.id_lemma 
					AND w.id_word = pw.id_word 
					AND pw.id_article = a.id_article 
					AND a.id_newspaper = n.id_newspaper 
					AND w.word = 'vWord' 
					AND n.name_newspaper = 'vName_newspaper' 
					AND a.date_publication BETWEEN 'vDateDebut' AND 'vDateFin' 
					GROUP BY n.name_newspaper, w.word;"""
		result = execute_query(query)
		keys = ['name_newspaper']
		json_return = to_json(keys, result)
		json_return.status_code = 200
		json_return.headers.add('Access-Control-Allow-Origin','*')
		json_return.headers.add('allow_redirects',True)
		return json_return

##query 10
@app.route("/list_source/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_list_source():
		"""
		input :
		output :
		
		list of all sources
		"""
		query = """
					SELECT n.name_newspaper
					FROM newspaper n;
				"""
		result = execute_query(query)
		keys = ['name_newspaper']
		json_return = to_json(keys, result)
		json_return.status_code = 200
		json_return.headers.add('Access-Control-Allow-Origin','*')
		json_return.headers.add('allow_redirects',True)
		return json_return

##query page Theme
##query 1
@app.route("/theme_per_crescent_article/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_theme_per_crescent_article():
		"""
		input :
		output :
		
		all topics ordered by increasing number of articles
		"""
		query = """
					SELECT la.label, count(a.id_article) AS nombre
					FROM article a, label la, belong b
					WHERE a.id_article = b.id_article
					AND la.id_label = b.id_label
					AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
					ORDER BY nombre ASC;
				"""
		result = execute_query(query)
		keys = ['Label','number']
		json_return = to_json(keys, result)
		json_return.status_code = 200
		json_return.headers.add('Access-Control-Allow-Origin','*')
		json_return.headers.add('allow_redirects',True)
		return json_return
		
##Requêtes page accueil :
##query 1: 
@app.route("/polarity_items/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_polarity_items():
		"""
		input :
		output : json_file
		
		felt the polarity of all items 7-day slippery
		"""
		query = """
					SELECT a.id_article, a.is_positive
					FROM article a  
					WHERE a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE;
				"""
		result = execute_query(query)
		keys = ['id_article','positivité']
		json_return = to_json(keys, result)
		json_return.status_code = 200
		json_return.headers.add('Access-Control-Allow-Origin','*')
		json_return.headers.add('allow_redirects',True)
		return json_return
		
##query 2: 
@app.route("/rate/", strict_slashes = False, methods = ['GET', 'POST'])	
def api_rate():
		"""
		input :
		output :
		
		felt the rate of all items 7-day slippery
		"""
		query = """
					SELECT a.id_article, sum(a.rate_joy)/count(a.id_article), sum(a.rate_fear)/count(a.id_article), 
					sum(a.rate_sadness)/count(a.id_article), sum(a.rate_angry)/count(a.id_article), 
					sum(a.rate_surprise)/count(a.id_article), sum(a.rate_disgust)/count(a.id_article), sum(a.subjectivity)/count(a.id_article)
					FROM article a  
					WHERE a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE;
				"""
		result = execute_query(query)
		keys = ['id_article','joie','peur','tristesse',]
		json_return = to_json(keys, result)
		json_return.status_code = 200
		json_return.headers.add('Access-Control-Allow-Origin','*')
		json_return.headers.add('allow_redirects',True)
		return json_return