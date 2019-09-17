/**
 * Reads data from Firestore and updates information
 * displayed on the dashboard
 * @param {String} sensor The sensor key.
 */
var readData = function(sensor) {
  var db = firebase.firestore();
  db.collection(sensor)
    .onSnapshot(function(querySnapshot) {
    querySnapshot.forEach(function(doc) {
      document.getElementById(sensor).innerText = doc.data().value;
    });
  });
}

/**
 * Triggered once DOM is loaded.
 */
document.addEventListener('DOMContentLoaded', function() {
  try {
  	let app = firebase.app();
  	let sensors = ["sensor1", "sensor2", "sensor3"];
  	sensors.forEach(function(sensor) {
  	  readData(sensor);
  	});
  } catch (e) {
	  console.error(e);
  }
});