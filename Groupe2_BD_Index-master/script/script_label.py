from flask_mysqldb import MySQL
import json
import pandas as pd
import mysql.connector
import MySQLdb

def label():
	data = request.get_json()
	for article in data :
		id_article = str(article['id_hash'])
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
	#cursor = db.cursor()
	print(cursor.execute(query))


if __name__ == '__main__':

	# MySQL configurations
	servername = "localhost"
	username = "root"
	passwordDB = "sidiots"
	databasename = "index"

	db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)
	cursor = db.cursor()
	