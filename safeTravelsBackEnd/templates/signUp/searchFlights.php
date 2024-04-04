<html>

<head>
    <meta charset="utf-8" />
    <meta name="'viewpoint">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/normalize.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/safetravels.css') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <title>Flights</title>
</head>

<script src="/../static/JS/safetravels.js"></script>
    <script>
        var result = [
            {% for flight in flights %}
                {{ flight | tojson }},
            {% endfor %}
        ];
        console.log(result);
        var filters={{data|tojson}}

 </script>
<body onload="onLoadFlight(filters)" style="margin-bottom:100px">

    <header>
        <a href="/"><img class="logo" src="{{ url_for('static', filename='Images/SafeTravelsLogo.png') }}"> </a>
        <!-- <p class="head">Search</p> -->
        <a href="/searchAttractions" class="head">Attractions</a>
        <a href="/flight" class="head">Flights</a>
        <a href="/searchHotels" class="head">Hotels</a>
        <a href="/searchRestaurants" class="head">Restaurants</a>
        <!-- maybe flights, hotels, and restaurants could be a drop down menu -->
        <a class="head" onclick="getUserItinerary()" >Itinerary</a>
        <!-- cant access the itinerary page till logged in -->
        <a class="head login nav-item nav-link" id="loginCustomer" href="/loginCustomer" onclick="loggingUser()">Login/Sign Up</a>
    </header>
    <div class="search-bar flight-search-bar">
            <div class="autocomplete">
                <div style="width:100%" class="inline">
                    <div style="width:50%;float:left;margin-left:5%">
                        <input id="fromCity" type="text" name="fromCity" placeholder="Source City"
                    class="form-control" onchange="setFromCity()" style="width:320px;border-radius:5px;border:1px solid black" value={{data.fromCity}}>
                     </div>
                    <div style="margin-left:55%;width:50%">
                        <input id="toCity" type="text" name="toCity" placeholder="Destination City"
                        class="form-control" onchange="setToCity()" style="width:320px;border-radius:5px;border:1px solid black" value={{data.toCity}}>
                    </div>
                </div>
                    <div class="dates">
                        <select name="journey-type" id="journey-type" style="width:250px;height:50px;padding:10px;margin:5px;font-size:20px;border-radius:5px;border:1px solid black" onchange="enableToDate()">
                            <option value="one-way" id="one-way">One-way</option>
                            <option value="return" id="return">Return</option>
                        </select>

                         <select name="level" id="level" style="width:250px;height:50px;padding:10px;margin:5px;font-size:20px;border-radius:5px;border:1px solid black">
                            <option value="Economy" id="economy">Economy</option>
                            <option value="Business" id="business">Business</option>
                            <option value="First Class" id="first_class">First Class</option>
                        </select>

                        <input id="passengers" type="text" name="passengers" placeholder="Number of passengers" onchange="setPassengers()" style="border-radius:5px;border:1px solid black" value={{data.passengers}}>
                    </div>
                    <div class="dates">
                         <input id="fromDate" type="date" name="fromDate" onchange="validatefromDate()" placeholder="From" title="Departure Date" style="border-radius:5px;border:1px solid black" value={{data.fromDate}}>
                        <input id="toDate" type="date" name="toDate" placeholder="To" onchange="validateToDate()" title="Return Date" style="margin-left:-150px;border-radius:5px;border:1px solid black" value={{data.toDate}}>
                    </div>
                <button class="submitB" onclick="validateAndStoreFlightInfo()">submit</button>
            </div>
    </div>
    <div class="loader"></div>
    <div class="spinner-border text-primary" id="spinner" role="status">
        <span class="sr-only">Loading...</span>
    </div>
    <div class="cards cards-rest">


    <div id="response" style="width: 100%">
        <div  style="width: 20%; float: left;padding: 20px">
            <!-- rating, price, open, hot_and_new, liked_by_vegetarians, outdoor_seating, parking_lot, parking_valet, delivery, takeout -->
            <div style="width: 100%">
            <h3>Filters</h3>
            <div style="width:100%;padding:10px;border: 1px solid black; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
                <p>Price Range</p>
                <div style="padding: 10px">
                    <input type="checkbox" id="0-250" name="price">
                    <label for="0-250">$0  -  $250</label>
                </div>

            <div style="padding: 10px">
            <input type="checkbox" id="250-500" name="price">
            <label for="250-500">$250-$500</label>
            </div>
            <div style="padding: 10px">
            <input type="checkbox" id="500-750" name="price">
                <label for="500-750">$500-$750</label>
            </div>
            <div style="padding: 10px">
            <input type="checkbox" id="750-1000" name="price">
            <label for="750-1000">$750-$1000</label>
            </div>

            </div>
            <!-- price -->

            <!-- rating -->
        <div style="margin-top: 15px;padding:10px;border: 1px solid black; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
                <p>Ratings</p>
                <div style="padding: 10px">
                    <input type="checkbox" id="0" name="ratings" value="0">
                    <label for="0">No ratings</label>
                </div>

             <div style="padding: 10px">
                    <input type="checkbox" id="1" name="ratings" value="1">
                    <label for="1">
                         {% for i in range(1,2) %}
                            <span class="fa fa-star checked inline"></span>
                        {% endfor %}
                    </label>
                </div>
             <div style="padding: 10px">
                    <input type="checkbox" id="2" name="ratings" value="2">
                    <label for="2">
                          {% for i in range(1,3) %}
                            <span class="fa fa-star checked inline"></span>
                        {% endfor %}

                    </label>
                </div>
             <div style="padding: 10px">
                    <input type="checkbox" id="3" name="ratings" value="3">
                    <label for="3">
                          {% for i in range(1,4) %}
                            <span class="fa fa-star checked inline"></span>
                        {% endfor %}

                    </label>
                </div>
             <div style="padding: 10px">
                    <input type="checkbox" id="4" name="ratings" value="4">
                    <label for="4">
                        {% for i in range(1,5) %}
                            <span class="fa fa-star checked inline"></span>
                        {% endfor %}
                    </label>
                </div>
            <div style="padding: 10px">
                    <input type="checkbox" id="5" name="ratings" value="5">
                    <label for="5">
                        {% for i in range(1,6) %}
                            <span class="fa fa-star checked inline"></span>
                        {% endfor %}
                    </label>
                </div>
            </div>


            <div style="margin-top: 15px;">
                <button style="height:35px;width:250px;background-color: #3B666B;color: black;border-color:#3B666B;border-radius: 5px" onclick="validateAndStoreFlightInfo()">Apply</button>
           </div>
            </div>
        </div>




        <div class="cards flight-crads">
            {% for flight in flights %}

            <div>
            {% if data.journeyType=="one-way"%}
            <div style="width:100%;margin-top: 15px;padding:20px;border: 1px solid black; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px;">
                 <h2><span class="inline" style="text-transform:capitalize">Airlines: {{ flight.name }}</span><sup>
                    {% for i in range(1,flight.rating | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}</sup></h2>
            <div style="padding-top: 5px">
               <div>
                <div>

                    <p>Departure Time: {{flight.departure_time}}</p>
                    <p>Journey Time: {{flight.journey_time}} hrs </p>
                     <p>Price: ${{ flight.price }} / person</p>
                     <div><button style="margin-top:15px;margin-left:83%;background-color: #F2C4CB;color: black;width: 120px;height:30px;border-radius: 4px" onclick="bookFlight('{{ flight.name }}','{{ flight.price }}','{{ flight.rating }}','{{ flight.display_phone }}','{{ flight.image_url }}','{{ flight.departure_time }}','{{ flight.journey_time }}','one-way')"> Book</button></div>

                </div>

                </div>

            </div>
            {%else%}

            <div style="width:100%;margin-top: 15px;padding:20px;border: 1px solid black; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">

              <div style="width:100%;margin-top: 15px;padding:15px; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
                <h2><span class="inline" style="text-transform:capitalize">Airlines: {{ flight.flight1.name }}</span><sup>
                    {% for i in range(1,flight.flight1.rating | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}</sup></h2>
                <div style="padding-top: 5px">
                    <p> {{flight.flight1.location.city}} To {{flight.flight2.location.city}}</p>
                    <p>Departure Time: {{flight.flight1.departure_time}}</p>
                     <p>Price: ${{ flight.flight1.price }} / person</p>

                </div>
               </div>

              <div style="width:100%;margin-top: 15px;padding:15px; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
                <h2><span class="inline" style="text-transform:capitalize">Airlines: {{ flight.flight2.name }}</span><sup>
                    {% for i in range(1,flight.flight2.rating | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}</sup></h2>
                <div style="padding-top: 5px">
                 <p> {{flight.flight2.location.city}} To {{flight.flight1.location.city}}</p>
                    <p>Departure Time: {{flight.flight2.departure_time}}</p>
                     <p>Price: ${{ flight.flight2.price }} / person</p>

                </div>
                </div>
            <div><button style="margin-top:15px;margin-left:83%;background-color: #F2C4CB;color: black;width: 120px;height:30px;border-radius: 4px" onclick="bookReturnFlight('{{ flight.flight1.name }}','{{ flight.flight1.price }}','{{ flight.flight1.rating }}','{{ flight.flight1.display_phone }}','{{ flight.flight1.image_url }}','{{ flight.flight1.departure_time }}','{{ flight.flight1.journey_time }}','{{ flight.flight2.name }}','{{ flight.flight2.price }}','{{ flight.flight2.rating }}','{{ flight.flight2.display_phone }}','{{ flight.flight2.image_url }}','{{ flight.flight2.departure_time }}','{{ flight.flight2.journey_time }}','return')"> Book</button></div>

            {%endif%}

            </div>

            {% endfor %}

        </div>
    </div>
    </div>

    <!-- <div style="float:right;margin-top:40px"><span class="material-symbols-outlined">arrow_upward</span></div> -->
</body>

</html>