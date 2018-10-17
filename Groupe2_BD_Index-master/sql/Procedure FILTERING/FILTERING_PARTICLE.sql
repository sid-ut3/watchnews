DELIMITER /
DROP PROCEDURE IF EXISTS FILTERING_PARTICLE/

CREATE PROCEDURE FILTERING_PARTICLE (IN v_date_publication DATE,IN v_name_newspaper VARCHAR(25), OUT v_id_article INT)

BEGIN

	DECLARE v_id_newspaper INT;

	SELECT id_newspaper INTO v_id_newspaper
    FROM newspaper
    WHERE newspaper.name_newspaper = v_name_newspaper;

    IF (v_id_newspaper IS NULL AND v_name_newspaper IS NOT NULL)  THEN

		INSERT INTO newspaper(id_newspaper, name_newspaper, link_newspaper, link_logo)
		VALUES(NULL, v_name_newspaper, NULL, NULL);

    	SELECT LAST_INSERT_ID() INTO v_id_newspaper;

	END IF;

	INSERT INTO article(id_article,date_publication,id_newspaper) VALUES(NULL,v_date_publication,v_id_newspaper);

	SELECT LAST_INSERT_ID() INTO v_id_article;

    COMMIT;
END/