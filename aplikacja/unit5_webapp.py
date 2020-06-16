from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
import statistics


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    plec = db.Column(db.String, nullable=False)
    wiek = db.Column(db.String, nullable=False)
    wyksztalcenie = db.Column(db.String, nullable=False)
    q1_1 = db.Column(db.String, nullable=False)
    q2_1 = db.Column(db.String, nullable=False)
    q3_1 = db.Column(db.String, nullable=False)
    odp1 = db.Column(db.Integer, nullable=False)
    q1_2 = db.Column(db.String, nullable=False)
    q2_2 = db.Column(db.String, nullable=False)
    q3_2 = db.Column(db.String, nullable=False)
    odp2 = db.Column(db.Integer, nullable=False)
    q1_3 = db.Column(db.String, nullable=False)
    q2_3 = db.Column(db.String, nullable=False)
    q3_3 = db.Column(db.String, nullable=False)
    odp3 = db.Column(db.Integer, nullable=False)
    q1_4 = db.Column(db.String, nullable=False)
    q2_4 = db.Column(db.String, nullable=False)
    q3_4 = db.Column(db.String, nullable=False)
    odp4 = db.Column(db.Integer, nullable=False)
    q1_5 = db.Column(db.String, nullable=False)
    q2_5 = db.Column(db.String, nullable=False)
    q3_5 = db.Column(db.String, nullable=False)
    odp5 = db.Column(db.Integer, nullable=False)
    q1_6 = db.Column(db.String, nullable=False)
    q2_6 = db.Column(db.String, nullable=False)
    q3_6 = db.Column(db.String, nullable=False)
    odp6 = db.Column(db.Integer, nullable=False)
    q1_7 = db.Column(db.String, nullable=False)
    q2_7 = db.Column(db.String, nullable=False)
    q3_7 = db.Column(db.String, nullable=False)
    odp7 = db.Column(db.Integer, nullable=False)
    q1_8 = db.Column(db.String, nullable=False)
    q2_8 = db.Column(db.String, nullable=False)
    q3_8 = db.Column(db.String, nullable=False)
    odp8 = db.Column(db.Integer, nullable=False)
    q1_9 = db.Column(db.String, nullable=False)
    q2_9 = db.Column(db.String, nullable=False)
    q3_9 = db.Column(db.String, nullable=False)
    odp9 = db.Column(db.Integer, nullable=False)
    q1_10 = db.Column(db.String, nullable=False)
    q2_10 = db.Column(db.String, nullable=False)
    q3_10 = db.Column(db.String, nullable=False)
    odp10 = db.Column(db.Integer, nullable=False)

    # def __init__(self, plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1,odp1, q1_2, q2_2, q3_2,odp2, q1_3, q2_3, q3_3, q1_4, q2_4, q3_4, q1_5, q2_5, q3_5):
    def __init__(self, plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1, odp1, q1_2, q2_2, q3_2, odp2, q1_3, q2_3, q3_3,odp3, q1_4, q2_4, q3_4, odp4, q1_5, q2_5, q3_5, odp5, q1_6, q2_6, q3_6, odp6, q1_7, q2_7, q3_7, odp7, q1_8, q2_8, q3_8, odp8, q1_9, q2_9, q3_9, odp9, q1_10, q2_10, q3_10, odp10):
        self.plec = plec
        self.wiek = wiek
        self.wyksztalcenie = wyksztalcenie
        self.q1_1 = q1_1
        self.q2_1 = q2_1
        self.q3_1 = q3_1
        self.odp1 = odp1
        self.q1_2 = q1_2
        self.q2_2 = q2_2
        self.q3_2 = q3_2
        self.odp2 = odp2
        self.q1_3 = q1_3
        self.q2_3 = q2_3
        self.q3_3 = q3_3
        self.odp3 = odp3
        self.q1_4 = q1_4
        self.q2_4 = q2_4
        self.q3_4 = q3_4
        self.odp4 = odp4
        self.q1_5 = q1_5
        self.q2_5 = q2_5
        self.q3_5 = q3_5
        self.odp5 = odp5
        self.q1_6 = q1_6
        self.q2_6 = q2_6
        self.q3_6 = q3_6
        self.odp6 = odp6
        self.q1_7 = q1_7
        self.q2_7 = q2_7
        self.q3_7 = q3_7
        self.odp7 = odp7
        self.q1_8 = q1_8
        self.q2_8 = q2_8
        self.q3_8 = q3_8
        self.odp8 = odp8
        self.q1_9 = q1_9
        self.q2_9 = q2_9
        self.q3_9 = q3_9
        self.odp9 = odp9
        self.q1_10 = q1_10
        self.q2_10 = q2_10
        self.q3_10 = q3_10
        self.odp10 = odp10


