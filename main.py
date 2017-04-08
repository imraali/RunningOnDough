
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/fill', methods = ['GET', 'POST'])
def fill():
#    if request.method == 'POST':
#        user = users(request.form['name'], request.form['flight'],
#        request.form['transport'], request.form['food'], request.form['entertainment'], request.form['living'])
#
#        db.session.add(user)
#        db.session.commit()
#
#        return render_template('show.html', users = users.query.all() )
    return render_template('fill.html')

#@app.route('/all')
#def show_all():
#    engine.execute('select * from users)
#    return render_template('show.html', users = users.query.all() )

#@app.route("/logout")
#def logout():
#    session['logged_in'] = False
#    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
