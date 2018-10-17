#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: article
#------------------------------------------------------------

CREATE TABLE article(
        id_article               int (11) Auto_increment  NOT NULL ,
        date_publication         Date ,
        id_journal_journal       Int NOT NULL ,
        id_classe_classification Int NOT NULL ,
        id_positivite_positivite Int NOT NULL ,
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
# Table: positivite
#------------------------------------------------------------

CREATE TABLE positivite(
        id_positivite int (11) Auto_increment  NOT NULL ,
        positivite    Bool ,
        PRIMARY KEY (id_positivite ) ,
        UNIQUE (positivite )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: mot_racine
#------------------------------------------------------------

CREATE TABLE mot_racine(
        id_racine  int (11) Auto_increment  NOT NULL ,
        mot        Varchar (25) ,
        id_mot_mot Int NOT NULL ,
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
        id_mot int (11) Auto_increment  NOT NULL ,
        mot    Varchar (50) NOT NULL ,
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
# Table: ecrit
#------------------------------------------------------------

CREATE TABLE ecrit(
        id_article_article Int NOT NULL ,
        id_auteur_auteur   Int NOT NULL ,
        PRIMARY KEY (id_article_article ,id_auteur_auteur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: apparaitre
#------------------------------------------------------------

CREATE TABLE apparaitre(
        position               Int ,
        id_racine_mot_racine   Int NOT NULL ,
        id_article_article     Int NOT NULL ,
        id_entite_entite       Int NOT NULL ,
        id_pos_tag_pos_tagging Int NOT NULL ,
        PRIMARY KEY (id_racine_mot_racine ,id_article_article ,id_entite_entite ,id_pos_tag_pos_tagging )
)ENGINE=InnoDB;

ALTER TABLE article ADD CONSTRAINT FK_article_id_journal_journal FOREIGN KEY (id_journal_journal) REFERENCES journal(id_journal);

ALTER TABLE article ADD CONSTRAINT FK_article_id_classe_classification FOREIGN KEY (id_classe_classification) REFERENCES classification(id_classe);

ALTER TABLE article ADD CONSTRAINT FK_article_id_positivite_positivite FOREIGN KEY (id_positivite_positivite) REFERENCES positivite(id_positivite);

ALTER TABLE mot_racine ADD CONSTRAINT FK_mot_racine_id_mot_mot FOREIGN KEY (id_mot_mot) REFERENCES mot(id_mot);

ALTER TABLE ecrit ADD CONSTRAINT FK_ecrit_id_article_article FOREIGN KEY (id_article_article) REFERENCES article(id_article);

ALTER TABLE ecrit ADD CONSTRAINT FK_ecrit_id_auteur_auteur FOREIGN KEY (id_auteur_auteur) REFERENCES auteur(id_auteur);

ALTER TABLE apparaitre ADD CONSTRAINT FK_apparaitre_id_racine_mot_racine FOREIGN KEY (id_racine_mot_racine) REFERENCES mot_racine(id_racine);

ALTER TABLE apparaitre ADD CONSTRAINT FK_apparaitre_id_article_article FOREIGN KEY (id_article_article) REFERENCES article(id_article);

ALTER TABLE apparaitre ADD CONSTRAINT FK_apparaitre_id_entite_entite FOREIGN KEY (id_entite_entite) REFERENCES entite(id_entite);

ALTER TABLE apparaitre ADD CONSTRAINT FK_apparaitre_id_pos_tag_pos_tagging FOREIGN KEY (id_pos_tag_pos_tagging) REFERENCES pos_tagging(id_pos_tag);
