/*global firebase, document */
/*jslint browser:true */
"use strict";
const agreed_temperature = 25

/**
 * Reads data from Firestore and updates information
 * displayed on the dashboard
 * @param {String} sensor The sensor key.
 */
function readData(sensor) {
    var db = firebase.firestore();
    db.collection(sensor)
        .onSnapshot(function (querySnapshot) {
            querySnapshot.forEach(function (doc) {

                /* Get the temperature value */
                var temperature = doc.data().value;
                document.getElementById(sensor).innerText = temperature;
                changeBackgroundColor(temperature)

                // document.getElementById(sensor).innerText = doc.data().value;
                var today = new Date();
                var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
                var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
                var dateTime = date + ' ' + time;
                document.getElementById("last-update").innerText = dateTime;

                /* Display  the message */
                var message = displayMessage(temperature);
                document.getElementById("message").innerText = message;
            });
        });
}

/**
 * This function is for changing the screen colors
 * when the temperature increases of decreases!
 */
function changeBackgroundColor(temperature) {
    /* Change the screen colors */
    var red_color = "#ff6666", blue_color = "#66a3ff", green_color = "#66ff66";

    if (temperature > agreed_temperature) {
        document.body.style.backgroundColor = red_color;
    } else if (temperature < agreed_temperature) {
        document.body.style.backgroundColor = blue_color;
    } else {
        document.body.style.backgroundColor = green_color;
    }
}

/**
 * This function is for displaying  the message
 * when the temperature increases of decreases!
 */
function displayMessage(temperature) {
// Retrieve Firebase Messaging object.
    const messaging = firebase.messaging();
    var message_over = "Current temperature is over the agreed temperature. Please lower it.";
    var message_under = "Current temperature is under the agreed temperature. Please raise it.";

    return (temperature > agreed_temperature)? message_over  : message_under;
    //return (temperature > agreed_temperature)? console.log(message_over)  : console.log(message_under);
}




/**
 * Triggered once DOM is loaded.
 */
document.addEventListener('DOMContentLoaded', function () {
    try {
        var sensors = ["temperature"];

        // var sensors = ["temperature", "humidity", "pressure"];
        sensors.forEach(function (sensor) {
            readData(sensor);
        });
    } catch (e) {
        console.error(e);
    }
});

