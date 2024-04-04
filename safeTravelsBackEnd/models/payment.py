from flask import Blueprint, redirect, url_for
from flask import jsonify
from flask import render_template, request
import requests
import requests
import json
from .dbModels import paymentQuestions

payment = Blueprint("payment", __name__)


finalCost = ""

@payment.route('/requestPayments', methods= ["GET", "POST"])
def requestPayment():
    if request.method == "POST":
        emailAddress = request.form.get("emailAddress")
        print(paymentQuestions)
        payment = paymentQuestions.query.filter_by(email = emailAddress).first()
        if payment :
            global finalCost
            finalCost = payment.cost
            return redirect(url_for('payment.process_payment'))
        else:
            return render_template('signUp/requestPayments.html')
    else:
        return render_template('signUp/requestPayments.html')

@payment.route('/payments', methods= ["GET", "POST"])
def process_payment():
    if request.method == "POST":
        cardNumber = request.form.get("cardNumber")
        expiry = request.form.get("expiry")
        nameCard = request.form.get("nameCard")
        CVV = request.form.get("CVV")
        if len(cardNumber)!= 16 or len(CVV) != 3:
            return render_template('signUp/payments.html', message = finalCost)
        else:

            return redirect(url_for('payment.confirmation'))
    else:
        return render_template('signUp/payments.html', message = finalCost)

@payment.route('/confirmation')
def confirmation():
    return render_template('signUp/confirmation.html')

# @payment.route('/payments', methods = ["GET", "POST"])
# def flights():
#     if request.method == "POST":
