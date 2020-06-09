from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
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
    q1_2 = db.Column(db.String, nullable=False)
    q2_2 = db.Column(db.String, nullable=False)
    q3_2 = db.Column(db.String, nullable=False)
    q1_3 = db.Column(db.String, nullable=False)
    q2_3 = db.Column(db.String, nullable=False)
    q3_3 = db.Column(db.String, nullable=False)
    q1_4 = db.Column(db.String, nullable=False)
    q2_4 = db.Column(db.String, nullable=False)
    q3_4 = db.Column(db.String, nullable=False)
    q1_5 = db.Column(db.String, nullable=False)
    q2_5 = db.Column(db.String, nullable=False)
    q3_5 = db.Column(db.String, nullable=False)
    q1_6 = db.Column(db.String, nullable=False)
    q2_6 = db.Column(db.String, nullable=False)
    q3_6 = db.Column(db.String, nullable=False)
    q1_7 = db.Column(db.String, nullable=False)
    q2_7 = db.Column(db.String, nullable=False)
    q3_7 = db.Column(db.String, nullable=False)
    q1_8 = db.Column(db.String, nullable=False)
    q2_8 = db.Column(db.String, nullable=False)
    q3_8 = db.Column(db.String, nullable=False)
    q1_9 = db.Column(db.String, nullable=False)
    q2_9 = db.Column(db.String, nullable=False)
    q3_9 = db.Column(db.String, nullable=False)
    q1_10 = db.Column(db.String, nullable=False)
    q2_10 = db.Column(db.String, nullable=False)
    q3_10 = db.Column(db.String, nullable=False)

    # def __init__(self, plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1, q1_2, q2_2, q3_2, q1_3, q2_3, q3_3, q1_4, q2_4, q3_4, q1_5, q2_5, q3_5):
    def __init__(self, plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1, q1_2, q2_2, q3_2, q1_3, q2_3, q3_3, q1_4, q2_4, q3_4, q1_5, q2_5, q3_5, q1_6, q2_6, q3_6, q1_7, q2_7, q3_7, q1_8, q2_8, q3_8, q1_9, q2_9, q3_9, q1_10, q2_10, q3_10):
        self.plec = plec
        self.wiek = wiek
        self.wyksztalcenie = wyksztalcenie
        self.q1_1 = q1_1
        self.q2_1 = q2_1
        self.q3_1 = q3_1
        self.q1_2 = q1_2
        self.q2_2 = q2_2
        self.q3_2 = q3_2
        self.q1_3 = q1_3
        self.q2_3 = q2_3
        self.q3_3 = q3_3
        self.q1_4 = q1_4
        self.q2_4 = q2_4
        self.q3_4 = q3_4
        self.q1_5 = q1_5
        self.q2_5 = q2_5
        self.q3_5 = q3_5
        self.q1_6 = q1_6
        self.q2_6 = q2_6
        self.q3_6 = q3_6
        self.q1_7 = q1_7
        self.q2_7 = q2_7
        self.q3_7 = q3_7
        self.q1_8 = q1_8
        self.q2_8 = q2_8
        self.q3_8 = q3_8
        self.q1_9 = q1_9
        self.q2_9 = q2_9
        self.q3_9 = q3_9
        self.q1_10 = q1_10
        self.q2_10 = q2_10
        self.q3_10 = q3_10


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
    fd_list = db.session.query(Formdata).all()

    q1_1 = []
    q2_1 = []
    q3_1 = []
    q1_2 = []
    q2_2 = []
    q3_2 = []
    q1_3 = []
    q2_3 = []
    q3_3 = []
    q1_4 = []
    q2_4 = []
    q3_4 = []
    q1_5 = []
    q2_5 = []
    q3_5 = []
    q1_6 = []
    q2_6 = []
    q3_6 = []
    q1_7 = []
    q2_7 = []
    q3_7 = []
    q1_8 = []
    q2_8 = []
    q3_8 = []
    q1_9 = []
    q2_9 = []
    q3_9 = []
    q1_10 = []
    q2_10 = []
    q3_10 = []
#
#     #
#     #
#     # for el in fd_list:
#     #     q1_1.append(int(el.q1_1))
#     #     q2_1.append(int(el.q2_1))
#     #     q3_1.append(int(el.q3_1))
#
#     # if len(q1) > 0:
#     #     mean_q1 = statistics.mean(q1)
#     # else:
#     #     mean_q1 = 0
#     #
#     # if len(q2) > 0:
#     #     mean_q2 = statistics.mean(q2)
#     # else:
#     #     mean_q2 = 0
#     #
#     # # Prepare data for google charts
#     # data = [['Satisfaction', mean_satisfaction], ['Python skill', mean_q1], ['Flask skill', mean_q2]]
#
    return render_template('wyniki.html')


@app.route("/save", methods=['POST'])
def save():
    #Get data from FORM
    plec= request.form['plec']
    wiek = request.form['wiek']
    wyksztalcenie = request.form['wyksztalcenie']
    q1_1 = request.form['q1_1']
    q2_1 = request.form['q2_1']
    q3_1 = request.form['q3_1']
    q1_2 = request.form['q1_2']
    q2_2 = request.form['q2_2']
    q3_2 = request.form['q3_2']
    q1_3 = request.form['q1_3']
    q2_3 = request.form['q2_3']
    q3_3 = request.form['q3_3']
    q1_4 = request.form['q1_4']
    q2_4 = request.form['q2_4']
    q3_4 = request.form['q3_4']
    q1_5 = request.form['q1_5']
    q2_5 = request.form['q2_5']
    q3_5 = request.form['q3_5']
    q1_6 = request.form['q1_6']
    q2_6 = request.form['q2_6']
    q3_6 = request.form['q3_6']
    q1_7 = request.form['q1_7']
    q2_7 = request.form['q2_7']
    q3_7 = request.form['q3_7']
    q1_8 = request.form['q1_8']
    q2_8 = request.form['q2_8']
    q3_8 = request.form['q3_8']
    q1_9 = request.form['q1_9']
    q2_9 = request.form['q2_9']
    q3_9 = request.form['q3_9']
    q1_10 = request.form['q1_10']
    q2_10 = request.form['q2_10']
    q3_10 = request.form['q3_10']



    # Save the data
    # fd = Formdata(plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1, q1_2, q2_2, q3_2, q1_3, q2_3, q3_3, q1_4, q2_4, q3_4, q1_5, q2_5, q3_5)
    fd = Formdata(plec, wiek, wyksztalcenie, q1_1, q2_1, q3_1, q1_2, q2_2, q3_2, q1_3, q2_3, q3_3, q1_4, q2_4, q3_4, q1_5, q2_5, q3_5, q1_6, q2_6, q3_6, q1_7, q2_7, q3_7, q1_8, q2_8, q3_8, q1_9, q2_9, q3_9, q1_10, q2_10, q3_10)
    db.session.add(fd)
    db.session.commit()

    return redirect('/wyniki')


if __name__ == "__main__":
    app.debug = True
    app.run()
