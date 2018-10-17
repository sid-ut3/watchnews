<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 17/01/2018
 * Time: 10:19
 */

namespace App\Persistence\V2;


use App\Repositories\Repository;
use Illuminate\Support\Facades\DB;

class TFIDFRepository extends Repository
{

    public function store($data) {
        try {

            // Store the label for this article
            DB::select('CALL update_mv_tf_idf(?,?,?)',array(
                $data['id_article'],
                $data['lemma'],
                $data['tf_idf']
            ));

            $this->response['message'] = "";
            $this->response['code'] =  Repository::$CREATION_SUCCEEDED;

            return $this->response;

        } catch (\PDOException $e) {
            // Get the pdo exception message
            $this->response['message'] = $e->getMessage();
            $this->response['code'] =  Repository::$INTERNAL_ERROR;

            return $this->response;
        }
    }
}