<?php
# Deletion of tables
# Group 1 : L.M. and F.C.

# Login connexion
include '../../../utils/connexion.php';

try {
    // connexion to the database
    $conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // drop all tables
    /*$query = "DROP TABLE article, newspaper, author, classification, lemma, entity, word, pos_tagging, 
    	position_word, synonym, wiki, realize, belong CASCADE;";*/

	$query = "DROP DATABASE DBIndex;";
    $data = $conn->query($query);
    $result = $data->fetchAll(PDO::FETCH_ASSOC);
 
    //view the entire array (for testing)
    print_r($result);
    
    }
catch(PDOException $e)
    {
    echo  $e->getMessage();
    }
$conn = null;

?>
