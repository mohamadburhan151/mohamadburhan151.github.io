<?php

// header
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: DELETE");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

// file koneksi
include_once 'koneksi.php';

$dbname = 'bdnr';
$collection = 'mhs';

//Koneksi Database
$db = new DbManager();
$conn = $db->getConnection();

$data = json_decode(file_get_contents("php://input", true));

//kolom _id 
$id = $data->{'where'};

// hapus data
$delete = new MongoDB\Driver\BulkWrite();
$delete->delete(
	['_id' => new MongoDB\BSON\ObjectId($id)],
	['limit' => 0]
);

$result = $conn->executeBulkWrite("$dbname.$collection", $delete);

//print_r($result);

// verifikasi
if ($result->getDeletedCount() == 1) {
    echo json_encode(
		array("message" => "Data sukses Terhapus")
	);
} else {
    echo json_encode(
            array("message" => "Error dalam proses hapus")
    );
}

?>