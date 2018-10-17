<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 17/01/2018
 * Time: 10:19
 */

namespace App\Services\V2;


use App\Persistence\V2\TFIDFRepository;
use App\Services\Service;

class TFIDFService implements Service
{
    private $tf_idf_repository;
    public function __construct()
    {
        $this->tf_idf_repository = new TFIDFRepository();
    }

    public function store($data)
    {
        return $this->tf_idf_repository->store($data);
    }
}