DROP PROCEDURE IF EXISTS PSYNONYM;
DELIMITER |
CREATE PROCEDURE PSYNONYM (IN vsynonym VARCHAR(50), IN vword VARCHAR(50))   
BEGIN
	DECLARE vid_synonym INT DEFAULT 0;

	INSERT INTO synonym (id_synonym, synonym) VALUES (NULL,vsynonym);
    SELECT LAST_INSERT_ID() INTO vid_synonym;

    UPDATE word
	SET word.id_synonym = vid_synonym
	WHERE word.word = vword;

END|         

DELIMITER ;
CALL PSYNONYM("ESSAI","TEST");
CALL PSYNONYM("MACRON","PRESIDENT");
