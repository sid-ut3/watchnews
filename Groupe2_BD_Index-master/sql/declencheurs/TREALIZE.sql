DELIMITER |
CREATE TRIGGER TREALIZE BEFORE INSERT
ON realize FOR EACH ROW

BEGIN

   DECLARE compteur1 INT;
   DECLARE CLE_ETRANGERE CONDITION FOR SQLSTATE '99995';
   DECLARE compteur2 INT;
   DECLARE CLE_ETRANGERE2 CONDITION FOR SQLSTATE '99996';

   SELECT COUNT(A.id_author) INTO compteur1
   FROM author A
   WHERE NEW.id_author IN (SELECT id_author FROM author);
   
   IF (compteur1=0)  THEN
	 SIGNAL CLE_ETRANGERE SET MESSAGE_TEXT = "AUTHOR's foreign key does not exist";
   END IF;
   
   SELECT COUNT(AR.id_article) INTO compteur2
   FROM article AR
   WHERE NEW.id_article IN (SELECT id_article FROM article);
   
   IF (compteur2=0)  THEN
	 SIGNAL CLE_ETRANGERE2 SET MESSAGE_TEXT = "ARTICLE's foreign key does not exist";
   END IF;
   
END |
DELIMITER ;