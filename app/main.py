from flask import Flask, render_template, request, make_response, redirect, url_for, jsonify
from functions import *
from cryptography.fernet import Fernet
import os
from encrypt import *

nodeid = "01272004"

def key_exists():
    if os.path.isfile('key.key')!=True:
        key = Fernet.generate_key()
        file = open('key.key', 'wb')
        file.write(key)
        file.close()
key_exists()

add_def_user('test', 'test', 'test')

app = Flask('app')

@app.route("/logout")
def logout():
	if 'WOWPOW' in request.cookies:
		if request.cookies['WOWPOW']=='':
			return redirect('/')
		else:
			send_name(str(request.cookies["WOWPOW"]), str(request.cookies['WOWPOW']), nodeid)
			res=make_response(redirect('/'))
			res.set_cookie('WOWPOW', '')
			return res
	else:
		return redirect("/")


@app.route('/')
def home():
	if 'WOWPOW' in request.cookies:
		if request.cookies['WOWPOW']=='':
			return redirect('/login')
		else:
			id = int(decrypt(request.cookies['WOWPOW'])[1])
			send_name(get_user_name(id), str(request.cookies['WOWPOW']), nodeid)
			return render_template('index.html', name=get_userinfo(id)[2])
	else:
		return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login_form():
    if request.method == 'POST':
        username = request.form.get('u')
        password = request.form.get('p')
        info = login(username, password)
        if info=='usernotexist':
            return render_template('login.html', error='usernotexist')
        elif info=='wrongpassword':
            return render_template('login.html', error='wrongpassword')
        else:
            res=make_response(redirect('/'))
            res.set_cookie('WOWPOW', encrypt(str(get_id(username))))
            return res
    else:
        return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup_form():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('u')
        password = request.form.get('p')
        rpassword = request.form.get('rp')
        email= request.form.get('email')
        nallowed = [' ', '/']
        for i in nallowed:
            if i in username:
                return render_template('signup.html', error='forbidchar')
        jeff = signup(username, password, rpassword, name, email)
        if jeff=='userexists':
            return render_template('signup.html', error='userexists')
        elif jeff=='passwordmatch':
            return render_template('signup.html', error='passwordnotmatch')
        else:
            print(jeff)
            user_id=get_id(username)[0]
            res=make_response(redirect('/'))
            res.set_cookie('WOWPOW',encrypt(str(get_id(username))))
            return res
    else:
        return render_template("signup.html")

app.run(host='0.0.0.0', port=80, debug=True)
