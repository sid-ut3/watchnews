  DELIMITER |
  CREATE TRIGGER TMOT_RACINE BEFORE INSERT
  ON MOT_RACINE FOR EACH ROW
  BEGIN
       DECLARE nb1 int ;
       DECLARE CLE_ETRANGERE CONDITION FOR SQLSTATE '99990';
       SIGNAL CLE_ETRANGERE SET MESSAGE_TEXT = 'la cle etrangere nexiste pas';
       DECLARE CAPACITY_ERROR CONDITION FOR SQLSTATE '99991';  
       SIGNAL CAPACITY_ERROR SET MESSAGE_TEXT = 'la clé ne peut pas etre nulle';
       IF (id_racine is NULL) THEN
		SIGNAL CAPACITY_ERROR;
	   END IF;

       Select count(*) into nb1
    from MOT M ,MOT_RACINE M1
    where M.id_racine= M1.id_racine ;
    IF (nb1= 0 )  THEN
        SIGNAL CLE_ETRANGERE ;
    END IF;
  END |
  DELIMITER ;
