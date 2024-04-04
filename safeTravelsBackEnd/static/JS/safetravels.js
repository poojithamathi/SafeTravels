if (document.getElementById("message") != null) {
    let message = document.getElementById("message");
    message.style.display="none";
    let messageText = message.textContent;
    messageText = messageText.slice(14, messageText.indexOf("@"));
    messageText = messageText.slice(0, messageText.indexOf("'"));
    alert(messageText);
}

if (document.getElementById("showPassword") != null) {
    document.getElementById("showPassword").addEventListener("mousedown", () => {
        document.getElementById("passwordInput").type="text";
    });
}
if (document.getElementById("showPassword2") != null) {
    document.getElementById("showPassword2").addEventListener("mousedown", () => {
        document.getElementById("passwordInput2").type="text";
    });
} 

if (document.getElementById("showPassword") != null) {
    document.getElementById("showPassword").addEventListener("mouseup", () => {
        document.getElementById("passwordInput").type="password";
    });
}
if (document.getElementById("showPassword2") != null) {
    document.getElementById("showPassword2").addEventListener("mouseup", () => {
        document.getElementById("passwordInput2").type="password";
    });
}


function addToFavouriteRestaurants(city,restaurantName,image_url,ratings,display_phone){
    console.log(restaurantName)
    let user=sessionStorage.getItem('user')
    fetch('http://127.0.0.1:5000/saveRestaurant', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "city":city,"restaurantName": restaurantName, "image":image_url,"ratings":ratings,"display_phone":display_phone,"user":user})
})
       .then(response=>response.json())
         .then(data=>{
             let result=data['data']
             if(result=="success"){
                document.getElementById('status').innerHTML="Saved Successfully!!!"
             }
             else{
                    document.getElementById('status').innerHTML="Restaurant is already saved!!!"
             }
             document.getElementById('myDialog').show()

        })

    // window.location.href = 'http://127.0.0.1:5000/saveRestaurant';
}

function addToFavouriteAttractions(city,attractionName,image_url,ratings,display_phone){
      console.log(attractionName)
    let user=sessionStorage.getItem('user')
    fetch('http://127.0.0.1:5000/saveAttraction', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "city":city,"attractionName": attractionName, "image":image_url,"ratings":ratings,"display_phone":display_phone,"user":user})
})
        .then(response=>response.json())
         .then(data=>{
             let result=data['data']
             if(result=="success"){
                document.getElementById('status').innerHTML="Saved Successfully!!!"
             }
             else{
                    document.getElementById('status').innerHTML="Attraction is already saved!!!"
             }
             document.getElementById('myDialog').show()

        })

}
function addToFavouriteHotels(hotelName,image_url,ratings,display_name){
  console.log(hotelName)

  fetch('http://127.0.0.1:5000/saveHotel', {
  method: 'POST',
  headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
  },
  body: JSON.stringify({ "city":sessionStorage.getItem('city'),"hotelName": hotelName, "image":image_url,"ratings":ratings,"display_phone":display_name})
})
      .then(response=>{
          if(response=="success"){
               document.getElementById('savedHotel').hidden=false

          }
      })

  // window.location.href = 'http://127.0.0.1:5000/saveRestaurant';
}

function removeFromFavouriteRestaurants(restaurantName,city){
    console.log(restaurantName)

    let user=sessionStorage.getItem('user')
   fetch('http://127.0.0.1:5000/unwishlistRestaurant', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "city":city,"restaurantName": restaurantName,"user":user})
})
        .then(response=>{
            console.log(response)
            if(response.status==200){

                window.location.href = 'http://127.0.0.1:5000/itinerary?user='+user;

            }
        })
}

function removeFromFavouriteAttractions(attractionName,city){

    let user=sessionStorage.getItem('user')
    fetch('http://127.0.0.1:5000/unwishlistAttraction', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "city":city,"attractionName": attractionName,"user":user})
})
        .then(response=>{
            console.log(response)
            if(response.status==200){

                window.location.href =  'http://127.0.0.1:5000/itinerary?user='+user;

            }
        })


}
function bookHotel(hotelName,price,ratings,phone,image){
    console.log(hotelName)
    let rooms= sessionStorage.getItem('rooms')
    let guests= sessionStorage.getItem('guests')
    let city= sessionStorage.getItem('hotel_city')
    let fromDate= sessionStorage.getItem('hotelfromDate')
    let toDate= sessionStorage.getItem('hoteltoDate')
    let hotel_data={hotel:hotelName,city:city,price:price,ratings:ratings,phone:phone,image:image,rooms:rooms,guests:guests,fromDate:fromDate,toDate:toDate}
    sessionStorage.setItem("booking_hotel",JSON.stringify(hotel_data))
    window.location.href = 'http://127.0.0.1:5000/bookHotel';

}

