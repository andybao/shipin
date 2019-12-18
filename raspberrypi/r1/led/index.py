import functools
import RPi.GPIO as GPIO

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('index', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        led_pin = 11
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(led_pin, GPIO.OUT)
        if request.form.get('submit_button') == 'ON':
            GPIO.output(led_pin, GPIO.HIGH)
            print ('ON')
        elif request.form.get('submit_button') == 'OFF':
            GPIO.output(led_pin, GPIO.LOW)
            print ('OFF')
        elif request.form.get('submit_button') == 'CLEANUP':
            GPIO.cleanup()
            print ('CLEANUP')
        else:
            pass
    return render_template('index.html')