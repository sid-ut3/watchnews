<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 12/01/2018
 * Time: 19:14
 */

namespace App\Services\V2;


use App\Persistence\V2\ArticleRepository;
use App\Persistence\V2\PositionWordRepository;
use App\Services\Service;


class FilteringService implements  Service
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

        // CALL FILTERING_PARTICLE & FILTERING_PAUTHOR
        array_push($response,$this->article_repository->store($data['article']));

        // CALL FILTERING_PPOSITION_WORD
        foreach ($data['position_word'] as $position_word){
            array_push($response,$this->position_word_repository->store($position_word,$response[0]['message']['id_article']));
        };

        return $response;
    }
}