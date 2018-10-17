#-- Group 2

DROP PROCEDURE IF EXISTS update_mv_number_article_week_label;

DELIMITER |
#--
#-- Procedure to update the number of articles per week and per theme
#--
CREATE IF NOT EXISTS PROCEDURE `update_mv_number_article_week_label`()
BEGIN
   TRUNCATE mv_number_article_week_label;

   INSERT INTO mv_number_article_week_label
   Select b.id_label, COUNT(b.id_article) as number_article
    From belong b, article ar
    Where b.id_article = ar.id_article AND TO_DAYS(Date(Now()))-7 <= TO_DAYS(ar.date_publication) AND TO_DAYS(ar.date_publication) < TO_DAYS (Date(Now()))
	GROUP BY b.id_label;
END |

DELIMITER ;