DELIMITER |
CREATE TRIGGER TARTICLE BEFORE INSERT
ON ARTICLE FOR EACH ROW
BEGIN
    IF id_article IS  NULL   
      THEN
        SELECT'La clé ne doit pas etre nulle' ;
    END IF;
     Select count(*) into nb1
    from ARTICLE M , JOURNAL M1
    where M.id_racine= M1.id_racine ;
    IF nb1== 0   
      THEN
        SELECT'La clé étrangère liée a l'article n'existe pas' ;
    END IF;
    Select count(*) into nb2
    from ARTICLE M ,POSITIVITE M1
    where M.id_positivite= M1.id_entite ;
    IF nb2== 0   
      THEN
        SELECT'La clé étrangère liée a la positivite n'existe pas' ;
    END IF;
    Select count(*) into nb3
    from ARTICLE M ,CLASSIFICATION M1
    where M.id_classe= M1.id_classe ;
    IF nb3== 0   
      THEN
        SELECT'La clé étrangère liée a la classification n'existe pas' ;
    END IF;
END |
DELIMITER ;
