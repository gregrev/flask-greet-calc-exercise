from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return "welcome"

@app.route('/welcome/home')
def home_home():
    return "welcome home"

@app.route('/welcome/back')
def back_home():
    return "welcome back"
