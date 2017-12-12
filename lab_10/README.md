# Index

	def index(request):
	    if 'user_login' in request.session:
	        response['login'] = True
	        return HttpResponseRedirect(reverse('lab-10:dashboard'))
	    else:
	        response['login'] = False
	        response['author'] = get_data_user(request, 'user_login')
	        html = 'lab_10/login.html'
	        return render(request, html, response)

cek apakah user sudah login dalam session tersebut. jika sudah, maka arahkan ke dashboard. jika belum, maka buka halaman login.

## Halaman login
	
	<div id="login-form">
		<form class="form" action="{% url 'lab-10:auth_login' %}" method="POST">
			{% csrf_token %}
	        <input type="text" class="zocial-dribbble" placeholder="Enter your username" id="username" name="username" required/>
	        <input type="password" placeholder="Password" id="password" name="password" required/>
	        <input type="submit" value="Login with SSO" />
        </form> 
	</div> 

saat disubmit maka request akan dipost ke auth_login. 

	def auth_login(request):
	    print ("#==> auth_login ")

	    if request.method == "POST":
	    	# mengambil data dari form
	        username = request.POST['username']
	        password = request.POST['password']
	        
	        #call csui_helper
	        access_token = get_access_token(username, password)
	        if access_token is not None:
	            ver_user = verify_user(access_token)
	            kode_identitas = ver_user['identity_number']
	            role = ver_user['role']

	            # set session
	            request.session['user_login'] = username
	            request.session['access_token'] = access_token
	            request.session['kode_identitas'] = kode_identitas
	            request.session['role'] = role
	            messages.success(request, "Anda berhasil login")
	        else:
	            messages.error(request, "Username atau password salah")
	    return HttpResponseRedirect(reverse('lab-10:index'))

jika sudah berhasil login, maka diarahkan ke dashboard

## Halaman dashboard
pada halaman ini dilihatkan username, npm, dan role mahasiswa yang didapat dari session. pada halaman ini juga terdapat menu untuk melihat daftar movie dan watch later.

### Movie list

	### MOVIE : LIST and DETAIL
	def movie_list(request):
	    if 'user_login' in request.session.keys():
	        response['login'] = True
	    else:
	        response['login'] = False
	    judul, tahun = get_parameter_request(request)

	    //APA INI???
	    urlDataTables = "/lab-10/api/movie/" + judul + "/" + tahun + "/"
	    jsonUrlDT = json.dumps(urlDataTables)
	    response['jsonUrlDT'] = jsonUrlDT
	    response['judul'] = judul
	    response['tahun'] = tahun

	    get_data_session(request)

	    html = 'lab_10/movie/list.html'
	    return render(request, html, response)

di bagian movie list terdapat table yang datanya diload dari datatable. saat usr mengklik button pencarian, maka akan dijalankan fungsi untuk mendapatkan url list movie yang sesuai. jquery datatables kemudian akan berjalan. dan mengisi table secara otomatis.

terdapat opsi details pada tiap movie yang akan diakses berdasarkan id movies

#### Details
Jika user sudah login maka akan dicek apakah sudah ditambahkan ke watch later dari database, sedangkan jika tidak login maka akan dicek dari session. 

	def movie_detail(request, id):
	    print ("MOVIE DETAIL = ", id)
	    response['id'] = id
	    if get_data_user(request, 'user_login'):
	        response['login'] = True
	        is_added = check_movie_in_database(request, id)
	    else:
	        response['login'] = False
	        is_added = check_movie_in_session(request, id)

	    response['added'] = is_added
	    response['movie'] = get_detail_movie(id)
	    html = 'lab_10/movie/detail.html'
	    return render(request, html, response)

Pada details terdapat opsi untuk memasukkan movie ke watch later


	### WATCH LATER : ADD and LIST
	def add_watch_later(request, id):
	    print ("ADD WL => ", id)
	    msg = "Berhasil tambah movie ke Watch Later"
	    if get_data_user(request, 'user_login'):
	        print ("TO DB")
	        is_in_db = check_movie_in_database(request, id)
	        if not is_in_db:
	            add_item_to_database(request, id)
	        else:
	            msg = "Movie already exist on DATABASE! Hacking detected!"
	    else:
	        print ("TO SESSION")
	        is_in_ssn = check_movie_in_session(request, id)
	        if not is_in_ssn:
	            add_item_to_session(request, id)
	        else:
	            msg = "Movie already exist on SESSION! Hacking detected!"

	    messages.success(request, msg)
	    return HttpResponseRedirect(reverse('lab-10:movie_detail', args=(id,)))

dicek apakah terdapat percobaan untuk mengakses data secara manual


### Watch later list

	def list_watch_later(request):
	    #  Implement this function by yourself
	    get_data_session(request)
	    moviesku = []
	    if get_data_user(request, 'user_login'):
	        response['login'] = True
	        moviesku = get_my_movies_from_database(request)
	    else:
	        response['login'] = False
	        moviesku = get_my_movies_from_session(request)

	    watch_later_movies = get_list_movie_from_api(moviesku)

	    response['watch_later_movies'] = watch_later_movies
	    html = 'lab_10/movie/watch_later.html'
	    return render(request, html, response)

Mengambil data watch later dari database atau session.