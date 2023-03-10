from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("mainPage.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/menu")
def menu():
    return render_template("menuPage.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/bookingService")
def bookingService():
    dataBase = open('dataBase.txt','a')
    dataBase.write(request.args.get("firstname") + " ")
    dataBase.write(request.args.get("surname") + " ")
    dataBase.write("Count of people: " + request.args.get("countOfPeople") + " ")
    dataBase.write("data: " + request.args.get("data"))
    dataBase.write('\n')
    return render_template("succesfulBooking.html")


if __name__ == "__main__":
    app.run()