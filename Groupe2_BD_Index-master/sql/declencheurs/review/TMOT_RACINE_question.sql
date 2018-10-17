DELIMITER |
CREATE TRIGGER TMOT_RACINE BEFORE INSERT
ON MOT_RACINE FOR EACH ROW
BEGIN
    IF id_racine IS  NULL   
      THEN
        SELECT'La clé ne doit pas etre nulle' ;
    END IF;
    Select count(*) into nb1
    from MOT_RACINE M ,MOT M1
    where M.id_mot= M1.id_mot ;
    IF nb1== 0   
      THEN
        SELECT'La clé étrangère n'existe pas' ;
    END IF;
END |
DELIMITER ;
