<?php
	require_once __DIR__.'/../vendor/autoload.php';
	require_once __DIR__.'/../config.php';

	$collection = $conn->unjaya->pegawai;

	$id = $_POST['No'];
	$field = $_POST['field'];
	$value = $_POST['value'];

	$updateResult = $collection->updateOne(
		[ 'No' => $id ],
		[ '$set' => [ $field => $value ]]
 	);

	// $updateResult = $collection->updateMany(
	// 	[ 'restaurant_id' => '40356151' ],
	// 	[ '$set' => [ 'name' => 'Brunos on Astoria' ]]
 	// );
 
	printf("Matched %d document(s)\n", $updateResult->getMatchedCount());
	printf("Modified %d document(s)\n", $updateResult->getModifiedCount());

?>