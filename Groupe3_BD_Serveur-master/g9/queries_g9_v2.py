##Requêtes page recherche :
##query 1
@app.route("/word/", methods = ['GET', 'POST'])	
def api_word():
		print("connexion reussie iw")
		query = """
					SELECT word FROM word ORDER BY word;
				"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"


##query 2
CREATE PROCEDURE found_word (IN vWord VARCHAR(50), OUT vResult VARCHAR(50), OUT vId_word INTEGER, OUT vId_entity INTEGER) 
BEGIN 
	SELECT w.id_word INTO vId_word 
	FROM position_word pw, word w 
	WHERE w.id_word = pw.id_word 
	AND w.word = 'vWord'; 

	SELECT id_entity INTO vId_entity 
	FROM position_word 
	WHERE id_word = vId_word;
	
	IF vId_entity <> NULL THEN 
		SELECT file_wiki INTO vResult 
		FROM wiki wk, position_word pw, word w 
		WHERE pw.id_word = vId_word 
		AND pw.id_wiki = wk.id_wiki; 
	ELSE 
		SELECT s.synonym INTO vResult 
		FROM synonym s, common c, position_word pw 
		WHERE pw.id_word = vId_word 
		AND c.position = pw.position 
		AND s.id_synonym = c.id_synonym; 
	END IF; 
END;


##query 3

##query 4
@app.route("/frequency_word_label_Periode/<String:vWord><Date:vDateDebut><Date:vDateFin><String:vLabel>", methods = ['GET', 'POST'])	
def api_frequency_word_label_Periode():
	try:
		print("connexion reussie iw")
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
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
		
##query 5
@app.route("/frequency_word_newspaper_Periode/<String:vWord><Date:vDateDebut><Date:vDateFin><String:vName_newspaper>", methods = ['GET', 'POST'])	
def api_frequency_word_newspaper_Periode():
		print("connexion reussie iw")
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
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"

##query 10
@app.route("/list_source/", methods = ['GET', 'POST'])	
def api_list_source():
		print("connexion reussie iw")
		query = """
					SELECT n.name_newspaper
					FROM newspaper n;
				"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"

##query page Theme
##query 1
@app.route("/theme_per_crescent_article/", methods = ['GET', 'POST'])	
def api_theme_per_crescent_article():
		print("connexion reussie iw")
		query = """
					SELECT la.label, count(a.id_article) AS nombre
					FROM article a, label la, belong b
					WHERE a.id_article = b.id_article
					AND la.id_label = b.id_label
					AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
					ORDER BY nombre ASC;
				"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##Requêtes page accueil :
##query 1: 
@app.route("/polarity_items/", methods = ['GET', 'POST'])	
def api_polarity_items():
		print("connexion reussie iw")
		query = """
					SELECT a.id_article, a.is_positive
					FROM article a  
					WHERE a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE;
				"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"
		
##query 2: 
@app.route("/rate/", methods = ['GET', 'POST'])	
def api_rate():
		print("connexion reussie iw")
		query = """
					SELECT a.id_article, a.rate_joy, a.rate_fear, a.rate_sadness, a.rate_angry, a.rate_surprise, a.rate_disgust, a.subjectivity
					FROM article a  
					WHERE a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE;
				"""
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()
		cursor.close()
		db.close()
		return "insert ok"