import flask
from flask import Blueprint, session, Flask
from flask import jsonify
from flask import render_template, request
import requests
import requests
import json

from numpy import random
from sqlalchemy import engine

from safeTravelsBackEnd import safeTravelsdb
from safeTravelsBackEnd.models.dbModels import wishlistRestaurants, hotelBookings, wishlistAttractions, flightBookings, \
    twoWayFlightBookings, saveRatings
from safeTravelsBackEnd.models.dbModels import wishlistHotels
import math

from flask_mail import Mail, Message
from twilio.rest import Client


# from flask import Flask, render_template, make_response
# from weasyprint import HTML


paths = Blueprint("Paths", __name__)

account_sid = 'AC0333b6029f104625a54bae7c3164f521'
auth_token = 'fc516d36d706ae08a99ee03d1c8fbbde'
client = Client(account_sid, auth_token)
@paths.route('/send_sms')
def send_sms():

    message = client.messages.create(
        to='+14258664226',  # replace with the phone number you want to send the message to
        from_='+18775895208',  # replace with your Twilio phone number
        body='Hello from Flask!'  # replace with the message body
    )

    return 'SMS sent'

@paths.route("/")
def basePage():
    return render_template("index.html")

@paths.route("/home")
def home():
    return render_template("signUp/loginDetails.html")

@paths.route("/searchAttractions")
def attractions():
    return render_template("signUp/searchAttractions.php",data={})

@paths.route("/flight")
def flight():
    return render_template("signUp/searchFlights.php",flights=[],data={"journeyType":"one-way"})

@paths.route("/hotels")
def hotels():
    return render_template("signUp/hotels.html")

@paths.route("/restaurants")
def restaurants():
    return render_template("signUp/restaurants.html")
@paths.route("/thankyou")
def thankyou():
    return render_template("signUp/thankyou.html")

@paths.route("/itinerary")
def itinerary():

    user = request.args.get('user')
    if user == None or user == "":
        return render_template('signUp/loginCustomer.html')
    results = wishlistRestaurants.query.filter_by(userId=user)
    hotels=hotelBookings.query.filter_by(userId=user)
    attractions = wishlistAttractions.query.filter_by(userId=user)
    flights = flightBookings.query.filter_by(userId=user)
    return_flights=twoWayFlightBookings.query.filter_by(userId=user)
    final_results=[]
    for row in results:
        final_results.append({"restaurantName":row.restaurantName,"image_url":row.image,"city":row.city,"ratings":row.ratings,"phone":row.phone})

    attractions_results=[]
    for row in attractions:
        attractions_results.append(
            {"attractionName": row.attractionName, "image_url": row.image, "city": row.city, "ratings": row.ratings,
             "phone": row.phone})

    hotel_results=[]
    for row in hotels:
            data={"id":row.id, "hotelName":row.hotelName, "city":row.city, "ratings":row.ratings, "image":row.image,"phone":row.phone,"basePrice":row.basePrice,"taxes":row.taxes
                                ,"totalAmount":row.totalAmount,"guestFirstName":row.guestFirstName,"guestLastName":row.guestLastName,"guestContactNumber":row.guestContactNumber,"guestEmailAddress":row.guestEmailAddress
                                ,"rooms":row.rooms,"guests":row.guests,"fromDate":row.fromDate,"toDate":row.toDate}
            hotel_results.append(data)

    flight_results=[]
    for row in flights:
            data={"id":row.id, "flightName":row.flightName, "fromCity":row.fromCity,"toCity":row.toCity,"ratings":row.ratings, "image":row.image,"phone":row.phone,"basePrice":row.basePrice,"taxes":row.taxes
                                ,"totalAmount":row.totalAmount,"fullName":row.fullName
                                ,"passengers":row.passengers,"departTime":row.departTime,"level":row.level,"journeyTime":row.journeyTime}
            flight_results.append(data)

    return_flight_results = []
    for row in return_flights:
        data = {"id": row.id, "flightName1": row.flightName, "fromCity1": row.fromCity, "toCity1": row.toCity,
                "ratings1": row.ratings, "image1": row.image, "phone1": row.phone, "basePrice": row.basePrice,
                "taxes": row.taxes
            , "totalAmount": row.totalAmount, "fullName": row.fullName
            , "passengers": row.passengers, "departTime1": row.departTime, "journeyTime1":row.journeyTime,"level": row.level,
                "flightName2": row.flightName1, "fromCity2": row.fromCity1, "toCity2": row.toCity1,
                "ratings2": row.ratings1, "image2": row.image1, "phone2": row.phone1,"departTime2": row.departTime1,"journeyTime2":row.journeyTime1
                }
        return_flight_results.append(data)

    print("got results")

    return render_template('signUp/itinerary.php',restaurants=final_results,hotels=hotel_results,attractions=attractions_results,flights=flight_results,return_flights=return_flight_results)

@paths.route("/wishlist")
def wishlist():
    return render_template("signUp/wishlist.php")

@paths.route("/success")
def success():
    # return render_template("signUp/success.html")
    return render_template("signUp/success.php")

@paths.route("/reviews")
def reviews():
    results = saveRatings.query.all()
    return render_template("signUp/reviews.php",results=results)

