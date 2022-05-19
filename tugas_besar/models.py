import pymysql
import config

db = cursor = None

class Pengguna():
	def __init__ (self, nama = None, username=None, password=None):
		self.nama = nama
		self.username = username
		self.password = password
		
	def openDB(self):
		global db, cursor
		db = pymysql.connect(
			host = config.DB_HOST,
			user = config.DB_USER,
			password = config.DB_PASSWORD,
			database = config.DB_NAME)
		cursor = db.cursor()
	def selectDB(self, username):
		self.username = username
		self.openDB()
		cursor.execute("SELECT * FROM user where userName='%s'" % self.username)
		container = cursor.fetchall()
		self.closeDB
		return container

	def insertDB(self, nama, username, password):
		self.nama = nama
		self.username = username
		self.password = password
		data = [nama, username, password]
		self.openDB()
		insert = cursor.execute("INSERT INTO user(namaUser, userName, password) VALUES ('%s', '%s', '%s')" % data)
		self.closeDB
		return insert

	def closeDB(self):
		global db, cursor
		db.close()
		
	def authenticate(self):
		self.openDB()
		cursor.execute("SELECT COUNT(*) FROM user WHERE userName = '%s' AND password = MD5('%s')" % (self.username, self.password))
		count_account = (cursor.fetchone())[0]
		self.closeDB()
		return True if count_account > 0 else False	
			
			
			
			