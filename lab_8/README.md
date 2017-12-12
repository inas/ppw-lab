# FB initiation function

  merupakan function yang akan dijalankan pertamakali untuk menginisiasi api facebook.

	  FB.init({
	    appId      : '132368680796186',
	    cookie     : true,
	    xfbml      : true,
	    version    : 'v2.11'
	  });

	  // Call init facebook. default dari facebook
	(function(d, s, id){
	   var js, fjs = d.getElementsByTagName(s)[0];
	   if (d.getElementById(id)) {return;}
	   js = d.createElement(s); js.id = id;
	   js.src = "https://connect.facebook.net/en_US/sdk.js";
	   fjs.parentNode.insertBefore(js, fjs);
	 }(document, 'script', 'facebook-jssdk'));

# cek apakah user sudah login atau belum. render halaman.

	  FB.getLoginStatus(function(response) {
	    console.log(response);
	    if (response.status === 'connected') {
	      // the user is logged in and has authenticated your
	      // app, and response.authResponse supplies
	      // the user's ID, a valid access token, a signed
	      // request, and the time the access token 
	      // and signed request each expire
	      render(true);
	    } else if (response.status === 'not_authorized') {
	      // the user is logged in to Facebook, 
	      // but has not authenticated your app
	      render(false);
	    } else {
	      // the user isn't logged in to Facebook.
	      render(false);
	    }
	   });


# Cek status login
Jika sudah login maka akan menjalankan fungsi render dengan param true.	

## Belum login
Jika belum login maka akan dirender halaman yang mengharuskan user untuk login. Jika user mengklik button login, maka facebook akan melakukan autentikasi.

    FB.login(function(response) {
      if (response.authResponse) {
       console.log('Welcome!  Fetching your information.... ');
       FB.api('/me', function(response) {
         console.log('Good to see you, ' + response.name + '.');
         // render(true);
         location.reload();
       });
      } else {
       console.log('User cancelled login or did not fully authorize.');
      }
    }, {scope : 'public_profile,email,user_about_me,user_birthday,user_posts,publish_actions,user_friends'}, {auth_type : 'reauthenticate'}
    );

response.authResponse akan mengambil status login user. Jika berhasil login maka halaman akan di reload. Scope mendeskripsikan konten apa saja yang ingin diambil oleh user dari api.

## Sudah login

yang dilakukan oleh halaman adalah meload data user dan juga userfeed

    // Method ini memodifikasi method getUserData di atas yang menerima fungsi callback bernama fun
    // lalu merequest data user dari akun yang sedang login dengan semua fields yang dibutuhkan di 
    // method render, dan memanggil fungsi callback tersebut setelah selesai melakukan request dan 
    // meneruskan response yang didapat ke fungsi callback tersebut
    // Apakah yang dimaksud dengan fungsi callback?
    const getUserData = (fun) => {
      // ...
      FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
           FB.api('/me?fields=id,about,email,name,cover,picture,gender,birthday,location', 'GET', function(response) {
            console.log('API response', response);
            fun(response);
            }
          );
        }
      });

FB akan meminta response yang berisi status login. jika sudah benar terhubung maka akan diminta dari api FB id, email, dan data user lainnya yang akan disampaikan dalam respnse. setelah mendapatkan response maka akan dijalankan fungsi callback fun yang menjadi parameter fungsi. Fungsi fun tersebut ternyata akan meload halaman html yang menamilkan profile user. selain data profile, akan diminta juga feed user.

    const getUserFeed = (fun) => {
      // TODO: Implement Method Ini
      // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
      // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
      // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
      // tersebut
      FB.getLoginStatus(function(response) {
        if (response.status === 'connected') { 
          FB.api('/me/feed', 'GET', function(response) {
              console.log('API response', response);
              fun(response);
            }
        );
        }
      });
    };

fungsi callback fun akan membuat elemen untuk tiap data yang didapatkan.

     feed.data.map(value => {.............})


### Post status
terdapat form yang dapat mengsubmit isinya untuk dipost. saat tombol submit diklik maka akan dijalankan fungsi postStatus()

    const postStatus = () => {
      const message = $('#postInput').val();
      postFeed(message);
    };

    const postFeed = (textmessage) => {
      // Todo: Implement method ini,
      // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
      // Melalui API Facebook dengan message yang diterima dari parameter.

      FB.api('/me/feed', 'POST',  {"message": textmessage}, function(response)
      {
        console.log("test " + JSON.stringify(response));
       if (!response || response.error)
       {
         console.log(response.error);
         alert('Posting error occured');
       }else{
         alert('Success - Post ID: ' + response.id);
         location.reload();
       }
      });
          
    };

akan dijalankan protokol post yang akan menambahkan status. halaman akan direload agar perubahan dapat terlihat.