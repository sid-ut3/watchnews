#-- Group 2

#-- Table of tf per period

CREATE TABLE IF NOT EXISTS `mv_term_frequency_period` (
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `frequency` int(11) NOT NULL,
  PRIMARY KEY (`id_word`,`id_article`),
  KEY `fk_article_tf_period` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_term_frequency_period`
  ADD CONSTRAINT `fk_article_tf_period` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;

#-- Table of numbers of articles per period

CREATE TABLE IF NOT EXISTS `nb_articles_period` (
  `nb_articles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#-- Table of article numbers by word

CREATE TABLE IF NOT EXISTS `nb_articles_word_period` (
  `id_word` int(11) NOT NULL,
  `nb_articles` int(11) NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `nb_articles_word_period`
  ADD CONSTRAINT `fk_word_nb_articles_word_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;
  
#-- Table of idf per period

CREATE TABLE IF NOT EXISTS `mv_inverse_document_frequency_period` (
  `id_word` int(11) NOT NULL,
  `idf` float NOT NULL,
  PRIMARY KEY (`id_word`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_inverse_document_frequency_period`
  ADD CONSTRAINT `fk_word_idf_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;


#-- Table of tf_idf per period

CREATE TABLE IF NOT EXISTS `mv_tf_idf_period` (
  `date_publication` date NOT NULL,
  `id_word` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  `tf` int(11) NOT NULL,
  `tf_idf` float NOT NULL,
  PRIMARY KEY (`date_publication`,`id_word`,`id_article`),
  KEY `fk_word_tf_idf_period` (`id_word`),
  KEY `fk_article_tf_idf_period` (`id_article`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `mv_tf_idf_period`
  ADD CONSTRAINT `fk_article_tf_idf_period` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_word_tf_idf_period` FOREIGN KEY (`id_word`) REFERENCES `word` (`id_word`) ON DELETE CASCADE ON UPDATE CASCADE;
