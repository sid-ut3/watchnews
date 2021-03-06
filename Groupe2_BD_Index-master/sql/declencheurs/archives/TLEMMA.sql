﻿DELIMITER |
CREATE TRIGGER TLEMMA BEFORE INSERT
ON LEMMA FOR EACH ROW
BEGIN
   DECLARE CAPACITY_ERROR CONDITION FOR SQLSTATE '99991';  
   SIGNAL CAPACITY_ERROR SET MESSAGE_TEXT = 'The primary key cannot be empty';
   IF (id_lemma is NULL) THEN
	SIGNAL CAPACITY_ERROR;
   END IF;

END |
DELIMITER ;
