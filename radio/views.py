import re

from flask import render_template, request, abort

from radio import app


# TODO, try to hunt down who "someone" is in the logs.


@app.route('/', methods=('GET',))
def index():
    return render_template('index.html')


@app.route('/pay', methods=('GET', 'POST'))
def pay():
    if request.method == 'GET':
        app.logger.info('Someone at entering their information and paying.')
        return render_template('pay.html')
    else:
        # So, generally, for speed there is a client-side validation, but for
        # safety (i.e. people like David modifying the source code) we also
        # implement an identical server-side validation.  If server-side fails,
        # we return a 400 bad request.

        app.logger.info('Someone is here at the QR code.')
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        wechat = request.form['wechat'].strip()

        # Simple validation on if the email is of ykpaoschool.cn domain.
        ykps_email = re.fullmatch(r'[A-Za-z0-9\._-]+@(stu\.)?ykpaoschool\.cn',
                                  email)

        if not name or not ykps_email or not wechat:
            return abort(400)
        else:
            return render_template('qr.html')


@app.route('/add', methods=('POST',))
def add():
    app.logger.info('Someone at the /add page.')
    return render_template('add.html')
