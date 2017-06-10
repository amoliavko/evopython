from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''
<html>
<head><title>New life</title>
</head>
<body>Hello Dasha. I love you :)<br>
<input>
<input type=submit>
</body>
</html>
'''
