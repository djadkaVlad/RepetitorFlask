import os
from dotenv import load_dotenv
import dotenv
import flask
from pprint import pprint
from flask import Flask, request, redirect, url_for, render_template
import flask_wtf
import wtforms
import data
import calendar
from datetime import datetime


load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
week =  {
    'mon':"Понедельник",'tue':"Вторник",
    'wed':"Среда",'thu':"Четверг",
    'fri':"Пятница",'sat':"Суббота",
    'sun':"Воскресенье"
}



def check_notfree_values(dictionary):
    '''Проверяет все значения в словаре'''
    free = all(value == False for value in dictionary.values())
    return free



class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('Имя')
    email = wtforms.StringField('Почта')
    submit = wtforms.SubmitField('ОТправить')


app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def home():

    return render_template('index.html',goals=data.goals,teachers=data.teachers)


@app.route('/all/')
def all_page():
    return render_template('all.html')


@app.route('/goals')
@app.route('/goals/<goal>/')
def goal_page(goal=None):
    return render_template('goal.html')



@app.route('/profiles/<int:id>/')
def profile_page(id):
    available = []
    grafik_free = data.teachers[id]['free']
    for key,value in grafik_free.items():
        ret = check_notfree_values(value)
        available.append(ret)
    print(available)
    # print(check_values(grafik_free))

    return render_template('profile.html',id=id,goals=data.goals,teachers=data.teachers,available=available)


@app.route('/request/', methods=['GET', 'POST'])
def request_page():
    return render_template('request.html')

@app.route('/request_done/', methods=['GET', 'POST'])
def request_done_page():
    return render_template('request_done.html')

@app.route('/booking/<int:id_teacher>/<day>/<time>/', methods=['GET', 'POST'])
def booking_page(id_teacher,day,time):
    return render_template('booking.html',id_teacher=id_teacher,day=day,time=time,teachers=data.teachers,week=week[day])

@app.route('/booking_done/', methods=['GET', 'POST'])
def booking_done_page():
    return render_template('booking_done.html')

if __name__ == '__main__':
    app.run(debug=True)
