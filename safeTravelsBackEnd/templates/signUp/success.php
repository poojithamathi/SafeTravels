<!DOCTYPE html>
<html lang="en">
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
    <title>Success</title>
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
        <a class="head" onclick="getUserItinerary()">Itinerary</a>
        <!-- cant access the itinerary page till logged in -->
        <a class="head login nav-item nav-link" id="loginCustomer" href="/loginCustomer" onclick="loggingUser()">Login/Sign Up</a>
    </header>
  <div class="main">
    <main>
      <p>Your Booking Is Successful. Please navigate to itinerary page to find your booking details.</p>

      <input id="user" name="user" style="display:None" value=""/>
      <div class="review-rating">
        <label for="rating">Rating:</label>
        <div>
          {% for i in range(1,6) %}
            <span class="fa fa-star inline" id="star{{i}}" onclick="setChecked({{i}})"></span>
          {% endfor %}
        </div>
      </div>

      <div>
        <label for="review">Review:</label>
        <textarea id="review" name="review"></textarea>
      </div>

      <button type="submit" onclick="submitReview()">Submit Review</button>
    </main>
  </div>
</body>
</html>