<?php
require_once __DIR__.'/vendor/autoload.php';

class DbManager
{

	//Konfigurasi Database
	private $dbhost = 'localhost';
	private $dbport = '27017';
	private $conn;

	function __construct()
	{
		//Koneksi ke MongoDB
		try {
			// $this->conn = new MongoDB\Driver\Manager('mongodb://' . $this->dbhost . ':' . $this->dbport);
			$this->conn = new MongoDB\Driver\Manager(
				'mongodb+srv://burhan:admin1234@praktek.8bcd6re.mongodb.net/?retryWrites=true&w=majority'
			);
			
		} catch (MongoDBDriverExceptionException $e) {
			echo $e->getMessage();
			echo nl2br("n");
		}
	}

	function getConnection()
	{
		return $this->conn;
	}
}

?>