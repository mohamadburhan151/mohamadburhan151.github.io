<?php
	require_once __DIR__.'/../vendor/autoload.php';
	require_once __DIR__.'/../config.php';

	// $_POST['No']= '22';
	// $_POST['Nama']= 'burhan';
	// $_POST['Departemen']='IT';
	// $_POST['Masuk_Kerja']='2021';
	// $_POST['Gaji']='10000000';

	$no = $_POST['No'];
	$nama = $_POST['Nama'];
	$departemen = $_POST['Departemen'];
	$masuk_kerja = $_POST['Masuk_Kerja'];
	$gaji = $_POST['Gaji'];

	//insert to db unjaya collections pegawai
	$collection = $conn->unjaya->pegawai;
	$insert = $collection->insertMany(
		[
			[
			'No'=>$no,
			'Nama'=>$nama,
			'Departemen'=>$departemen,
			'Masuk Kerja'=>$masuk_kerja,
			'Gaji'=>$gaji,
			]
		]
	);
	printf("Inserted %d document(s)\n", $insert->getInsertedCount());

	var_dump($insert->getInsertedIds());

?>