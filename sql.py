# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:37:20 2017

@author: s42355
"""
import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
#    c.execute("""DROP TABLE posts""")
    c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
