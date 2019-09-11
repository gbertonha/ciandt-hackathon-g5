var readData = function(sensor) {
	var db = firebase.firestore();

	db.collection(sensor)
    .onSnapshot(function(querySnapshot) {
       
        querySnapshot.forEach(function(doc) {
        	document.getElementById(sensor).innerText = doc.data().value;
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
	try {
	  let app = firebase.app();
	  readData("sensor1");
	  readData("sensor2");
	  readData("sensor3");
	} catch (e) {
	  console.error(e);
	}

});