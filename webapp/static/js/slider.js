/**
 * Created by audi on 15.01.16.
 */
var range1 = document.getElementById("range1");
var range2 = document.getElementById("range2");

range1.addEventListener("input", function(e) {
    range2.value = 100 - (e.target.value);
}, false);
range2.addEventListener("input", function(e) {
    range1.value = 100 - (e.target.value);
}, false);


//alert(document.getElementById("name").id);


document.getElementById("r_name").innerHTML = document.getElementById("range1").value;
