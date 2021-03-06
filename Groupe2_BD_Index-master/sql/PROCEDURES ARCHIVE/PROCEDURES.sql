DELIMITER /

DROP PROCEDURE IF EXISTS PARTICLE/
	CREATE PROCEDURE PARTICLE (IN VDATE_PUBLICATION DATE, IN VRATE_POSITIVITY FLOAT,
	IN VRATE_NEGATIVITY FLOAT, IN VRATE_JOY FLOAT, IN VRATE_FEAR FLOAT, IN VRATE_SADNESS FLOAT,
	IN VRATE_ANGRY FLOAT, IN VRATE_SURPRISE FLOAT, IN VRATE_DISGUST FLOAT, IN VID_NEWSPAPER INT, OUT VID_ARTICLE INT)

BEGIN

	INSERT INTO ARTICLE (id_article, date_publication, rate_positivity, rate_negativity, rate_joy, 
	rate_fear, rate_sadness, rate_angry, rate_surprise, rate_disgust, id_newspaper) 
	VALUES (NULL,VDATE_PUBLICATION,VRATE_POSITIVITY,VRATE_NEGATIVITY,VRATE_JOY,VRATE_FEAR,
	VRATE_SADNESS,VRATE_ANGRY,VRATE_SURPRISE,VRATE_DISGUST,VID_NEWSPAPER);
	SELECT LAST_INSERT_ID() INTO VID_ARTICLE;

END/       

--- 

DROP PROCEDURE IF EXISTS PAUTHOR/

CREATE PROCEDURE PAUTHOR (IN VID_ARTICLE INT, IN VSURNAME_AUTHOR VARCHAR(50), IN VFIRSTNAME_AUTHOR VARCHAR(50))   
BEGIN
	
	DECLARE COUNT_ID_ INT DEFAULT 0;
	DECLARE VID_AUTHOR INT DEFAULT 0;
	
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET VID_AUTHOR = NULL;

	SELECT AUTHOR.ID_AUTHOR INTO VID_AUTHOR
	FROM AUTHOR 
	WHERE AUTHOR.SURNAME_AUTHOR = VSURNAME_AUTHOR
	AND AUTHOR.FIRSTNAME_AUTHOR = VFIRSTNAME_AUTHOR;

	IF (VID_AUTHOR IS NULL)  THEN 
		INSERT INTO AUTHOR (ID_AUTHOR, SURNAME_AUTHOR, FIRSTNAME_AUTHOR) VALUES (NULL, VSURNAME_AUTHOR,VFIRSTNAME_AUTHOR);
    	SELECT LAST_INSERT_ID() INTO VID_AUTHOR;
	END IF;
	
    INSERT INTO REALIZE (ID_AUTHOR, ID_ARTICLE) VALUES (VID_AUTHOR ,VID_ARTICLE);

END/

--
DROP PROCEDURE IF EXISTS PBELONG/


CREATE PROCEDURE PBELONG (IN VID_ARTICLE INT, IN VID_LABEL INT)   
BEGIN
	 
     INSERT INTO BELONG (id_article,id_label) VALUES (VID_ARTICLE ,VID_LABEL);

END/
--

DROP PROCEDURE IF EXISTS PENTITY/


CREATE PROCEDURE PENTITY (IN VENTITY VARCHAR(50))   
BEGIN
     INSERT INTO ENTITY(id_entity,type_entity) VALUES (NULL,VENTITY);
END/


-- 

DROP PROCEDURE IF EXISTS PLABEL/

CREATE PROCEDURE PLABEL (IN VLABEL VARCHAR(50))
BEGIN
     INSERT INTO LABEL (id_label,label) VALUES (NULL,VLABEL);
END/ 

-- 

DROP PROCEDURE IF EXISTS PNEWSPAPER/

CREATE PROCEDURE PNEWSPAPER (IN VNAME_NEWSPAPER VARCHAR(50),IN VLINK_NEWSPAPER VARCHAR(255),IN VLINK_LOGO VARCHAR(255))
BEGIN
     INSERT INTO NEWSPAPER(id_newspaper,name_newspaper,link_newspaper,link_logo) VALUES (NULL,VNAME_NEWSPAPER,VLINK_NEWSPAPER,VLINK_LOGO);
