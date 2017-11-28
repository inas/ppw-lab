<NOT LOGGED IN>
saat pertama kali membuka url lab 9, akan dicek apakah user sudah login atau belum. kalau sudah maka akan diarahkan ke halaman profil. kalau belum maka diarahkan ke halaman login.

di halaman login, user diminta untuk mengisi form. respon akan dikirim ke halaman url(r'^custom_auth/login/$', auth_login, name='auth_login') yang akan memanggil fungsi auth_login yang ada di dalam file .custom_auth.

dari username dan password yang diberi user, akan dilanjutkan ke csui_helper untuk meminta token dengan fungsi get_access_token. jika ternyata sso yang dimasukkan benar, maka akan lanjut ke fungsi selanjutnya. jika salah maka akan kembali ke halaman login

setelah mendapat token, jalankan fungsi verify_user di csui_helper untuk mendapatkan id num dan role user.

simpan di session: username, access token, kode identitas, dan role.

jika sudah maka akan kembali ke index.



<LOGGED IN>
Dari fungsi index sudah diketahui bahwa user berhasil login pada sesi saat itu, maka akan dijalankan fungsi profile.

<PROFILE>
verifikasi bahwa user memang sudah pernah login. Jika belum pernah login maka user akan diminta untuk login. jika benar pernah login, maka jalankan fungsi set_data_for_session yang akan menyimpan data kedalam session seperti: author, access_token, id, role, dan drones. Drones didapat dari api enterkomputer. Setelah itu load halaman profile.

di halaman profile ditampilkan username, npm, role mahasiswa yang ter logged in. ditampilkan juga daftar drones, soundcard, dan optical.

	<DRONES, SOUNDCARD, OPTICAL>
	data akan ditampilkan pada tab berbeda. data didapat dari halaman html pada folder tables. Masukkan tiap objek drone yang didapat dalam tabel. drone dapat dijadikan favorit.

		<favoritkan>
		jalankan fungsi add_session_drones dengan parameter drone id. jika drone belum tersimpan dalam session, maka akan ditambahkan. jika sudah disimpan sebelumnya, maka akan dicek semua daftar drones yang sudah disimpan pada session. jika ternyata id drone yang ingin difavoritkan tidak terdapat pada daftar, maka akan ditambahkan id tersebut, lalu disimpan kedalam daftar drones favorite di session. halaman akan diarahkan kembali ke profile.

		<hapus favorit>
		jalankan fungsi del_session_drones dengan parameter drone.id. id drone akan dihapus dari daftar drone yang disimpan dalam daftar favorite di session. halaman akan dikembalikan ke profile

		<reset favorite>
		akan dijalankan fungsi clear_session_drones. fungsi del request.session['drones'] dijalankan sehingga daftar drones yang difavoritkan kosong. halaman akan diarahkan kembali ke profile.

Di halaman profile terdapat link untuk masuk ke halaman cookies. jika diklik maka akan diarahkan ke fungsi cookie_login
	
	<COOKIE>
	saat pertama kali menjalankan fungsi cookie_login, berdasarkan fungsi def is_login(request):
    	return 'user_login' in request.COOKIES and 'user_password' in request.COOKIES
    akan dicek apakah user sudah login cookie atau belum. kalau sudah maka akan diarahkan ke halaman profil cookie. kalau belum maka diarahkan ke halaman login cookie.

	<NOT LOGGED IN COOKIE>

		di halaman login, user diminta untuk mengisi form SSO. JANGAN menggunakan sso asli karena akan disimpan dalam cookies. respon akan dikirim ke halaman url(r'^cookie/auth_login/$', cookie_auth_login, name='cookie_auth_login'), yang akan memanggil fungsi cookie_auth_login yang ada di dalam file .views

		dari username dan password yang diberi user, akan dilanjutkan ke fungsi my_cookie_auth untuk disesuaikan dengan username dan password yang ditentukan dalam source code. Jika sama maka pada halaman url(r'^cookie/login/$', cookie_login, name='cookie_login') akan disimpan cookie yang berisi user_login dan user_pasword.

		halaman dikembalikan ke url(r'^cookie/login/$', cookie_login, name='cookie_login'),

	<LOGGED IN>

		Jika sudah log in maka akan diarahkan ke fungsi cookie_profile. 

		verifikasi bahwa user memang sudah pernah login dengan fungsi is_login. is_login mengecek apakah user dan pass sudah pernah login sebelumnya atau tidak. Pada fungsi ini akan dijalanJika belum pernah login maka user akan diminta untuk login. jika benar pernah login, maka ambil kembali cookie user_login dan pass yang sudah disimpan lalu cek dengan my_cookie_auth. jika benar, maka load halaman profile. jika pass tidak sesuai, maka arahkan ke halaman login.

		<PROFILE>
		di halaman profile ditampilkan username yang disimpan di cookies untuk login. pada halaman profile terdapat pilihan untuk reset cookies pada url(r'^cookie/clear/$', cookie_clear, name='cookie_clear'). pada halaman cookie login akan dihapus username dan pass. halaman akan dikembalikan ke login.

