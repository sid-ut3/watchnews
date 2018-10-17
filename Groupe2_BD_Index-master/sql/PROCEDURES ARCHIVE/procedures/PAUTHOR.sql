DELIMITER /
DROP PROCEDURE IF EXISTS pauthor/

CREATE PROCEDURE pauthor (IN vid_article INT, IN vsurname_author VARCHAR(50), IN vfirstname_author VARCHAR(50))   
BEGIN
	
	DECLARE count_id_ INT DEFAULT 0;
	DECLARE vid_author INT DEFAULT 0;
	
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET vid_author = NULL;

	SELECT author.id_author INTO vid_author
	FROM author 
	WHERE author.surname_author = vsurname_author;

	IF (vid_author IS NULL)  THEN 
		INSERT INTO author (id_author, surname_author, firstname_author) VALUES (NULL, VSURNAME_AUTHOR,VFIRSTNAME_AUTHOR);
    	SELECT LAST_INSERT_ID() INTO vid_author;
	END IF;
	
    INSERT INTO realize (id_author, id_article) VALUES (VID_AUTHOR ,VID_ARTICLE);

END/

DELIMITER ; 