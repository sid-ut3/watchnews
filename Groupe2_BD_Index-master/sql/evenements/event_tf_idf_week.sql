#-- Group 2

#-- Needed for launching events

SET GLOBAL event_scheduler = ON;

#-- Event triggering the procedure to update tf_idf per week

DELIMITER |

CREATE EVENT IF NOT EXISTS `e_tf_idf_week` 
ON SCHEDULE EVERY 1 DAY STARTS '2018-01-10 01:00:00' 
ON COMPLETION PRESERVE ENABLE 
DO CALL update_mv_term_frequency_week() |

DELIMITER ;