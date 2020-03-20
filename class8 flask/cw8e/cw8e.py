from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> 8e  Hello book hw</h1>'
    
# tjust for testting
# @app.route('/user')
# def user_0():
#     return '<h1> hello simple user , ! </h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1> hello , {}! </h1>'.format(name)
    
app.run(debug=True)
