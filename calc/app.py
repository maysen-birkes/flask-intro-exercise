from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def calc_add():
    '''Add a and b'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return f"The answer is: {str(result)}"

@app.route('/sub')
def calc_sub():
    '''Subtract b from a'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return f"The answer is: {str(result)}"

@app.route('/mult')
def calc_mult():
    '''Multiply a and b'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return f"The answer is: {str(result)}"

@app.route('/div')
def calc_div():
    '''divide a and b'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return f"The answer is: {str(result)}"

# FURTHER STUDY

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<oper>')
def calculator(oper):
    '''Return selected operation of a and b'''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[oper](a, b)

    return f"The answer is: {str(result)}"