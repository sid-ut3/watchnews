#-- Group 2

#-- Procedure to update materialized view 'mv_tf_idf'


DROP PROCEDURE IF EXISTS update_mv_tf_idf;
DELIMITER |
CREATE PROCEDURE `update_mv_tf_idf`(IN v_id_article VARCHAR(50), IN v_lemma VARCHAR(25), IN v_tf_idf FLOAT(11))
BEGIN
	DECLARE v_id_lemma INT(11);
    DECLARE v_test_tf_idf FLOAT(11);
    
    SET v_id_lemma = get_id_lemma(v_lemma);
    
    SELECT tf_idf INTO v_test_tf_idf
    FROM mv_tf_idf
    WHERE id_article = v_id_article AND id_lemma = v_id_lemma;
    
    IF (v_test_tf_idf IS NOT NULL) THEN
    
    	UPDATE mv_tf_idf
        SET tf_idf = v_tf_idf
        WHERE id_article = v_id_article AND id_lemma = v_id_lemma;
      
    ELSE
    
    	INSERT INTO mv_tf_idf (id_article, id_lemma, tf_idf)
        VALUES(v_id_article, v_id_lemma, v_tf_idf);
        
    END IF;
        
   
END |
DELIMITER ;