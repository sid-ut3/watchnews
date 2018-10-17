<?php
/**
 * Created by PhpStorm.
 * User: Utilisateur
 * Date: 08/01/2018
 * Time: 18:08
 */
namespace App\Persistence\V2;
use App\Repositories\Repository;
use Illuminate\Support\Facades\DB;

class PositionWordRepository extends Repository
{
    public function store($data,$id_article) {
        try {
            // Store in DB the data given
            DB::select('CALL FILTERING_PPOSITION_WORD(?,?,?,?,?,?,?)',array(
                $data['position'],
                $data['word'],
                $data['lemma'],
                $data['title'],
                $data['pos_tag'],
                $data['type_entity'],
                $id_article
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

    public function update($data,$id_article) {

        try {
            // Store in DB the data given
            DB::select('CALL SEMANTIC_PWORD(?,?,?,?)',array(
                $id_article,
                $data['position'],
                $data['word'],
                $data['file_wiki'],
            ));

            if (is_array($data['synonym'])) {
                foreach($data['synonym'] as $synonym) {
                    DB::select('CALL SEMANTIC_PSYNONYM(?,?,?)', array(
                        $id_article,
                        $data['position'],
                        $synonym
                    ));
                }
            }

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