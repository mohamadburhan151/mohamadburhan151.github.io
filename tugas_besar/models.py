from ast import dump
from hashlib import md5
import pymysql
import config

db = cursor = None

class Pengguna():
	def __init__ (self, nama=None, username=None, password=None):
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
	def selectDB(self, username, password):
		self.username = username
		self.password = password
		self.openDB()
		cursor.execute("SELECT * FROM user where userName='%s' AND password=MD5('%s')" % (self.username, self.password))
		container = cursor.fetchall()
		self.closeDB
		return container

	def insertDB(self):
		level = "user"
		self.openDB()
		cursor.execute("INSERT INTO user(namaUser, userName, password, keterangan, level) VALUES('%s' , '%s' , MD5('%s') , '%s' , '%s')"  % (self.nama, self.username, self.password, self.password, level))
		db.commit()
		self.closeDB()

	def closeDB(self):
		global db, cursor
		db.close()

	def authenticate(self):
		self.openDB()
		cursor.execute("SELECT COUNT(*) FROM user WHERE userName = '%s' AND password = MD5('%s')" % (self.username, self.password))
		count_account = (cursor.fetchone())[0]
		self.closeDB()
		return True if count_account > 0 else False	
			
			
			
			