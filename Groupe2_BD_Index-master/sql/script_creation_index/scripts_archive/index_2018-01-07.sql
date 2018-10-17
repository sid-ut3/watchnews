# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Hôte: 127.0.0.1 (MySQL 5.7.20)
# Base de données: index
# Temps de génération: 2018-01-06 23:40:02 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Affichage de la table article
# ------------------------------------------------------------

DROP TABLE IF EXISTS `article`;

CREATE TABLE `article` (
  `id_article` int(11) NOT NULL AUTO_INCREMENT,
  `date_publication` date DEFAULT NULL,
  `id_journal` int(11) NOT NULL,
  `id_classe` int(11) NOT NULL,
  `id_positivite` int(11) NOT NULL,
  PRIMARY KEY (`id_article`),
  KEY `FK_article_id_journal` (`id_journal`),
  KEY `FK_article_id_classe` (`id_classe`),
  KEY `FK_article_id_positivite` (`id_positivite`),
  CONSTRAINT `FK_article_id_classe` FOREIGN KEY (`id_classe`) REFERENCES `classification` (`id_classe`),
  CONSTRAINT `FK_article_id_journal` FOREIGN KEY (`id_journal`) REFERENCES `journal` (`id_journal`),
  CONSTRAINT `FK_article_id_positivite` FOREIGN KEY (`id_positivite`) REFERENCES `positivite` (`id_positivite`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

LOCK TABLES `article` WRITE;
/*!40000 ALTER TABLE `article` DISABLE KEYS */;

INSERT INTO `article` (`id_article`, `date_publication`, `id_journal`, `id_classe`, `id_positivite`)
VALUES
	(1,'2017-12-31',1,1,1),
	(2,'2017-12-31',1,1,1),
	(3,'2018-01-26',1,1,2);

/*!40000 ALTER TABLE `article` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table auteur
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auteur`;

CREATE TABLE `auteur` (
  `id_auteur` int(11) NOT NULL AUTO_INCREMENT,
  `nom_auteur` varchar(50) DEFAULT NULL,
  `prenom_auteur` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_auteur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Affichage de la table classification
# ------------------------------------------------------------

DROP TABLE IF EXISTS `classification`;

CREATE TABLE `classification` (
  `id_classe` int(11) NOT NULL AUTO_INCREMENT,
  `classe` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id_classe`),
  UNIQUE KEY `classe` (`classe`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

LOCK TABLES `classification` WRITE;
/*!40000 ALTER TABLE `classification` DISABLE KEYS */;

INSERT INTO `classification` (`id_classe`, `classe`)
VALUES
	(2,'HUMOUR'),
	(1,'SPORT');

/*!40000 ALTER TABLE `classification` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table ecrit
# ------------------------------------------------------------

DROP TABLE IF EXISTS `ecrit`;

CREATE TABLE `ecrit` (
  `id_article` int(11) NOT NULL,
  `id_auteur` int(11) NOT NULL,
  PRIMARY KEY (`id_article`,`id_auteur`),
  KEY `FK_ecrit_id_auteur` (`id_auteur`),
  CONSTRAINT `FK_ecrit_id_article` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`),
  CONSTRAINT `FK_ecrit_id_auteur` FOREIGN KEY (`id_auteur`) REFERENCES `auteur` (`id_auteur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Affichage de la table entite
# ------------------------------------------------------------

DROP TABLE IF EXISTS `entite`;

CREATE TABLE `entite` (
  `id_entite` int(11) NOT NULL AUTO_INCREMENT,
  `type_entite` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id_entite`),
  UNIQUE KEY `type_entite` (`type_entite`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

LOCK TABLES `entite` WRITE;
/*!40000 ALTER TABLE `entite` DISABLE KEYS */;

INSERT INTO `entite` (`id_entite`, `type_entite`)
VALUES
	(2,'LIEU'),
	(1,'PERSONNE');

/*!40000 ALTER TABLE `entite` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table journal
# ------------------------------------------------------------

DROP TABLE IF EXISTS `journal`;

CREATE TABLE `journal` (
  `id_journal` int(11) NOT NULL AUTO_INCREMENT,
  `nom_journal` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_journal`),
  UNIQUE KEY `nom_journal` (`nom_journal`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

LOCK TABLES `journal` WRITE;
/*!40000 ALTER TABLE `journal` DISABLE KEYS */;

INSERT INTO `journal` (`id_journal`, `nom_journal`)
VALUES
	(2,'FIGARO'),
	(3,'Gorafi'),
	(1,'LIBERATION'),
	(5,'NouveauJournal'),
	(4,'PECHE');

/*!40000 ALTER TABLE `journal` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table mot
# ------------------------------------------------------------

DROP TABLE IF EXISTS `mot`;

CREATE TABLE `mot` (
  `id_mot` int(11) NOT NULL AUTO_INCREMENT,
  `mot` varchar(50) NOT NULL,
  PRIMARY KEY (`id_mot`),
  UNIQUE KEY `mot` (`mot`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

LOCK TABLES `mot` WRITE;
/*!40000 ALTER TABLE `mot` DISABLE KEYS */;

INSERT INTO `mot` (`id_mot`, `mot`)
VALUES
	(2,'PHP'),
	(1,'VBA');

/*!40000 ALTER TABLE `mot` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table mot_racine
# ------------------------------------------------------------

DROP TABLE IF EXISTS `mot_racine`;

CREATE TABLE `mot_racine` (
  `id_racine` int(11) NOT NULL AUTO_INCREMENT,
  `mot` varchar(25) DEFAULT NULL,
  `id_mot` int(11) NOT NULL,
  PRIMARY KEY (`id_racine`),
  UNIQUE KEY `mot` (`mot`),
  KEY `FK_mot_racine_id_mot` (`id_mot`),
  CONSTRAINT `FK_mot_racine_id_mot` FOREIGN KEY (`id_mot`) REFERENCES `mot` (`id_mot`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

LOCK TABLES `mot_racine` WRITE;
/*!40000 ALTER TABLE `mot_racine` DISABLE KEYS */;

INSERT INTO `mot_racine` (`id_racine`, `mot`, `id_mot`)
VALUES
	(1,'PYTHON',1),
	(2,'JAVA',2);

/*!40000 ALTER TABLE `mot_racine` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table pos_tagging
# ------------------------------------------------------------

DROP TABLE IF EXISTS `pos_tagging`;

CREATE TABLE `pos_tagging` (
  `id_pos_tag` int(11) NOT NULL AUTO_INCREMENT,
  `pos_tag` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id_pos_tag`),
  UNIQUE KEY `pos_tag` (`pos_tag`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

LOCK TABLES `pos_tagging` WRITE;
/*!40000 ALTER TABLE `pos_tagging` DISABLE KEYS */;

INSERT INTO `pos_tagging` (`id_pos_tag`, `pos_tag`)
VALUES
	(1,'ADVERBE'),
	(2,'SUJET');

/*!40000 ALTER TABLE `pos_tagging` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table position_mot
# ------------------------------------------------------------

DROP TABLE IF EXISTS `position_mot`;

CREATE TABLE `position_mot` (
  `id_position` int(11) NOT NULL AUTO_INCREMENT,
  `position` int(11) NOT NULL,
  `titre` tinyint(1) NOT NULL,
  `id_racine` int(11) NOT NULL,
  `id_entite` int(11) NOT NULL,
  `id_pos_tag` int(11) NOT NULL,
  `id_article` int(11) NOT NULL,
  PRIMARY KEY (`id_position`),
  KEY `FK_position_mot_id_racine` (`id_racine`),
  KEY `FK_position_mot_id_entite` (`id_entite`),
  KEY `FK_position_mot_id_pos_tag` (`id_pos_tag`),
  KEY `FK_position_mot_id_article` (`id_article`),
  CONSTRAINT `FK_position_mot_id_article` FOREIGN KEY (`id_article`) REFERENCES `article` (`id_article`),
  CONSTRAINT `FK_position_mot_id_entite` FOREIGN KEY (`id_entite`) REFERENCES `entite` (`id_entite`),
  CONSTRAINT `FK_position_mot_id_pos_tag` FOREIGN KEY (`id_pos_tag`) REFERENCES `pos_tagging` (`id_pos_tag`),
  CONSTRAINT `FK_position_mot_id_racine` FOREIGN KEY (`id_racine`) REFERENCES `mot_racine` (`id_racine`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

LOCK TABLES `position_mot` WRITE;
/*!40000 ALTER TABLE `position_mot` DISABLE KEYS */;

INSERT INTO `position_mot` (`id_position`, `position`, `titre`, `id_racine`, `id_entite`, `id_pos_tag`, `id_article`)
VALUES
	(1,1,1,1,1,1,1),
	(2,2,0,2,1,1,1);

/*!40000 ALTER TABLE `position_mot` ENABLE KEYS */;
UNLOCK TABLES;


# Affichage de la table positivite
# ------------------------------------------------------------

DROP TABLE IF EXISTS `positivite`;

CREATE TABLE `positivite` (
  `id_positivite` int(11) NOT NULL AUTO_INCREMENT,
  `positivite` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_positivite`),
  UNIQUE KEY `positivite` (`positivite`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

LOCK TABLES `positivite` WRITE;
/*!40000 ALTER TABLE `positivite` DISABLE KEYS */;

INSERT INTO `positivite` (`id_positivite`, `positivite`)
VALUES
	(2,0),
	(1,1);

/*!40000 ALTER TABLE `positivite` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