function bookFlight(name,price,ratings,phone,image,depart_time,journey_time,type){
    let passengers=document.getElementById('passengers').value
    let level=document.getElementById('level').value
    let data={name:name,price:price,ratings:ratings,phone:phone,image:image,depart_time:depart_time,journey_time:journey_time,type:type,level:level}
    sessionStorage.setItem("booking_flight",JSON.stringify(data))
    window.location.href = 'http://127.0.0.1:5000/bookFlight?passengers='+passengers.toString()+'&journeyType='+type.toString();
}

function bookReturnFlight(name,price,ratings,phone,image,depart_time,journey_time,name1,price1,ratings1,phone1,image1,depart_time1,journey_time1,type){

    let passengers=document.getElementById('passengers').value
    let level=document.getElementById('level').value
    let data={name:name,price:price,ratings:ratings,phone:phone,image:image,depart_time:depart_time,journey_time:journey_time,
        name1:name1,price1:price1,ratings1:ratings1,phone1:phone1,image1:image1,depart_time1:depart_time1,journey_time1:journey_time1,type:type,level:level}
    sessionStorage.setItem("booking_flight",JSON.stringify(data))

    window.location.href = 'http://127.0.0.1:5000/bookFlight?passengers='+passengers.toString()+'&journeyType='+type.toString();
}
function getHotelDetails(){
    let data=JSON.parse(sessionStorage.getItem('booking_hotel'))
    let rooms=parseInt(data['rooms'])
    let price=parseInt(Number(data['price']).toFixed(2))
    console.log(data)
    document.getElementById('hotelName').innerHTML=data['hotel']
    document.getElementById('hotelphone').innerHTML=data['phone']
    document.getElementById('rooms').innerHTML=data['rooms']
    document.getElementById('hotel_image').src=data['image']
    document.getElementById('ratings').innerHTML=data['ratings']
    document.getElementById('price').innerHTML=price
    document.getElementById('taxes').innerHTML=Number(rooms*price*0.05).toFixed(2)

    let total=parseInt(Number(rooms*price).toFixed(2))+parseInt(Number(rooms*price*0.05).toFixed(2))
    document.getElementById('total').innerHTML=Number(total).toFixed(2)

    changeCurrency()
    setUser()
}

function changeCurrency(){
          sessionStorage.setItem('currentCurrency','USD')
    document.getElementById('current_currency1').innerHTML='USD '
    document.getElementById('current_currency2').innerHTML='USD '
    document.getElementById('current_currency3').innerHTML='USD '

    let currencies={"USD": 1,
    "AUD": 1.498804,
    "BGN": 1.790131,
    "BRL": 5.056787,
    "CAD": 1.355752,
    "CHF": 0.905564,
    "CNY": 6.870714,
    "CZK": 21.381139,
    "DKK": 6.830613,
    "EUR": 0.909401,
    "GBP": 0.80509,
    "HKD": 7.849764,
    "HRK": 6.851882,
    "HUF": 344.370526,
    "IDR": 14940.975982,
    "ILS": 3.601056,
    "INR": 81.840591,
    "ISK": 137.280148,
    "JPY": 132.14517,
    "KRW": 1316.442084,
    "SGD": 1.329802

  }

    for(var key in currencies){
                    const option = document.createElement('option');
                    option.value = key;
                    option.id =key;
                    option.text = key;
                    const select = document.getElementById('currency');
                    select.appendChild(option);
    }
}

function getFlightDetails(){
    let data=JSON.parse(sessionStorage.getItem('booking_flight'))
    let passengers=sessionStorage.getItem('passengers')
    let journeyType=data['type']
    if(journeyType=='one-way'){
        document.getElementById('flightName').innerHTML=data['name']
        document.getElementById('flight_image').src=data['image']
        document.getElementById('depart_time').innerHTML=data['depart_time']
        document.getElementById('journey_time').innerHTML=data['journey_time']
        document.getElementById('fromCity').innerHTML=sessionStorage.getItem('flightFromCity').toUpperCase()
        document.getElementById('toCity').innerHTML=sessionStorage.getItem('flightToCity').toUpperCase()
        var total_price=parseInt(data['price'])

    }
    else{
        document.getElementById('flightName1').innerHTML=data['name']
        document.getElementById('flight_image1').src=data['image']
        document.getElementById('depart_time1').innerHTML=data['depart_time']
        document.getElementById('journey_time1').innerHTML=data['journey_time']
        document.getElementById('fromCity1').innerHTML=sessionStorage.getItem('flightFromCity').toUpperCase()
        document.getElementById('toCity1').innerHTML=sessionStorage.getItem('flightToCity').toUpperCase()

        document.getElementById('flightName2').innerHTML=data['name1']
        document.getElementById('flight_image2').src=data['image1']
        document.getElementById('depart_time2').innerHTML=data['depart_time1']
        document.getElementById('journey_time2').innerHTML=data['journey_time1']
        document.getElementById('fromCity2').innerHTML=sessionStorage.getItem('flightToCity').toUpperCase()
        document.getElementById('toCity2').innerHTML=sessionStorage.getItem('flightFromCity').toUpperCase()
        var total_price=parseInt(data['price'])+parseInt(data['price1'])

    }

    let price=total_price.toFixed(2)
    document.getElementById('price').innerHTML=price
    document.getElementById('taxes').innerHTML=Number(passengers*price*0.05).toFixed(2)

    let total=parseInt(Number(passengers*price).toFixed(2))+parseInt(Number(passengers*price*0.05).toFixed(2))
    document.getElementById('total').innerHTML=Number(total).toFixed(2)

    document.getElementById('passenger').innerHTML=passengers
    changeCurrency()
    setUser()

}