@paths.route('/flights', methods = ["GET", "POST"])
def flights():
    if request.method == "GET":
        
        api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMThhZjI0ODI2NWRkZmYyMGFlZWUxZDc3NjBlYmMyNjRlMGRiYjQ4ZWIyOWE1MjM5M2FlNGI0ZGI2ODc5ODVkYWIwOTVmZDA5ZjM5MzBhOTAiLCJpYXQiOjE2NzczNzU0ODIsIm5iZiI6MTY3NzM3NTQ4MiwiZXhwIjoxNzA4OTExNDgyLCJzdWIiOiIyMDI1NyIsInNjb3BlcyI6W119.tqXpmywCcXjFfU8mmrdgISEsTpIHSFwuAJRdqv2iMKAomZxKF1zIROIVcoOZne6jBEsqwoj-gDFY6vuzK8DeNQ',
        #departure_airport = request.args.get('origin')
        #arrival_airport = request.args.get('destination')
        #departure_date = request.args.get('departure_date')
        #return_date = request.args.get('return_date')
        #num_passengers = 1

        #params={
       #     'access_key' : api_key,
       #     'adults' : num_passengers,
       #     'origin' : departure_airport,
        #    'destination' : arrival_airport,
       #     'departureDate' : departure_date,
       #     'returnDate' : return_date
       #     
       # }
        url = 'https://app.goflightlabs.com/search-best-flights?access_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMThhZjI0ODI2NWRkZmYyMGFlZWUxZDc3NjBlYmMyNjRlMGRiYjQ4ZWIyOWE1MjM5M2FlNGI0ZGI2ODc5ODVkYWIwOTVmZDA5ZjM5MzBhOTAiLCJpYXQiOjE2NzczNzU0ODIsIm5iZiI6MTY3NzM3NTQ4MiwiZXhwIjoxNzA4OTExNDgyLCJzdWIiOiIyMDI1NyIsInNjb3BlcyI6W119.tqXpmywCcXjFfU8mmrdgISEsTpIHSFwuAJRdqv2iMKAomZxKF1zIROIVcoOZne6jBEsqwoj-gDFY6vuzK8DeNQ&adults=1&origin=MAD&destination=FCO&departureDate=2023-03-14'
        #'https://app.goflightlabs.com/search-best-flights'
        #response = requests.get(url, params)
        response = requests.get(url)

        if response.status_code == 200:
            flights = response.json()
            return flights
        #render_template('flights.html', flights=flights)
        else:
            return f'Error {response.status_code}: {response.text}'




# @paths.route("/loginCustomer")
# def loginCustomer():
#     return "<p>Login</p>"

# @paths.route("/logoutCustomer")
# def login():
#     return "<p>Logout</p>"

# @paths.route("/RegisterCustomer")
# def register():
#     return "<p>Register</p>"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer HhGdlofFqUDQPq9uJ8iTatq22xRCCn5SZLhPryz2hvxKNQSEbZ8UcQ5apkfiEkAEfH1zUSIzJDga3aJyFkj-r8D7fbanzAM7EjCdUGUVSFFT1_Ze6BzLPRZnkokDZHYx"
}


@paths.route('/searchRestaurants', methods=['POST','GET'])
def resturantsHome():

     # return render_template('signUp/searchRestaurants.html')
     return render_template('signUp/searchRestaurants.php',city="",data={})
@paths.route('/showRestaurants', methods=['POST','GET'])
def search():

    user=request.args.get('user')
    if user==None or user=="":
        return render_template('signUp/loginCustomer.html')
    city = request.args.get('myCity')

    price_list_mapping = {'0-250': 'one', '250-500': 'two', '500-750': 'three', '750-1000': 'four'}
    prices = json.loads(request.args.get('priceFilters'))
    new_prices = {}
    for key in price_list_mapping.keys():
        new_prices[price_list_mapping[key]] = prices[key]

    ratings = json.loads(request.args.get('ratingFilters'))

    my_data = {}
    my_data['myCity'] = city
    my_data['priceFilters'] = new_prices
    my_data['ratingFilters'] = ratings

    # if request.method == 'GET':
    #     city = 'NYC' 
        
    #     #request.args.get['city']
    #     attractions = requests.get(f'https://api.yelp.com/v3/businesses/search?term=attractions&location={city}&sort_by=best_match&limit=5', headers=headers)
    #     hotels = requests.get(f'https://api.yelp.com/v3/businesses/search?term=hotels&location={city}&sort_by=best_match&limit=5', headers=headers)
    #     restaurants = requests.get(f'https://api.yelp.com/v3/businesses/search?term=restaurants&location={city}&sort_by=best_match&limit=5', headers=headers)
    #     #travel_options = requests.get(f'https://maps.googleapis.com/maps/api/directions/json?origin={city}&destination={city}', headers=headers).json()
    #     return ['restaurants=', restaurants.text, 'hotels=',hotels.text, 'attractions=',attractions.text]
    if request.method == "GET":
        API_KEY = 'RAwHNXwEO7PuovTE-VXhl2dVeHgIc57iaQFnKwveHwZLLDtyF6ThCd52FAveW2Ped9UCUxZocOu0tITb91M2JlhErry_2BqCn4R2v0d7boBGtJRNhGwaGbvNJywRZHYx'
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

        # set the parameters for the API request
        params = {
            'location': city,
            'categories': 'restaurants',
            'limit': 50,  # number of results per request
            'offset': 0   # starting index for the results
        }

        restaurants = []

        while True:
            # make the API request and get the response
            headers = {'Authorization': 'Bearer %s' % API_KEY}
            response = requests.get(ENDPOINT, headers=headers, params=params)
            
            # check if the response is successful
            if response.status_code == 200:
                # parse the response and extract the restaurant data
                data = json.loads(response.text)
                restaurants.extend(data['businesses'])
                
                # check if there are more results to retrieve
                if len(data['businesses']) < params['limit']:
                    break
                else:
                    params['offset'] += params['limit']
            else:
                # handle errors
                print('Error:', response.status_code)
                break

        # print the list of restaurants
        print(restaurants[0])


        for i in range(len(restaurants)):
            restaurants[i]['price']=random.randint(250,600)


        final_restaurants=filter_list(restaurants, prices, ratings)
        print(final_restaurants[:10])

        return render_template('signUp/searchRestaurants.php',restaurants=final_restaurants[:50],city=city,data=my_data)
        # return render_template('signUp/searchRestaurants.html', restaurants=restaurants[:50])
