<?php
	require_once __DIR__.'/../vendor/autoload.php';
	require_once __DIR__.'/../config.php';

	$collection = $conn->unjaya->pegawai;

	$id = $_POST['No'];

	// $result = $collection->deleteMany(['No'=>$id]);
	$result = $collection->deleteOne(['No'=>$id]);

	printf("Deleted %d document(s)\n", $result->getDeletedCount());
?>