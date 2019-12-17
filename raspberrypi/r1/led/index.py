import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('index', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        if request.form.get('submit_button') == 'ON':
            print ('ON')
        elif request.form.get('submit_button') == 'OFF':
            print ('OFF')
        else:
            pass
    return render_template('index.html')