@paths.route('/saveRestaurant', methods=['POST','GET'])
def saveRestaurant():
    if request.method == "POST":
        data=request.get_json()
        user=data['user']
        city = data['city']
        restaurantName = data['restaurantName']
        ratings = data['ratings']
        image= data['image']
        phone = data['display_phone']
        print(city,restaurantName,image,ratings)
        results = wishlistRestaurants.query.filter_by(restaurantName=restaurantName,city=city,userId=user).all()
        print(results)
        if len(results):
            # wishlistRestaurants.query.filter_by(restaurantName=restaurantName, city=city,userId=user).update({"restaurantName": restaurantName, "city": city, "ratings": ratings, "image": image, "phone": phone})
            return {"data": "already exists"}
        else:
            my_data = wishlistRestaurants(restaurantName=restaurantName,city=city, ratings=ratings,image=image,phone=phone,userId=user)
            safeTravelsdb.session.add(my_data)

        safeTravelsdb.session.commit()
        session.clear()
    # return render_template('signUp/success.html')
    return {"data":"success"}

@paths.route('/saveAttraction', methods=['POST','GET'])
def saveAttraction():
    if request.method == "POST":
        data=request.get_json()
        user=data['user']
        city = data['city']
        attractionName = data['attractionName']
        ratings = data['ratings']
        image= data['image']
        phone = data['display_phone']
        print(city,attractionName,image,ratings)
        results = wishlistAttractions.query.filter_by(attractionName=attractionName,city=city,userId=user).all()
        print(results)
        if len(results):
            # wishlistAttractions.query.filter_by(attractionName=attractionName, city=city,userId=user).update({"attractionName": attractionName, "city": city, "ratings": ratings, "image": image, "phone": phone})
            return {"data":"already exists"}
        else:
            my_data = wishlistAttractions(attractionName=attractionName,city=city, ratings=ratings,image=image,phone=phone,userId=user)
            safeTravelsdb.session.add(my_data)

        safeTravelsdb.session.commit()
        session.clear()
    # return render_template('signUp/success.html')
    return {"data":"success"}

@paths.route('/unwishlistRestaurant', methods=['POST','GET'])
def unwishlistRestaurant():
        data=request.get_json()
        user=data['user']
        city = data['city']
        restaurantName = data['restaurantName']
        print(city,restaurantName)
        row_to_delete = wishlistRestaurants.query.filter_by(restaurantName=restaurantName,city=city,userId=user).first()

        safeTravelsdb.session.delete(row_to_delete)
        safeTravelsdb.session.commit()

        session.clear()

        results = wishlistRestaurants.query.all()
        final_results = []
        for row in results:
            final_results.append(
                {"restaurantName": row.restaurantName, "image_url": row.image, "city": row.city, "ratings": row.ratings,
                 "phone": row.phone})
        # return final_results
        return "success"

@paths.route('/unwishlistAttraction', methods=['POST','GET'])
def unwishlistAttraction():
        data=request.get_json()
        user=data['user']
        city = data['city']
        attractionName = data['attractionName']
        print(city,attractionName)
        row_to_delete = wishlistAttractions.query.filter_by(attractionName=attractionName,city=city,userId=user).first()

        safeTravelsdb.session.delete(row_to_delete)
        safeTravelsdb.session.commit()

        session.clear()

        results = wishlistAttractions.query.all()
        final_results = []
        for row in results:
            final_results.append(
                {"attractionName": row.attractionName, "image_url": row.image, "city": row.city, "ratings": row.ratings,
                 "phone": row.phone})
        # return final_results
        return "success"


@paths.route('/getSavedRestaurants',methods=['GET','POST'])
def getSavedRestaurants():
    results = wishlistRestaurants.query.all()
    final_results=[]
    for row in results:
        final_results.append({"restaurantName":row.restaurantName,"image_url":row.image,"city":row.city,"ratings":row.ratings,"phone":row.phone})
    # return final_results
    return render_template('signUp/itinerary.php',restaurants=final_results)





@paths.route('/searchHotels', methods=['POST','GET'])
def hotelsHome():

     data = {'city': '', 'state':'','restaurant':'','fromDate': '', 'toDate': '', 'rooms': '', 'guests': '','priceFilters':{'one':False,'two':False,'three':False,'four':False}}
     # url = 'https://countriesnow.space/api/v0.1/countries/states'
     # data1 = {
     #     'country': 'United States',
     # }
     # headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
     # response = requests.post(url, json=data1, headers=headers)
     # result=json.loads(response.text)
     result=['California','Indiana','Texas','Colarado','Tennessee']

     # return render_template('signUp/searchHotels.php',data=data,states=result['data']['states'][:50])
     return render_template('signUp/searchHotels.php',data=data,states=result)
