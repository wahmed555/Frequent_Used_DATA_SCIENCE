from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello book hw 8f Programm </h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1> hello , ! </h1>', 400 
    
app.run(debug=True)
