#-- Group 2

#-- Table of tf per day

CREATE TABLE IF NOT EXISTS `mv_term_frequency_day` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `frequency` int(11) NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_article`),
  KEY `fk_word_tf_day` (`id_word`),
  KEY `fk_article_tf_day` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_term_frequency_day`
  ADD CONSTRAINT `fk_article_tf_day` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_day` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;
  
#-- Table of numbers of articles per day

CREATE TABLE IF NOT EXISTS `nb_articles` (
  `date_publication` date NOT NULL,
  `nb_article` int(11) NOT NULL,
  PRIMARY KEY (`date_publication`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  
#-- Table of article numbers by word

CREATE TABLE IF NOT EXISTS `nb_articles_word` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `nb_articles` int(11) NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`),
  KEY `fk_word_nb_articles_word_day` (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `nb_articles_word`
  ADD CONSTRAINT `fk_word_nb_articles_word_day` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;
  
#-- Table of idf per day

CREATE TABLE IF NOT EXISTS `mv_inverse_document_frequency_day` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`),
  KEY `fk_word_idf` (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_inverse_document_frequency_day`
  ADD CONSTRAINT `fk_word_idf` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;
  
  
#-- Table of tf_idf per day 

CREATE TABLE IF NOT EXISTS `mv_tf_idf_day` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_articles` int(11) NOT NULL,
  `tf` int(11) NOT NULL,
  `tf_idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_articles`),
  KEY `fk_word_tf_idf_day` (`id_word`),
  KEY `fk_article_tf_idf_day` (`id_articles`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_tf_idf_day`
  ADD CONSTRAINT `fk_article_tf_idf_day` FOREIGN KEY (`id_articles`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_idf_day` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;