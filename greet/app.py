from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def greet_welcome():
    return '<h1>welcome</h1>'

@app.route('/welcome/home')
def greet_welcome_home():
    return '<h1>welcome home</h1>'

@app.route('/welcome/back')
def greet_welcome_back():
    return '<h1>welcome back</h1>'