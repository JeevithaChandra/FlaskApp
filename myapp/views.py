# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:16:40 2017

@author: jeevitha
"""

from myapp import myapp
from flask import render_template,redirect,url_for,request,session,flash

myapp.secret_key = "secret"

@myapp.route('/')
@myapp.route('/msg')
def msg():
    return "Hello. Welcome!"
    

# route for handling login page
@myapp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['uname']!='NA' and request.form['pswd']!= 'NA':
            uname = request.form['uname']
            pswd = request.form['pswd']
            return redirect(url_for('Authenticate',username=uname,password=pswd))
        else:
            flash("Invalid Credentials. Try again")
            return redirect(url_for('msg'))
    return render_template('index.html')

#route for handling home page
@myapp.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        if request.form['username']!="jeevitha22" or request.form['password']!="jeevitha123":
            return "Invalid Credentials. Try again"
        else:
            return redirect(url_for('msg'))
    return render_template('home.html')

@myapp.route('/SignUp',methods=['GET','POST'])
def SignUp():
    if request.method == 'POST':
        uname = request.form['uname']
        pswd = request.form['pswd']
        if(uname!='NA' and pswd!='NA' ):
            return redirect(url_for('New_User',username=uname,password=pswd))
        else:
            return "Please enter proper values"
    
    return render_template('signup.html')


@myapp.route("/logout")
#@login_required
def logout():
    session['logged_in'] = False
    return login()

