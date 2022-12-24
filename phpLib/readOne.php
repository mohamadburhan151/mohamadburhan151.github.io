<?php
	header("Access-Control-Allow-Origin: *");
	header("Content-Type: application/json; charset=UTF-8");

	require_once __DIR__.'/../vendor/autoload.php';
	require_once __DIR__.'/../config.php';

	$no = $_GET['No'];

	$collection = $conn->unjaya->pegawai;
	$documents = $collection->Find(
		['No'=>IntVal($no)],
		['projection'=>[
				'No'=>1,
				'Nama'=>1,
				'Departemen'=>1,
				'Masuk_Kerja'=>1,
				'Gaji'=>1
		],
		'sort'=>['No'=>1],
		]
	);
	$data = [];
	foreach($documents as $document){
		$data[]=$document;
	}

	echo json_encode($data);
?>