from sqlalchemy.dialects import postgresql

from .. import safeTravelsdb
from flask_login import UserMixin
#from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import *

class User(safeTravelsdb.Model, UserMixin):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key = True)
    userName = safeTravelsdb.Column(safeTravelsdb.String(150))
    email = safeTravelsdb.Column(safeTravelsdb.String(150), unique = True)
    password = safeTravelsdb.Column(safeTravelsdb.String(150))
    # itineraries = safeTravelsdb.relationship('Itinerary', backref='user', lazy=True)
    # reviews = safeTravelsdb.relationship('Review', backref='user', lazy=True)
    # note = safeTravelsdb.relationship('Note')

class Note(safeTravelsdb.Model):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key = True)
    data = safeTravelsdb.Column(safeTravelsdb.String(1000))
    #date = safeTravelsdb.Column(safeTravelsdb.DateTime(timezone = True), default = func.now())
    userId = safeTravelsdb.Column(safeTravelsdb.Integer, safeTravelsdb.ForeignKey('user.id'))

class passwordQuestions(safeTravelsdb.Model):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key = True)
    email = safeTravelsdb.Column(safeTravelsdb.String(150), unique = True)
    answerOne = safeTravelsdb.Column(safeTravelsdb.String(1000))
    answerTwo = safeTravelsdb.Column(safeTravelsdb.String(1000))
    answerThree = safeTravelsdb.Column(safeTravelsdb.String(1000))

class paymentQuestions(safeTravelsdb.Model):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key = True)
    email = safeTravelsdb.Column(safeTravelsdb.String(150), unique = True)
    cost = safeTravelsdb.Column(safeTravelsdb.String(1000))

class wishlistRestaurants(safeTravelsdb.Model):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key=True)
    userId = safeTravelsdb.Column(safeTravelsdb.String(20))
    restaurantName = safeTravelsdb.Column(safeTravelsdb.String(150),unique=True)
    city = safeTravelsdb.Column(safeTravelsdb.String(150))
    ratings=safeTravelsdb.Column(safeTravelsdb.Integer)
    image=safeTravelsdb.Column(safeTravelsdb.String(150))
    phone = safeTravelsdb.Column(safeTravelsdb.String(20))

class wishlistAttractions(safeTravelsdb.Model):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key=True)
    userId = safeTravelsdb.Column(safeTravelsdb.String(20))
    attractionName = safeTravelsdb.Column(safeTravelsdb.String(150),unique=True)
    city = safeTravelsdb.Column(safeTravelsdb.String(150))
    ratings=safeTravelsdb.Column(safeTravelsdb.Integer)
    image=safeTravelsdb.Column(safeTravelsdb.String(150))
    phone = safeTravelsdb.Column(safeTravelsdb.String(20))

class wishlistHotels(safeTravelsdb.Model):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key=True)
    userId = safeTravelsdb.Column(safeTravelsdb.String(20))
    hotelName = safeTravelsdb.Column(safeTravelsdb.String(150),unique=True)
    city = safeTravelsdb.Column(safeTravelsdb.String(150),unique=True)
    ratings=safeTravelsdb.Column(safeTravelsdb.Integer)
    image=safeTravelsdb.Column(safeTravelsdb.String(150))

class hotelBookings(safeTravelsdb.Model):
    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key=True)
    userId = safeTravelsdb.Column(safeTravelsdb.String(20))
    hotelName = safeTravelsdb.Column(safeTravelsdb.String(150))
    city = safeTravelsdb.Column(safeTravelsdb.String(150))
    ratings=safeTravelsdb.Column(safeTravelsdb.Integer)
    image=safeTravelsdb.Column(safeTravelsdb.String(150))
    basePrice=safeTravelsdb.Column(safeTravelsdb.String(20))
    taxes = safeTravelsdb.Column(safeTravelsdb.String(20))
    totalAmount=safeTravelsdb.Column(safeTravelsdb.String(20))
    phone = safeTravelsdb.Column(safeTravelsdb.String(20))
    guestFirstName=safeTravelsdb.Column(safeTravelsdb.String(20))
    guestLastName = safeTravelsdb.Column(safeTravelsdb.String(20))
    guestContactNumber=safeTravelsdb.Column(safeTravelsdb.String(10))
    guestEmailAddress=safeTravelsdb.Column(safeTravelsdb.String(100))
    rooms=safeTravelsdb.Column(safeTravelsdb.String(2))
    guests=safeTravelsdb.Column(safeTravelsdb.String(2))
    fromDate = safeTravelsdb.Column(safeTravelsdb.String(20))
    toDate = safeTravelsdb.Column(safeTravelsdb.String(20))

