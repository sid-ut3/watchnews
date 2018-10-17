DROP PROCEDURE IF EXISTS PBELONG;
DELIMITER |
CREATE PROCEDURE PBELONG (IN v_id_article INT, IN v_label VARCHAR(25),IN v_strongest_label BOOLEAN)
BEGIN

    DECLARE v_id_label INT DEFAULT 0;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_id_label = NULL;

    SELECT label.id_label INTO v_id_label
    FROM label
    WHERE label.label = v_label;

    IF (v_id_label IS NULL)  THEN
        INSERT INTO label(id_label, label) VALUES(NULL, v_label);
        SELECT LAST_INSERT_ID() INTO v_id_label;
    END IF;

    INSERT INTO belong(id_article,id_label,strongest_label) VALUES(v_id_article , v_id_label, v_strongest_label);

END|         

DELIMITER ;
