<?php

namespace App\Http\Controllers;

use App\Services\Service;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function parse($raw_data,Service $service) {
        // Response
        $response = array();

        foreach ($raw_data as $data) {
            // Get the raw_response from entity_service's associated method
            array_push($response,$service->store($data));
        };

        return(response($response,200));
    }
}
