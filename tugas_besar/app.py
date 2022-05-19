from flask import Flask, render_template, session, \
	request, redirect, url_for
from models import Pengguna

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'


@app.route('/')
def index():
	if 'username' in session:
		username = session['username']
		model = Pengguna()
		tabel = []
		tabel = model.selectDB(username)
		return render_template('index.html',
			tabel=tabel, username=username
		)
	return render_template('landingPage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		pengguna = Pengguna('', username, password)
		if pengguna.authenticate():
			session['username'] = username
			session['password'] = password
			return redirect(url_for('index'))
		msg = 'Username / Password salah.'
		return render_template('form.html', msg=msg)
	return render_template('form.html')

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
  if request.method == 'POST':
    nama = request.form['nama']
    username = request.form['username']
    password = request.form['password']
    data = (nama, username, password)
    pengguna = Pengguna(nama, username, password)
    pengguna.insertDB(nama, username, password)
    return redirect(url_for('login'))
  else:
    return render_template('formSignUp.html')

@app.route('/logout')
def logout():
	session.pop('username', '')
	return redirect(url_for('index'))
	
if __name__ == '__main__':
	app.run(debug=True)