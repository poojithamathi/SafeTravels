<html>

<head>
    <meta charset="utf-8" />
    <meta name="'viewpoint">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/normalize.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/safetravels.css') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <title>Restaurants</title>
</head>

<script src="/../static/JS/safetravels.js"></script>
    <script>
        var filters={{data|tojson}}
        console.log(filters.restaurant)
    </script>
<body onload="setFilters(filters)" style="margin-bottom:100px">

    <header>
        <a href="/"><img class="logo" src="{{ url_for('static', filename='Images/SafeTravelsLogo.png') }}"> </a>
        <!-- <p class="head">Search</p> -->
        <a href="/searchAttractions" class="head">Attractions</a>
        <a href="/flight" class="head">Flights</a>
        <a href="/searchHotels" class="head">Hotels</a>
        <a href="/searchRestaurants" class="head">Restaurants</a>
        <!-- maybe flights, hotels, and restaurants could be a drop down menu -->
        <a class="head" onclick="getUserItinerary()">Itinerary</a>
        <!-- cant access the itinerary page till logged in -->
        <a class="head login nav-item nav-link" id="loginCustomer" href="/loginCustomer" onclick="loggingUser()">Login/Sign Up</a>
    </header>
    <div class="search-bar restaurant-search-bar">
           <div class="autocomplete">
                <input id="myCity" type="text" name="myCity" placeholder="Which city you are going to"
                    class="form-control" onchange="setCity()" value="{{data.myCity}}">
                <input id="user" name="user" style="display:None" value=""/>
                <button class="submitB" onclick="fetchRestaurants()">submit</button>
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
                <button style="height:35px;width:250px;background-color: #3B666B;color: black;border-color:#3B666B;border-radius: 5px" onclick="fetchRestaurants()">Apply</button>
           </div>
            </div>
        </div>




        <div class="cards cards-rest">
            {% for restaurant in restaurants %}

            <div class="card rest rest-page">
                <h2>{{ restaurant.name }}</h2>
                <img src="{{ restaurant.image_url }}" alt="{{ restaurant.name }}" style="height:200px">
                <div style="padding-top: 5px">

                 <div>
                 <p>Price: ${{ restaurant.price }}</p>
                    <span class="inline">Ratings:</span>
                    {% for i in range(1,restaurant.rating | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}

                    </div>
                    <p>Contact Number: {{ restaurant.display_phone }}</p>
                </div>
                <span class="material-symbols-outlined" onclick="addToFavouriteRestaurants('{{restaurant.location.city}}','{{restaurant.name}}','{{restaurant.image_url}}','{{restaurant.rating}}','{{restaurant.display_phone}}')"> add</span>
            </div>
            {% endfor %}
        </div>
        </div>
    </div>

    <dialog id="myDialog" style="height:70px;border:1px solid grey">
        <h2 style="margin:2px"><span id="status"></span> <span class="close-button" style="float:right" onclick="document.getElementById('myDialog').close()">&#x2716;</span></h2>
    </dialog>

</body>

</html>