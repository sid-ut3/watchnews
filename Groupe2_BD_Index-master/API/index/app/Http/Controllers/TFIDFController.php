<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 17/01/2018
 * Time: 10:18
 */

namespace App\Http\Controllers;


use App\Http\JsonMapper\JsonMapper;
use App\Services\V2\TFIDFService;
use Illuminate\Http\Request;

class TFIDFController extends Controller
{

    private $json_mapper;
    private $tf_idf_service;

    public function __construct()
    {
        $this->json_mapper = new JsonMapper();
        $this->tf_idf_service = new TFIDFService();
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        // Parse automatically the json sent by client
        $raw_data = $this->json_mapper->json_mapper($request->all());


        // Return the appropriate message to client
        return $this->parse($raw_data,$this->tf_idf_service);
    }
}