@paths.route('/showHotels', methods=['POST','GET','PUT'])
def searchHotel():
    user=request.args.get('user')
    if user==None or user=="":
        return render_template('signUp/loginCustomer.html')
    city = request.args.get('myCity')
    state=request.args.get('state')
    hotel = request.args.get('hotel')
    fromDate=request.args.get('fromDate')
    toDate=request.args.get('toDate')
    rooms = request.args.get('rooms')
    guests = request.args.get('guests')
    price_list_mapping = {'0-250': 'one', '250-500': 'two', '500-750': 'three', '750-1000': 'four'}
    prices = json.loads(request.args.get('priceFilters'))
    new_prices={}
    for key in price_list_mapping.keys():
        new_prices[price_list_mapping[key]]=prices[key]
    print(new_prices)
    ratings = json.loads(request.args.get('ratingFilters'))
    my_data={'city':city,'fromDate':fromDate,'toDate':toDate,'rooms':rooms,'guests':guests,'priceFilters':new_prices,'ratingFilters':ratings,'state':state,'hotel':hotel}
    # if request.method == 'GET':
    #     city = 'NYC' 
        
    #     #request.args.get['city']
    #     attractions = requests.get(f'https://api.yelp.com/v3/businesses/search?term=attractions&location={city}&sort_by=best_match&limit=5', headers=headers)
    #     hotels = requests.get(f'https://api.yelp.com/v3/businesses/search?term=hotels&location={city}&sort_by=best_match&limit=5', headers=headers)
    #     restaurants = requests.get(f'https://api.yelp.com/v3/businesses/search?term=restaurants&location={city}&sort_by=best_match&limit=5', headers=headers)
    #     #travel_options = requests.get(f'https://maps.googleapis.com/maps/api/directions/json?origin={city}&destination={city}', headers=headers).json()
    #     return ['restaurants=', restaurants.text, 'hotels=',hotels.text, 'attractions=',attractions.text]
    if request.method == "GET":
        API_KEY = 'RAwHNXwEO7PuovTE-VXhl2dVeHgIc57iaQFnKwveHwZLLDtyF6ThCd52FAveW2Ped9UCUxZocOu0tITb91M2JlhErry_2BqCn4R2v0d7boBGtJRNhGwaGbvNJywRZHYx'
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

        # set the parameters for the API request
        params = {
            'location': city,
            'categories': 'hotels',
            'limit': 50,  # number of results per request
            'offset': 0   # starting index for the results
        }

        hotels = []

        while True:
            # make the API request and get the response
            headers = {'Authorization': 'Bearer %s' % API_KEY}
            response = requests.get(ENDPOINT, headers=headers, params=params)
            
            # check if the response is successful
            if response.status_code == 200:
                # parse the response and extract the restaurant data
                data = json.loads(response.text)
                hotels.extend(data['businesses'])
                
                # check if there are more results to retrieve
                if len(data['businesses']) < params['limit']:
                    break
                else:
                    params['offset'] += params['limit']
            else:
                # handle errors
                print('Error:', response.status_code)
                break


        # print(hotels)
        for i in range(len(hotels)):
            hotels[i]['price']=random.randint(250,1000)


        price_list = ['0-250', '250-500', '500-750', '750-1000'];
        ratings_list = ['0', '1', '2', '3', '4', '5'];
        price_filter=False
        ratings_filter=False

        final_hotels1 = []
        final_hotels = []
        for i in range(len(price_list)):
            if prices[price_list[i]]==True:
                price_filter = True
        for i in range(len(ratings_list)):
            if ratings[ratings_list[i]]==True:
                ratings_filter=True

        if ratings_filter and price_filter:
            for i in range(len(hotels)):
                for j in range(len(price_list)):
                    if prices[price_list[j]]==True:
                        value= price_list[j].split('-')
                        if hotels[i]['price'] >= int(value[0]) and hotels[i]['price'] <=int(value[1]):
                            final_hotels1.append(hotels[i])
                            break

            # print(final_hotels1)
            for i in range(len(final_hotels1)):
                for j in range(len(ratings_list)):
                    if ratings[ratings_list[j]]==True:
                        value= ratings_list[j]
                        if math.floor(final_hotels1[i]['rating']) == int(value):
                            final_hotels.append(final_hotels1[i])
                            break
        elif ratings_filter:

            for i in range(len(hotels)):
                for j in range(len(ratings_list)):
                    if ratings[ratings_list[j]]==True:
                        value= ratings_list[j]
                        if math.floor(hotels[i]['rating']) == int(value):
                            final_hotels.append(hotels[i])
                            break
        elif price_filter:

            for i in range(len(hotels)):
                for j in range(len(price_list)):
                    if prices[price_list[j]] == True:
                        value = price_list[j].split('-')
                        if hotels[i]['price'] >= int(value[0]) and hotels[i]['price'] <= int(value[1]):
                            final_hotels.append(hotels[i])
                            break
        else:
            final_hotels=hotels

        print(hotel)
        if hotel!="":
            temp_hotels=final_hotels
            final_hotels=[]
            for temp_hotel in temp_hotels:
                print(hotel)
                if hotel[:3] in temp_hotel['name']:
                    final_hotels.append(temp_hotel)

        print(final_hotels[0])
        result=['California','Indiana','Texas','Colarado','Tennessee']

        return render_template('signUp/searchHotels.php',hotels= final_hotels[:50],data=my_data,states=result)



