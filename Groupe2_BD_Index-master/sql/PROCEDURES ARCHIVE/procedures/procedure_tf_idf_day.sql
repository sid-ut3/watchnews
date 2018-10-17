#-- Group 2

#-- Procedure to update the tf per day

DROP PROCEDURE IF EXISTS update_mv_term_frequency_day;
DELIMITER |
CREATE PROCEDURE `update_mv_term_frequency_day`()
BEGIN
   TRUNCATE mv_term_frequency_day;

   INSERT INTO mv_term_frequency_day
   Select a.date_publication, w.id_word, a.id_article, COUNT(id_position) as frequency
    From article a, position_word pw, word w
    Where a.id_article = pw.id_article AND pw.id_word = w.id_word AND TO_DAYS(Date(Now()))-31 <= TO_DAYS(a.date_publication) AND TO_DAYS(a.date_publication) < TO_DAYS (Date(Now()))
    GROUP BY a.date_publication, w.id_word, a.id_article;
    
    CALL update_nb_articles();
END |
DELIMITER ;

#-- Procedure to update the number of articles per day

DROP PROCEDURE IF EXISTS update_nb_articles;
DELIMITER |

CREATE PROCEDURE `update_nb_articles`()
BEGIN
   TRUNCATE nb_articles;

   INSERT INTO nb_articles
   Select date_publication, COUNT(DISTINCT id_article) as nb_article
    From mv_term_frequency_day
    GROUP BY date_publication;
    
    CALL update_nb_articles_word();
END |
DELIMITER ;

#-- Procedure to update the number of articles by word 

DROP PROCEDURE IF EXISTS update_nb_articles_word;
DELIMITER |

CREATE PROCEDURE `update_nb_articles_word`()
BEGIN
   TRUNCATE nb_articles_word;

   INSERT INTO nb_articles_word
   Select date_publication, id_word, COUNT(id_article) as nb_article
    From mv_term_frequency_day
    GROUP BY date_publication, id_word;
    
    CALL update_mv_inverse_document_frequency_day();
END |
DELIMITER ;

#-- Procedure to update idf per day

DROP PROCEDURE IF EXISTS update_mv_inverse_document_frequency_day;
DELIMITER |

CREATE PROCEDURE `update_mv_inverse_document_frequency_day`()
BEGIN
   TRUNCATE mv_inverse_document_frequency_day;

   INSERT INTO mv_inverse_document_frequency_day
   Select naw.date_publication, naw.id_word,LOG10( na.nb_article/naw.nb_articles)
    From nb_articles na, nb_articles_word naw
    Where naw.date_publication = na.date_publication;
    
    CALL update_mv_tf_idf_day();
END |
DELIMITER ;

#-- Procedure to update tf_idf per day

DROP PROCEDURE IF EXISTS update_mv_tf_idf_day;
DELIMITER |

CREATE PROCEDURE `update_mv_tf_idf_day`()
BEGIN
   TRUNCATE mv_tf_idf_day;

   INSERT INTO mv_tf_idf_day
   Select tf.date_publication, tf.id_word, tf.id_article, tf.frequency, tf.frequency*idf.idf
    From mv_term_frequency_day tf, mv_inverse_document_frequency_day idf
    Where tf.date_publication = idf.date_publication AND tf.id_word = idf.id_word;
END |
DELIMITER ;

