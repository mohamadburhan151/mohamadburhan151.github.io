<?php

// header
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

// file koneksi
include_once 'koneksi.php';

$no = $_GET['Nama'];

$dbname = 'unjaya';
$collection = 'pegawai';


//Koneksi Database
$db = new DbManager();
$conn = $db->getConnection();

// Baca Data
$filter = ['Nama'=>$no];
$option = [];
$read = new MongoDB\Driver\Query($filter, $option);

//Mengirimkan data untuk dibaca
$records = $conn->executeQuery("$dbname.$collection", $read);
// var_dump($records);

echo json_encode(iterator_to_array($records));

?>