@paths.route('/saveHotel', methods=['POST','GET'])
def saveHotel():
    if request.method == "POST":
        data=request.get_json()
        city = data['city']
        hotelName = data['hotelName']
        ratings = data['ratings']
        image= data['image']
        print(city,hotelName,image,ratings)
        my_data = wishlistHotels(restaurantName=hotelName,city=city, ratings=ratings,image=image)
        safeTravelsdb.session.add(my_data)
        safeTravelsdb.session.commit()
        session.clear()
    # return render_template('signUp/success.html')
    return "success"

@paths.route('/getSavedHotels',methods=['GET','POST'])
def getSavedHotels():
    results = wishlistHotels.query.all()
    final_results=[]
    for row in results:
        final_results.append({"HotelName":row.hotelName,"image":row.image,"city":row.city,"ratings":row.ratings})
    return final_results


@paths.route('/showAttractions', methods=['POST','GET'])
def searchAttractions():

    user=request.args.get('user')
    print(user)
    if user==None or user=="":
        return render_template('signUp/loginCustomer.html')
    city = request.args.get('myCity')

    price_list_mapping = {'0-250': 'one', '250-500': 'two', '500-750': 'three', '750-1000': 'four'}
    prices = json.loads(request.args.get('priceFilters'))
    new_prices = {}
    for key in price_list_mapping.keys():
        new_prices[price_list_mapping[key]] = prices[key]
    print(new_prices)
    ratings = json.loads(request.args.get('ratingFilters'))

    my_data={}
    my_data['myCity'] =city
    my_data['priceFilters']=new_prices
    my_data['ratingFilters']=ratings

    if request.method == "GET":
        API_KEY = 'RAwHNXwEO7PuovTE-VXhl2dVeHgIc57iaQFnKwveHwZLLDtyF6ThCd52FAveW2Ped9UCUxZocOu0tITb91M2JlhErry_2BqCn4R2v0d7boBGtJRNhGwaGbvNJywRZHYx'
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

        # set the parameters for the API request
        params = {
            'location': city,
            'categories': 'active',
            'limit': 50,  # number of results per request
            'offset': 0   # starting index for the results
        }

        attractions = []

        while True:
            # make the API request and get the response
            headers = {'Authorization': 'Bearer %s' % API_KEY}
            response = requests.get(ENDPOINT, headers=headers, params=params)
            
            # check if the response is successful
            if response.status_code == 200:
                # parse the response and extract the restaurant data
                data = json.loads(response.text)
                attractions.extend(data['businesses'])
                
                # check if there are more results to retrieve
                if len(data['businesses']) < params['limit']:
                    break
                else:
                    params['offset'] += params['limit']
            else:
                # handle errors
                print('Error:', response.status_code)
                break


        # print(attractions)

        for i in range(len(attractions)):
            attractions[i]['price']=random.randint(250,600)


        final_attractions=filter_list(attractions, prices, ratings)
        print(final_attractions[:10])

        return render_template('signUp/searchAttractions.php', attractions=final_attractions[:50],data=my_data)


