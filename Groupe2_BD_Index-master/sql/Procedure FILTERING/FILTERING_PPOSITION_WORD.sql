DELIMITER /
DROP PROCEDURE IF EXISTS FILTERING_PPOSITION_WORD/

CREATE PROCEDURE FILTERING_PPOSITION_WORD (IN v_position INT, IN v_word VARCHAR(25), IN v_lemma VARCHAR(25),IN v_title BOOLEAN, IN v_pos_tag VARCHAR(25), IN v_type_entity VARCHAR(25), IN v_id_article INT)

	BEGIN
		DECLARE v_id_word INT;
		DECLARE v_id_entity INT;
		DECLARE v_id_pos_tag INT;
		DECLARE v_id_lemma INT;

		SELECT id_word INTO v_id_word
		FROM word
		WHERE word = v_word;

		SELECT id_entity INTO v_id_entity
		FROM entity
		WHERE type_entity = v_type_entity;

		SELECT id_pos_tag INTO v_id_pos_tag
		FROM pos_tagging
		WHERE pos_tag = v_pos_tag;

		SELECT id_lemma INTO v_id_lemma
		FROM lemma
		WHERE lemma = v_lemma;

		IF (v_id_lemma IS NULL AND v_lemma IS NOT NULL)  THEN
			INSERT INTO lemma (id_lemma, lemma) VALUES (NULL, v_lemma);
			SELECT LAST_INSERT_ID() INTO v_id_lemma;
		END IF;

		IF (v_id_word IS NULL AND v_word IS NOT NULL)  THEN
			INSERT INTO word (id_word, word,id_lemma) VALUES (NULL, v_word,v_id_lemma);
			SELECT LAST_INSERT_ID() INTO v_id_word;
		ELSE
			UPDATE word SET id_lemma = v_id_lemma WHERE id_word = v_id_word;
		END IF;

		IF (v_id_entity IS NULL AND v_type_entity IS NOT NULL)  THEN
			INSERT INTO entity (id_entity, type_entity) VALUES (NULL, v_type_entity);
			SELECT LAST_INSERT_ID() INTO v_id_entity;
		END IF;

		IF (v_id_pos_tag IS NULL AND v_pos_tag IS NOT NULL)  THEN
			INSERT INTO pos_tagging (id_pos_tag, pos_tag) VALUES (NULL, v_pos_tag);
			SELECT LAST_INSERT_ID() INTO v_id_pos_tag;
		END IF;

		INSERT INTO position_word (position,title,id_word,id_entity,id_pos_tag,id_article)
		VALUES (v_position, v_title, v_id_word, v_id_entity, v_id_pos_tag, v_id_article);

	END/