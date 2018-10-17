DROP PROCEDURE IF EXISTS PWORD;
DELIMITER |
CREATE PROCEDURE PWORD (IN vword VARCHAR(50), IN vlemma VARCHAR(50), OUT vid_word INT)

BEGIN
DECLARE vid_lemma INT DEFAULT 0;
DECLARE vid_synonym INT DEFAULT 0 ;

    INSERT INTO lemma (id_lemma,lemma) VALUES (NULL,vlemma);  
    SELECT LAST_INSERT_ID() INTO vid_lemma;
	
    INSERT INTO word (id_word,word,id_lemma,id_synonym) VALUES (NULL, vword, vid_lemma, NULL);
    SELECT LAST_INSERT_ID() INTO vid_word;

END|         

DELIMITER ;

CALL pword("VBA", "PYTHON", @id_word);
CALL pword("PHP", "JAVA", @id_word); 
SELECT @id_word;
