#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: article
#------------------------------------------------------------

CREATE TABLE article(
        id_article       int (11) Auto_increment  NOT NULL ,
        date_publication Date ,
        taux_positivite  Float ,
        id_auteur        Int NOT NULL ,
        id_journal       Int NOT NULL ,
        id_classe        Int NOT NULL ,
        PRIMARY KEY (id_article )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: journal
#------------------------------------------------------------

CREATE TABLE journal(
        id_journal  int (11) Auto_increment  NOT NULL ,
        nom_journal Varchar (50) ,
        PRIMARY KEY (id_journal ) ,
        UNIQUE (nom_journal )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: auteur
#------------------------------------------------------------

CREATE TABLE auteur(
        id_auteur     int (11) Auto_increment  NOT NULL ,
        nom_auteur    Varchar (50) ,
        prenom_auteur Varchar (50) ,
        PRIMARY KEY (id_auteur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: classification
#------------------------------------------------------------

CREATE TABLE classification(
        id_classe int (11) Auto_increment  NOT NULL ,
        classe    Varchar (25) ,
        PRIMARY KEY (id_classe ) ,
        UNIQUE (classe )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: mot_racine
#------------------------------------------------------------

CREATE TABLE mot_racine(
        id_racine int (11) Auto_increment  NOT NULL ,
        mot       Varchar (25) ,
        PRIMARY KEY (id_racine ) ,
        UNIQUE (mot )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: entite
#------------------------------------------------------------

CREATE TABLE entite(
        id_entite   int (11) Auto_increment  NOT NULL ,
        type_entite Varchar (25) ,
        PRIMARY KEY (id_entite ) ,
        UNIQUE (type_entite )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: mot
#------------------------------------------------------------

CREATE TABLE mot(
        id_mot    int (11) Auto_increment  NOT NULL ,
        mot       Varchar (50) NOT NULL ,
        id_racine Int NOT NULL ,
        PRIMARY KEY (id_mot ) ,
        UNIQUE (mot )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: pos_tagging
#------------------------------------------------------------

CREATE TABLE pos_tagging(
        id_pos_tag int (11) Auto_increment  NOT NULL ,
        pos_tag    Varchar (25) ,
        PRIMARY KEY (id_pos_tag ) ,
        UNIQUE (pos_tag )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: position_mot
#------------------------------------------------------------

CREATE TABLE position_mot(
        id_position int (11) Auto_increment  NOT NULL ,
        position    Int NOT NULL ,
        titre       Bool NOT NULL ,
        id_mot      Int NOT NULL ,
        id_entite   Int NOT NULL ,
        id_pos_tag  Int NOT NULL ,
        id_article  Int NOT NULL ,
        id_synonyme Int NOT NULL ,
        PRIMARY KEY (id_position )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: synonyme
#------------------------------------------------------------

CREATE TABLE synonyme(
        id_synonyme int (11) Auto_increment  NOT NULL ,
        synonyme    Varchar (50) NOT NULL ,
        PRIMARY KEY (id_synonyme ) ,
        UNIQUE (synonyme )
)ENGINE=InnoDB;

ALTER TABLE article ADD CONSTRAINT FK_article_id_auteur FOREIGN KEY (id_auteur) REFERENCES auteur(id_auteur);
ALTER TABLE article ADD CONSTRAINT FK_article_id_journal FOREIGN KEY (id_journal) REFERENCES journal(id_journal);
ALTER TABLE article ADD CONSTRAINT FK_article_id_classe FOREIGN KEY (id_classe) REFERENCES classification(id_classe);
ALTER TABLE mot ADD CONSTRAINT FK_mot_id_racine FOREIGN KEY (id_racine) REFERENCES mot_racine(id_racine);
ALTER TABLE position_mot ADD CONSTRAINT FK_position_mot_id_mot FOREIGN KEY (id_mot) REFERENCES mot(id_mot);
ALTER TABLE position_mot ADD CONSTRAINT FK_position_mot_id_entite FOREIGN KEY (id_entite) REFERENCES entite(id_entite);
ALTER TABLE position_mot ADD CONSTRAINT FK_position_mot_id_pos_tag FOREIGN KEY (id_pos_tag) REFERENCES pos_tagging(id_pos_tag);
ALTER TABLE position_mot ADD CONSTRAINT FK_position_mot_id_article FOREIGN KEY (id_article) REFERENCES article(id_article);
ALTER TABLE position_mot ADD CONSTRAINT FK_position_mot_id_synonyme FOREIGN KEY (id_synonyme) REFERENCES synonyme(id_synonyme);
