from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> 8D  23nd Hello World</h1>'

@app.route('/pakistan/<city>')
# defining 1st method
def index1(city):
    if (city=='karachi'):
        return '<h1> karachi is the largest city of Pakistan <br> in future we shall be picking this all info from  database</h1>'
    elif (city=='lahore'):
        return '<h1> Lahore is the 2nd largest city of Pakistan </h1>' 
    else:   
        return '<h1>lahore \n Karachi \n islamabad </h1>'

@app.route('/india')
# defining 2nd  method
def index2():
    return '<h1>2 amritsur \n bambay \n banglore </h1>'

app.run(debug=True)