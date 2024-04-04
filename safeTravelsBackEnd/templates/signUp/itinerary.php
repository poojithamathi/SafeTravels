<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="utf-8" />
    <meta name="'viewpoint">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/normalize.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/safetravels.css') }}">

    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,700,0,0" />
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
     <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <title>Itinerary</title>

    </head>
<script src="/../static/JS/safetravels.js"></script>
<body onload="setUser()">
    <header>
        <a href="/"><img class="logo" src="{{ url_for('static', filename='Images/SafeTravelsLogo.png') }}"> </a>
        <!-- <p class="head">Search</p> -->
        <a href="/searchAttractions" class="head">Attractions</a>
        <a href="/flight" class="head">Flights</a>
        <a href="/searchHotels" class="head">Hotels</a>
        <a href="/searchRestaurants" class="head">Restaurants</a>
            <!-- maybe flights, hotels, and restaurants could be a drop down menu -->
        <a class="head" onclick="getUserItinerary()" >Itinerary</a>
<!--         <a href='/reviews' class="head" onclick="getUserReviews()" >Reviews</a> -->
        <a class="head login nav-item nav-link" id="loginCustomer" href="/loginCustomer" onclick="loggingUser()">Login/Sign Up</a>
            <!-- login page -->
    </header>

    <div class="favorites" style="margin-bottom:300px">
        <div class="search-bar itinerary-search-bar">
            <h1 id="itinerary">Itinerary</h1>
             <div class="buttons-main">
                <a href="#restaurantId" class="more-link">Restaurants</a>
                <a href="#attractionId" class="more-link">Attractions</a>
                <a href="#hotelId" class="more-link">Hotel Bookings</a>
                <a href="#flightsId" class="more-link">Flight Bookings</a>
            </div>
        </div>

         <div style="width:100%">
        <div class="favorite-restaurants">
                <div class="title-itinerary">
                    <h2 id="restaurantId">Favourite Restaurants</h2>
                </div>
                 <div class="cards cards-rest">
                    {% for restaurant in restaurants %}

                <div class="card rest rest-page" style="margin-left:90px">
                <h2>{{ restaurant.restaurantName }}</h2>
                <img src="{{ restaurant.image_url }}" alt="{{ restaurant.name }}" style="height:50%;width:70%">
                <div>
                 <div style="margin-top:20px">
                    <span class="inline">Ratings:</span>
                    {% for i in range(1,restaurant.ratings | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}

                 </div>
                  <div style="margin-top:20px">City: {{ restaurant.city }}</div>
                  <div style="margin-top:20px">Contact Number: {{ restaurant.phone }}</div>

                 <div>
                  <button class="material-icons" title="Delete" style="float:right;margin-top:20px;border:none;background:none" onclick="removeFromFavouriteRestaurants('{{ restaurant.restaurantName}}','{{ restaurant.city}}')" >&#xe872;</button>
                    </div>
                </div>


                </div>

                {% endfor %}
        </div>

        </div>


<hr>
        <div class="favorite-restaurants">
                <div class="title-itinerary">
                    <h2 id="attractionId">Favourite Attractions</h2>

                </div>
                <div style="margin-top:40px;position:relative;float:right;text-underline:none" class="material-symbols-outlined"><a href="#itinerary">arrow_upward</a></div>
                 <div class="cards cards-rest">
                    {% for attraction in attractions %}

                <div class="card rest rest-page" style="margin-left:90px">
                <h2>{{ attraction.attractionName }}</h2>
                <img src="{{ attraction.image_url }}" alt="{{ attraction.attractionName }}" style="height:50%;width:70%">
                <div>
                 <div style="margin-top:20px">
                    <span class="inline">Ratings:</span>
                    {% for i in range(1,attraction.ratings | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}

                 </div>
                  <div style="margin-top:20px">City: {{ attraction.city }}</div>
                  <div style="margin-top:20px">Contact Number: {{ attraction.phone }}</div>

                 <div>
                         <button class="material-icons" title="Delete" style="float:right;margin-top:20px;border:none;background:none"  onclick="removeFromFavouriteAttractions('{{ attraction.attractionName}}','{{ attraction.city}}')" value="Unfavourite">&#xe872;</button>
                    </div>
                </div>


                </div>

                {% endfor %}
        </div>
        </div>

<hr></hr>

 <h2 style="margin:25px" id="hotelId">Hotel Bookings</h2>
     <div style="margin-top:40px;position:relative;float:right;text-underline:none" class="material-symbols-outlined"><a href="#itinerary">arrow_upward</a></div>
     <div style="padding:10px;width: 80%">
            {% for hotel in hotels %}

            <div style="width:100%;height:100%;margin: 45px;padding:10px;border: 1px solid black; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
                <h2>  <span class="inline" style="text-transform:capitalize"> {{ hotel.hotelName }} , {{hotel.city}} </span><sup>
                    {% for i in range(1,hotel.ratings | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}</sup>
                    <span style="float:right;font-size:20px;padding-right:20px">Booking ID: {{hotel.id}} </span>
                    </h2>

                <div style="width: 50%;float: left;">
                    <img src="{{ hotel.image }}" alt="{{ hotel.hotelName }}" style="width:60%;height: 150px">

                </div>
                <div style="margin-left: 60%;float: bottom">
                     <h4>Guest Name: {{ hotel.guestFirstName }} {{hotel.guestLastName}}</h4>
                     <h4>Number of rooms: {{ hotel.rooms }}</h4>
                     <h4>Check-in : <strong>{{ hotel.fromDate }}</strong>  12:00 PM  </h4>
                      <h4>Check-out : <strong>{{ hotel.toDate }}</strong>  11:00 AM  </h4>
                     <h4>City: {{ hotel.city }}</h4>
                     <h4>Total Payment: {{ hotel.totalAmount }}</h4>
                 <div><button style="background-color:#3B666B;color: black;width: 200px;height:30px;border-radius: 4px"  onclick="deleteHotelBooking('{{ hotel.id}}')" value="Cancel Booking">Cancel Booking</button></div>
                </div>

                </div>

            {% endfor %}


        </div>
            <div style="margin-top:150px">
            {%if not hotels%}
            <h1 style="text-align:center">You don't have hotel bookings!!Please navigate to hotels page to book  <a href="/searchHotels">Click Here</a></h1>


        <div id="map"></div>


            {%endif%}
             </div>

        </div>

</div>
 <hr></hr>

      <h2 style="margin:25px" id="flightsId">Flight Bookings</h2>
     <div style="margin-top:40px;position:relative;float:right;text-underline:none" class="material-symbols-outlined"><a href="#itinerary">arrow_upward</a></div>
     <div style="padding:10px;width: 80%;">
            {% for flight in flights %}

            <div style="width:100%;height:;height:100%;margin: 45px;padding:15px;border: 1px solid black; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
                <h2>  <span class="inline" style="text-transform:capitalize"> {{ flight.flightName }} </span><sup>
                    {% for i in range(1,flight.ratings | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}</sup>
                    </h2>
                <div style="width: 50%;float: left;">
                    <img src="{{ flight.image }}" alt="{{ flight.flightName }}" style="width:60%;height: 150px">
                </div>
                <div style="margin-left: 60%;float: bottom">
                     <h4>Booking ID: {{flight.id}} </h4>
                     <h4>{{ flight.fromCity }} TO {{flight.toCity}}</h4>
                     <h4>Travel Class: {{ flight.level}}</h4>
                     <h4>Name : {{ flight.fullName }}</h4>
                     <h4>Number of passengers: {{ flight.passengers }}</h4>

                     <h4>Departure Time: <strong>{{ flight.departTime }}</strong>   </h4>
                     <h4>Total Payment: {{ flight.totalAmount }}</h4>
                 <div><button style="background-color:#3B666B;color: black;width: 200px;height:30px;border-radius: 4px"  onclick="deleteHotelBooking('{{ flight.id}}')" value="Cancel Booking">Cancel Booking</button></div>
                </div>

                </div>

            {% endfor %}


            {% for flight in return_flights %}

            <div style="width:100%;height:;height:100%;margin: 45px;padding:15px;border: 1px solid black; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">

                 <h4 >Booking ID: {{flight.id}} </h4>

                 <div style="padding:20px; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2)">
                 <h2> <span class="inline" style="text-transform:capitalize"> {{ flight.flightName1 }} </span><sup>
                    {% for i in range(1,flight.ratings1 | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}</sup>
                    </h2>
                <div style="width: 50%;float: left;">
                    <img src="{{ flight.image1 }}" alt="{{ flight.flightName1 }}" style="width:60%;height: 150px">
                </div>
                <div style="margin-left: 60%;float: bottom">
                     <h4>Name : {{ flight.fullName }}</h4>
                     <h4>{{ flight.fromCity1 }} TO {{flight.toCity1}}</h4>
                     <h4>Travel Class: {{ flight.level}}</h4>
                     <h4>Number of passengers: {{ flight.passengers }}</h4>

                     <h4>Departure Time: <strong>{{ flight.departTime1 }}</strong>   </h4>
                     <h4>Journey Time: <strong>{{ flight.journeyTime1 }} hrs</strong>   </h4>

                </div>

                </div>


                 <div style="padding:20px; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2)">
                    <h2>  <span class="inline" style="text-transform:capitalize"> {{ flight.flightName2 }} </span><sup>
                    {% for i in range(1,flight.ratings2 | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}</sup>
                    </h2>
                <div style="width: 50%;float: left;">
                    <img src="{{ flight.image2 }}" alt="{{ flight.flightName2 }}" style="width:60%;height: 150px">
                </div>
                <div style="margin-left: 60%;float: bottom">
                     <h4>{{ flight.fromCity2 }} TO {{flight.toCity2}}</h4>
                     <h4>Travel Class: {{ flight.level}}</h4>
                     <h4>Number of passengers: {{ flight.passengers }}</h4>

                     <h4>Departure Time: <strong>{{ flight.departTime2 }}</strong>   </h4>
                      <h4>Journey Time: <strong>{{ flight.journeyTime2 }} hrs</strong>   </h4>
                     <h4>Total Payment: ${{ flight.totalAmount }}</h4>
                 <div><button style="background-color:#3B666B;color: black;width: 200px;height:30px;border-radius: 4px"  onclick="deleteReturnFlightBooking('{{ flight.id}}')" value="Cancel Booking">Cancel Booking</button></div>
                </div>

                </div>

                </div>

            {% endfor %}


        </div>
        <div style="margin-top:150px;margin-bottom:100px">
             {%if not flights and not return_flights%}
            <h1 style="text-align:center">You don't have flight bookings!!Please navigate to flights page to book  <a href="/flight">Click Here</a></h1>
            {%endif%}
             </div>
        </div>

    </div>
</body>
</html>