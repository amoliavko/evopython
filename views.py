import app, db

from flask import render_template, redirect, request
from forms import InputName
import random


@app.route('/success', methods=['GET', 'POST'])
def success():
    return 'By'


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello"
