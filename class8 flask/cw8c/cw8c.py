from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>2Hello World</h1>'

@app.route('/pakistan')
def index1():
    return '<h1>lahore \n Karachi \n islamabad </h1>'

@app.route('/india')
def index2():
    return '<h1>amritsur \n bambay \n banglore </h1>'

app.run(debug=True)