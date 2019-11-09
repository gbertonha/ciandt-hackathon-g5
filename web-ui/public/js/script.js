/*global firebase, document */
/*jslint browser:true */
"use strict";

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
    var agreed_temperature = 25

    if (temperature > agreed_temperature) {
        document.body.style.backgroundColor = red_color;
    } else if (temperature < agreed_temperature) {
        document.body.style.backgroundColor = blue_color;
    } else {
        document.body.style.backgroundColor = green_color;
    }
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