function validatefromDate(){
    let fromDate=document.getElementById('fromDate').value
    let fromDateformatted=new Date(fromDate).toJSON().slice(0, 10);
    let date = new Date().toJSON().slice(0, 10);
    if(fromDateformatted<date){
        alert('From date should be today or future date')
        document.getElementById('fromDate').value=""
    }
    else{
        sessionStorage.setItem('hotelfromDate',fromDate)
    }
}

function validateToDate(){
    let toDate=document.getElementById('toDate').value
    let fromDate=document.getElementById('fromDate').value
    let fromDateformatted=new Date(fromDate).toJSON().slice(0, 10);
    let toDateformatted=new Date(toDate).toJSON().slice(0, 10);

    if(toDateformatted<=fromDateformatted){
        alert('To date should be greater than from date')
        document.getElementById('toDate').value=""
    }
    else{
        sessionStorage.setItem('hoteltoDate',toDate)
    }
}

function validateName(){
    let name=document.getElementById('nameoncard').value
    if(name.length==0){
        document.getElementById('nameoncarderror').innerHTML='Name should not be empty'
    }
    else{
         document.getElementById('nameoncarderror').innerHTML=''
    }
}
function setCity(){
    let city=document.getElementById('city').value
    sessionStorage.setItem("hotel_city",city)
}

function setFromCity(){
    let city=document.getElementById('fromCity').value
    sessionStorage.setItem("flightFromCity",city)

}
function setToCity(){
    let city=document.getElementById('toCity').value
    sessionStorage.setItem("flightToCity",city)

}
function setRooms(){
    let rooms=document.getElementById('rooms').value
    if(rooms>5){
        alert('Maximum of 5 rooms allowed per booking')
    }
    else{
         sessionStorage.setItem("rooms",rooms)
    }

}

function setGuests(){
      let guests=document.getElementById('guests').value
      let rooms=document.getElementById('rooms').value
    if(rooms!=""){
        if(guests>rooms*2){
        alert('Maximum of 2 guests allowed per room');
        document.getElementById('guests').value=""
        }
    else{
         sessionStorage.setItem("guests",guests)
     }
    }

}
function setPassengers(){
      let passengers=document.getElementById('passengers').value
    sessionStorage.setItem("passengers",passengers)

}
function validateAndStoreHotelInfo(){

    let rooms=document.getElementById('rooms').value
    let city=document.getElementById('city').value
    let state=document.getElementById('states').value
    let toDate=document.getElementById('toDate').value
    let fromDate=document.getElementById('fromDate').value
    let guests=document.getElementById('guests').value
    let hotel=document.getElementById('hotel').value
    console.log(guests)
     if(guests=="" || rooms=="" || city=="" || toDate=="" || fromDate==""){
         alert('Please enter all the fields')
         // window.location.href='http://127.0.0.1:5000/searchHotels'
     }
     else{
         const url = new URL("http://127.0.0.1:5000/showHotels");
         url.searchParams.set('guests',guests);
         url.searchParams.set('rooms',rooms);
         url.searchParams.set('myCity',city);
         url.searchParams.set('toDate',toDate);
         url.searchParams.set('fromDate',fromDate);
         url.searchParams.set('hotel',hotel);
         url.searchParams.set('state',state);

         var price_list = ['0-250', '250-500', '500-750', '750-1000'];
         var ratings_list=[0,1,2,3,4,5];
         var prices={}
         var ratings={}
         for (var j = 0; j < price_list.length; j++) {
            if(document.getElementById(price_list[j]).checked){
            prices[price_list[j]]=true
            }
            else{
                prices[price_list[j]]=false
            }
        }

        for (var j = 0; j < ratings_list.length; j++) {
            if(document.getElementById(ratings_list[j]).checked){
            ratings[j]=true
            }
            else{
                 ratings[j]=false
            }
        }
        console.log(JSON.stringify(prices))
        url.searchParams.set('priceFilters',JSON.stringify(prices));
        url.searchParams.set('ratingFilters',JSON.stringify(ratings));
        url.searchParams.set('user',sessionStorage.getItem('user'))
         const updatedUrl = url.toString();
         console.log(updatedUrl)
         window.location.href=updatedUrl
     }

}

