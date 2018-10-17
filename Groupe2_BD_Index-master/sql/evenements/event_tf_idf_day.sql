#-- Group 2

#-- Needed for launching events

SET GLOBAL event_scheduler = ON;

#-- Event triggering the procedure to update tf_idf per day

DELIMITER |

CREATE EVENT IF NOT EXISTS `e_tf_idf_day` 
ON SCHEDULE EVERY 1 DAY STARTS '2018-01-11 00:30:00' 
ON COMPLETION PRESERVE ENABLE 
DO CALL update_mv_term_frequency_day() |

DELIMITER ;