db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')


@app.route("/form/questions")
def show_questions():
    return render_template('questions.html')

@app.route("/aboutus")
def show_aboutus():
    return render_template('aboutus.html')

@app.route("/aboutproject")
def show_aboutproject():
    return render_template('aboutproject.html')

@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/wyniki")
def show_wyniki():
    fd = db.session.query(Formdata).all()
    suma1 = []
    suma2 = []
    sumaW1 = []
    sumaW2 = []
    sumaW3 = []
    sumaW4 = []
    sumaW5 = []
    sumaWy1 = []
    sumaWy2 = []
    sumaWy3 = []
    sumaWy4 = []
    sumaWy5 = []
    sumaWy6 = []
    sumaWy7 = []
    lF = 0
    lM = 0
    lw1 = 0
    lw2 = 0
    lw3 = 0
    lw4 = 0
    lw5 = 0
    lwy1 = 0
    lwy2 = 0
    lwy3 = 0
    lwy4 = 0
    lwy5 = 0
    lwy6 = 0
    lwy7 = 0
    for el in fd:
        if el.plec == 'F':
            lF += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or ((el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp1 = 10
            else:
                temp1 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or ((el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp2 = 10
            else:
                temp2 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or ((el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp3 = 10
            else:
                temp3 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or ((el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp4 = 10
            else:
                temp4 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or ((el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp5 = 10
            else:
                temp5 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or ((el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp6 = 10
            else:
                temp6 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or ((el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp7 = 10
            else:
                temp7 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or ((el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp8 = 10
            else:
                temp8 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or ((el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp9 = 10
            else:
                temp9 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or ((el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp10 = 10
            else:
                temp10 = 0
            s1 = temp1 + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8 + temp9 + temp10
            suma1.append(int(s1))
        if el.plec == 'M':
            lM += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or ((el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp11 = 10
            else:
                temp11 = 0
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or ((el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp12 = 10
            else:
                temp12 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or ((el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp13 = 10
            else:
                temp13 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or ((el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp14 = 10
            else:
                temp14 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or ((el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp15 = 10
            else:
                temp15 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or ((el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp16 = 10
            else:
                temp16 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or ((el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp17 = 10
            else:
                temp17 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or ((el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp18 = 10
            else:
                temp18 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or ((el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp19 = 10
            else:
                temp19 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or ((el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp20 = 10
            else:
                temp20 = 0
            s2 = temp11 + temp12 + temp13 + temp14 + temp15 + temp16 + temp17 + temp18 + temp19 + temp20
            suma2.append(int(s2))
        if el.wiek == '<18':
            lw1 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp21 = 10
            else:
                temp21 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp22 = 10
            else:
                temp22 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp23 = 10
            else:
                temp23 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp24 = 10
            else:
                temp24 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp25 = 10
            else:
                temp25 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp26 = 10
            else:
                temp26 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp27 = 10
            else:
                temp27 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp28 = 10
            else:
                temp28 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp29 = 10
            else:
                temp29 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp30 = 10
            else:
                temp30 = 0
            sw1 = temp21 + temp22 + temp23 + temp24 + temp25 + temp26 + temp27 + temp28 + temp29 + temp30
            sumaW1.append(int(sw1))
        if el.wiek == '18-25':
            lw2 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp31 = 10
            else:
                temp31 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp32 = 10
            else:
                temp32 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp33 = 10
            else:
                temp33 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp34 = 10
            else:
                temp34 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp35 = 10
            else:
                temp35 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp36 = 10
            else:
                temp36 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp37 = 10
            else:
                temp37 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp38 = 10
            else:
                temp38 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp39 = 10
            else:
                temp39 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp40 = 10
            else:
                temp40 = 0
            sw2 = temp31 + temp32 + temp33 + temp34 + temp35 + temp36 + temp37 + temp38 + temp39 + temp40
            sumaW2.append(int(sw2))
        if el.wiek == '25-40':
            lw3 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp41 = 10
            else:
                temp41 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp42 = 10
            else:
                temp42 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp43 = 10
            else:
                temp43 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp44 = 10
            else:
                temp44 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp45 = 10
            else:
                temp45 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp46 = 10
            else:
                temp46 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp47 = 10
            else:
                temp47 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp48 = 10
            else:
                temp48 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp49 = 10
            else:
                temp49 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp50 = 10
            else:
                temp50 = 0
            sw3 = temp41 + temp42 + temp43 + temp44 + temp45 + temp46 + temp47 + temp48 + temp49 + temp50
            sumaW3.append(int(sw3))
        if el.wiek == '41-60':
            lw4 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp51 = 10
            else:
                temp51 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp52 = 10
            else:
                temp52 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp53 = 10
            else:
                temp53 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp54 = 10
            else:
                temp54 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp55 = 10
            else:
                temp55 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp56 = 10
            else:
                temp56 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp57 = 10
            else:
                temp57 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp58 = 10
            else:
                temp58 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp59 = 10
            else:
                temp59 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp60 = 10
            else:
                temp60 = 0
            sw4 = temp51 + temp52 + temp53 + temp54 + temp55 + temp56 + temp57 + temp58 + temp59 + temp60
            sumaW4.append(int(sw4))
        if el.wiek == '60+':
            lw5 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp61 = 10
            else:
                temp61 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp62 = 10
            else:
                temp62 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp63 = 10
            else:
                temp63 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp64 = 10
            else:
                temp64 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp65 = 10
            else:
                temp65 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp66 = 10
            else:
                temp66 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp67 = 10
            else:
                temp67 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp68 = 10
            else:
                temp68 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp69 = 10
            else:
                temp69 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp70 = 10
            else:
                temp70 = 0
            sw5 = temp61 + temp62 + temp63 + temp64 + temp65 + temp66 + temp67 + temp68 + temp69 + temp70
            sumaW5.append(int(sw5))
        if el.wyksztalcenie == 'podstawowe':
            lwy1 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp71 = 10
            else:
                temp71 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp72 = 10
            else:
                temp72 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp73 = 10
            else:
                temp73 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp74 = 10
            else:
                temp74 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp75 = 10
            else:
                temp75 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp76 = 10
            else:
                temp76 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp77 = 10
            else:
                temp77 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp78 = 10
            else:
                temp78 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp79 = 10
            else:
                temp79 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp80 = 10
            else:
                temp80 = 0
            swy1 = temp71 + temp72 + temp73 + temp74 + temp75 + temp76 + temp77 + temp78 + temp79 + temp80
            sumaWy1.append(int(swy1))
        if el.wyksztalcenie == 'średnie':
            lwy2 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp81 = 10
            else:
                temp81 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp82 = 10
            else:
                temp82 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp83 = 10
            else:
                temp83 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp84 = 10
            else:
                temp84 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp85 = 10
            else:
                temp85 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp86 = 10
            else:
                temp86 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp87 = 10
            else:
                temp87 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp88 = 10
            else:
                temp88 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp89 = 10
            else:
                temp89 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp90 = 10
            else:
                temp90 = 0
            swy2 = temp81 + temp82 + temp83 + temp84 + temp85 + temp86 + temp87 + temp88 + temp89 + temp90
            sumaWy2.append(int(swy2))
        if el.wyksztalcenie == 'wyższe':
            lwy3 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp91 = 10
            else:
                temp91 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp92 = 10
            else:
                temp92 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp93 = 10
            else:
                temp93 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp94 = 10
            else:
                temp94 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp95 = 10
            else:
                temp95 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp96 = 10
            else:
                temp96 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp97 = 10
            else:
                temp97 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp98 = 10
            else:
                temp98 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp99 = 10
            else:
                temp99 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp100 = 10
            else:
                temp100 = 0
            swy3 = temp91 + temp92 + temp93 + temp94 + temp95 + temp96 + temp97 + temp98 + temp99 + temp100
            sumaWy3.append(int(swy3))
        if el.wyksztalcenie == 'zawodowe':
            lwy4 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp101 = 10
            else:
                temp101 = 0
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp102 = 10
            else:
                temp102 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp103 = 10
            else:
                temp103 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp104 = 10
            else:
                temp104 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp105 = 10
            else:
                temp105 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp106 = 10
            else:
                temp106 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp107 = 10
            else:
                temp107 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp108 = 10
            else:
                temp108 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp109 = 10
            else:
                temp109 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp110 = 10
            else:
                temp110 = 0
            swy4 = temp101 + temp102 + temp103 + temp104 + temp105 + temp106 + temp107 + temp108 + temp109 + temp110
            sumaWy4.append(int(swy4))
        if el.wyksztalcenie == 'gimnazjalne':
            lwy5 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp111 = 10
            else:
                temp111 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp112 = 10
            else:
                temp112 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp113 = 10
            else:
                temp113 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp114 = 10
            else:
                temp114 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp115 = 10
            else:
                temp115 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp116 = 10
            else:
                temp116 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp117 = 10
            else:
                temp117 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp118 = 10
            else:
                temp118 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp119 = 10
            else:
                temp119 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp120 = 10
            else:
                temp120 = 0
            swy5 = temp111 + temp112 + temp113 + temp114 + temp115 + temp116 + temp117 + temp118 + temp119 + temp120
            sumaWy5.append(int(swy5))
        if el.wyksztalcenie == 'brak':
            lwy6 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp121 = 10
            else:
                temp121 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp122 = 10
            else:
                temp122 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp123 = 10
            else:
                temp123 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp124 = 10
            else:
                temp124 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp125 = 10
            else:
                temp125 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp126 = 10
            else:
                temp126 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp127 = 10
            else:
                temp127 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp128 = 10
            else:
                temp128 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp129 = 10
            else:
                temp129 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp130 = 10
            else:
                temp130 = 0
            swy6 = temp121 + temp122 + temp123 + temp124 + temp125 + temp126 + temp127 + temp128 + temp129 + temp130
            sumaWy6.append(int(swy6))
        if el.wyksztalcenie == 'inne':
            lwy7 += 1
            if ((el.q3_1 == '100' or el.q3_1 == '75') and el.odp1 >= 17) or (
                    (el.q3_1 == '0' or el.q3_1 == '25') and el.odp1 < 17):
                temp131 = 10
            else:
                temp131 = 10
            if ((el.q3_2 == '100' or el.q3_2 == '75') and el.odp2 >= 17) or (
                    (el.q3_2 == '0' or el.q3_2 == '25') and el.odp2 < 17):
                temp132 = 10
            else:
                temp132 = 0
            if ((el.q3_3 == '100' or el.q3_3 == '75') and el.odp3 >= 17) or (
                    (el.q3_3 == '0' or el.q3_3 == '25') and el.odp3 < 17):
                temp133 = 10
            else:
                temp133 = 0
            if ((el.q3_4 == '100' or el.q3_4 == '75') and el.odp4 >= 17) or (
                    (el.q3_4 == '0' or el.q3_4 == '25') and el.odp4 < 17):
                temp134 = 10
            else:
                temp134 = 0
            if ((el.q3_5 == '100' or el.q3_5 == '75') and el.odp5 >= 17) or (
                    (el.q3_5 == '0' or el.q3_5 == '25') and el.odp5 < 17):
                temp135 = 10
            else:
                temp135 = 0
            if ((el.q3_6 == '100' or el.q3_6 == '75') and el.odp6 >= 17) or (
                    (el.q3_6 == '0' or el.q3_6 == '25') and el.odp6 < 17):
                temp136 = 10
            else:
                temp136 = 0
            if ((el.q3_7 == '100' or el.q3_7 == '75') and el.odp7 >= 17) or (
                    (el.q3_7 == '0' or el.q3_7 == '25') and el.odp7 < 17):
                temp137 = 10
            else:
                temp137 = 0
            if ((el.q3_8 == '100' or el.q3_8 == '75') and el.odp8 >= 17) or (
                    (el.q3_8 == '0' or el.q3_8 == '25') and el.odp8 < 17):
                temp138 = 10
            else:
                temp138 = 0
            if ((el.q3_9 == '100' or el.q3_9 == '75') and el.odp9 >= 17) or (
                    (el.q3_9 == '0' or el.q3_9 == '25') and el.odp9 < 17):
                temp139 = 10
            else:
                temp139 = 0
            if ((el.q3_10 == '100' or el.q3_10 == '75') and el.odp10 >= 17) or (
                    (el.q3_10 == '0' or el.q3_10 == '25') and el.odp10 < 17):
                temp140 = 10
            else:
                temp140 = 0
            swy7 = temp131 + temp132 + temp133 + temp134 + temp135 + temp136 + temp137 + temp138 + temp139 + temp140
            sumaWy7.append(int(swy7))
    if len(suma1) > 0:
        mean_s1 = statistics.mean(suma1)
    else:
        mean_s1 = 0
    if len(suma2) > 0:
        mean_s2 = statistics.mean(suma2)
    else:
        mean_s2 = 0
    plec = [mean_s2, mean_s1]
    if len(sumaW1) > 0:
        mean_w1 = statistics.mean(sumaW1)
    else:
        mean_w1 = 0
    if len(sumaW2) > 0:
        mean_w2 = statistics.mean(sumaW2)
    else:
        mean_w2 = 0
    if len(sumaW3) > 0:
        mean_w3 = statistics.mean(sumaW3)
    else:
        mean_w3 = 0
    if len(sumaW4) > 0:
        mean_w4 = statistics.mean(sumaW4)
    else:
        mean_w4 = 0
    if len(sumaW5) > 0:
        mean_w5 = statistics.mean(sumaW5)
    else:
        mean_w5 = 0
    wiek = [mean_w1, mean_w2, mean_w3, mean_w4, mean_w5]
    if len(sumaWy1) > 0:
        mean_wy1 = statistics.mean(sumaWy1)
    else:
        mean_wy1 = 0
    if len(sumaWy2) > 0:
        mean_wy2 = statistics.mean(sumaWy2)
    else:
        mean_wy2 = 0
    if len(sumaWy3) > 0:
        mean_wy3 = statistics.mean(sumaWy3)
    else:
        mean_wy3 = 0
    if len(sumaWy4) > 0:
        mean_wy4 = statistics.mean(sumaWy4)
    else:
        mean_wy4 = 0
    if len(sumaWy5) > 0:
        mean_wy5 = statistics.mean(sumaWy5)
    else:
        mean_wy5 = 0
    if len(sumaWy6) > 0:
        mean_wy6 = statistics.mean(sumaWy6)
    else:
        mean_wy6 = 0
    if len(sumaWy7) > 0:
        mean_wy7 = statistics.mean(sumaWy7)
    else:
        mean_wy7 = 0
    wyk = [mean_wy1, mean_wy2, mean_wy3, mean_wy4, mean_wy5, mean_wy6, mean_wy7]
    lP = [lM, lF]
    lwiek = [lw1, lw2, lw3, lw4, lw5]
    lwyk = [lwy1, lwy2, lwy3, lwy4, lwy5, lwy6, lwy7]
    return render_template('wyniki.html', dataP=plec, dataW=wiek, dataWy=wyk, lP=lP, lwiek=lwiek, lwyk=lwyk)


@app.route("/save", methods=['POST'])
def save():
    #Get data from FORM
    plec= request.form['plec']
    wiek = request.form['wiek']
    wyksztalcenie = request.form['wyksztalcenie']
    q1_1 = request.form['q1_1']
    q2_1 = request.form['q2_1']
    q3_1 = request.form['q3_1']
    odp1 = request.form['odp1']
    q1_2 = request.form['q1_2']
    q2_2 = request.form['q2_2']
    q3_2 = request.form['q3_2']
    odp2 = request.form['odp2']
    q1_3 = request.form['q1_3']
    q2_3 = request.form['q2_3']
    q3_3 = request.form['q3_3']
    odp3 = request.form['odp3']
    q1_4 = request.form['q1_4']
    q2_4 = request.form['q2_4']
    q3_4 = request.form['q3_4']
    odp4 = request.form['odp4']
    q1_5 = request.form['q1_5']
    q2_5 = request.form['q2_5']
    q3_5 = request.form['q3_5']
    odp5 = request.form['odp5']
    q1_6 = request.form['q1_6']
    q2_6 = request.form['q2_6']
    q3_6 = request.form['q3_6']
    odp6 = request.form['odp6']
    q1_7 = request.form['q1_7']
    q2_7 = request.form['q2_7']
    q3_7 = request.form['q3_7']
    odp7 = request.form['odp7']
    q1_8 = request.form['q1_8']
    q2_8 = request.form['q2_8']
    q3_8 = request.form['q3_8']
    odp8 = request.form['odp8']
    q1_9 = request.form['q1_9']
    q2_9 = request.form['q2_9']
    q3_9 = request.form['q3_9']
    odp9 = request.form['odp9']
    q1_10 = request.form['q1_10']
    q2_10 = request.form['q2_10']
    q3_10 = request.form['q3_10']
    odp10 = request.form['odp10']



    # Save the data
    # fd = Formdata(plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1, q1_2, q2_2, q3_2, q1_3, q2_3, q3_3, q1_4, q2_4, q3_4, q1_5, q2_5, q3_5)
    fd = Formdata(plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1, odp1, q1_2, q2_2, q3_2, odp2,q1_3, q2_3, q3_3, odp3, q1_4, q2_4, q3_4, odp4, q1_5, q2_5, q3_5, odp5, q1_6, q2_6, q3_6, odp6, q1_7, q2_7, q3_7, odp7, q1_8, q2_8, q3_8, odp8, q1_9, q2_9, q3_9, odp9, q1_10, q2_10, q3_10, odp10)
    db.session.add(fd)
    db.session.commit()

    return redirect('/wyniki')


if __name__ == "__main__":
    app.debug = True
    app.run()
