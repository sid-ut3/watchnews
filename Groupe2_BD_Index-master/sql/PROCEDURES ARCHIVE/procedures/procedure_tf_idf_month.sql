#-- Group 2

#-- Procedure to update the tf per month

DROP PROCEDURE IF EXISTS update_mv_term_frequency_month;
DELIMITER |

CREATE PROCEDURE `update_mv_term_frequency_month`()
BEGIN
   TRUNCATE mv_term_frequency_month;

   INSERT INTO mv_term_frequency_month
   Select w.id_word, a.id_article, COUNT(id_position) as frequency
    From article a, position_word pw, word w
    Where a.id_article = pw.id_article AND pw.id_word = w.id_word AND TO_DAYS(Date(Now()))- 31 <= TO_DAYS(a.date_publication) AND TO_DAYS(a.date_publication) < TO_DAYS (Date(Now()))
    GROUP BY w.id_word,a.id_article;
    
    CALL update_nb_articles_month();
END |
DELIMITER ;

#-- Procedure to update the number of articles per month

DROP PROCEDURE IF EXISTS update_nb_articles_month;
DELIMITER |

CREATE PROCEDURE `update_nb_articles_month`()
BEGIN
   TRUNCATE nb_articles_month;

   INSERT INTO nb_articles_month
   Select COUNT(DISTINCT id_article) as nb_article
    From mv_term_frequency_month;
    
    CALL update_nb_articles_word_month();
END |
DELIMITER ;

#-- Procedure to update the number of articles by word 

DROP PROCEDURE IF EXISTS update_nb_articles_word_month;
DELIMITER |

CREATE PROCEDURE `update_nb_articles_word_month`()
BEGIN
   TRUNCATE nb_articles_word_month;

   INSERT INTO nb_articles_word_month
   Select id_word, COUNT(id_article) as nb_article
    From mv_term_frequency_month
    GROUP BY id_word;
    
    CALL update_mv_inverse_document_frequency_month();
END |
DELIMITER ;

#-- Procedure to update idf per month

DROP PROCEDURE IF EXISTS update_mv_inverse_document_frequency_month;
DELIMITER |

CREATE PROCEDURE `update_mv_inverse_document_frequency_month`()
BEGIN
   TRUNCATE mv_inverse_document_frequency_month;

   INSERT INTO mv_inverse_document_frequency_month
   Select naw.id_word, LOG10(na.nb_articles/naw.nb_articles)
    From nb_articles_month na, nb_articles_word_month naw;
    
    CALL update_mv_tf_idf_month();
END |
DELIMITER ;

#-- Procedure to update tf_idf per month

DROP PROCEDURE IF EXISTS update_mv_tf_idf_month;
DELIMITER |

CREATE PROCEDURE `update_mv_tf_idf_month`()
BEGIN
   TRUNCATE mv_tf_idf_month;

   INSERT INTO mv_tf_idf_month
   Select a.date_publication, tf.id_word, tf.id_article, tf.frequency, tf.frequency*idf.idf
    From mv_term_frequency_month tf, mv_inverse_document_frequency_month idf, article a
    Where  tf.id_word = idf.id_word AND a.id_article = tf.id_article;
END |
DELIMITER ;