"""
g1
@Author : F.C
g3 
@Author : L.B. M.I. A.H. C.G.
g8
@Author : F.R.
"""
import MySQLdb
from datetime import datetime, timedelta
import timestring
servername = "localhost"
username = "root"
passwordDB = ""
databasename = "bdd_test"
db = MySQLdb.connect(user = username, passwd = passwordDB, host = servername, db = databasename)

week = {}
list_word  = []


date_min = """Select min(date) from mv_tf_idf_week"""
date_max = """Select max(date) from mv_tf_idf_week"""
cursor = db.cursor()
cursor.execute(date_min)
date_min_res = cursor.fetchall()
cursor.close()
cursor2 = db.cursor()
cursor2.execute(date_max)
date_max_res = cursor2.fetchall()
cursor2.close()
date_max_res = str(date_max_res[0][0])
date_min_res = str(date_min_res[0][0])

week["Period"] = date_min_res + " - " + date_max_res
id_words = """Select DISTINCT id_word from mv_tf_idf_week where date between %s and %s order by id_word""" % ("'" + date_min_res + "'", "'" + date_max_res + "'" )
cursor3 = db.cursor()
cursor3.execute(id_words)
id_words_res = cursor3.fetchall()
cursor3.close()
for i in range(0, len(id_words_res)):
	list_word.append(id_words_res[i][0])
	

for word in range(0, len(list_word)):
	week_words_tf_idf =[]
	week_words_tf = []
	list_week = []
	for day in range(7):
		day_query = datetime.strptime(date_min_res, "%Y-%m-%d") + timedelta(days=day)
		list_article = []
		id_article = """SELECT id_article from mv_tf_idf_week where date = %s AND id_word = %s ORDER BY id_article""" % ("'" +  str(day_query) + "'", list_word[word])
		cursor4 = db.cursor()
		cursor4.execute(id_article)
		id_article_res = cursor4.fetchall()
		cursor4.close()
		list_tf_idf = []
		list_tf = []
		for article in range(0, len(id_article_res)):
			list_article.append(id_article_res[article][0])
			rq_tf_idf = """SELECT tf_idf FROM mv_tf_idf_week WHERE id_word = %s AND id_article = %s AND date = %s """ % (list_word[word], list_article[article], "'" +  str(day_query) + "'")
			cursor5 = db.cursor()
			cursor5.execute(rq_tf_idf)
			tf_idf_res = cursor5.fetchall()
			cursor5.close()
			tf = []
			tf_idf = []
			for j in range(0, len(tf_idf_res)):
				tf_idf.append(tf_idf_res[j][0])
			list_tf_idf.append(tf_idf[0])
			rq_tf = """SELECT tf FROM mv_tf_idf_week WHERE id_word = %s AND id_article = %s AND date = %s """ % (list_word[word], list_article[article], "'" +  str(day_query) + "'")
			cursor6 = db.cursor()
			cursor6.execute(rq_tf)
			tf_res = cursor6.fetchall()
			cursor6.close()
			for k in range(0, len(tf_res)):
				tf.append(tf_res[k][0])
			list_tf.append(tf[0])
		week_words_tf_idf.append(list_tf_idf)
		list_week.append(list_article)
		week_words_tf.append(list_tf)
	week[str(list_word[word])+"_tf_idf"] = week_words_tf_idf
	week[str(list_word[word])+"_tf"] = week_words_tf
	
print (week)
		
		