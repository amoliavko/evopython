from randomapp import app, db
from randomapp.model import Table
from flask import render_template, redirect, request
from randomapp.forms import InputName
import random



@app.route('/')
def index():
    return render_template('index.html')
