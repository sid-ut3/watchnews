<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 12/01/2018
 * Time: 22:06
 */

namespace App\Services\V2;


use App\Persistence\V2\ArticleRepository;
use App\Persistence\V2\PositionWordRepository;
use App\Services\Service;

class SemanticService implements Service
{

    private $article_repository;
    private $position_word_repository;
    public function __construct()
    {
        $this->article_repository = new ArticleRepository();
        $this->position_word_repository = new PositionWordRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        $response = array();

        // CALL SEMANTIC_PARTICLE
        array_push($response,$this->article_repository->update($data['article']));

        // CALL SEMANTIC_PWORD
        foreach ($data['position_word'] as $position_word){
            array_push($response,$this->position_word_repository->update($position_word,$data['article']['id_article']));
        };
        return $response;
    }
}