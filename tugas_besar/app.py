from itertools import count
from turtle import title
from flask import Flask, render_template, session, \
	request, redirect, url_for
from models import Pengguna, Database
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/tugas_besar/static/uploads'
app.config['MAX_COTENT_PATH'] = 10000000


@app.route('/')
def index():
	g = []
	gmbr = Database()
	g = gmbr.selectAll('landingPage')
	if 'username' in session:
		username = session['username']
		password = session['password']
		model = Pengguna()
		tabel = []
		tabel = model.selectDB(username, password)
		for kolom in tabel:
			if kolom[5] == 'user':
				return render_template('index.html', tabel=tabel, username=username, title="Index"
			)
			elif kolom[5] == 'admin':
				return render_template('index.admin.html', tabel=tabel, username=username, title="Index Admin"
			)
	return render_template('landingPage.html', title="Landing Page", gmbrs=g)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		
		data = {
			'username' : request.form['username'],
			'password' : request.form['password']
		}
		pengguna = Pengguna('',data['username'], data['password'])
		if pengguna.authenticate():
			session['username'] = pengguna.username
			session['password'] = pengguna.password
			return redirect(url_for('index'))
		msg = 'Username / Password salah.'
		return render_template('form.html', msg=msg)
	return render_template('form.html', title="Login")

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
	if request.method == 'POST':
		data = {
			'nama' : request.form['nama'],
			'username' : request.form['username'],
			'password' : request.form['password']
		}
		pengguna = Pengguna(data['nama'], data['username'], data['password'])
		pengguna.insertDB()
		return redirect(url_for('login'))
	else:
		return render_template('formSignUp.html', title="Daftar")

@app.route('/logout')
def logout():
	session.pop('username', '')
	return redirect(url_for('index'))

@app.route('/varData')
def varData():
	if 'username' in session:
		username = session['username']
		
		return render_template('varTData.html',
			username=username, title="Variabel Dan Tipe Data"
		)
	return redirect(url_for('logout'))

@app.route('/tblUser', methods=['GET', 'POST'])
def tblUser():
	if 'username' in session:
		username = session['username']

		dataUser = []
		users = Database()
		dataUser = users.selectAll('user')
		if request.method == 'POST':
			data = {
				'nama' : request.form['nama'],
				'username' : request.form['username'],
				'password' : request.form['password'],
				'level' : request.form['level'],
				'aksi' : request.form['aksi']
			}
			if data['aksi'] == 'tambah':
				tambah = Database()
				tambah.act(data)
				dataUser=[]
				dataUser=tambah.selectAll('user')
				return render_template('tblUser.html',
					username=username, title="Tabel User", data=dataUser
				)
			elif data['aksi'] == 'edit':
				dataEdit = {
					'nama' : request.form['nama'],
					'username' : request.form['username'],
					'password' : request.form['password'],
					'level' : request.form['level'],
					'aksi' : request.form['aksi'],
					'id' : int(request.form['id'])
				}
				edit = Database()
				edit.act(dataEdit)
				datas = []
				datas= edit.selectAll('user')
				return render_template('tblUser.html',
					username=username, title="Tabel User", data=datas
				)
		return render_template('tblUser.html',
			username=username, title="Tabel User", data=dataUser
		)
	return redirect(url_for('logout'))

@app.route('/editUser/<id>', methods=['GET', 'POST'])
def editUser(id):
	if 'username' in session:
		username = session['username']
		if request.method == 'GET':
			data = []
			users = Database()
			data = users.selectAll('user')
			dt=[]
			dt = users.select('user', 'idUser', id)
			return render_template('editUser.html',
				username=username, title="Tabel User", data=data, dt=dt
			)
	return redirect(url_for('logout'))

@app.route('/tblUserDel/<id>', methods=['GET', 'POST'])
def tblUserDel(id):
	if 'username' in session:
		if request.method == 'GET':
			hapus = Database()
			hapus.delete('user', 'idUser', id)
			return redirect(url_for('tblUser'))
			
	return redirect(url_for('logout'))

@app.route('/tblLP', methods=['GET', 'POST'])
def tblLP():
	if 'username' in session:
		username = session['username']

		dataUser = []
		users = Database()
		dataUser = users.selectAll('landingPage')
		if request.method == 'POST':
			if request.form['aksi'] == 'tambah':
				f = request.files['gambar']
				filename = app.config['UPLOAD_FOLDER'] + '/' + secure_filename(f.filename)
				f.save(filename)
				data = {
						'judul' : request.form['judul'],
						'deskripsi' : request.form['deskripsi'],
						'gambar' : f.filename,
						'aksi' : request.form['aksi']
					}
				tambah = Database()
				tambah.tambahLP(data)
			return redirect(url_for('tblLP'))
		return render_template('tblLandingPage.html',
			username=username, title="Tabel Landing Page", data=dataUser
		)
	return redirect(url_for('logout'))
	
if __name__ == '__main__':
	app.run(debug=True)