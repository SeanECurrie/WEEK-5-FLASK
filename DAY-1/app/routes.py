from app import app
from flask import render_template

@app.route('/home')
def home():
    
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


