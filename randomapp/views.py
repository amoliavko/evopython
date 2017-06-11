from randomapp import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'YES'