class flightBookings(safeTravelsdb.Model):

    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key=True)
    userId = safeTravelsdb.Column(safeTravelsdb.String(20))
    flightName = safeTravelsdb.Column(safeTravelsdb.String(150))
    fromCity = safeTravelsdb.Column(safeTravelsdb.String(150))
    toCity = safeTravelsdb.Column(safeTravelsdb.String(150))
    ratings=safeTravelsdb.Column(safeTravelsdb.Integer)
    image=safeTravelsdb.Column(safeTravelsdb.String(150))
    level = safeTravelsdb.Column(safeTravelsdb.String(50))

    basePrice=safeTravelsdb.Column(safeTravelsdb.String(20))
    taxes = safeTravelsdb.Column(safeTravelsdb.String(20))
    totalAmount=safeTravelsdb.Column(safeTravelsdb.String(20))
    phone = safeTravelsdb.Column(safeTravelsdb.String(20))
    fullName=safeTravelsdb.Column(safeTravelsdb.String(30))

    passengers=safeTravelsdb.Column(safeTravelsdb.String(2))
    passengers_list=safeTravelsdb.Column(safeTravelsdb.String(2000))

    departTime = safeTravelsdb.Column(safeTravelsdb.String(100))
    journeyTime = safeTravelsdb.Column(safeTravelsdb.String(100))


class twoWayFlightBookings(safeTravelsdb.Model):

    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key=True)

    userId = safeTravelsdb.Column(safeTravelsdb.String(20))

    flightName = safeTravelsdb.Column(safeTravelsdb.String(150))
    fromCity = safeTravelsdb.Column(safeTravelsdb.String(150))
    toCity = safeTravelsdb.Column(safeTravelsdb.String(150))
    ratings=safeTravelsdb.Column(safeTravelsdb.Integer)
    image=safeTravelsdb.Column(safeTravelsdb.String(150))
    basePrice=safeTravelsdb.Column(safeTravelsdb.Integer)
    taxes = safeTravelsdb.Column(safeTravelsdb.String(20))
    totalAmount=safeTravelsdb.Column(safeTravelsdb.String(20))
    phone = safeTravelsdb.Column(safeTravelsdb.String(20))
    fullName=safeTravelsdb.Column(safeTravelsdb.String(30))
    level = safeTravelsdb.Column(safeTravelsdb.String(50))
    journeyTime = safeTravelsdb.Column(safeTravelsdb.String(100))

    passengers=safeTravelsdb.Column(safeTravelsdb.String(2))
    passengers_list=safeTravelsdb.Column(safeTravelsdb.String(2000))

    departTime = safeTravelsdb.Column(safeTravelsdb.String(100))

    flightName1 = safeTravelsdb.Column(safeTravelsdb.String(150))
    fromCity1 = safeTravelsdb.Column(safeTravelsdb.String(150))
    toCity1 = safeTravelsdb.Column(safeTravelsdb.String(150))
    ratings1=safeTravelsdb.Column(safeTravelsdb.Integer)
    image1=safeTravelsdb.Column(safeTravelsdb.String(150))
    phone1 = safeTravelsdb.Column(safeTravelsdb.String(20))
    fullName1=safeTravelsdb.Column(safeTravelsdb.String(30))
    departTime1 = safeTravelsdb.Column(safeTravelsdb.String(100))
    journeyTime1 = safeTravelsdb.Column(safeTravelsdb.String(100))
class saveRatings(safeTravelsdb.Model):

    id = safeTravelsdb.Column(safeTravelsdb.Integer, primary_key=True)
    userId = safeTravelsdb.Column(safeTravelsdb.String(20))
    ratings = safeTravelsdb.Column(safeTravelsdb.String(2))
    reviews = safeTravelsdb.Column(safeTravelsdb.String(100))