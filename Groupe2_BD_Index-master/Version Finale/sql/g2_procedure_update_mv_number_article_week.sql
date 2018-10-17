#-- Group 2

DROP PROCEDURE IF EXISTS update_mv_number_article_week;
DELIMITER |
#--
#-- Procedure to update the number of articles per week
#--
CREATE IF NOT EXISTS PROCEDURE `update_mv_number_article_week`()
BEGIN
   TRUNCATE mv_number_article_week;

   INSERT INTO mv_number_article_week
   Select COUNT(id_article) as number_article
    From article 
    Where TO_DAYS(Date(Now()))-7 <= TO_DAYS(date_publication) AND TO_DAYS(date_publication) < TO_DAYS (Date(Now()));
END |

DELIMITER ;