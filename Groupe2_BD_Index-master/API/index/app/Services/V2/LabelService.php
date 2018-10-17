<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 14:40
 */
namespace App\Services\V2;

use App\Persistence\V2\LabelRepository;
use App\Services\Service;

class LabelService implements  Service
{
    private $belong_repository;
    public function __construct()
    {
        $this->belong_repository = new LabelRepository();
    }

    public function store($data) {
        // Need validation steps for the data

        $repository_response=array();

        if(is_string($data['label'])) {
            array_push($repository_response,$this->belong_repository->store(
                $data['id_article'],$data['label'],$data['strongest_label'])
            );
        }

        if(is_array($data['label'])) {

            for ($i = 0; $i < count($data['label']) ; $i++) {
                array_push($repository_response,$this->belong_repository->store(
                    $data['id_article'],$data['label'][$i],$data['strongest_label'][$i])
                );
            }
        }

        return $repository_response;


    }
}