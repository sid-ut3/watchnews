<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:11
 */
namespace App\Services\V1;

use App\Persistence\V1\WordRepository;

class WordService
{
    private $word_repository;
    public function __construct()
    {
        $this->word_repository = new WordRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        return $this->word_repository->store($data);
    }
}