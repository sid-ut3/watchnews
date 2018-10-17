# Groupe2 BD Index
OBJECTIFS :  

Travail en commun des deux groupes (2 et 3):  

- Le schéma général de la base qui permet de stocker le résultat du travail des groupes
5,6, 7 (et 8?) et d’alimenter le site Web et le groupe 8.  
- Le schéma général doit permettre de répondre à tous les Use Cases minimaux
présentés par le groupe de direction en début de projet.    

Travail spécifique au groupe 2 :  

- Créer la base (tables, contraintes)  
- Insérer les données mises à disposition en début de projet  
- Gérer l’évolution du schéma (nouveaux Use Cases et gestion des logs)  
- Implémenter une API REST (dans le langage décidé dans le travail préliminaire) pour
permettre l’insertion de données envoyées par les groupes 5, 6 et 7  

Nous testons le commit puis le push.

TESt2


flag :=0

SELECT ARTICLE.IDARTICLE INTO VIDARTICLE_VERIF,
FROM ARTICLE
WHERE $VIDARTICLE=ARTICLE.IDARTICLE

flag:=1

RAISE EXCEPTION ERROR :
if(flag==0)
if(flag=1)