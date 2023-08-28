var owKey = ''
var weatherCity = ''
var tempUnit = ''

var ouvKey = ''

var lat = ''
var lng = ''

var hereAPI_key = ''

var quantity = 0; // Initial quantity

function getTime() {
    var time = new Date();

    var secs;
    var min;
    var hrs;

    if (time.getSeconds().toString().length < 2) {
        secs = '0' + time.getSeconds().toString()
    } else {
        secs = time.getSeconds().toString()
    }

    if (time.getMinutes().toString().length < 2) {
        min = '0' + time.getMinutes().toString()
    } else {
        min = time.getMinutes().toString()
    }

    if (time.getHours().toString().length < 2) {
        hrs = '0' + time.getHours().toString()
    } else {
        hrs = time.getHours().toString()
    }

    var curTime = hrs + ':' + min + ':' + secs;
    document.getElementById('time').innerHTML = curTime;

    var curDate = time.getDate() + '/' + (parseInt(time.getMonth() + 1)).toString() + '/' + time.getFullYear();
    document.getElementById('date').innerHTML = curDate;

    setTimeout(getTime, 500);
}

function getWeather() {
    weatherURL = 'https://api.openweathermap.org/data/2.5/weather?q=' + weatherCity + '&units=' + tempUnit + '&appid=' + owKey


    /*if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getUVLatLong, posError, {
            timeout: 30000,
            enableHighAccuracy: true
        })
    }*/

    var time = new Date();

    var secs;
    var min;
    var hrs;

    if (time.getSeconds().toString().length < 2) {
        secs = '0' + time.getSeconds().toString()
    } else {
        secs = time.getSeconds().toString()
    }

    if (time.getMinutes().toString().length < 2) {
        min = '0' + time.getMinutes().toString()
    } else {
        min = time.getMinutes().toString()
    }

    if (time.getHours().toString().length < 2) {
        hrs = '0' + time.getHours().toString()
    } else {
        hrs = time.getHours().toString()
    }

    var curTime = hrs + ':' + min + ':' + secs;

    document.getElementById('weatherUpdateDate').innerHTML = 'Last update: ' + curTime;
    setTimeout(getWeather, 1800000);
}


function reboot() {
    console.log('Rebooting...');
    $.ajax({ type: 'GET', url: '/reboot' });
}



function increaseQuantity() {
    quantity++;
    updateQuantity();
    updateContinueButton();
}

function decreaseQuantity() {
    if (quantity > 0) {
        quantity--;
        updateQuantity();
        updateContinueButton();
    }
}

function updateQuantity() {
    document.getElementById("quantity").textContent = quantity;
}

function updateContinueButton() {
    var continueButton = document.getElementById("continueButton");
    if (quantity > 0) {
        continueButton.removeAttribute("disabled");
    } else {
        continueButton.setAttribute("disabled", "disabled");
    }
}

function generateQRCode() {
    const quantity = document.getElementById("quantity").innerText;
    //const amount = quantity * 10; // Assuming each unit costs 10

    fetch("/generate_qr", {  // Update the URL to the new Flask app's endpoint
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "quantity": quantity })
    })
    .then(response => response.json())
    .then(data => {
        const qrCodeImage = document.getElementById("qrCodeImage");
        qrCodeImage.src = "data:image/jpeg;base64," + data.qr_code;  // Assuming data.qr_code contains the base64 image
        document.getElementById("qrCodeContainer").style.display = "block";
        document.getElementById("quantity_div").style.display = "none";
        console.log("jabba gaya")
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
