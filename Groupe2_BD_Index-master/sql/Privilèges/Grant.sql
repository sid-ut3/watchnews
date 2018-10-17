-- Création Utilisateur et admission des droits.

CREATE USER 'test'@'localhost'
IDENTIFIED BY 'test';

GRANT SELECT, INSERT, UPDATE
ON bd_index.*
TO 'test'@'localhost';

GRANT EXECUTE
ON bd_index.*
TO 'test'@'localhost';


-- Si l'administrateur veut supprimer les droits 
-- de Select, insert, update après lui avoir autorisé.

REVOKE SELECT, INSERT, UPDATE
ON bd_index.*
FROM 'test'@'localhost';

