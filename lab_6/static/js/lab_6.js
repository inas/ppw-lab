 //chat box
 var text = document.getElementById('chat-text');
 var send = true;

$('textarea').keyup(function(e) {
  if(e.keyCode == 13) {
    if (send){
      $(".msg-insert").append('<div class = "msg-send">'+ text.value + '</div>')
      send = false;
    }
    else{
      $(".msg-insert").append('<div class = "msg-receive">'+ text.value + '</div>')
      send = true;
    }
    text.value = "";
  }
});

//Chat-box
$(document).ready(function(){
    $(".chat-head").click(function(){
        $(".chat-body").toggle();
    });
});


// Calculator
var print = document.getElementById('print');
var erase = false;

function go(x) {
  if (x === 'ac') {
    print.value = '';
    erase = true;
  } else if (x === 'eval') {
    print.value = Math.round(evil(print.value) * 10000) / 10000;
    erase = true;
  }else if (x === 'sin'){
    print.value = Math.sin(print.value);
  } else if (x === 'log'){
  print.value = Math.log(print.value) / Math.log(10);  
  } else if (x === 'tan'){
    print.value = Math.tan(print.value);
  } else {
    print.value += x;
  }
};


function evil(fn) {
  return new Function('return ' + fn)();
}
// END


// ----------------- theme ---------------------

var themes = [
    {"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#FAFAFA"},
    {"id":1,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
    {"id":2,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#FAFAFA"},
    {"id":3,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"},
    {"id":4,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
    {"id":5,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
    {"id":6,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
    {"id":7,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
    {"id":8,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
    {"id":9,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
    {"id":10,"text":"Brown","bcgColor":"#795548","fontColor":"#FAFAFA"}
]

$(document).ready(function() {
  $('.my-select').select2({'data' : themes});
  $('.apply-button').on('click', function(){
    theme = themes[$('.my-select').val()];
    changeTheme(theme);
    localStorage.setItem('selectedTheme',JSON.stringify(theme));
  })
});

function changeTheme(newTheme){
  $('body').css({"backgroundColor": newTheme['bcgColor']});
  $('.text-center').css({"color": newTheme['fontColor']});
}

if (localStorage.getItem('themes') === null){ 
  localStorage.setItem('themes', JSON.stringify(themes)); 
}

var themes = JSON.parse(localStorage.getItem('themes'));

if (localStorage.getItem('selectedTheme') === null) { 
  localStorage.setItem('selectedTheme', JSON.stringify(themes[3])); 
}

var theme = JSON.parse(localStorage.getItem('selectedTheme'));
changeTheme(theme);

