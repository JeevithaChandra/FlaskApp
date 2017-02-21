# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:18:57 2017

@author: jeevitha
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp = Flask(__name__)
myapp.config['DEBUG'] = True
myapp.config['SQLALCHEMY_DATABASE_URI']="mysql://root:Arsenal@1986@localhost/myapp"

db = SQLAlchemy(myapp)

#from flaskext.compass import Compass
#from flask_scss import Scss
#compass = Compass(myapp)
#Scss(myapp)

            
from myapp import views,models