function validateAndStoreFlightInfo(){

    let journeyType=document.getElementById('journey-type').value
    let level=document.getElementById('level').value
    let fromCity=document.getElementById('fromCity').value
    let toCity=document.getElementById('toCity').value
    let toDate=document.getElementById('toDate').value
    let fromDate=document.getElementById('fromDate').value
    let passengers=document.getElementById('passengers').value

    var condition=passengers=="" || fromCity=="" || toCity=="" || fromDate==""
    if(journeyType=="return") {
        condition = passengers == "" || fromCity=="" || toCity==""|| fromDate == "" || toDate == ""
    }

     if(condition){
         alert('Please enter all the fields')
         // window.location.href='http://127.0.0.1:5000/searchHotels'
     }
     else{
         const url = new URL("http://127.0.0.1:5000/showFlights");
         url.searchParams.set('passengers',passengers);
         url.searchParams.set('fromCity',fromCity);
         url.searchParams.set('toCity',toCity);
         url.searchParams.set('toDate',toDate);
         url.searchParams.set('fromDate',fromDate);
         url.searchParams.set('level',level);
         url.searchParams.set('journeyType',journeyType);
         url.searchParams.set('user',sessionStorage.getItem('user'))

         var price_list = ['0-250', '250-500', '500-750', '750-1000'];
         var ratings_list=[0,1,2,3,4,5];
         var prices={}
         var ratings={}
         for (var j = 0; j < price_list.length; j++) {
            if(document.getElementById(price_list[j]).checked){
            prices[price_list[j]]=true
            }
            else{
                prices[price_list[j]]=false
            }
        }

        for (var j = 0; j < ratings_list.length; j++) {
            if(document.getElementById(ratings_list[j]).checked){
            ratings[j]=true
            }
            else{
                 ratings[j]=false
            }
        }
        console.log(JSON.stringify(prices))
        url.searchParams.set('priceFilters',JSON.stringify(prices));
        url.searchParams.set('ratingFilters',JSON.stringify(ratings));

         const updatedUrl = url.toString();
         console.log(updatedUrl)
         window.location.href=updatedUrl
     }

}

function fetchAttractions(){

         const url = new URL("http://127.0.0.1:5000/showAttractions");


         var price_list = ['0-250', '250-500', '500-750', '750-1000'];
         var ratings_list=[0,1,2,3,4,5];
         var prices={}
         var ratings={}
         for (var j = 0; j < price_list.length; j++) {
            if(document.getElementById(price_list[j]).checked){
            prices[price_list[j]]=true
            }
            else{
                prices[price_list[j]]=false
            }
        }

        for (var j = 0; j < ratings_list.length; j++) {
            if(document.getElementById(ratings_list[j]).checked){
            ratings[j]=true
            }
            else{
                 ratings[j]=false
            }
        }
        console.log(JSON.stringify(prices))

        url.searchParams.set('myCity',document.getElementById('myCity').value)
        url.searchParams.set('user',sessionStorage.getItem('user'))
        url.searchParams.set('priceFilters',JSON.stringify(prices));
        url.searchParams.set('ratingFilters',JSON.stringify(ratings));


         const updatedUrl = url.toString();
         console.log(updatedUrl)
         window.location.href=updatedUrl

}

function fetchRestaurants(){

         const url = new URL("http://127.0.0.1:5000/showRestaurants");


         var price_list = ['0-250', '250-500', '500-750', '750-1000'];
         var ratings_list=[0,1,2,3,4,5];
         var prices={}
         var ratings={}
         for (var j = 0; j < price_list.length; j++) {
            if(document.getElementById(price_list[j]).checked){
            prices[price_list[j]]=true
            }
            else{
                prices[price_list[j]]=false
            }
        }

        for (var j = 0; j < ratings_list.length; j++) {
            if(document.getElementById(ratings_list[j]).checked){
            ratings[j]=true
            }
            else{
                 ratings[j]=false
            }
        }
        console.log(JSON.stringify(prices))

        url.searchParams.set('myCity',document.getElementById('myCity').value)
        url.searchParams.set('user',sessionStorage.getItem('user'))
        url.searchParams.set('priceFilters',JSON.stringify(prices));
        url.searchParams.set('ratingFilters',JSON.stringify(ratings));


         const updatedUrl = url.toString();
         console.log(updatedUrl)
         window.location.href=updatedUrl

}
function onLoadFlight(filters){

    document.getElementById('toDate').disabled=filters['journeyType']=="one-way"

    document.getElementById('one-way').selected=(filters['journeyType']=="one-way")
    document.getElementById('return').selected=(filters['journeyType']=="return")
    document.getElementById('economy').selected=(filters['level']=="Economy")
    document.getElementById('business').selected=(filters['level']=="Business")
    document.getElementById('first_class').selected=(filters['level']=="First Class")
    setUser()
    setFilters(filters)


}

