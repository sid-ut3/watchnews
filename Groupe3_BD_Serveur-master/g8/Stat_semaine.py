import MySQLdb
servername = "localhost"
username = "root"
passwordDB = ""
databasename = "bdd_test"
db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)

week = {}
list_word  = []


date_min = """Select min(date) from vue"""
date_max = """Select max(date) from vue"""
cursor = db.cursor()
cursor.execute(date_min)
date_min_res = cursor.fetchall()
cursor.close()
cursor2 = db.cursor()
cursor2.execute(date_max)
date_max_res = cursor2.fetchall()
cursor2.close()

week["Period"] = str(date_min_res[0][0]) + " - " + str(date_max_res[0][0])

id_words = """Select id_mot from vue where date between '2017-11-13' and '2018-01-09' order by id_mot""" #(date_min_res[0][0], date_max_res[0][0])
cursor3 = db.cursor()
cursor3.execute(id_words)
id_words_res = cursor3.fetchall()
cursor3.close()

for i in range(0, len(id_words_res)):
	list_word.append(id_words_res[i][0])
#ça marche jusqu'ici


for word in range(0, len(list_word)):
	week_words_tf_idf =[]
	week_words_tf = []
	for day in range(7):
      # day_query = datetime.date(date_min) + datetime.timedelta(days=jour, hours=0, minutes=0, seconds=0)
		list_article = []
		id_article = """SELECT id_Article from vue where date '2017-11-13'"""# day_query
		cursor4 = db.cursor()
		cursor4.execute(id_article)
		id_article_res = cursor4.fetchall()
		cursor4.close()
	for i in range(0, len(id_article_res)):
	   list_article.append(id_article_res[i][0])
print(list_article)
	 

'''
for i in range(0, len(id_words_res)):
	list_word.append(id_words_res[i][0])
	   day_word_tf_idf = []
       day_word_tf = []
       for article in range(nb_article_jour):
	       day_word_tf_idf.append 
		   day-word-tf.append    
		   SELECT tf_idf FROM vue where 
		   
		  
db.close()
		   
		   
db.close()
id_articles = """Select id_article from article where date between ? and ?""" (date_min, date_max)





test = """ SELECT id_article from article"""
cursor = db.cursor()
cursor.execute(test)
result = cursor.fetchall()
cursor.close()
db.close()
test1 = []

print(list(result))
'''