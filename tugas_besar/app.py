from itertools import count
from turtle import title
from flask import Flask, render_template, session, \
	request, redirect, url_for
from models import Pengguna

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'



@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		password = session['password']
		model = Pengguna()
		tabel = []
		tabel = model.selectDB(username, password)
		return render_template('index.html',
			tabel=tabel, username=username, title="Index"
		)
	return render_template('landingPage.html', title="Landing Page")


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
	return render_template('landingPage.html', title="Landing Page")

	
if __name__ == '__main__':
	app.run(debug=True)