function enableToDate(){
    if(document.getElementById('journey-type').value == "one-way"){
       document.getElementById('toDate').disabled= true
    }
    else{
        document.getElementById('toDate').disabled= false
    }

}
function validateEmail() {
    let email=document.getElementById('email').value
  const regex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,}$/;
  if(regex.test(email)==false){
       // document.getElementById('email').value=""
      document.getElementById('emailerror').innerHTML="Please enter valid email(Eg: abc@domain.com or abc@domain.co.in )"
       return false
  }
  else{
      document.getElementById('emailerror').innerHTML=""
  }
   return true
}

function validatePhone(){
    let phone=document.getElementById('phone').value
    if(phone.length!=10){
        // document.getElementById('phone').value=""
         document.getElementById('phoneerror').innerHTML="Please enter 10 digit contact number(Eg: 1234567890 )"
         return false
    }
    else{
          document.getElementById('phoneerror').innerHTML=""
    }
     return true
}

function validateCardNumber(){

     let phone=document.getElementById('cardnumber').value
    if(phone.length!=16){
        // document.getElementById('cardnumber').value=""
         document.getElementById('cardnumbererror').innerHTML="Please enter 16 digit valid card number"
         return false
    }
    else{
          document.getElementById('cardnumbererror').innerHTML=""
    }
     return true

}

function validateExpiry(){
    let regex = /^(0[1-9]|1[0-2])\/\d{4}$/;
    let expiry = document.getElementById('expiry').value
    if(regex.test(expiry)==false){
        // document.getElementById('expiry').value=""
      document.getElementById('expiryerror').innerHTML="Please enter expiry date in MM/YYYY format"
        return false
  }
  else{
        let [month, year] = expiry.split('/');
        let date = new Date(year, month - 1, 1);
        let currentDate = new Date();

        if (date.getTime() < currentDate.getTime()) {
            // document.getElementById('expiry').value=""
           document.getElementById('expiryerror').innerHTML="Please enter valid expiry date"
            return false
        }
        else{
             document.getElementById('expiryerror').innerHTML=""
        }

  }
  return true

}

function validateCVV(){
    let cvv= document.getElementById('cvv').value
    if(cvv.length==3 || cvv.length==4){
          document.getElementById('cvverror').innerHTML=""
    }
    else{
          // document.getElementById('cvv').value=""
          document.getElementById('cvverror').innerHTML="Please enter valid cvv"
        return false
    }
    return true
}
function onPageLoad(){
    setUser()
    // document.getElementById('savedRestaurant').hidden=true
    document.getElementById('city').value=sessionStorage.getItem('city');
    let cities=["NYC","ABC"];
    autocomplete(document.getElementById("city"), cities);

}

function proceedhotelpayment(){

    let data=JSON.parse(sessionStorage.getItem('booking_hotel'))

    let user=sessionStorage.getItem('user')
    let firstname=document.getElementById('firstname').value
    let lastname=document.getElementById('lastname').value
    let city = data['city']
    let hotelName = data['hotel']
    let ratings =data['ratings']
    let image = data['image']
    let phone = data['phone']
    let fromDate=data['fromDate']
    let toDate=data['toDate']
    let current_currency=sessionStorage.getItem('currentCurrency')
    let basePrice = document.getElementById('price').innerHTML +" "+ current_currency
    let taxes =document.getElementById('taxes').innerHTML  +" "+ current_currency
    let totalAmount =document.getElementById('total').innerHTML  +" "+ current_currency
    let guestContactNumber = document.getElementById('phone').value
    let guestEmailAddress = document.getElementById('email').value
    let rooms = data['rooms']
    let guests =data['guests']
    if(firstname!="" && lastname!="" && validatePhone() && validateEmail() && validateCardNumber() && validateExpiry() && validateCVV()){

         fetch('http://127.0.0.1:5000/hotelPayment', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
            },
            body: JSON.stringify({ "hotelName":hotelName, "city":city, "ratings":ratings, "image":image,"phone":phone,"basePrice":basePrice,"taxes":taxes
                                ,"totalAmount":totalAmount,"guestFirstName":firstname,"guestLastName":lastname,"guestContactNumber":guestContactNumber,"guestEmailAddress":guestEmailAddress
                                ,"rooms":rooms,"guests":guests,"fromDate":fromDate,"toDate":toDate,"user":user})
            })
        .then(response=>{
            if(response.status==200){
                window.location.href="http://127.0.0.1:5000/success"

            }
        })
        console.log('Booked')

    }
    else{
          alert('Please enter valid information')
    }
}


