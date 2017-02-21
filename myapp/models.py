# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:11:40 2017

@author: jeevitha
"""
from myapp import myapp
from flaskext.mysql import MySQL
from flask import redirect,url_for,session
#from flask_login import LoginManager, UserMixin, login_user, login_required,logout_user

mysql = MySQL()
myapp.config['MYSQL_DATABASE_USER'] = 'root'
myapp.config['MYSQL_DATABASE_PASSWORD'] = 'Arsenal@1986'
myapp.config['MYSQL_DATABASE_DB'] = 'myapp'
myapp.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(myapp)

@myapp.route('/Authenticate/<username>/<password>')
def Authenticate(username,password):
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from login where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone() #fetchall()
    if data is None:
     return "Username or Password is wrong"
    else:
     #return render_template('success.html', name = username)
     session['logged_in'] = True
     return redirect(url_for('msg'))
 
    
@myapp.route('/New_User/<username>/<password>')
def New_User(username,password):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("Insert into login values(%s,%s)",(username,password))
    conn.commit()
    return "You have registered successfully"