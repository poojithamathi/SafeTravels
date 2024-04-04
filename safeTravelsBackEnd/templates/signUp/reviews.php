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
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-hyb/lC1noJyfdl+ttPcYY7Pn5Z5JNhZfI5QFL/m35/J+uSPvG8c7Bxwo2JDKC7m/wZOAzZMam7bOkt9pCDVJg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
     <script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
        <title>Reviews</title>

    </head>
<script src="/../static/JS/safetravels.js"></script>

  <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  chat-title="Hotel-Booking"
  agent-id="53fed34b-baf5-4c0d-bacc-9c57b36125e9"
  language-code="en"
></df-messenger>
<script>
input: string // Text entered by user
const dfMessenger = document.querySelector('df-messenger');
const payload = [
  {
    "type": "info",
    "title": "Info item title",
    "subtitle": "Info item subtitle",
    "image": {
      "src": {
        "rawUrl": "https://example.com/images/logo.png"
      }
    },
    "actionLink": "https://example.com"
  }];
dfMessenger.renderCustomCard(payload);
</script>
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
        <a href='/reviews' class="head" onclick="getUserReviews()" >Reviews</a>
        <a class="head login nav-item nav-link" id="loginCustomer" href="/loginCustomer" onclick="loggingUser()">Login/Sign Up</a>
            <!-- login page -->
    </header>
     <div id="dialogflow"></div>

         <div style="width:100%">
        <div class="favorite-restaurants">
                <div class="title-itinerary">
                    <h2 id="restaurantId">User Reviews</h2>
                </div>
                 <div class="cards cards-rest">
                    {% for review in results %}

                <div class="card rest rest-page" style="margin-left:90px;height:200px;width:25%">
                <span style="font-size:20px;float:left"> <i class="fa fa-user inline">  </i> {{ review.userId }}</span>

                <div style="padding-top: 25px">

                 <div>
                    <span class="inline">Ratings:</span>
                    {% for i in range(1,review.ratings | int + 1) %}
                        <span class="fa fa-star checked inline"></span>
                    {% endfor %}

                 </div>
                    <p>Review: {{ review.reviews }}</p>
                </div>


                </div>

                {% endfor %}
        </div>

        </div>


    </div>
</body>
</html>