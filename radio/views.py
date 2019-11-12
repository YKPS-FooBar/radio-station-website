import re

from flask import render_template, request, abort, redirect

from radio import app


def validate(with_song=False):
    """Validate the name, email, and wechat fields of the request.

    So, generally, for speed there is a client-side validation, but for safety
    (i.e. people like David modifying the source code) we also implement an
    identical server-side validation.  If server-side fails, we return a 400
    bad request.

    Returns name, email, wechat[, slot, song].
    """
    form = request.form.to_dict()

    name = form.pop('name', '').strip()
    email = form.pop('email', '').strip()
    wechat = form.pop('wechat', '').strip()

    # Simple validation on if the email is of ykpaoschool.cn domain.
    ykps_email = re.fullmatch(
        r'[A-Za-z0-9\._-]+@(stu\.)?ykpaoschool\.cn', email
    )

    if not name or not ykps_email or not wechat:
        abort(400)

    if with_song:
        if not form:
            abort(400)
        slot, song = form.popitem()
        slot = slot.strip()
        song = song.strip()
        if not re.fullmatch(r'[0-9]+', slot) or not song:
            abort(400)

        return name, email, wechat, slot, song
    else:
        return name, email, wechat


@app.route('/', methods=('GET',))
def index():
    return render_template('index.html')


@app.route('/pay', methods=('GET', 'POST'))
def pay():
    if request.method == 'GET':
        app.logger.info('Someone at entering their information and paying.')
        return render_template('pay.html')
    else:
        name, email, wechat = validate()
        app.logger.info('Someone is here attempting to access the QR code.\n'
                        f'\tname: {name}, email: {email}, wechat: {wechat}')
        # I know this logic will seem wierd at first, to enter info then pay
        # then enter song.  This is to prevent if the user forgot to pay.  When
        # this happens, if the logic is such that the user pays last, then
        # he/she can't pay again without choosing another song.  In our logic,
        # he/she can simply enter the original info, then pay, then exit
        # without submitting another song.
        return render_template('qr.html',
                               name=name, email=email, wechat=wechat)


@app.route('/add', methods=('POST',))
def add():
    name, email, wechat = validate()
    app.logger.info('Someone at the cell-editing page.\n'
                    f'\tname: {name}, email: {email}, wechat: {wechat}')
    return render_template('add.html',
                           name=name, email=email, wechat=wechat)


@app.route('/submit', methods=('POST',))
def submit():
    name, email, wechat, slot, song = validate(with_song=True)
    app.logger.info(f'Someone added {song!r} at slot {slot}.\n'
                    f'\tname: {name}, email: {email}, wechat: {wechat}')
    return redirect('/')
