#from my_app import app

#app.run()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return "Hello"


app.run()

