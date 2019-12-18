from flask import Blueprint, render_template, request

bp = Blueprint('index', __name__)

@bp.route('/', methods=('POST'))
def index():
    if request.method == 'POST':
        if request.form.get('submit_button') == 'ON':
            print ('ON')
        elif request.form.get('submit_button') == 'OFF':
            print ('OFF')
        elif request.form.get('submit_button') == 'CLEANUP':
            print ('CLEANUP')
        else:
            pass
    return render_template('index.html')