@paths.route('/showFlights', methods=['POST', 'GET'])
def showFlights():

    user=request.args.get('user')
    if user==None or user=="":
        return render_template('signUp/loginCustomer.html')
    price_list_mapping = {'0-250': 'one', '250-500': 'two', '500-750': 'three', '750-1000': 'four'}
    prices = json.loads(request.args.get('priceFilters'))
    new_prices={}
    for key in price_list_mapping.keys():
        new_prices[price_list_mapping[key]]=prices[key]
    print(new_prices)
    ratings = json.loads(request.args.get('ratingFilters'))

    my_data={}
    my_data['fromCity'] = request.args.get('fromCity')
    my_data['journeyType']=request.args.get('journeyType')
    my_data['level']=request.args.get('level')
    my_data['toCity']=request.args.get('toCity')
    my_data['toDate']=request.args.get('toDate')
    my_data['fromDate']=request.args.get('fromDate')
    my_data['passengers']=request.args.get('passengers')
    my_data['priceFilters']=new_prices
    my_data['ratingFilters']=ratings

    if request.method == "GET":
        API_KEY = 'RAwHNXwEO7PuovTE-VXhl2dVeHgIc57iaQFnKwveHwZLLDtyF6ThCd52FAveW2Ped9UCUxZocOu0tITb91M2JlhErry_2BqCn4R2v0d7boBGtJRNhGwaGbvNJywRZHYx'
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

        # set the parameters for the API request
        params = {
            'location': my_data['fromCity'] ,
            'categories': 'airlines',
            'limit': 50,  # number of results per request
            'offset': 0  # starting index for the results
        }


        flights = []

        while True:
            # make the API request and get the response
            headers = {'Authorization': 'Bearer %s' % API_KEY}
            response = requests.get(ENDPOINT, headers=headers, params=params)

            # check if the response is successful
            if response.status_code == 200:
                # parse the response and extract the restaurant data
                data = json.loads(response.text)
                flights.extend(data['businesses'])

                # check if there are more results to retrieve
                if len(data['businesses']) < params['limit']:
                    break
                else:
                    params['offset'] += params['limit']
            else:
                # handle errors
                print('Error:', response.status_code)
                break

        if my_data['journeyType'] == "return":
            params = {
                'location': my_data['toCity'],
                'categories': 'airlines',
                'limit': 50,  # number of results per request
                'offset': 0  # starting index for the results
            }

            return_flights = []

            while True:
                # make the API request and get the response
                headers = {'Authorization': 'Bearer %s' % API_KEY}
                response = requests.get(ENDPOINT, headers=headers, params=params)

                # check if the response is successful
                if response.status_code == 200:
                    # parse the response and extract the restaurant data
                    data = json.loads(response.text)
                    return_flights.extend(data['businesses'])

                    # check if there are more results to retrieve
                    if len(data['businesses']) < params['limit']:
                        break
                    else:
                        params['offset'] += params['limit']
                else:
                    # handle errors
                    print('Error:', response.status_code)
                    break

            for i in range(len(return_flights)):
                if my_data['level'] == "First Class":
                    return_flights[i]['price'] = random.randint(1000, 1200)
                elif my_data['level'] == "Business":
                    return_flights[i]['price'] = random.randint(800, 1000)
                else:
                    return_flights[i]['price'] = random.randint(250, 600)

                return_flights[i]['departure_time'] = my_data['toDate'] + " " + str(random.randint(0, 14)).zfill(2) + ":" + str(
                    random.randint(0, 60)).zfill(2)
                return_flights[i]['journey_time'] = str(random.randint(1, 7))

            final_return_flights = filter_list(return_flights, prices, ratings)


        for i in range(len(flights)):
            if my_data['level']=="First Class":
                flights[i]['price'] = random.randint(1000, 1200)
            elif my_data['level'] == "Business":
                flights[i]['price'] = random.randint(800, 1000)
            else:
                flights[i]['price']=random.randint(250,600)

            flights[i]['departure_time']=my_data['fromDate'] + " " + str(random.randint(0, 14)).zfill(2) + ":" + str(
                    random.randint(0, 60)).zfill(2)
            flights[i]['journey_time'] = str(random.randint(1, 7))

        final_flights=filter_list(flights,prices,ratings)


        if my_data['journeyType'] == "return":
            result_flights=[]
            while len(final_flights)!=0 and len(final_return_flights)!=0:
                    result={}
                    flight1=random.choice(final_flights)
                    final_flights.remove(flight1)
                    flight2 = random.choice(final_return_flights)
                    final_return_flights.remove(flight2)
                    result['flight1']=flight1
                    result['flight2'] = flight2
                    result_flights.append(result)
        else:
            result_flights=final_flights[:50]


        return render_template('signUp/searchFlights.php', flights=result_flights,data=my_data)

def filter_list(temp_list,prices,ratings):

    print(prices)
    print(ratings)
    price_list = ['0-250', '250-500', '500-750', '750-1000'];
    ratings_list = ['0', '1', '2', '3', '4', '5'];
    price_filter = False
    ratings_filter = False

    final_flights1 = []
    final_flights = []

    for i in range(len(price_list)):
        if prices[price_list[i]] == True:
            price_filter = True
    for i in range(len(ratings_list)):
        if ratings[ratings_list[i]] == True:
            ratings_filter = True
    print(ratings_filter,price_filter)
    if ratings_filter and price_filter:
        for i in range(len(temp_list)):
            for j in range(len(price_list)):
                if prices[price_list[j]] == True:
                    value = price_list[j].split('-')
                    if temp_list[i]['price'] >= int(value[0]) and temp_list[i]['price'] <= int(value[1]):
                        final_flights1.append(temp_list[i])
                        break

        # print(final_hotels1)
        for i in range(len(final_flights1)):
            for j in range(len(ratings_list)):
                if ratings[ratings_list[j]] == True:
                    value = ratings_list[j]
                    if math.floor(final_flights1[i]['rating']) == int(value):
                        final_flights.append(final_flights1[i])
                        break
    elif ratings_filter:

        for i in range(len(temp_list)):
            for j in range(len(ratings_list)):
                if ratings[ratings_list[j]] == True:
                    value = ratings_list[j]
                    if math.floor(temp_list[i]['rating']) == int(value):
                        final_flights.append(temp_list[i])
                        break
    elif price_filter:
        for i in range(len(temp_list)):
            for j in range(len(price_list)):
                if prices[price_list[j]] == True:
                    value = price_list[j].split('-')
                    # print(temp_flights[i])
                    if temp_list[i]['price'] >= int(value[0]) and temp_list[i]['price'] <= int(value[1]):
                        final_flights.append(temp_list[i])
                        break
    else:
        final_flights = temp_list
    return final_flights

@paths.route('/bookHotel', methods=['POST','GET'])
def bookHotel():

     return render_template('signUp/bookHotel.php')

@paths.route('/bookFlight', methods=['POST','GET'])
def bookFlight():

    passengers=request.args.get('passengers')
    journeyType = request.args.get('journeyType')

    return render_template('signUp/bookFlight.php',passengers=passengers,journeyType=journeyType)

