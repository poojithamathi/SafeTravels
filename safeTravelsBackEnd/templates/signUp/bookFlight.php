<html>

<head>
    <meta charset="utf-8" />
    <meta name="'viewpoint">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/normalize.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='CSS/safetravels.css') }}">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,700,0,0" />
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>Flight Booking Page</title>
</head>

<script src="/../static/JS/safetravels.js"></script>
<body onload="getFlightDetails()">

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
   <div style="display: flex;justify-content: space-between;align-items: center;">
            <h1>Flight Booking</h1>
            <h4 style="margin-right:1%">Change Currency:
            <select id="currency" name="currency" onchange="changePrice()">
            </select>
            </h4>
   </div>
   <div style="width:100%;height:80%;margin:35px">

        <div style="width:65%;float:left;padding:20px;border: 3px solid green; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">

        {% if journeyType=='one-way'%}
          <div style="padding:20px; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2)">

            <h1 id="flightName"></h1>
            <div style="width:100%;padding-top: 5px">
                <div style="width: 50%;float: left;">
                    <img src="" id="flight_image" alt="123" style="width:60%;height: 70px">
                </div>
                <div style="margin-left: 60%">
                     <p><span id="fromCity"></span> TO <span id="toCity"></span></p>
                     <p>Departure Time: <span id="depart_time"></span></p>
                    <p>Journey Time: <span id="journey_time"></span> hrs</p>
                </div>

            </div>
          </div>
        {%else%}

         <div style="padding:20px; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2)">

            <h1 id="flightName1"></h1>
            <div style="width:100%;padding-top: 5px">
                <div style="width: 50%;float: left;">
                    <img src="" id="flight_image1" alt="123" style="width:60%;height: 70px">
                </div>
                <div style="margin-left: 60%">
                    <p><span id="fromCity1"></span> TO <span id="toCity1"></span></p>
                    <p>Departure Time: <span id="depart_time1"></span></p>
                    <p>Journey Time: <span id="journey_time1"></span> hrs</p>
                </div>

            </div>
          </div>

           <div style="padding:20px; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2)">

            <h1 id="flightName2"></h1>
            <div style="width:100%;padding-top: 5px">
                <div style="width: 50%;float: left;">
                    <img src="" id="flight_image2" alt="123" style="width:60%;height: 70px">
                </div>
                <div style="margin-left: 60%">
                    <p><span id="fromCity2"></span> TO <span id="toCity2"></span></p>
                    <p>Departure Time: <span id="depart_time2"></span></p>
                    <p>Journey Time: <span id="journey_time2"></span> hrs</p>
                </div>

            </div>
          </div>

        {%endif%}
        </div>

        <div style="margin-left:70%;">
            <div style="width:90%;padding:20px;border: 3px solid green; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
            <h2>Price Details</h2>
            <hr></hr>
            <div style="padding-top: 5px">
                <div>
                     <p>Ticket Price per passenger : <span id="price"></span> <span id="current_currency1"></span></p>
                      <p>Number of passengers : <span id="passenger"></span></p>
                     <p>Taxes  : <span id="taxes"></span> <span id="current_currency2"></span></p>
                    <p>Total Amount : <span id="total"></span> <span id="current_currency3"> </span></p>
                </div>
            </div>
            </div>
        </div>
    </div>


   <div style="width:65%;margin:35px;padding:10px;border:3px solid green; box-shadow: 2px 4px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
        <h1>Passenger Information</h1>

         <div style="padding:10px"  id="passengerslist">
            {% for i in range(1,passengers | int + 1) %}
            <div style="margin:5px">
                <label for="firstname"> PASSENGER {{i}}<sup> <span style="color:red">*</span></sup></label>
                <input class="passengersnames" style="border-radius:5px;border:2px solid gray;width:300px;margin-left: 15px;margin-right:10px;font-size:15px;text-color:black" id="passenger1" name="passenger1" placeholder="ENTER FULL NAME"/>
                <label  for="age"> AGE <sup> <span style="color:red">*</span></sup></label>
                <input class="passengersages" style="border-radius:5px;border:2px solid gray;width:60px;margin-left: 15px;margin-right:10px;font-size:15px;text-color:black" id="age" name="age" placeholder="AGE" >
                <label for="gender"> GENDER<sup> <span style="color:red">*</span></sup></label>
                <input class="passengersgenders" style="border-radius:5px;border:2px solid gray;width:200;margin-left: 15px;font-size:15px;text-color:black" id="gender" name="gender" placeholder="GENDER"/>

            </div>
             {% endfor %}
        </div>

    </div>


   <div style="width:100%;margin:35px">
        <div style="width:65%;float:left;padding:20px;border: 3px solid green; box-shadow: 0 8px 8px 0 rgba(0,0,0,0.2);border-radius: 5px">
            <h1>Payment Details</h1>

         <div style="padding:10px" >
            <div style="margin:30px">
                <label for="nameoncard"> NAME <sup> <span style="color:red">*</span></sup></label>
                <input style="border-radius:5px;border:2px solid gray;width:300px;margin-left: 128px;font-size:15px;text-color:black" id="nameoncard" name="nameoncard" placeholder="NAME ON THE CARD" onchange="validateName()"/>
                <div id="nameoncarderror" style="margin-left: 180px;margin-top:10px;color:red;font-size:15px"></div>
            </div>
            <div style="margin:30px">
                <label for="cardnumber"> CARD NUMBER <sup> <span style="color:red">*</span></sup></label>
                <input style="border-radius:5px;border:2px solid gray;width:300px;margin-left: 65px;font-size:15px;text-color:black" id="cardnumber" name="cardnumber" placeholder="ENTER CARD NUMBER" onchange="validateCardNumber()"/>
                <div id="cardnumbererror" style="margin-left: 180px;margin-top:10px;color:red;font-size:15px"></div>
            </div>
            <div style="margin:30px">
                <label for="expiry"> EXPIRY DATE<sup> <span style="color:red">*</span></sup></label>
                <input style="border-radius:5px;border:2px solid gray;width:300px;margin-left: 82px;font-size:15px;text-color:black" type="text" id="expiry" name="expiry" placeholder="MM/YYYY" onchange="validateExpiry()"/>
                 <div id="expiryerror" style="margin-left: 180px;margin-top:10px;color:red;font-size:15px"></div>
            </div>
            <div style="margin:30px">
                <label for="cvv">CVV<sup> <span style="color:red">*</span></sup></label>
               <input style="border-radius:5px;border:2px solid gray;width:300px;margin-left: 146px;font-size:15px;text-color:black" type="password" id="cvv" name="cvv" placeholder="CVV" onchange="validateCVV()"/>
               <div id="cvverror" style="margin-left: 180px;margin-top:10px;color:red;font-size:15px"></div>
            </div>
            <div style="margin:30px">
                <label for="phone">CONTACT NUMBER <sup> <span style="color:red">*</span></sup></label>
              <input style="border-radius:5px;border:2px solid gray;;width:300px;margin-left: 35px;font-size:15px;text-color:black" type="text" id="phone" name="phone" value="" placeholder="CONTACT NUMBER" onchange="validatePhone()"/>
              <div id="phoneerror" style="margin-left: 180px;margin-top:10px;color:red;font-size:15px"></div>
            </div>

            <div style="margin:30px">
                <label for="phone">EMAIL ADDRESS </label>
              <input style="border-radius:5px;border:2px solid gray;;width:300px;margin-left: 65px;font-size:15px;text-color:black" type="text" id="email" name="email" value="" placeholder="EMAIL ADDRESS"/>
              <div id="emailerror" style="margin-left: 180px;margin-top:10px;color:red;font-size:15px"></div>
            </div>

            <div style="margin:30px">
                <label for="zipcode">ZIP CODE </label>
              <input style="border-radius:5px;border:2px solid gray;;width:300px;margin-left: 115px;font-size:15px;text-color:black" type="text" id="zipcode" name="zipcode" value="" placeholder="ZIP CODE"/>
            </div>
            <div style="margin:30px">
             <button style="width:500px;height:50px;border-radius:5px;background-color:dodgerblue;text-color:white" id="proceed" onclick="proceedFlightpayment()">Proceed with payment</button>
            </div>
        </div>
    </div>

    </div>



</body>

</html>