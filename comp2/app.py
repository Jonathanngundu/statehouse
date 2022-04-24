from click import option
from flask import Flask, flash, redirect, render_template, request, url_for
from algorithm import Hosue

app = Flask(__name__)

house_rent = [
    "buying",
    "renting"
]

car_payment = [
    "yes",
    "no"
]



@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.htm", house_rent=house_rent, car_payment=car_payment)

@app.route("/answer", methods=["POST", 'GET'])
def answer():
    global children
    global cars
    global houses
    global state 
    global option_house
    if request.method == "POST":
        state = request.form["state"]
    try:
        if request.method == "POST":
           houses = request.form["house_op"]
           r1 = Hosue(houses, state)
           r1.owner()
           soo = r1.month
    except:
        return "<h1>you forgot to enter something<a href=""/"">Home</a></h1>"
    return render_template("answer.htm", state=state, houses=houses, soo=soo)


