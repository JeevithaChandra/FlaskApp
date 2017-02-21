# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:16:40 2017

@author: jeevitha
"""

from myapp import myapp
from flask import render_template,redirect,url_for,request

@myapp.route('/')
@myapp.route('/msg')
def msg():
    return "Hello Admin. Welcome!"
    

# route for handling login page
@myapp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['uname']!="jeevitha22" or request.form['pswd']!="jeevitha123":
            return "Invalid Credentials. Try again"
        else:
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
