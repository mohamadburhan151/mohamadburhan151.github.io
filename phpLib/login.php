<?php
	header("Access-Control-Allow-Origin: *");
	header("Content-Type: application/json; charset=UTF-8");

	require_once __DIR__.'/../vendor/autoload.php';
	require_once __DIR__.'/../config.php';

	//collectin pegawai
	$collection = $conn->unjaya->akun;	
	$documents = $collection->find(
		[
			'username'=>$_POST['username'],
			'password'=>$_POST['password'],
		],
		['projection'=>[
				'username'=>1,
				'password'=>1
		],
		'sort'=>['username'=>1]
		]
	);
	$data = [];
	foreach($documents as $document){
		$data[]=$document;
	}

	// echo '<prev>';
	// var_dump($documents);
	// echo '</prev>';
	echo json_encode($data);
?>