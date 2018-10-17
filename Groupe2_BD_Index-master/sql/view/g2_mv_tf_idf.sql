#-- Group 2


#-- Structure of the materialized view 'mv_tf_idf'

CREATE TABLE IF NOT EXISTS `mv_tf_idf` (
  `id_article` VARCHAR(50) NOT NULL,
  `id_lemma` int(11) NOT NULL,
  `tf_idf` float NOT NULL,
  PRIMARY KEY (`id_article`,`id_lemma`),
  KEY `fk_lemma_tf_idf` (`id_lemma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



#-- Constraints for the materialized view 'mv_tf_idf'


ALTER TABLE `mv_tf_idf`
  ADD CONSTRAINT `fk_lemma_tf_idf` FOREIGN KEY (`id_lemma`) REFERENCES `lemma` (`id_lemma`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_article_tf_idf` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`) ON DELETE CASCADE ON UPDATE CASCADE;