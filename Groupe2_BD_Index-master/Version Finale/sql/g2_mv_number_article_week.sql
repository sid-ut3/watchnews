#-- Group 2

#--
#-- Structure of the materialized view `mv_number_article_week` to store the number of articles published per week
#--

CREATE TABLE IF NOT EXISTS `mv_number_article_week` (
  `number_article` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
