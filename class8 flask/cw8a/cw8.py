from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>00Hello World</h1>'

app.run(debug=True)