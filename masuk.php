<?php

// header
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

// file koneksi
include_once 'koneksi.php';

$user = $_POST['username'];
$pass = $_POST['password'];

$dbname = 'unjaya';
$collection = 'akun';


//Koneksi Database
$db = new DbManager();
$conn = $db->getConnection();

// Baca Data
$filter = ['username'=>$user,'password'=>$pass];
$option = [];
$read = new MongoDB\Driver\Query($filter, $option);

//Mengirimkan data untuk dibaca
$records = $conn->executeQuery("$dbname.$collection", $read);
// var_dump($records);

echo json_encode(iterator_to_array($records));

?>