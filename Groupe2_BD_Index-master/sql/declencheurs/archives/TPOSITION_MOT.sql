DELIMITER |
CREATE TRIGGER Tposition_word BEFORE INSERT
ON position_word FOR EACH ROW
BEGIN
    DECLARE nb1 INT;
    DECLARE nb2 INT;
    DECLARE nb3 INT;
    DECLARE nb4 INT;
    DECLARE nb5 INT;
    DECLARE nb6 INT;
    DECLARE CAPACITY_ERROR CONDITION FOR SQLSTATE '99991';  
    DECLARE CLE_ETRANGERE1 CONDITION FOR SQLSTATE '99990';
    DECLARE CLE_ETRANGERE2 CONDITION FOR SQLSTATE '99992';
    DECLARE CLE_ETRANGERE3 CONDITION FOR SQLSTATE '99993';
    DECLARE CLE_ETRANGERE4 CONDITION FOR SQLSTATE '99994';
    DECLARE CLE_ETRANGERE5 CONDITION FOR SQLSTATE '99995';
    DECLARE CLE_ETRANGERE6 CONDITION FOR SQLSTATE '99996';
    SIGNAL CLE_ETRANGERE1 SET MESSAGE_TEXT = "Foreign key of Word doesn't exist";
    SIGNAL CLE_ETRANGERE2 SET MESSAGE_TEXT = "Foreign key of Entity doesn't exist";
    SIGNAL CLE_ETRANGERE3 SET MESSAGE_TEXT = "Foreign key of POS_TAGGING doesn't exist";
    SIGNAL CLE_ETRANGERE4 SET MESSAGE_TEXT = "Foreign key of ARTICLE doesn't exist";
    SIGNAL CLE_ETRANGERE5 SET MESSAGE_TEXT = "Foreign key of SYNONYME doesn't exist";
    SIGNAL CLE_ETRANGERE6 SET MESSAGE_TEXT = "Foreign key of WIKI doesn't exist";
    SIGNAL CAPACITY_ERROR SET MESSAGE_TEXT = "Key Cannot be empty";
    IF (id_position IS  NULL) THEN  
      SIGNAL CAPACITY_ERROR ;
    END IF;

    SELECT count(PW.id_position) INTO nb1
    FROM position_word PW, word W
    WHERE PW.id_position = W.id_position;
    IF (nb1 = 0) THEN
        SIGNAL CLE_ETRANGERE1;
    END IF;

    SELECT count(PW.id_entity) INTO nb2
    FROM position_word PW, entity E
    WHERE PW.id_entity = E.id_entity;
    IF (nb2 = 0 ) THEN
        SIGNAL CLE_ETRANGERE2;
    END IF;

    SELECT count(PW.id_post_tag) INTO nb3
    FROM position_word PW ,POS_TAGGING PT
    WHERE PW.id_pos_tag = PT.id_pos_tag;
    IF (nb3 = 0) THEN
        SIGNAL CLE_ETRANGERE3;
    END IF;

    SELECT count(PW.id_article) INTO nb4
    FROM position_word PW, article A
    WHERE PW.id_article = A.id_article;
    IF (nb4 = 0) THEN
        SIGNAL CLE_ETRANGERE4;
    END IF;
    
    SELECT count(PW.id_synonym) INTO nb5
    FROM position_word PW ,SYNONYM S
    WHERE PW.id_synonym = S.id_synonym;
    IF (nb5 = 0) THEN
        SIGNAL CLE_ETRANGERE5;
    END IF;

    SELECT count(PW.id_wiki) INTO nb6
    FROM position_word PW ,wiki W
    WHERE PW.id_wiki = W.id_wiki;
    IF (nb6 = 0) THEN
        SIGNAL CLE_ETRANGERE6;
    END IF;
END |
DELIMITER ;






