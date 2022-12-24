<?php
	require_once __DIR__.'/vendor/autoload.php';
	
	class Config{
		private $conn;

		function __construct()
		{
			try {
				$this->conn = (new MongoDB\Client('mongodb+srv://burhan:admin1234@praktek.8bcd6re.mongodb.net/?retryWrites=true&w=majority',[],[]));
				// $this->conn = (new MongoDB\Client('mongodb://127.0.0.1/',[],[
				// 	'typeMap' => [
				// 			'array' => 'array',
				// 			'document' => 'array',
				// 			'root' => 'array',
				// 			],
				// 		]
				// 	)
				// );
			} catch (MongoDB\Exception\Exception $e) {
				echo $e->getMessage();
				echo nl2br("n");
			}

		}
		function getConnection()
		{
			return $this->conn;
		}
	}

	$config = new Config();
	$conn = $config->getConnection();

?>