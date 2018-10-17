--Groupe3_LauraBouzidi_CyrilGaillard_RemiVives_EnzoMartineau
--requete 1 : View the most common keywords of the week
	--Combien de word(TOP ?)
	--Date : semaine d'avant ? semaine en cours ? quand recalculer ?

SELECT w.word, count(w.word)
FROM article a, word w,lemma l, position_word pw 
WHERE w.id_lemma = l.id_lemma
AND w.id_word = pw.id_word
AND pw.id_article = a.id_article
GROUP BY w.word 
ORDER BY 2 DESC LIMIT 5;


--requete 2 : Show theme + percentage of number of articles 
--of this theme for the week

CREATE PROCEDURE percent_Theme (INOUT vTheme varchar(25), OUT vPercent FLOAT) 
BEGIN 
	SELECT c.class, ((count(a.id_article)/(SELECT count(id_article) FROM article))*100) 
	INTO vTheme, vPercent
	FROM article a, belong b, classification c 
	WHERE c.class = 'vTheme' 
	AND b.id_class = c.id_class 
	AND b.id_article = a.id_article; 
END;

--requete 3 : Top 10 sources with the most articles per week 
--(name of the source and number of articles)

SELECT n.name_newspaper, count(a.id_article)
FROM article a , newspaper n
WHERE n.id_newspaper = a.id_newspaper
GROUP BY n.name_newspaper
ORDER BY 2 DESC LIMIT 10;

--requete 4 : For each source, retrieve the link + the link of the image

SELECT DISTINCTn.name_newspaper, n.link_newspaper, n.link_logo
FROM newspaper n;

--requete 5 : Most answered words / week for the selected theme
			--wordplus traités dans le titre ou dans les articles ?
SELECT c.class, w.word, count(w.word)
FROM article a, classification c, word w, lemma l, position_word pw
belong b 
WHERE w.id_lemma = l.id_lemma
AND w.id_word = pw.id_word
AND pw.id_article = a.id_article
AND a.id_article = b.id_article
AND c.id_class = b.id_class
GROUP BY c.class, w.word 
ORDER BY 3 DESC LIMIT 5;

--requete 7 : Frequency of appearance of the word per week 
CREATE PROCEDURE frequency_Word (INOUT vWord varchar(50), OUT vfrequency FLOAT) 
BEGIN
	SELECT DISTINCT w.word, ((count(w.word)/(SELECT count(word) FROM word))*100) INTO vWord, vfrequency
	FROM article a, belong b, classification c, word w, lemma l, position_word pw 
	WHERE w.id_lemma = l.id_lemma
	AND w.id_word = pw.id_word
	AND pw.id_article = a.id_article
	AND b.id_article = a.id_article
	AND c.id_class = b.id_class
	AND w.word = vWord;
END;

		
--requete 8 : Frequency of the word by source

CREATE PROCEDURE word_percent  (INOUT vSource varchar(50),
OUT vPercent FLOAT, OUT vWord varchar(50))
BEGIN
   SELECT w.word, (count(w.word)/(SELECT count(word) FROM word)) INTO vWord, vPercent
   FROM word w, lemma l, position_word pw, article a, newspaper n
   WHERE w.id_lemma = l.id_lemma
   AND w.id_word = pw.id_word
   AND pw.id_article = a.id_article
   AND n.id_newspaper = a.id_newspaper
   AND n.name_newspaper=vSource;
END;


--requete 9 : Liste de words associés au wordclé (nombre à définir)
CREATE PROCEDURE list_Key_Word (INOUT vWord varchar(50), OUT vSynonym varchar(50)) 
BEGIN
	SELECT s.synonym INTO vSynonym
	FROM   word w, lemma l, position_word pw, synonym s
	WHERE w.id_lemma = l.id_lemma
	AND w.id_word = pw.id_word
	AND pw.id_synonyme = s.id_synonyme
	AND w.word = vWord;
END;


--requete 10 : Fréquence d'apparition du wordpar thème
CREATE PROCEDURE frequency_Word_Theme (INOUT vWord varchar(50), OUT vfrequency FLOAT, OUT vclassification varchar(25))
BEGIN
	SELECT c.class, w.word, (count(w.word)/(SELECT count(w.word) FROM word)) INTO vclassification, vWord, vfrequency
	FROM article a, belong b, classification c, word w, lemma l, position_word pw   
	WHERE w.id_lemma = l.id_lemma
	AND w.id_word = pw.id_word
	AND pw.id_article = a.id_article
	AND c.id_class = b.id_class
	AND b.id_article = a.id_article
	AND w.word = vWord
	GROUP BY c.class, w.word;
END;

--requete 11 : compter le nombre de journaux

SELECT count(n.id_newspaper)
FROM newspaper n;

--requete 12 : ressortir tous les noms de journaux

SELECT DISTINCT n.name_newspaper
FROM newspaper n;