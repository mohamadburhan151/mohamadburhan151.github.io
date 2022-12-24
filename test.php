<?php

use MongoDB\Client;

use function PHPSTORM_META\type;

	require_once __DIR__.'/vendor/autoload.php';
	$url = 'mongodb+srv://burhan:admin1234@atlascluster.atnphn0.mongodb.net/?retryWrites=true&w=majority';
	// $url = 'mongodb+srv://burhan:admin1234@cluster0.mongodb.net/test?serverSelectionTryOnce=false&serverSelectionTimeoutMS=15000&w=majority';
	$conn = new MongoDB\Client($uri=$url);
	$collection = $conn->unjaya->Tugas_Agregation;
	$cursor =$conn->unjaya->resapi;
	$dt = $cursor->find()->toArray();

	echo ("<pre>");
	print_r($conn->test);
	print_r($dt);
	// print_r($conn->unjaya->pegawai);
	echo ("</pre>");


	// $collection = (new MongoDB\Client)->unjaya->pegawai; //http://testmongo.id/test.php; db=unjaya; collection=pegawai
	// $books = $collection->find([]);
	// echo ("<pre>");
	// print_r($books);
	// echo ("</pre>");
	// $data = [];
	// foreach($books as $book){
	// 	var_dump($book);
	// 		$data[]=$book;
	// }
	// echo json_encode($data);
?>