-- Number of words items of the day
CREATE PROCEDURE word_article (IN vNombre INT) 
BEGIN
	SELECT s.id_article, count(s.id_word)
	FROM statistique s
	WHERE s.date_publication = CURRENT_DATE-vNombre;
END;

--Number of items of the day
CREATE PROCEDURE nombre_article_day (IN vNombre INT) 
BEGIN
	SELECT count(DISTINCT s.id_article)
	FROM statistique s
	WHERE s.date_publication = CURRENT_DATE-vNombre;
END;

--All id word for the items of the day 

CREATE PROCEDURE word_article_day (IN vNombre INT) 
BEGIN
	SELECT s.id_article, s.id_word
	FROM statistique s
	WHERE s.date_publication = CURRENT_DATE-vNombre;
END;

--The tf_idf for this word and this article, for a particular day

CREATE PROCEDURE word_article_tf_idf (IN vWord INT(50),IN vArticle INT(50),IN vNombre INT) 
BEGIN
	SELECT s.id_article, s.id_word, s.tf_idf
	FROM statistique s
	WHERE s.date_publication = CURRENT_DATE-vNombre;
END;

--The tf for this word and this article, for a particular day

CREATE PROCEDURE word_tf_article(IN vWord INT(50),IN vArticle INT(50),IN vNombre INT) 
BEGIN
	SELECT s.id_article, s.id_word, s.tf
	FROM statistique s
	WHERE s.date_publication = CURRENT_DATE-vNombre;
END;

--All the id_articles of the day, for a particular day

CREATE PROCEDURE article_day (IN vNombre INT) 
BEGIN
	SELECT s.id_article
	FROM statistique s
	WHERE s.date_publication = CURRENT_DATE-vNombre;
END;

