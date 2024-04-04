from flask import Blueprint, render_template, request, flash, redirect, url_for

from safeTravelsBackEnd import safeTravelsdb
import safeTravelsBackEnd
from .loginDetails import loginDetails
from .dbModels import User, passwordQuestions
from werkzeug.security import generate_password_hash, check_password_hash
import requests
auth = Blueprint("auth", __name__)

@auth.route("/loginCustomer",  methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        emailAddress = request.form.get("emailAddress")
        password = request.form.get("password")
        if len(emailAddress) == 0 and len(password) == 0:
            flash("please enter your email and password")
            return render_template("signUp/loginCustomer.html", category = "Login Error",user="",error_message="Please enter your email and password")
        if len(emailAddress) == 0 and len(password) != 0:
            flash("please enter your email")
            return render_template("signUp/loginCustomer.html", category = "Login Error",user="",error_message="Please enter your email")
        if len(emailAddress) != 0 and len(password) == 0:
            flash("please enter your password")
            return render_template("signUp/loginCustomer.html", category = "Login Error",user="",error_message="Please enter your password")
        login = loginDetails(emailAddress, password)
        emailValidation = login.validateEmail()
        if emailValidation:
            user = User.query.filter_by(email = emailAddress).first()
            if user :
                if check_password_hash(user.password, password):
                    flash("Logged In", category="success")
                    return render_template("signUp/loginDetails.html",user=user.userName)
                else:
                    flash("Wrong credentials", category="error")
                    return render_template("signUp/loginCustomer.html",user="",error_message="Wrong credentials")
            else:
                flash("Email does not exist", category = "error")
                return render_template("signUp/loginCustomer.html",user="",error_message="Email does not exist")
        else:
            flash("Please Enter a valid Email")
            return render_template("signUp/loginCustomer.html",error_message="Please Enter a valid Email")
    return render_template("signUp/loginCustomer.html", text = "Trial",user="")

@auth.route("/logoutCustomer", methods = ["GET", "POST"])
def logout():
    if request.method == "POST":
        return redirect(url_for("auth.login"))
    return render_template("signUp/loginCustomer.html",user="")


@auth.route("/registerCustomer", methods=["GET", "POST"])
def registerPage():
    return render_template("signUp/registerCustomer.html")


@auth.route("/registerCustomerDetails", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        emailAddress = request.form.get("emailAddress")
        userName = request.form.get("userName")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        answerOne = request.form.get("answerOne")
        answerTwo = request.form.get("answerTwo")
        answerThree = request.form.get("answerThree")

        username_exists=User.query.filter_by(userName = userName).first()
        if username_exists:
            return render_template("signUp/registerCustomer.html", message="Username is already taken!!")
        login = loginDetails(emailAddress, password)
        emailValidation = login.validateEmail()

        if emailValidation:
            user = User.query.filter_by(email = emailAddress).first()
            if user:
                flash("Email already exists", category = "error")
                return render_template("signUp/registerCustomer.html",message="Email already exists")
            if password != confirmPassword:
                flash("Passwords do not match with each other", category = "error")
                return render_template("signUp/registerCustomer.html",message="Passwords do not match with each other")

        else:
            flash("Please Enter a valid Email")
            return render_template("signUp/registerCustomer.html")
        if len(answerOne) == 0 or len(answerTwo) == 0 or len(answerThree) == 0:
            flash("Please Answer all the questions", category = "error")
            return render_template("signUp/registerCustomer.html",message="Please answer all the questions")
        else:

            newUser = User(userName=userName, email=emailAddress,password=generate_password_hash(password, method='sha256'))
            safeTravelsdb.session.add(newUser)
            safeTravelsdb.session.commit()
            newAnswers = passwordQuestions(answerOne = answerOne, answerTwo = answerTwo, answerThree = answerThree, email = emailAddress)
            safeTravelsdb.session.add(newAnswers)
            safeTravelsdb.session.commit()
    return render_template("signUp/registerCustomer.html",message="success")

@auth.route("/forgetPassword", methods = ["GET", "POST"])
def forgetPassword():
    if request.method == "POST":
        emailAddress = request.form.get("emailAddress")
        answerOne = request.form.get("answerOne")
        answerTwo = request.form.get("answerTwo")
        answerThree = request.form.get("answerThree")
        if len(emailAddress) == 0:
            flash("Please enter an email ", category = "error")
            return render_template("signUp/forgetPassword.html")
        if len(answerOne) == 0 or len(answerTwo) == 0 or len(answerThree) == 0:
            flash("Please Answer all the questions", category = "error")
            return render_template("signUp/forgetPassword.html")
        else:
            user = passwordQuestions.query.filter_by(email = emailAddress)
            if user:
                for u in user:
                    if u.answerOne == answerOne and u.answerTwo == answerTwo and u.answerThree == answerThree:
                        return redirect(url_for("auth.changePassword"))
                    else:
                        flash("Please Check your answers", category = "error")
                        return render_template("signUp/forgetPassword.html")
            else:
                flash("Email not found", category = "error")
                return render_template("signUp/forgetPassword.html")
    else:
        return render_template("signUp/forgetPassword.html")
    

@auth.route("/changePassword", methods = ["GET", "POST"])
def changePassword():
    if request.method == "POST":
        emailAddress = request.form.get("emailAddress")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        if len(emailAddress) == 0:
            flash("Please enter an email ", category = "error")
            return render_template("signUp/changePassword.html")
        if password != confirmPassword:
                flash("Passwords do not match with each other", category = "error")
                return render_template("signUp/changePassword.html")
        user = passwordQuestions.query.filter_by(email = emailAddress)
        if user:
            User.query.filter_by(email = emailAddress).update({'password': generate_password_hash(password, method = 'sha256')})
            safeTravelsdb.session.commit()
            return redirect(url_for("auth.login"))
        else:
            flash("Email does not exists", category = "error")
            return render_template("signUp/changePassword.html")
    else:
        return render_template("signUp/changePassword.html")


@auth.route("/searchHotels", methods = ["GET", "POST"])
def searchHotelsByCity():
    if request.method == "GET":
        args = request.args
        cityName = args.get("cityName")
        adults = args.get("adults")
        rooms = args.get("rooms")
        checkin = args.get("checkin")
        checkout = args.get("checkout")
        params = {
            'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMThhZjI0ODI2NWRkZmYyMGFlZWUxZDc3NjBlYmMyNjRlMGRiYjQ4ZWIyOWE1MjM5M2FlNGI0ZGI2ODc5ODVkYWIwOTVmZDA5ZjM5MzBhOTAiLCJpYXQiOjE2NzczNzU0ODIsIm5iZiI6MTY3NzM3NTQ4MiwiZXhwIjoxNzA4OTExNDgyLCJzdWIiOiIyMDI1NyIsInNjb3BlcyI6W119.tqXpmywCcXjFfU8mmrdgISEsTpIHSFwuAJRdqv2iMKAomZxKF1zIROIVcoOZne6jBEsqwoj-gDFY6vuzK8DeNQ',
            'query':cityName
        }
        api_result = requests.get('https://app.goflightlabs.com/get-location-data', params)
        api_response = api_result.json()
        print(api_response["data"][0])
        if len(api_response["data"])!=0:
            locationId = api_response["data"][0]["location_id"]
            params = {
            'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMThhZjI0ODI2NWRkZmYyMGFlZWUxZDc3NjBlYmMyNjRlMGRiYjQ4ZWIyOWE1MjM5M2FlNGI0ZGI2ODc5ODVkYWIwOTVmZDA5ZjM5MzBhOTAiLCJpYXQiOjE2NzczNzU0ODIsIm5iZiI6MTY3NzM3NTQ4MiwiZXhwIjoxNzA4OTExNDgyLCJzdWIiOiIyMDI1NyIsInNjb3BlcyI6W119.tqXpmywCcXjFfU8mmrdgISEsTpIHSFwuAJRdqv2iMKAomZxKF1zIROIVcoOZne6jBEsqwoj-gDFY6vuzK8DeNQ',
            'locationId': locationId,
            'adults':adults,
            'rooms':rooms,
            'checkin':checkin,
            'checkout':checkout
            }
            api_result = requests.get('https://app.goflightlabs.com/search-hotel-rooms', params)
            hotels = api_result.json()
            print(hotels)
            return hotels["data"]["hotels"]
        else:
            return {}

