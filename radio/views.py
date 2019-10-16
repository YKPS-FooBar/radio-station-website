from radio import app

from flask import render_template


@app.route('/')
def home():
	return render_template('index')


@app.route('/add')
def add():
	return render_template('add')