@paths.route('/hotelPayment', methods=['POST','GET'])
def hotelPayment():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        user = data['user']
        if user == None or user == "":
            return render_template('signUp/loginCustomer.html')
        city = data['city']
        hotelName = data['hotelName']
        ratings = data['ratings']
        image = data['image']
        phone = data['phone']
        basePrice = data['basePrice']
        taxes = data['taxes']
        totalAmount =data['totalAmount']

        guestFirstName = data['guestFirstName']
        guestLastName = data['guestLastName']
        guestContactNumber = data['guestContactNumber']
        guestEmailAddress = data['guestEmailAddress']
        fromDate= data['fromDate']
        toDate=data['toDate']
        rooms = data['rooms']
        guests = data['guests']
        my_data = hotelBookings(hotelName=hotelName, city=city, ratings=ratings, image=image,phone=phone,basePrice=basePrice,taxes=taxes
                                ,totalAmount=totalAmount,guestFirstName=guestFirstName,guestLastName=guestLastName,guestContactNumber=guestContactNumber,guestEmailAddress=guestEmailAddress
                                ,rooms=rooms,guests=guests,fromDate=fromDate,toDate=toDate,userId=user)
        safeTravelsdb.session.add(my_data)
        safeTravelsdb.session.commit()

        sms_content = "\nHi "+str(guestFirstName)+" "+str(guestLastName)+"\nHere are your hotel booking confirmation details.\nBooking ID:"+str(my_data.id)+"\nHotel Name:"+str(hotelName)+"\nCheck-in:"+str(fromDate)+" 12:00 PM\nNumber of rooms:"+str(rooms)+"\n-From SafeTravels"


        print(guestContactNumber)
        message = client.messages.create(
            to='+1'+guestContactNumber,  # replace with the phone number you want to send the message to
            from_='+18775895208',  # replace with your Twilio phone number
            body=sms_content  # replace with the message body
        )


        return render_template('signUp/success.html',data=data)
    return "success"



@paths.route('/flightPayment', methods=['POST','GET'])
def flightPayment():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        user = data['user']
        if user == None or user == "":
            return render_template('signUp/loginCustomer.html')

        level = data['level']
        fromCity = data['fromCity']
        toCity = data['toCity']
        flightName = data['flightName']
        ratings = data['ratings']
        image = data['image']
        phone = data['phone']

        fullName = data['fullName']
        basePrice = data['basePrice']
        taxes = data['taxes']
        totalAmount = data['totalAmount']

        departTime = data['departTime']
        journeyTime = data['journeyTime']

        passengers = data['passengers']
        passengers_list = str(data['passengers_list'])

        contactNumber=data['contactNumber']

        if data['journeyType']=='one-way':

            my_data = flightBookings(flightName=flightName, fromCity=fromCity, toCity=toCity, ratings=ratings, image=image,phone=phone,fullName=fullName,basePrice=basePrice,taxes=taxes
                                ,totalAmount=totalAmount,passengers=passengers
                                ,passengers_list=passengers_list,departTime=departTime,level=level,userId=user)
            safeTravelsdb.session.add(my_data)
            safeTravelsdb.session.commit()

            sms_content = ""+"\nHi " + str(
                user) + "\nHere are your flight booking confirmation details.\nBooking ID : " + str(
                my_data.id) + "\nFlight : " + str(flightName) + "\nDeparture:" + str(
                departTime) + "\n-From SafeTravels"

            print(sms_content)
            print(phone)

            message = client.messages.create(
                to='+1' + contactNumber,  # replace with the phone number you want to send the message to
                from_='+18775895208',  # replace with your Twilio phone number
                body=sms_content  # replace with the message body
            )

        else:

            fromCity1 = data['fromCity1']
            toCity1 = data['toCity1']
            flightName1 = data['flightName1']
            ratings1 = data['ratings1']
            image1 = data['image1']
            phone1 = data['phone1']
            departTime1=data['departTime1']
            journeyTime1 = data['journeyTime1']

            my_data = twoWayFlightBookings(flightName=flightName, fromCity=fromCity, toCity=toCity, ratings=ratings,
                                     image=image, phone=phone,journeyTime=journeyTime, fullName=fullName, basePrice=basePrice, taxes=taxes
                                     , totalAmount=totalAmount, passengers=passengers
                                     , passengers_list=passengers_list, departTime=departTime, level=level,flightName1=flightName1, fromCity1=fromCity1, toCity1=toCity1, ratings1=ratings1,
                                     image1=image1, phone1=phone1,departTime1=departTime1,journeyTime1=journeyTime1,userId=user)

            safeTravelsdb.session.add(my_data)
            safeTravelsdb.session.commit()

            sms_content = ""+"\nHi " + str(user) + "\nHere are your flight booking confirmation details.\nBooking ID:" + str(
                my_data.id) + "\nFlight1 : " + str(flightName) + "\nDeparture : " + str(
                departTime) + "\nFlight2 : " + str(flightName1) + "\nDeparture : " + str(
                departTime1) + "\n-From SafeTravels"

            print(sms_content)
            print(contactNumber)

            message = client.messages.create(
                to='+1' + contactNumber,  # replace with the phone number you want to send the message to
                from_='+18775895208',  # replace with your Twilio phone number
                body=sms_content  # replace with the message body
            )



        return render_template('signUp/success.html',data=data)
    return "success"


@paths.route('/deleteHotelBooking', methods=['POST','GET'])
def deleteHotelBooking():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        user =data['user']
        if user == None or user == "":
            return render_template('signUp/loginCustomer.html')
        id = data['id']

        row_to_delete = hotelBookings.query.filter_by(id=id,userId=user).first()
        safeTravelsdb.session.delete(row_to_delete)
        safeTravelsdb.session.commit()

        return render_template('signUp/success.html')
    return "success"



