<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
*/
Route::prefix('API/index')->group(function () {

    // Label's routes
    Route::post('label', 'LabelController@store');

    // Filtering group's routes
    Route::post('filtering', 'FilteringController@store');

    // Semantic group's routes
    Route::patch('semantic', 'SemanticController@store');

    // TF IDF's routes
    Route::post('tf_idf','TFIDFController@store');

    Route::get('test',function() {
        return view('welcome');
    });
});