END/

--

DROP PROCEDURE IF EXISTS PPOS_TAGGING/

CREATE PROCEDURE PPOS_TAGGING (IN VPOS_TAG VARCHAR(25))   
BEGIN
	INSERT INTO POS_TAGGING (id_pos_tag, pos_tag) VALUES (NULL,VPOS_TAG);

END/      

--

DROP PROCEDURE IF EXISTS PPOSITION_WORD/

CREATE PROCEDURE PPOSITION_WORD (IN VPOSITION INT, IN VTITLE BOOLEAN, IN VWORD VARCHAR(50), VTYPE_ENTITY VARCHAR(25), IN VPOS_TAG VARCHAR(25), IN VID_ARTICLE INT,IN VFILE_WIKI VARCHAR(255))   

BEGIN
	DECLARE VID_WORD INT;
     DECLARE VID_ENTITY INT; 
     DECLARE VID_POS_TAG INT;
     DECLARE VID_WIKI INT;
     
     SELECT ID_WORD INTO VID_WORD
     FROM WORD
     WHERE WORD = VWORD;
     
     SELECT ID_ENTITY INTO VID_ENTITY
     FROM ENTITY
     WHERE TYPE_ENTITY = VTYPE_ENTITY;
     
     SELECT ID_POS_TAG INTO VID_POS_TAG
     FROM POS_TAGGING
     WHERE POS_TAG = VPOS_TAG;
     
     SELECT ID_WIKI INTO VID_WIKI
     FROM WIKI
     WHERE FILE_WIKI = VFILE_WIKI;

     INSERT INTO POSITION_WORD (ID_POSITION, POSITION,TITLE,ID_WORD,ID_ENTITY,ID_POS_TAG,ID_ARTICLE,ID_WIKI) 
     VALUES (NULL, VPOSITION,VTITLE,VID_WORD,VID_ENTITY,VID_POS_TAG,VID_ARTICLE,VID_WIKI);

END/ 

-- 

DROP PROCEDURE IF EXISTS PSYNONYM/
CREATE PROCEDURE PSYNONYM (IN VSYNONYM VARCHAR(50), IN VWORD VARCHAR(50))   
BEGIN
	DECLARE VID_SYNONYM INT DEFAULT 0;

	INSERT INTO SYNONYM (ID_SYNONYM, SYNONYM) VALUES (NULL,VSYNONYM);
    SELECT LAST_INSERT_ID() INTO VID_SYNONYM;

    UPDATE WORD
	SET WORD.ID_SYNONYM = VID_SYNONYM
	WHERE WORD.WORD = VWORD;

END/

--

DROP PROCEDURE IF EXISTS PWIKI/

CREATE PROCEDURE PWIKI (IN VFILE_WIKI VARCHAR(500), OUT VID_WIKI INT)   
BEGIN
     INSERT INTO WIKI (ID_WIKI, FILE_WIKI) VALUES (NULL, VFILE_WIKI);
     SELECT LAST_INSERT_ID() INTO VID_WIKI;
END/

--

DROP PROCEDURE IF EXISTS PWORD/

CREATE PROCEDURE PWORD (IN VWORD VARCHAR(50), IN VLEMMA VARCHAR(50), OUT VID_WORD INT)

BEGIN
DECLARE VID_LEMMA INT DEFAULT 0;
DECLARE VID_SYNONYM INT DEFAULT 0 ;

    INSERT INTO LEMMA (id_lemma,lemma) VALUES (NULL,VLEMMA);  
    SELECT LAST_INSERT_ID() INTO VID_LEMMA;
	
    INSERT INTO WORD (id_word,word,id_lemma,id_synonym) VALUES (NULL, VWORD, VID_LEMMA, NULL);
    SELECT LAST_INSERT_ID() INTO VID_WORD;

END/   

DELIMITER ;