function proceedFlightpayment(){

    let data=JSON.parse(sessionStorage.getItem('booking_flight'))


    let user=sessionStorage.getItem('user')
    let fullName=document.getElementById('nameoncard').value
    let contactNumber=document.getElementById('phone').value
    var inputsContainer = document.getElementById("passengerslist");
    var names = inputsContainer.getElementsByClassName("passengersnames");
    var ages = inputsContainer.getElementsByClassName("passengersages");
    var genders = inputsContainer.getElementsByClassName("passengersgenders");
    var passengers_list={}
    var names_list=[]
    var ages_list=[]
    var genders_list=[]
    var passengers=sessionStorage.getItem('passengers')
    for (var i = 0; i < names.length; i++) {
             names_list.push(names[i].value);
             ages_list.push(ages[i].value);
             genders_list.push(genders[i].value);
    }

    passengers_list['names']=names_list
    passengers_list['ages']=ages_list
    passengers_list['genders']=genders_list


    var journeyType=data['type']
    var flight_data={}

    if(data['type']=="one-way"){


        let fromCity = sessionStorage.getItem('flightFromCity').toUpperCase()
        let toCity = sessionStorage.getItem('flightToCity').toUpperCase()
        let flightName = data['name']
        let ratings =data['ratings']
        let image = data['image']
        let phone = data['phone']
        let departTime=data['depart_time']
        let journeyTime=data['journey_time']


        let level=data['level']
        let current_currency=sessionStorage.getItem('currentCurrency')
        let basePrice = document.getElementById('price').innerHTML +" "+current_currency
        let taxes =document.getElementById('taxes').innerHTML +" "+current_currency
        let totalAmount =document.getElementById('total').innerHTML +" "+current_currency

        flight_data={ "flightName":flightName, "fromCity":fromCity,"toCity":toCity, "ratings":ratings, "image":image,"phone":phone,"basePrice":basePrice,"taxes":taxes
                                ,"totalAmount":totalAmount,"passengers":passengers,"passengers_list":passengers_list,
                                "departTime":departTime,"journeyTime":journeyTime,"fullName":fullName,"level":level,"journeyType":journeyType,"user":user,"contactNumber":contactNumber}


    }
    else{

        let fromCity = sessionStorage.getItem('flightFromCity').toUpperCase()
        let toCity = sessionStorage.getItem('flightToCity').toUpperCase()
        let flightName = data['name']
        let ratings =data['ratings']
        let image = data['image']
        let phone = data['phone']
        let departTime=data['depart_time']
        let journeyTime=data['journey_time']


        let level=data['level']
        let current_currency=sessionStorage.getItem('currentCurrency')
        let basePrice = document.getElementById('price').innerHTML +" "+current_currency
        let taxes =document.getElementById('taxes').innerHTML +" "+current_currency
        let totalAmount =document.getElementById('total').innerHTML +" "+current_currency


        let fromCity1 = sessionStorage.getItem('flightToCity').toUpperCase()
        let toCity1 = sessionStorage.getItem('flightFromCity').toUpperCase()
        let flightName1 = data['name1']
        let ratings1 =data['ratings1']
        let image1 = data['image1']
        let phone1 = data['phone1']
        let departTime1=data['depart_time1']
        let journeyTime1=data['journey_time1']


        flight_data={ "flightName":flightName, "fromCity":fromCity,"toCity":toCity, "ratings":ratings, "image":image,"phone":phone,"journeyTime":journeyTime,"basePrice":basePrice,"taxes":taxes
                                ,"totalAmount":totalAmount,"passengers":passengers,"passengers_list":passengers_list,
                                "departTime":departTime,"fullName":fullName,"level":level,"flightName1":flightName1,
                                "fromCity1":fromCity1,"toCity1":toCity1, "ratings1":ratings1, "image1":image1,"phone1":phone1,
                                 "departTime1":departTime1,"journeyType":journeyType,"journeyTime1":journeyTime1,"user":user,"contactNumber":contactNumber}

    }


    if(validatePhone() && validateEmail() && validatePhone() && validateCardNumber() && validateExpiry() && validateCVV() && fullName!="" ){

         fetch('http://127.0.0.1:5000/flightPayment', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(flight_data)
            })
            .then(response=>{
            if(response.status==200){
                window.location.href="http://127.0.0.1:5000/success"

                }
            })
        console.log('Booked')

        }
        else{
          alert('Please enter valid information')
         }
}

function deleteHotelBooking(bookingId){

    let user=sessionStorage.getItem('user')
     fetch('http://127.0.0.1:5000/deleteHotelBooking', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "id":bookingId,"user":user})
    })
        .then(response=>{
            if(response.status==200){
                window.location.href= 'http://127.0.0.1:5000/itinerary?user='+user;

            }
        })



}

function deleteFlightBooking(bookingId){

    let user=sessionStorage.getItem('user')
     fetch('http://127.0.0.1:5000/deleteFlightBooking', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "id":bookingId,"user":user})
    })
        .then(response=>{
            if(response.status==200){
                window.location.href='http://127.0.0.1:5000/itinerary?user='+user;

            }
        })



}

function deleteReturnFlightBooking(bookingId){

    let user=sessionStorage.getItem('user')
     fetch('http://127.0.0.1:5000/deleteReturnFlightBooking', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "id":bookingId,"user":user})
    })
        .then(response=>{
            if(response.status==200){
                window.location.href="http://127.0.0.1:5000/success"

            }
        })



}

