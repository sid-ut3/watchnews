DELIMITER /
DROP PROCEDURE IF EXISTS SEMANTIC_PWORD/

CREATE PROCEDURE SEMANTIC_PWORD(IN v_id_article VARCHAR(50), IN v_position INT, IN v_word VARCHAR(25), IN v_file_wiki VARCHAR(255))
  BEGIN

    DECLARE v_id_word INT;
    DECLARE v_id_wiki INT;
    DECLARE v_position_up INT;


    SELECT id_word INTO v_id_word
    FROM word
    WHERE word = v_word;

    SELECT id_wiki INTO v_id_wiki
    FROM wiki
    WHERE file_wiki = v_file_wiki;

    # If the word doesn't exist, we can't add a wiki
    IF (v_id_word IS NOT NULL AND v_id_wiki IS NULL AND LENGTH(v_file_wiki) > 2) THEN
      INSERT INTO wiki(id_wiki,file_wiki) VALUES(NULL,v_file_wiki);
      SELECT LAST_INSERT_ID() INTO v_id_wiki;
    END IF;

    # If the word doesn't exist, we get the id_word for the article and the postion choosen
    IF (v_id_word IS NULL) THEN
      SELECT W.id_word  INTO v_id_word FROM position_word PW,word W
      WHERE PW.id_word = W.id_word AND PW.id_article = v_id_article
            AND PW.position = v_position;
    END IF;

    SELECT position INTO v_position_up FROM position_word WHERE id_article = v_id_article AND position = v_position;

    IF (v_position_up IS NOT NULL) THEN
      UPDATE position_word
      SET
        id_word = v_id_word,
        id_wiki = v_id_wiki
      WHERE id_article = v_id_article
            AND position = v_position;
    END IF;

  END/