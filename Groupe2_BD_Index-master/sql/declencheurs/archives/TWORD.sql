﻿DELIMITER |
CREATE TRIGGER TWORD BEFORE UPDATE
ON WORD FOR EACH ROW
BEGIN
   DECLARE counter1 int;
   DECLARE CLE_ETRANGERE CONDITION FOR SQLSTATE '99996';
   
   SELECT COUNT(S.id_synonym) INTO counter2
   FROM SYNONYM S
   WHERE NEW.id_synonym IN (SELECT id_synonym FROM SYNONYM);
   
   IF (counter2=0)  THEN   
	 SIGNAL CLE_ETRANGERE2 SET MESSAGE_TEXT = "SYNONYM's Foreign key does not exist";
   END IF;
END |
DELIMITER ;