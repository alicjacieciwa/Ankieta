from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    plec = db.Column(db.String)
    wiek = db.Column(db.String)
    wyksztalcenie = db.Column(db.String)
    q1 = db.Column(db.String)
    q2 = db.Column(db.String)
    q3 = db.Column(db.String)


    def __init__(self, plec, wiek, wyksztalcenie, q1, q2, q3):
        self.plec= plec
        self.wiek = wiek
        self.wyksztalcenie = wyksztalcenie
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/form_ankieta")
def show_form_ankieta():
    return render_template('form_ankieta.html')

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




@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions

    q1 = []
    q2 = []
    q3 = []

    for el in fd_list:
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        q3.append(int(el.q3))

    # if len(q1) > 0:
    #     mean_q1 = statistics.mean(q1)
    # else:
    #     mean_q1 = 0
    #
    # if len(q2) > 0:
    #     mean_q2 = statistics.mean(q2)
    # else:
    #     mean_q2 = 0
    #
    # # Prepare data for google charts
    # data = [['Satisfaction', mean_satisfaction], ['Python skill', mean_q1], ['Flask skill', mean_q2]]

    return render_template('result.html', data=data)


@app.route("/save", methods=['POST'])
def save():
    #Get data from FORM
    plec = request.form['plec']
    wiek = request.form['wiek']
    wyksztalcenie = request.form['wyksztalcenie']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']

    # Save the data
    fd = Formdata(plec, wiek, wyksztalcenie, q1, q2, q3)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
