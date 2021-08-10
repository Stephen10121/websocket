from flask import Flask, render_template, request, make_response, redirect, url_for, jsonify

app = Flask('app')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('index2.html')

app.run(host='0.0.0.0', port=80, debug=True)