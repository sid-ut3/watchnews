#-- Group 2

#-- Function to get id_lemma with lemma

DELIMITER |
 
CREATE FUNCTION get_id_lemma(v_lemma VARCHAR(25)) RETURNS INT(11)
    DETERMINISTIC
BEGIN
    DECLARE v_id_lemma INT(11);
 
    SELECT id_lemma INTO v_id_lemma
	FROM lemma
	WHERE lemma = v_lemma;
	
	RETURN v_id_lemma;
END |

DELIMITER;