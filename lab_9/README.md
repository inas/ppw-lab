<NOT LOGGED IN>
saat pertama kali membuka url lab 9, akan dicek apakah user sudah login atau belum. kalau sudah maka akan diarahkan ke halaman profil. kalau belum maka diarahkan ke halaman login.

di halaman login, user diminta untuk mengisi form. respon akan dikirim ke halaman url(r'^custom_auth/login/$', auth_login, name='auth_login') yang akan memanggil fungsi auth_login yang ada di dalam file .custom_auth.

dari username dan password yang diberi user, akan dilanjutkan ke csui_helper untuk meminta token dengan fungsi get_access_token. jika ternyata sso yang dimasukkan benar, maka akan lanjut ke fungsi selanjutnya. jika salah maka akan kembali ke halaman login

setelah mendapat token, jalankan fungsi verify_user di csui_helper untuk mendapatkan id num dan role user.

simpan di session: username, access token, kode identitas, dan role.

jika sudah maka akan kembali ke halaman index.



<LOGGED IN>
Dari fungsi index sudah diketahui bahwa user berhasil login pada sesi saat itu, maka akan dijalankan fungsi profile.

<PROFILE>
verifikasi bahwa user memang sudah pernah login. Jika belum pernah login maka user akan diminta untuk login. jika benar pernah login, maka jalankan fungsi set_data_for_session yang akan menyimpan data kedalam session seperti: author, access_token, id, role, dan drones. Drones didapat dari api enterkomputer. Setelah itu load halaman profile.

di halaman profile ditampilkan username, npm, role mahasiswa yang ter logged in. ditampilkan juga daftar drones, soundcard, dan api.

data akan ditampilkan pada tab berbeda. data didapat dari halaman html pada folder tables. Masukkan tiap objek drone yang didapat dalam tabel. drone dapat dijadikan favorit.

	<favoritkan>
	jalankan fungsi add_session_drones dengan parameter drone id. jika drone belum tersimpan dalam session, maka akan ditambahkan. jika sudah disimpan sebelumnya, maka akan dicek semua daftar drones yang sudah disimpan pada session. jika ternyata id drone yang ingin difavoritkan tidak terdapat pada daftar, maka akan ditambahkan id tersebut, lalu disimpan kedalam daftar drones favorite di session. halaman akan diarahkan kembali ke profile.

	<hapus favorit>
	jalankan fungsi del_session_drones dengan parameter drone.id. id drone akan dihapus dari daftar drone yang disimpan dalam daftar favorite di session. halaman akan dikembalikan ke profile

pada halaman profile terdapat pilihan untuk mereset favorite drone

	<reset favorite>
