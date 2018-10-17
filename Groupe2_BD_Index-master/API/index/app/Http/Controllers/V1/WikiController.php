<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 10:35
 */

namespace App\Http\Controllers\V1;


use App\Http\Controllers\Controller;
use App\Http\JsonMapper\JsonMapper;
use App\Services\V1\WikiService;
use Illuminate\Http\Request;

class WikiController extends Controller
{
    private $json_mapper;
    private $wiki_service;

    public function __construct()
    {
        $this->json_mapper = new JsonMapper();
        $this->wiki_service = new WikiService();
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
        return $this->parse($raw_data,$this->wiki_service);
    }
}