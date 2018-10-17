<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 12/01/2018
 * Time: 19:12
 */

namespace App\Http\Controllers;


use App\Http\JsonMapper\JsonMapper;
use App\Services\V2\FilteringService;
use Illuminate\Http\Request;

class FilteringController extends Controller
{

    private $json_mapper;
    private $filtering_service;

    public function __construct()
    {
        $this->json_mapper = new JsonMapper();
        $this->filtering_service = new FilteringService();
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
        return $this->parse($raw_data,$this->filtering_service);

    }
}