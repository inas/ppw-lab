const resizeImage = () => {
  console.log('resizing image...');
  console.log($('.image-banner').height());
  console.log($('.image-profile').height());
  $(".image-profile").height($('.image-banner').height() - $(".stats-bar").height() ); 
  $(".image-profile").width($('.image-banner').height() - $(".stats-bar").height() );
}

const modalFunction = () => {
  // Get the modal
  var modal = document.getElementById('myModal');

  // Get the button that opens the modal
  var btn = document.getElementById("modalBtn");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal 
  btn.onclick = function() {
      modal.style.display = "block";
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
      modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }

}

const getInfo = () => {
  FB.api('/me/friends', 'GET', {fields: 'summary'}, function(response)
  {
  document.getElementById('get-friends').innerHTML = 
  response.summary.total_count;
  });
}

const loadFeed = () => {
  console.log("jalankan");
  var counter;
  feed.data.map(value => {
    // Render feed, kustomisasi sesuai kebutuhan.
    
    if (value.message && value.story) {
      $('#timeline').append(
        '<div class="feed">' +
          '<div id="pp"> ' + 
            '<img class="picture" src="'   + user.picture.data.url + '" alt="profpic" />'+
          '</div>' +
          '<div class="fb-status">' +
            '<p id="id-status">' + user.name + '</p>' +
            '<p>' + value.message + '</p>' +
            '<p>' + value.story + '</p>' +
          '</div>' +
          '<div class="delete">' +
            '<img class="picture" onclick="deleteStatus(\''+ value.id + '\')" src="https://cdn4.iconfinder.com/data/icons/devine_icons/Black/PNG/Folder%20and%20Places/Trash-Recyclebin-Empty-Closed.png" alt="delete" />' +
          '</div>' +
        '</div>'
      );
    } else if (value.message) {
      $('#timeline').append(
          '<div class="feed">' +
            '<div id="pp"> ' + 
              '<img class="picture" src="'   + user.picture.data.url + '" alt="profpic" />'+
            '</div>' +
            '<div class="fb-status">' +
              '<p id="id-status">' + user.name + '</p>' +
              '<p>' + value.message + '</p>' +
            '</div>' +
            '<div class="delete">' +
              '<img onclick="deleteStatus(\''+ value.id + '\')" class="picture" src="https://cdn4.iconfinder.com/data/icons/devine_icons/Black/PNG/Folder%20and%20Places/Trash-Recyclebin-Empty-Closed.png" alt="delete" />' +
            '</div>' +
          '</div>'
      );
    } else if (value.story) {
      $('#timeline').append(
          '<div class="feed">' +
            '<div id="pp"> ' + 
              '<img onclick="deleteStatus(\''+ value.id + '\')" class="picture" src="'   + user.picture.data.url + '" alt="profpic" />'+
            '</div>' +
            '<div class="fb-status">' +
              '<p id="id-status">' + user.name + '</p>' +
              '<p>' + value.story + '</p>' +
            '</div>' +
            '<div class="delete">' +
              '<img class="picture" src="https://cdn4.iconfinder.com/data/icons/devine_icons/Black/PNG/Folder%20and%20Places/Trash-Recyclebin-Empty-Closed.png" alt="delete" />' +
            '</div>' +
          '</div>'
      );
      
    }
    counter+=1;
  });
  return counter;
}

$(document).ready(() => {
  resizeImage();

})
      
$(window).resize(function(){ // On resize
  resizeImage();  
});

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
const render = (loginFlag) => {
  if (loginFlag) {
    // Jika yang akan dirender adalah tampilan sudah login

    // Memanggil method getUserData (lihat ke bawah) yang Anda implementasi dengan fungsi callback
    // yang menerima object user sebagai parameter.
    // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
    getUserData(user => {
      $("#profile").load("profile", () => {
        resizeImage(); 
        modalFunction();
        $(".image-profile").append(
          '<img class="object-fit_cover" src="' + user.picture.data.url + '"/>'
        );
        $("#username").append(
            user.name
          );
        getInfo();
        $(".nav-container").append(
            '<button id="logoutBtn" onclick="facebookLogout()">'+
              'log out'+
            '</button>'
          );
        $(".image-banner").css("background-image", "url( '" + user.cover.source + "')");
      });

      // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
      // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
      // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
      // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
      getUserFeed(feed => {
        var counter = loadFeed();
        console.log(counter);
        
        $("#get-birth").append(
          counter
        );
      });
    });
  } else {
    // Tampilan ketika belum login
    $('#lab8').html(
      '<p>ready for it...?</p>' +
      '<div id="login-btn">' +
        '<button type="button" class="btn btn-primary btn-lg btn-block" onclick="facebookLogin()">Login with Facebook</button>' +
      '</div>'
      );
  }
};

const facebookLogin = () => {
  // TODO: Implement Method Ini
  // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
  // ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
  // pada scope yang ada. Anda dapat memodifikasi fungsi facebookLogin di atas.
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
  }, {scope : 'public_profile,email,user_about_me,user_birthday,user_posts,publish_actions,user_friends'},
      {auth_type : 'reauthenticate'}
);
};

const facebookLogout = () => {
  // TODO: Implement Method Ini
  // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
  // ketika logout sukses. Anda dapat memodifikasi fungsi facebookLogout di atas.
  FB.logout(function(response) {
    render(false);
    location.reload();
  // user is now logged out
  });
};

// TODO: Lengkapi Method Ini
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



};

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

const postStatus = () => {
  const message = $('#postInput').val();
  postFeed(message);
};
  
const deleteStatus = (id) => {
  var postId = id;
  FB.api(postId, 'delete', function(response) {
    if (!response || response.error) {
      alert('Error occured');
    } else {
      alert('post deleted')
      location.reload();
    }
  });
}