function setFilters(data){

    setUser()
    document.getElementById('0-250').checked=data.priceFilters.one
    document.getElementById('250-500').checked=data.priceFilters.two
    document.getElementById('500-750').checked=data.priceFilters.three
    document.getElementById('750-1000').checked=data.priceFilters.four
    document.getElementById('0').checked=data.ratingFilters['0']
    document.getElementById('1').checked=data.ratingFilters['1']
    document.getElementById('2').checked=data.ratingFilters['2']
    document.getElementById('3').checked=data.ratingFilters['3']
    document.getElementById('4').checked=data.ratingFilters['4']
    document.getElementById('5').checked=data.ratingFilters['5']

    let state=data.state

    document.getElementById(state).selected=true
    getCities(data)



}
function saveCity(){
    sessionStorage.setItem('city',document.getElementById('city').value)
}

// function getCities(my_data){
//
//     var state=document.getElementById('states').value
//     sessionStorage.setItem('state',state)
//
//      fetch('https://countriesnow.space/api/v0.1/countries/state/cities', {
//     method: 'POST',
//     headers: {
//         'Accept': 'application/json',
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify({ "country":"United States","state":state})
// })
//         .then(response=>response.json())
//          .then(data=>{
//              console.log(data['data'])
//              let cities=data['data']
//              const select = document.getElementById('city');
//              while (select.options.length > 0) {
//                      select.remove(0);
//                 }
//                 const option = document.createElement('option');
//                 option.value ="";
//                 option.id = "Select_City";
//                 option.text = "--Select City--";
//                 select.appendChild(option);
//              for(var i=0;i<cities.length;i++){
//                     const option = document.createElement('option');
//                     option.value = cities[i];
//                     option.id = cities[i];
//                     option.text = cities[i];
//                     select.appendChild(option);
//
//              }
//             //  let city=my_data.city
//             // document.getElementById(city).selected=true
//          })
//
//
// }



function getCities(my_data){

    const states_cities={'Texas':["Abernathy",
        "Abilene",
        "Abram",
        "Addison",
        "Agua Dulce",
        "Alamo",
        "Alamo Heights",
        "Albany",
        "Aldine",
        "Aledo"],
        'California':["Acalanes Ridge",
        "Acton",
        "Adelanto",
        "Agoura",
        "Agoura Hills",
        "Agua Dulce",
        "Aguanga",
        "Ahwahnee",
        "Alameda",
        "Alameda County",
        "Alamo",
        "Albany"],'Indiana':["Aberdeen",
        "Adams County",
        "Akron",
        "Albany",
        "Albion",
        "Alexandria",
        "Allen County",
        "Anderson",
        "Andrews",
        "Angola",
        "Arcadia",
        "Argos",
        "Attica"],'Colarado':[ "Acres Green",
        "Adams County",
        "Air Force Academy",
        "Akron",
        "Alamosa",
        "Alamosa County",
        "Alamosa East",
        "Applewood",
        "Arapahoe County",
        "Archuleta County",
        "Aristocrat Ranchettes",
        "Arvada",
        "Aspen",
        "Ault",
        "Aurora",
        "Avon",
        "Baca County",
        "Basalt",
        "Battlement Mesa",
        "Bayfield",
        "Bennett",
        "Bent County",
        "Berkley",
        "Berthoud",
        "Black Forest",
        "Boulder",
        "Boulder County",
        "Breckenridge",
        "Brighton",
        "Broomfield",
        "Broomfield County",
        "Brush",
        "Buena Vista",
        "Burlington",
        "Byers",
        "Campion",
        "Cañon City",
        "Carbondale",
        "Carriage Club",
        "Cascade-Chipita Park",
        "Castle Pines",
        "Castle Pines North",
        "Castle Rock",
        "Castlewood",
        "Cedaredge",
        "Centennial",
        "Center"],'Tennessee':[ "Adamsville",
        "Alamo",
        "Alcoa",
        "Algood",
        "Altamont",
        "Anderson County",
        "Apison",
        "Ardmore",
        "Arlington",
        "Ashland City",
        "Athens",
        "Atoka",
        "Banner Hill",
        "Bartlett",
        "Baxter",
        "Bean Station",
        "Bedford County",
        "Belle Meade",
        "Bells",
        "Benton",
        "Benton County",
        "Blaine",
        "Bledsoe County",
        "Bloomingdale",
        "Blount County",
        "Blountville",
        "Bluff City",
        "Bolivar",
        "Bon Aqua Junction",
        "Bradford",
        "Bradley County",
        "Brentwood",
        "Brentwood Estates",
        "Brighton",
        "Bristol",
        "Brownsville",
        "Bruceton",
        "Burns",
        "Byrdstown",
        "Camden",
        "Campbell County",
        "Cannon County",
        "Carroll County",
        "Carter County",
        "Carthage",
        "Caryville",
        "Celina",
        "Centerville",
        "Central",
        "Chapel Hill",
        "Charlotte",
        "Chattanooga",
        "Cheatham County",
        "Chester County",
        "Christiana",
        "Church Hill",
        "Claiborne County",
        "Clarksville",
        "Clay County",
        "Cleveland",
        "Clifton",
        "Clinton",
        "Coalfield",
        "Cocke County",
        "Coffee County",
        "Collegedale",
        "Collierville",
        "Colonial Heights",
        "Columbia",
        "Condon",
        "Cookeville",
        "Coopertown",
        "Cornersville",
        "Covington",
        "Cowan",
        "Crockett County",
        "Cross Plains",
        "Crossville",
        "Crump",
        "Cumberland County",
        "Dandridge",
        "Davidson County",
        "Dayton",
        "Decatur",
        "Decatur County",
        "Decaturville",
        "Decherd",
        "DeKalb County",
        "Dickson",
        "Dickson County",
        "Dodson Branch",
        "Dover",
        "Dresden",
        "Dunlap",
        "Dyer"]}
    var state=document.getElementById('states').value
    sessionStorage.setItem('state',state);

             let cities=states_cities[state]
             const select = document.getElementById('city');
             while (select.options.length > 0) {
                     select.remove(0);
                }
                const option = document.createElement('option');
                option.value ="";
                option.id = "Select_City";
                option.text = "--Select City--";
                select.appendChild(option);
             for(var i=0;i<cities.length;i++){
                    const option = document.createElement('option');
                    option.value = cities[i];
                    option.id = cities[i];
                    option.text = cities[i];
                    select.appendChild(option);

             }


}

