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
			
class Database():
	
	def openDB(self):
		global db, cursor
		db = pymysql.connect(
			host = config.DB_HOST,
			user = config.DB_USER,
			password = config.DB_PASSWORD,
			database = config.DB_NAME)
		cursor = db.cursor()
	
	def closeDB(self):
		global db, cursor
		db.close()
	
	def selectAll(self, namaTable):
		self.tbl = namaTable
		self.openDB()
		cursor.execute("SELECT * FROM %s" % self.tbl)
		container = []
		for self.col in cursor.fetchall():
			container.append((self.col))
		self.closeDB()
		return container
	
	def select(self, namaTable,kol,  id):
		self.tbl = namaTable
		self.openDB()
		cursor.execute("SELECT * FROM %s WHERE %s = %s" % (self.tbl, kol, id))
		container = []
		for kol in cursor.fetchall():
			container.append(kol)
		self.closeDB()
		return container

	def act(self,data):
		
		self.data = data
		if self.data['aksi'] == 'tambah':
			self.openDB()
			cursor.execute("INSERT INTO user(namaUser, userName, password, keterangan, level) VALUES('%s' , '%s' , MD5('%s') , '%s' , '%s')"  % (self.data['nama'], self.data['username'], self.data['password'], self.data['password'], self.data['level']))
			db.commit()
			self.closeDB()
		if self.data['aksi'] == 'edit':
			self.openDB()
			cursor.execute("UPDATE user SET namaUser='%s', userName='%s', password=MD5('%s'), keterangan='%s', level='%s' WHERE idUser=%d"  % (self.data['nama'], self.data['username'], self.data['password'], self.data['password'], self.data['level'], self.data['id']))
			db.commit()
			self.closeDB()
	def delete(self,tabel, kol, id):
		self.openDB()
		cursor.execute("DELETE FROM %s WHERE %s = %s" % (tabel, kol, id))
		db.commit()
		self.closeDB()
	def tambahLP(self, data):
		self.data = data
		if self.data['aksi'] == 'tambah':
			self.openDB()
			cursor.execute("INSERT INTO landingPage(judul, deskripsi, gambar) VALUES('%s' , '%s', '%s')"  % (self.data['judul'], self.data['deskripsi'], self.data['gambar']))
			db.commit()
			self.closeDB()
		if self.data['aksi'] == 'edit':
			self.openDB()
			cursor.execute("UPDATE landingPage SET judul='%s', deskripsi='%s', gambar='%s' WHERE idUser=%d"  % (self.data['nama'], self.data['username'], self.data['password'], self.data['password'], self.data['level'], self.data['id']))
			db.commit()
			self.closeDB()

