
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
app = Flask(__name__)

@app.route('/')
def home():
#    <input type="submit" name="submit" value="Do Something">
    if request.method == 'POST':
        return render_template('page2.html')
    return render_template('page1.html')

@app.route('/form')
def two():
    if request.method == 'POST':
        return render_template('page3.html')
    return render_template('page2.html')


@app.route('/plan')
def three():
    return render_template('page3.html')

#@app.route("/logout")
#def logout():
#    session['logged_in'] = False
#    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
