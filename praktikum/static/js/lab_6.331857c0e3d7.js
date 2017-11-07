// Calculator
var print = document.getElementById('print');
var erase = false;

var go = function(x) {
  if (x === 'ac') {
    print.value = '';
    erase = true;
  } else if (x === 'eval') {
    print.value = Math.round(evil(print.value) * 10000) / 10000;
    erase = true;
  } else if (x === 'sin'){
    print.value = Math.sin(print.value);
  } else if (x === 'log'){
  print.value = Math.log(print.value) / Math.log(10);  
  } else if (x === 'tan'){
    print.value = Math.tan(print.value);
  }else {
    print.value += x;
  }
};

function evil(fn) {
  return new Function('return ' + fn)();
}
// END
