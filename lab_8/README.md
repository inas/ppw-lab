# FB initiation function

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

1. cek apakah user sudah login atau belum. render halaman.

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


2. Cek status login
	>>>Jika sudah login
		      // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
      // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
      // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
      // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
      getUserFeed(feed => {
        var counter = 0;
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
        console.log(counter);
        $("#get-status").append(
          counter
        );
      });