/**
 * Created by audi on 15.01.16.
 */
var range1 = document.getElementById("range1");
var range2 = document.getElementById("range2");
var charityText = document.getElementById("charity");
var contentText = document.getElementById("content");

function rang(r1, r2) {
    r1.addEventListener("input", function (w) {
        r1.value = (w.target.value);
        charityText.value = w.target.value;
    });
    r2.addEventListener("input", function (j) {
        r2.value = (j.target.value);
        contentText.value = j.target.value;
    });

}
rang(range1, range2);
//range2.addEventListener("input", function(e) {
//    range1.value = 100 - (e.target.value);
//    contentText.value = e.target.value;
//}, false);


function bind(el, type, handler) {
  if (el.addEventListener) {
    el.addEventListener(type, handler, false);
  } else {
    el.attachEvent('on' + type, handler);
  }
}


var btnGroup = document.querySelectorAll('.btn-default');
console.dir(btnGroup);
var resultInput = document.getElementById('amount');

function btnGroupHandle(e) {
  resultInput.value = e.target.value;
}

for (i = 0; i < btnGroup.length; i++) {
  var btn = btnGroup[i];
  bind(btn, 'click', btnGroupHandle);
}