from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''
<html>
<head><title></title></head><body>I am alive</body>
</html>
'''
