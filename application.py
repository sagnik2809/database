# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z2ziwmIwY6kwiJ0eyLLfMYbJiccgQ7_h
"""

print("hello world")

import pymysql
import pandas as pd
from flask import Flask
from flask import template_rendered
conn = pymysql.connect(
    host='database-1.cnui1vzr7htw.us-east-2.rds.amazonaws.com',
    user="admin",
    passwd='black10belt',
    database='moviedb')
mycursor = conn.cursor()
application = Flask(__name__)
@application.route('/')
def index():
  mycursor.execute("select * from movies")
  data=mycursor.fetchall()
  return render_template('index.html',data=data)
if __name__=="_main_":
  application.run(debug=true)

