saat halaman pertama dibuka, maka akan dijalankan fungsi index yang akan merender html.

	def index(request):
		html = 'lab_6/lab_6.html'
		return render(request, html, response)

pada html terdapat 3 bagian fitur yaitu kalkulator, ganti tema, dan chat.

//Kalkulator
pada bagian html, kalkulator dibentuk dari button-button yang akan menjalankan fungsi bernama go() yang menerima parameter sesuai dengan button yang diklik. Fugsi yang terdapat pada file lab_6.js akan dijalankan ketika user mengklik button tersebut. 

pada js terdapat variable elemen ber id print pada web akan menampilkan konten sesuai fungsi yang dijalankan. Jika user memencet tombol '=' maka akan dijalankan fungsi evil yang menerima parameter value dari elemen print

#----------------------------- Calculator-------------------------
	
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

///////////////////////FUNGSI EVIL??? ERASE TERUS KENAPA???

#----------------------------Chat-------------------------------------
User dapat mengetik konten chat pada text area. Jika user mengklik enter <e.keycode == 13> maka akan diappend value dari text area menjadi text bubble

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


pada chat box terdapat oggle untuk meng-hide chat box yang menggunakan jquery

//Chat-box
	
	$(document).ready(function(){
	    $(".chat-head").click(function(){
	        $(".chat-body").toggle();
	    });
	});

#-------------------------------- theme -------------------------------
Pertama, buat elemen select

    <select class="my-select"></select>

    <button class="apply-button">apply</button>


kemudian lakukan inisiasi select2 dengan
	
	$(document).ready(function() {
	    $('.my-select').select2();
	});


Lakukan inisiasi dataJSON di local storage. Buat list of dictionaries yang disimpan dalam variable themes. tiap elemen list menyimpan properties untuk tema.

	var themes = [
	    {"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#FAFAFA"},
	    {"id":1,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
	]

Saat pertamakali membuka halaman maka simpan data tema dan tema yang dipilih dalam local storage dengan cara

	if (localStorage.getItem('themes') === null){ 
	  localStorage.setItem('themes', JSON.stringify(themes)); 
	}

	var themes = JSON.parse(localStorage.getItem('themes'));

	if (localStorage.getItem('selectedTheme') === null) { 
	  localStorage.setItem('selectedTheme', JSON.stringify(themes[3])); 
	}

JSON.stringify turns a Javascript object into JSON text and stores that JSON text in a string.

JSON.parse turns a string of JSON text into a Javascript object.

untuk pertama kali jika di local storage belum ada apa-apa maka, maka gunakan tema id ketiga.

	function changeTheme(newTheme){
	  $('body').css({"backgroundColor": newTheme['bcgColor']});
	  $('.text-center').css({"color": newTheme['fontColor']});
	}

User dapat mengganti tema dengan cara mengklik button submit.

	$(document).ready(function() {
	  $('.my-select').select2({'data' : themes});
	  $('.apply-button').on('click', function(){
	    theme = themes[$('.my-select').val()];
	    changeTheme(theme);
	    localStorage.setItem('selectedTheme',JSON.stringify(theme));
	  })
	});

