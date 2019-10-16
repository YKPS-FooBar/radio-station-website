from flask import render_template

from radio import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=('POST',))
def add():
    app.logger.info('Someone at the /add page.')
    return render_template('add.html')
