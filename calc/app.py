# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def lets_add():
    "add A and B"

    # get the values and make integer
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    # use the function that was imported from the operations.py file
    result = add(a, b)
    # return the result as string because returned as int
    return str(result)

@app.route('/sub')
def lets_sub():
    "add A and B"

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def lets_mult():
    "multiply A and B"

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def lets_div():
    "divide A by B"

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)

# make single route 
# create a dict that maps string keys to the functions in operations.py file. 
operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

# make route with a string variable
@app.route('/math/<operator>')
def lets_math(operator):
    "do math on a and b"
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    # get the corresponding function of inputted operator
    result = operations[operator](a,b)

    return str(result)