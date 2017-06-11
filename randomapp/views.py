from randomapp import app, db

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'YES'
