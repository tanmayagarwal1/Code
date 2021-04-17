import sqlite3 as sq 
import numpy as np 
con=sq.connect("new.db")
c=con.cursor()

class emp:
    def __init__(self,first,last,gpa):
        self.first=first 
        self.last=last 
        self.gpa=gpa
    @property 
    def email(self):
        return f"{self.first}{self.last}@gmail.com"
def insert(self):
    c.execute("""INSERT INTO emp VALUES (:first,:last,:mail)""",{'first':self.first, 'last':self.last,'mail':self.email})
def fetch(self):
    with con:
        c.execute("SELECT * FROM emp WHERE first= :first",{'first':self.first})
        print(c.fetchall())
def create():
    with con:
        c.execute("""CREATE TABLE emp(first text, last text, mail text)""")
t=emp('tanmay','agarwal',9)
