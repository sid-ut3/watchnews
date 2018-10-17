#-- Group 2

#-- Procedure to update the tf per week

DROP PROCEDURE IF EXISTS update_mv_term_frequency_week;
DELIMITER |

CREATE PROCEDURE `update_mv_term_frequency_week`()
BEGIN
   TRUNCATE mv_term_frequency_week;

   INSERT INTO mv_term_frequency_week
   Select w.id_word, a.id_article, COUNT(id_position) as frequency
    From article a, position_word pw, word w
    Where a.id_article = pw.id_article AND pw.id_word = w.id_word AND TO_DAYS(Date(Now()))-7 <= TO_DAYS(a.date_publication) AND TO_DAYS(a.date_publication) < TO_DAYS (Date(Now()))
    GROUP BY w.id_word,a.id_article;
    
    CALL update_nb_articles_week();
END |
DELIMITER ;

#-- Procedure to update the number of articles per week

DROP PROCEDURE IF EXISTS update_nb_articles_week;
DELIMITER |

CREATE PROCEDURE `update_nb_articles_week`()
BEGIN
   TRUNCATE nb_articles_week;

   INSERT INTO nb_articles_week
   Select COUNT(DISTINCT id_article) as nb_article
    From mv_term_frequency_week;
    
    CALL update_nb_articles_word_week();
END |
DELIMITER ;

#-- Procedure to update the number of articles by word 

DROP PROCEDURE IF EXISTS update_nb_articles_word_week;
DELIMITER |

CREATE PROCEDURE `update_nb_articles_word_week`()
BEGIN
   TRUNCATE nb_articles_word_week;

   INSERT INTO nb_articles_word_week
   Select id_word, COUNT(id_article) as nb_article
    From mv_term_frequency_week
    GROUP BY id_word;
    
    CALL update_mv_inverse_document_frequency_week();
END |
DELIMITER ;

#-- Procedure to update idf per week

DROP PROCEDURE IF EXISTS update_mv_inverse_document_frequency_week;
DELIMITER |

CREATE PROCEDURE `update_mv_inverse_document_frequency_week`()
BEGIN
   TRUNCATE mv_inverse_document_frequency_week;

   INSERT INTO mv_inverse_document_frequency_week
   Select naw.id_word, LOG10(na.nb_articles/naw.nb_articles)
    From nb_articles_week na, nb_articles_word_week naw;
    
    CALL update_mv_tf_idf_week();
END |
DELIMITER ;

#-- Procedure to update tf_idf per week

DROP PROCEDURE IF EXISTS update_mv_tf_idf_week;
DELIMITER |

CREATE PROCEDURE `update_mv_tf_idf_week`()
BEGIN
   TRUNCATE mv_tf_idf_week;

   INSERT INTO mv_tf_idf_week
   Select a.date_publication, tf.id_word, tf.id_article,tf.frequency, tf.frequency*idf.idf
    From mv_term_frequency_week tf, mv_inverse_document_frequency_week idf, article a
    Where  tf.id_word = idf.id_word AND a.id_article = tf.id_article;
    
END |
DELIMITER ;