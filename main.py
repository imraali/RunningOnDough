from flask import Flask, render_template,redirect, request, flash,g,session,url_for
import sqlite3 as sql
import os
from models import *

conn = sqlite3.connect('database.db')
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    return render_template('page1.html')

@app.route('/form', methods=["GET","POST"])
def two():
    return render_template('page2.html')

@app.route("/filled", methods=["GET","POST"])
def filled():
    name = request.form['name']
    flight = request.form['flight']
    transport = request.form['transport']
    food = request.form.get('food')
    entertainment = request.form.get('entertainment')
    living = request.form.get('living')

    with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (name,flight,transport,food,entertainment,living) VALUES (?,?,?,?,?,?)", (name,flight,transport,food,entertainment,living) )
            
            con.commit()
    return render_template("page2.html") 
    con.close()


@app.route('/plan')
def three():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from users")

    rows = cur.fetchall();
    return render_template('page3.html', rows=rows)

#@app.route("/logout")
#def logout():
#    session['logged_in'] = False
#    return home()
 
if __name__ == "__main__":
    app.run(debug = True)
