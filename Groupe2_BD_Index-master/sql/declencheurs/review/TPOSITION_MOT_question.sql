DELIMITER |
CREATE TRIGGER TPOSITION_MOT BEFORE INSERT
ON POSITION_MOT FOR EACH ROW
BEGIN
    IF id_position IS  NULL   
      THEN
        SELECT'La clé ne doit pas etre nulle' ;
    END IF;
    Select count(*) into nb1
    from POSITION_MOT M ,MOT_RACINE M1
    where M.id_racine= M1.id_racine ;
    IF nb1== 0   
      THEN
        SELECT'La clé étrangère liée a la racine n'existe pas' ;
    END IF;
    Select count(*) into nb2
    from POSITION_MOT M ,entite M1
    where M.id_entite= M1.id_entite ;
    IF nb2== 0   
      THEN
        SELECT'La clé étrangère liée a l'entité n'existe pas' ;
    END IF;
    Select count(*) into nb3
    from POSITION_MOT M ,POS_TAGGING M1
    where M.pos_tag= M1.pos_tag ;
    IF nb3== 0   
      THEN
        SELECT'La clé étrangère liée a la position n'existe pas' ;
    END IF;
    Select count(*) into nb4
    from POSITION_MOT M ,article M1
    where M.id_article= M1.id_article ;
    IF nb4== 0   
      THEN
        SELECT'La clé étrangère liée a l'article n'existe pas' ;
    END IF;
END |
DELIMITER ;
