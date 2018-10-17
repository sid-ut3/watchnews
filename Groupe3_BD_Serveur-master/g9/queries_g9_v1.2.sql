--Groupe3_LauraBouzidi_CyrilGaillard_RemiVives_EnzoMartineau
--query 1 : View the most common keywords of the week
	

SELECT w.word, count(w.word)
FROM article a, word w,lemma l, position_word pw 
WHERE w.id_lemma = l.id_lemma
AND w.id_word = pw.id_word
AND pw.id_article = a.id_article
AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
GROUP BY w.word 
ORDER BY 2 DESC LIMIT 5;


--query 2 : Show theme + percentage of number of articles 
--of this theme for the week

CREATE PROCEDURE percent_Theme (INOUT vTheme varchar(25), OUT vPercent FLOAT) 
BEGIN 
	SELECT la.label, ((count(a.id_article)/(SELECT count(id_article) FROM article))*100) 
	INTO vTheme, vPercent
	FROM article a, belong b, label la 
	WHERE la.label = 'vTheme' 
	AND b.id_label = la.id_label 
	AND b.id_article = a.id_article
	AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE; 
END;

--query 3 : Top 10 sources with the most articles per week 
--(name of the source and number of articles)

SELECT n.name_newspaper, count(a.id_article)
FROM article a , newspaper n
WHERE n.id_newspaper = a.id_newspaper
AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE
GROUP BY n.name_newspaper
ORDER BY 2 DESC LIMIT 10;

--query 4 : For each source, retrieve the link + the link of the image

SELECT DISTINCT n.name_newspaper, n.link_newspaper, n.link_logo
FROM newspaper n;

--query 5 : Most answered words / week for the selected theme
CREATE PROCEDURE count_word_Theme (INOUT vTheme VARCHAR(50)) 
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
END;

--query 7 : Frequency of appearance of the word per week 
CREATE PROCEDURE frequency_per_Word (INOUT vWord varchar(50), OUT vfrequency FLOAT) 
BEGIN
	SELECT DISTINCT w.word, count(pw.id_word) INTO vWord, vfrequency
	FROM article a, belong b, label la, word w, lemma l, position_word pw 
	WHERE w.id_lemma = l.id_lemma
	AND w.id_word = pw.id_word
	AND pw.id_article = a.id_article
	AND b.id_article = a.id_article
	AND la.id_label = b.id_label
	AND w.word = vWord
	AND a.date_publication BETWEEN CURRENT_DATE-7 AND CURRENT_DATE;
END;

		
--query 8 : Frequency of the word by source

CREATE PROCEDURE frequency_word_per_source  (INOUT vSource varchar(50),
OUT vPercent FLOAT, OUT vWord varchar(50))
BEGIN
   SELECT w.word, count(pw.id_word) INTO vWord, vPercent
   FROM word w, lemma l, position_word pw, article a, newspaper n
   WHERE w.id_lemma = l.id_lemma
   AND w.id_word = pw.id_word
   AND pw.id_article = a.id_article
   AND n.id_newspaper = a.id_newspaper
   AND n.name_newspaper=vSource;
END;


--query 9 : List of words associated with the keyword
CREATE PROCEDURE list_Key_Word (INOUT vWord varchar(50), OUT vSynonym varchar(50)) 
BEGIN
	SELECT s.synonym INTO vSynonym
	FROM   word w, lemma l, synonym s
	WHERE w.id_lemma = l.id_lemma
	AND w.id_synonyme = s.id_synonyme
	AND w.word = vWord;
END;


--query 10 : Frequency of appearance of the word by theme
CREATE PROCEDURE frequency_Word_Theme (INOUT vWord varchar(50), OUT vfrequency FLOAT, OUT vlabel varchar(25))
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
END;

--query 11 : count the number of newspapers

SELECT count(n.id_newspaper)
FROM newspaper n;

--query 12 : bring out all the newspaper names

SELECT DISTINCT n.name_newspaper
FROM newspaper n;


--query 13 : number of items 
SELECT number_article 
FROM mv_number_article_week ;

--query 14 : number of items/labels
SELECT id_label,number_article
FROM mv_number_article_week_label ;