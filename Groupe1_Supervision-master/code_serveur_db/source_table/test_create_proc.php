<?php
# Deletion of tables
# Group supervision : Loann Michon and Florence Canal

# Login connexion
include '../../../utils/connexion.php';

try {
    // connexion to the database
    $conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    // requete creation proc
    $query = "DROP PROCEDURE IF EXISTS PTEST;
    CREATE PROCEDURE PTEST(IN VLABEL VARCHAR(50)) BEGIN INSERT INTO label(id_entity,type_entity) VALUES (NULL,VLABEL);END;
    DROP PROCEDURE IF EXISTS PTEST2;
    CREATE PROCEDURE PTEST2(IN VLABEL VARCHAR(50)) BEGIN INSERT INTO label(id_entity,type_entity) VALUES (NULL,VLABEL);END;";
    //$data = 
    $conn->query($query);
    //$result = $data->fetchAll(PDO::FETCH_ASSOC);		
    //view the entire array (for testing)
    //print_r($result);
    
    }
catch(PDOException $e)
    {
    echo  $e->getMessage();
    }
$conn = null;

?>
