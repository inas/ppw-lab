// FB initiation function
window.fbAsyncInit = () => {
  FB.init({
    appId      : '132368680796186',
    cookie     : true,
    xfbml      : true,
    version    : 'v2.11'
  });

  // implementasilah sebuah fungsi yang melakukan cek status login (getLoginStatus)
  // dan jalankanlah fungsi render di bawah, dengan parameter true jika
  // status login terkoneksi (connected)

  // Hal ini dilakukan agar ketika web dibuka dan ternyata sudah login, maka secara
  // otomatis akan ditampilkan view sudah login
};

// Call init facebook. default dari facebook
(function(d, s, id){
   var js, fjs = d.getElementsByTagName(s)[0];
   if (d.getElementById(id)) {return;}
   js = d.createElement(s); js.id = id;
   js.src = "https://connect.facebook.net/en_US/sdk.js";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));

// Fungsi Render, menerima parameter loginFlag yang menentukan apakah harus
// merender atau membuat tampilan html untuk yang sudah login atau belum
// Ubah metode ini seperlunya jika kalian perlu mengganti tampilan dengan memberi
// Class-Class Bootstrap atau CSS yang anda implementasi sendiri
const render = loginFlag => {
  if (loginFlag) {
    // Jika yang akan dirender adalah tampilan sudah login

    // Memanggil method getUserData (lihat ke bawah) yang Anda implementasi dengan fungsi callback
    // yang menerima object user sebagai parameter.
    // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
    getUserData(user => {
      // Render tampilan profil, form input post, tombol post status, dan tombol logout
      $('#lab8').html(
        '<div class="profile">' +
          '<img class="cover" src="' + user.cover.source + '" alt="cover" />' +
          '<img class="picture" src="' + user.picture.data.url + '" alt="profpic" />' +
          '<div class="data">' +
            '<h1>' + user.name + '</h1>' +
            '<h2>' + user.about + '</h2>' +
            '<h3>' + user.email + ' - ' + user.gender + '</h3>' +
          '</div>' +
        '</div>' +
        '<input id="postInput" type="text" class="post" placeholder="Ketik Status Anda" />' +
        '<button class="postStatus" onclick="postStatus()">Post ke Facebook</button>' +
        '<button class="logout" onclick="facebookLogout()">Logout</button>'
      );

      // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
      // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
      // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
      // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
      getUserFeed(feed => {
        feed.data.map(value => {
          // Render feed, kustomisasi sesuai kebutuhan.
          if (value.message && value.story) {
            $('#lab8').append(
              '<div class="feed">' +
                '<h1>' + value.message + '</h1>' +
                '<h2>' + value.story + '</h2>' +
              '</div>'
            );
          } else if (value.message) {
            $('#lab8').append(
              '<div class="feed">' +
                '<h1>' + value.message + '</h1>' +
              '</div>'
            );
          } else if (value.story) {
            $('#lab8').append(
              '<div class="feed">' +
                '<h2>' + value.story + '</h2>' +
              '</div>'
            );
          }
        });
      });
    });
  } else {
    // Tampilan ketika belum login
    alert("wy")
    $('#lab8').html('<button class="login" onclick="facebookLogin()">Login</button>');
  }
};

const facebookLogin = () => {
  // TODO: Implement Method Ini
  // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
  // ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
  // pada scope yang ada. Anda dapat memodifikasi fungsi facebookLogin di atas.
};

const facebookLogout = () => {
  // TODO: Implement Method Ini
  // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
  // ketika logout sukses. Anda dapat memodifikasi fungsi facebookLogout di atas.
};

// TODO: Lengkapi Method Ini
// Method ini memodifikasi method getUserData di atas yang menerima fungsi callback bernama fun
// lalu merequest data user dari akun yang sedang login dengan semua fields yang dibutuhkan di 
// method render, dan memanggil fungsi callback tersebut setelah selesai melakukan request dan 
// meneruskan response yang didapat ke fungsi callback tersebut
// Apakah yang dimaksud dengan fungsi callback?
const getUserData = (fun) => {
  ...
  FB.api('/me?fields=....', 'GET', function (response){
    fun(response);
  });
  ...
};

const getUserFeed = (fun) => {
  // TODO: Implement Method Ini
  // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
  // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
  // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
  // tersebut
};

const postFeed = () => {
  // Todo: Implement method ini,
  // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
  // Melalui API Facebook dengan message yang diterima dari parameter.
};

const postStatus = () => {
  const message = $('#postInput').val();
  postFeed(message);
};
