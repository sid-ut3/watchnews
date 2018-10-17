#-- Group 2

#-- Needed for launching events

SET GLOBAL event_scheduler = ON;

DELIMITER |
#--
#-- Event triggering the procedure to update the article number of the week
#--
CREATE EVENT IF NOT EXISTS `e_article_number_week` 
	ON SCHEDULE EVERY 1 WEEK STARTS '2018-01-08 00:00:05' 
	ON COMPLETION PRESERVE ENABLE 
	DO CALL update_mv_number_article_week();
	|
DELIMITER ;