<?php

// header 
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: PUT");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

// include file koneksi
include_once 'koneksi.php';

$dbname = 'bdnr';
$collection = 'mhs';

//Koneksi Database
$db = new DbManager();
$conn = $db->getConnection();

//update data
$data = json_decode(file_get_contents("php://input", true));

$fields = $data->{'fields'};

$set_values = array();

foreach ($fields as $key => $fields) {
	$arr = (array)$fields;
	foreach ($fields as $key => $value) {
		$set_values[$key] = $value;
	}
}

//kolom _id
$id = $data->{'where'};

// update record
$update = new MongoDB\Driver\BulkWrite();
$update->update(
	['_id' => new MongoDB\BSON\ObjectId($id)], ['$set' => $set_values], ['multi' => false, 'upsert' => false]
);

$result = $conn->executeBulkWrite("$dbname.$collection", $update);

// verifikasi
if ($result->getModifiedCount() == 1) {
    echo json_encode(
		array("message" => "Data Sukses Terupdate")
	);
} else {
    echo json_encode(
            array("message" => "Error dalam proses update")
    );
}

?>