from flask import Flask, render_template, request, make_response, redirect, url_for, jsonify
from functions import *
from cryptography.fernet import Fernet
import os

def key_exists():
    if os.path.isfile('key.key')!=True:
        key = Fernet.generate_key()
        file = open('key.key', 'wb')
        file.write(key)
        file.close()
key_exists()

add_def_user('test', 'test', 'test')

app = Flask('app')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('index2.html')

app.run(host='0.0.0.0', port=80, debug=True)
