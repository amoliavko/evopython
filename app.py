from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''
<html>
<head><title>New life</title>
</head>
<body>I am alive<br>
<input>
<input type=submit>
</body>
</html>
'''