@paths.route('/deleteFlightBooking', methods=['POST','GET'])
def deleteFlightBooking():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        id = data['id']
        user =data['user']
        if user == None or user == "":
            return render_template('signUp/loginCustomer.html')

        row_to_delete = flightBookings.query.filter_by(id=id,userId=user).first()
        safeTravelsdb.session.delete(row_to_delete)
        safeTravelsdb.session.commit()

        return render_template('signUp/success.html')
    return "success"

@paths.route('/deleteReturnFlightBooking', methods=['POST','GET'])
def deleteReturnFlightBooking():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        id = data['id']
        user = data['user']
        if user == None or user == "":
            return render_template('signUp/loginCustomer.html')
        row_to_delete = twoWayFlightBookings.query.filter_by(id=id,userId=user).first()
        safeTravelsdb.session.delete(row_to_delete)
        safeTravelsdb.session.commit()

        return render_template('signUp/success.html')
    return "success"

@paths.route('/saveRatings', methods=['POST','GET'])
def saveRatingsAndReviews():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        user = data['user']
        if user == None or user == "":
            return render_template('signUp/loginCustomer.html')
        ratings=data['ratings']
        reviews=data['reviews']
        print(ratings,reviews,user)
        my_data = saveRatings(userId=user,ratings=ratings,reviews=reviews)
        safeTravelsdb.session.add(my_data)
        safeTravelsdb.session.commit()

        return render_template('signUp/success.html')
    return "success"


@paths.route('/homePage',methods=['GET','POST'])
def homePage():

    user = request.args.get('user')
    if user == None or user == "":
        return render_template('signUp/loginCustomer.html')
    city = request.args.get('myCountry')

    if request.method == "GET":
        API_KEY = 'RAwHNXwEO7PuovTE-VXhl2dVeHgIc57iaQFnKwveHwZLLDtyF6ThCd52FAveW2Ped9UCUxZocOu0tITb91M2JlhErry_2BqCn4R2v0d7boBGtJRNhGwaGbvNJywRZHYx'
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

        # set the parameters for the API request
        restaurant_params = {
            'location': city,
            'categories': 'restaurants',
            'limit': 50,  # number of results per request
            'offset': 0  # starting index for the results
        }
        attraction_params = {
            'location': city,
            'categories': 'active',
            'limit': 50,  # number of results per request
            'offset': 0  # starting index for the results
        }

        hotel_params = {
            'location': city,
            'categories': 'hotels',
            'limit': 50,  # number of results per request
            'offset': 0  # starting index for the results
        }
        restaurants = []
        attractions = []
        hotels = []

        while True:
            # make the API request and get the response
            headers = {'Authorization': 'Bearer %s' % API_KEY}
            restaurants_response = requests.get(ENDPOINT, headers=headers, params=restaurant_params)
            attractions_response = requests.get(ENDPOINT, headers=headers, params=attraction_params)
            hotels_response = requests.get(ENDPOINT, headers=headers, params=hotel_params)

            # check if the response is successful
            if restaurants_response.status_code == 200:
                # parse the response and extract the restaurant data
                data = json.loads(restaurants_response.text)
                restaurants.extend(data['businesses'])

                # check if there are more results to retrieve
                if len(data['businesses']) < restaurant_params['limit']:
                    break
                else:
                    restaurant_params['offset'] += restaurant_params['limit']
            else:
                # handle errors
                print('Error:', restaurants_response.status_code)
                break

            # check if the response is successful
            if attractions_response.status_code == 200:
                # parse the response and extract the restaurant data
                data = json.loads(attractions_response.text)
                attractions.extend(data['businesses'])

                # check if there are more results to retrieve
                if len(data['businesses']) < attraction_params['limit']:
                    break
                else:
                    attraction_params['offset'] += attraction_params['limit']
            else:
                # handle errors
                print('Error:', attractions_response.status_code)
                break

            # check if the response is successful
            if hotels_response.status_code == 200:
                # parse the response and extract the restaurant data
                data = json.loads(hotels_response.text)
                hotels.extend(data['businesses'])

                # check if there are more results to retrieve
                if len(data['businesses']) < hotel_params['limit']:
                    break
                else:
                    hotel_params['offset'] += hotel_params['limit']
            else:
                # handle errors
                print('Error:', hotels_response.status_code)
                break

    print(restaurants[:4],hotels[:4])

    for i in range(len(restaurants)):
        restaurants[i]['price'] = random.randint(250, 600)

    for i in range(len(attractions)):
        attractions[i]['price'] = random.randint(250, 600)

    for i in range(len(hotels)):
        hotels[i]['price'] = random.randint(250, 600)

    return render_template('signUp/loginDetails.html',restaurants=restaurants[:4],hotels=hotels[:4],attractions=attractions[:4])


@paths.route('/send_email')
def send_email():
    # create message object
    msg = Message('Hello from Flask', sender='poojithamathi97@gmail.com', recipients=['ppfrndlypooja@gmail.com'])

    # add message body
    msg.body = 'Hello world!'
    # send email
    safeTravel = Flask(__name__)
    mail = Mail(safeTravel)
    mail.send(msg)

    return 'Email sent'


# @paths.route('/download_pdf')
# def download_pdf():
#     # Fetch HTML content
#     html = render_template('signUp/bookHotel.php')
#
#     # Create PDF file
#     pdf = HTML(string=html).write_pdf()
#
#     # Return PDF file as response
#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=download.pdf'
#     return response

@paths.route('/download_pdf')
def download_pdf():
    return render_template('signUp/download.php')


@paths.route('/maps')
def maps():
    return render_template('signUp/maps.html')
