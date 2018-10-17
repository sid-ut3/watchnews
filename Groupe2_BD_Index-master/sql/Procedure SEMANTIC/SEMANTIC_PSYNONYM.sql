DELIMITER /
DROP PROCEDURE IF EXISTS SEMANTIC_PSYNONYM/

CREATE PROCEDURE SEMANTIC_PSYNONYM (IN v_id_article INT, IN v_position INT,v_synonym VARCHAR(25))
	BEGIN

		DECLARE v_id_synonym INT;
		
		SELECT s.id_synonym INTO v_id_synonym
		FROM synonym s
		WHERE s.synonym = v_synonym;

		IF (v_id_synonym IS NULL AND v_synonym IS NOT NULL)  THEN
			INSERT INTO synonym (id_synonym, synonym) VALUES (NULL, v_synonym);
			SELECT LAST_INSERT_ID() INTO v_id_synonym;
		END IF;

		INSERT INTO common(id_synonym,position,id_article) VALUES (v_id_synonym,v_position,v_id_article);
		
		COMMIT;

	END/