<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 09/01/2018
 * Time: 14:39
 */

namespace App\Persistence\V2;


use App\Repositories\Repository;
use Illuminate\Support\Facades\DB;

class LabelRepository extends Repository
{
    public function store($id_article,$label,$strongest_label) {
        try {

            // Store the label for this article
            DB::select('CALL PBELONG(?,?,?)',array(
                $id_article,
                $label,
                $strongest_label
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