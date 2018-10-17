#-- Group 2

#--
#-- Structure of the materialized view `mv_number_article_week` to store the number of articles published per week and  per theme
#--

CREATE TABLE IF NOT EXISTS `mv_number_article_week_label` (
  `id_label` int(11) NOT NULL,
  `number_article` int(11) NOT NULL,
  PRIMARY KEY (`id_label`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#--
#-- Foreign key constraint
#--

ALTER TABLE `mv_number_article_week_label`
  ADD CONSTRAINT `fk_article_label` FOREIGN KEY (`id_label`) REFERENCES `label` (`id_label`) ON DELETE CASCADE ON UPDATE CASCADE;