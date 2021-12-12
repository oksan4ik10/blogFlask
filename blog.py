from time import time
from flask import Flask, request, g
from werkzeug.exceptions import BadRequest


app = Flask(__name__)

@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(error):
    print(error)  # prints str version of error: 'division by zero'
    app.logger.exception("Here's traceback for zero division error")
    return "Never divide by zero!", 400

@app.route('/')
def func():
    return 'Hello'

