<?php

// header
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

// file koneksi
include_once 'koneksi.php';

$dbname = 'bdnr';
$collection = 'mhs';

//Koneksi Database
$db = new DbManager();
$conn = $db->getConnection();

//data yang akan disimpan
$data = json_decode(file_get_contents("php://input", true));

// menyimpan data
$insert = new MongoDB\Driver\BulkWrite();
$insert->insert($data);

$result = $conn->executeBulkWrite("$dbname.$collection", $insert);

// verifikasi
if ($result->getInsertedCount() == 1) {
    echo json_encode(
		array("message" => "Data Sukses Tersimpan")
	);
} else {
    echo json_encode(
            array("message" => "Error dalam Proses Simpan")
    );
}

?>