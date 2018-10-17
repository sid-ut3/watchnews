#-- Group 2

#-- Procedure to update the tf per period

DROP PROCEDURE IF EXISTS update_mv_term_frequency_period;
DELIMITER |

CREATE PROCEDURE `update_mv_term_frequency_period`(IN date_debut DATE, IN date_fin DATE)
BEGIN
   TRUNCATE mv_term_frequency_period;

   INSERT INTO mv_term_frequency_period
   Select w.id_word, a.id_article, COUNT(id_position) as frequency
    From article a, position_word pw, word w
    Where a.id_article = pw.id_article AND pw.id_word = w.id_word AND TO_DAYS(DATE(date_debut)) <= TO_DAYS(a.date_publication) AND TO_DAYS(a.date_publication) <= TO_DAYS (DATE(date_fin))
    GROUP BY w.id_word,a.id_article;
    
    CALL update_nb_articles_period();
END |
DELIMITER ;

#-- Procedure to update the number of articles per period

DROP PROCEDURE IF EXISTS update_nb_articles_period;
DELIMITER |

CREATE PROCEDURE `update_nb_articles_period`()
BEGIN
   TRUNCATE nb_articles_period;

   INSERT INTO nb_articles_period
   Select COUNT(DISTINCT id_article) as nb_article
    From mv_term_frequency_period;
    
    CALL update_nb_articles_word_period();
END |
DELIMITER ;

#-- Procedure to update the number of articles by word 

DROP PROCEDURE IF EXISTS update_nb_articles_word_period;
DELIMITER |

CREATE PROCEDURE `update_nb_articles_word_period`()
BEGIN
   TRUNCATE nb_articles_word_period;

   INSERT INTO nb_articles_word_period
   Select id_word, COUNT(id_article) as nb_article
    From mv_term_frequency_period
    GROUP BY id_word;
    
    CALL update_mv_inverse_document_frequency_period();
END |
DELIMITER ;

#-- Procedure to update idf per period

DROP PROCEDURE IF EXISTS update_mv_inverse_document_frequency_period;
DELIMITER |

CREATE PROCEDURE `update_mv_inverse_document_frequency_period`()
BEGIN
   TRUNCATE mv_inverse_document_frequency_period;

   INSERT INTO mv_inverse_document_frequency_period
   Select naw.id_word, LOG10(na.nb_articles/naw.nb_articles)
    From nb_articles_period na, nb_articles_word_period naw;
    
    CALL update_mv_tf_idf_period();
END |
DELIMITER ;

#-- Procedure to update tf_idf per period

DROP PROCEDURE IF EXISTS update_mv_tf_idf_period;
DELIMITER |

CREATE PROCEDURE `update_mv_tf_idf_period`()
BEGIN
   TRUNCATE mv_tf_idf_period;

   INSERT INTO mv_tf_idf_period
   Select a.date_publication, tf.id_word, tf.id_article,tf.frequency, tf.frequency*idf.idf
    From mv_term_frequency_period tf,  mv_inverse_document_frequency_period idf, article a
    Where  tf.id_word = idf.id_word AND a.id_article = tf.id_article;
    
    
END |
DELIMITER ;