function setHotel(){
    let restaurant=document.getElementById('hotel')
    sessionStorage.setItem('hotel',hotel)
}
function setUser(){

        var user=sessionStorage.getItem('user')
        if(user==null){
            alert('Please login')
            window.location.href='http://127.0.0.1:5000/loginCustomer'
        }
        else{
        document.getElementById('loginCustomer').innerHTML='Hi '+user+', logout?'

            document.getElementById('loginCustomer').href='/logoutCustomer'
            document.getElementById('user').value=user
        }
}



function getUserItinerary(){

    let user=sessionStorage.getItem('user')
    window.location.href='http://127.0.0.1:5000/itinerary?&user='+user;

}

function loggingUser(){
    let user=sessionStorage.getItem('user')
    if(user!=null){
        sessionStorage.removeItem('user')
    }
}

function setChecked(starNumber){
    for(var i=1;i<=starNumber;i++){
        let idValue='star'+i
        document.getElementById(idValue).className='fa fa-star fa-1x inline checked'
    }
     for(var i=starNumber+1;i<=5;i++){
        let idValue='star'+i
        document.getElementById(idValue).className='fa fa-star fa-1x inline'
    }

}
function submitReview(){
    let ratings=0;
    for(var i=5;i>=1;i--){
        let tempValue='star'+i
          if(document.getElementById(tempValue).className=='fa fa-star inline checked'){
              ratings=i;
              break;
          }

    }
    let reviews=document.getElementById('review').value
    let user=sessionStorage.getItem('user')
    fetch('http://127.0.0.1:5000/saveRatings', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "ratings":ratings,"reviews": reviews, "user":user})
})
        .then(response=>{
            if(response.status==200){
                window.location.href='/thankyou'

            }
        })



}

function changePrice(){

    var currencies={
    "AUD": 1.498804,
    "BGN": 1.790131,
    "BRL": 5.056787,
    "CAD": 1.355752,
    "CHF": 0.905564,
    "CNY": 6.870714,
    "CZK": 21.381139,
    "DKK": 6.830613,
    "EUR": 0.909401,
    "GBP": 0.80509,
    "HKD": 7.849764,
    "HRK": 6.851882,
    "HUF": 344.370526,
    "IDR": 14940.975982,
    "ILS": 3.601056,
    "INR": 81.840591,
    "ISK": 137.280148,
    "JPY": 132.14517,
    "KRW": 1316.442084,
    "SGD": 1.329802,
    "USD": 1
  }

    let price=document.getElementById('price').innerHTML
    let taxes=document.getElementById('taxes').innerHTML
    let total=document.getElementById('total').innerHTML
    // let api_key="RLHYh61Uk2TU9tVxv0tA4BN2yVzCBpbmK8e7Tic2"
    let current_currency=sessionStorage.getItem('currentCurrency').toString()
    let current_value=currencies[current_currency]
    let updated_currency=document.getElementById('currency').value
    let updated_value=currencies[updated_currency]

    let new_price=price*(updated_value/current_value)
    let new_taxes=taxes*(updated_value/current_value)
    let new_total=total*(updated_value/current_value)
    document.getElementById('price').innerHTML= new_price.toFixed(4).toString()
    document.getElementById('taxes').innerHTML= new_taxes.toFixed(4).toString()
    document.getElementById('total').innerHTML= new_total.toFixed(4).toString()

    document.getElementById('current_currency1').innerHTML=updated_currency
    document.getElementById('current_currency2').innerHTML=updated_currency
    document.getElementById('current_currency3').innerHTML=updated_currency

    sessionStorage.setItem('currentCurrency',updated_currency)
}
function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
              b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}