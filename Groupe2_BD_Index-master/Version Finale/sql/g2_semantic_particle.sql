DELIMITER /
DROP PROCEDURE IF EXISTS SEMANTIC_PARTICLE/

CREATE PROCEDURE SEMANTIC_PARTICLE(IN v_id_article VARCHAR(50), IN v_rate_positivity FLOAT, IN v_rate_negativity FLOAT,
  IN v_rate_joy FLOAT,  IN v_rate_fear FLOAT,  IN v_rate_sadness FLOAT, IN v_rate_angry FLOAT,
  IN v_rate_surprise FLOAT, IN v_rate_disgust FLOAT, IN v_rate_subjectivity FLOAT, IN v_is_positive BOOLEAN)
BEGIN

  DECLARE v_count INT;

  SELECT count(*) INTO v_count
  FROM article
  WHERE id_article = v_id_article;

  IF (v_count = 1) THEN

    UPDATE article
    SET
      rate_positivity = v_rate_positivity,
      rate_negativity= v_rate_negativity,
      rate_joy= v_rate_joy,
      rate_fear= v_rate_fear,
      rate_sadness= v_rate_sadness,
      rate_angry= v_rate_angry,
      rate_surprise= v_rate_surprise,
      rate_disgust= v_rate_disgust,
      rate_subjectivity  = v_rate_subjectivity,
      is_positive =  v_is_positive
    WHERE id_article = v_id_article;

  END IF;

END/