<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 12/01/2018
 * Time: 19:25
 */

namespace App\Services;


interface Service
{
    /**
     * Allow to store data in the concerned table
     * @param $data :an array containing all the data parse
     * from the json sent by client
     * @return :a response that will be interpreted by client
     */
    public function store($data);
}