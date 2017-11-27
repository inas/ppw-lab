[![pipeline status](https://gitlab.com/anishainas/ppw-lab/badges/master/pipeline.svg)](https://gitlab.com/anishainas/ppw-lab/commits/master)
[![coverage report](https://gitlab.com/anishainas/ppw-lab/badges/master/coverage.svg)](https://gitlab.com/anishainas/ppw-lab/commits/master)

## Checklist

### Mandatory
1. Membuat halaman untuk menampilkan semua mahasiswa fasilkom
    1. [v] Terdapat list yang berisi daftar mahasiswa fasilkom, yang dipanggil dari django model.
    buat objek csui_helper. isinya pi dari csui. bakal ngambil password dari file .env. jangan lupa diignore. disitu bakal login macem-macem deh. ke api kita akan minta semua daftar mahasiswa melalui method yang kemudian akan dipaginate terlebih dahulu.
    
    2. [v] Buatlah tombol untuk dapat menambahkan list mahasiswa kedalam daftar teman (implementasikan menggunakan ajax).
    nanti kalau tombol dipencet bakal pass ke function add-friend. liat dulu apakah udah pernah ada npm yang sama di friend. nanti tambahin friendnya ke object.

    3. [v] Mengimplentasikan validate_npm untuk mengecek apakah teman yang ingin dimasukkan sudah ada didalam daftar teman atau belum.
    kalau ada perubahan di textbox nanti jalanan fungsi cek npm. kalo misal emang udah ada nanti akan muncul alert.

    4. [v] Membuat pagination (hint: salah satu data yang didapat dari kembalian api.cs.ui.ac.id adalah `next` dan `previous` yang bisa digunakan dalam membuat pagination)
    ada di dokumentasi django. nanti list mahasiswa bakal dibagi jadi beberapa halaman sesuai yang kita  inginkan misal "paginator = Paginator(data_list, 20)". hitung start index dan last index untuk menentukan halaman yang dipaginate.

2. Membuat halaman untuk menampilkan daftar teman
    1. [v] Terdapat list yang berisi daftar teman, data daftar teman didapat menggunakan ajax.
    jalanin fungsi get friend list abis itu nanti bikin htmlnya. akan dipanggil function untuk mendapatkan objects di model Friend. untuk setiap objek di Friend akan dibuat div nya sehingga muncul di halaman friend-list

    2. [v] Buatlah tombol untuk dapat menghapus teman dari daftar teman (implementasikan menggunakan ajax).
    kalau tombol dipencet nanti jalanin fungsi delete friend. akan meng-pass parameter berupa id yang sudah ditentukan sejak membuat div friend di halaman daftar-teman

3. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [v] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab` di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md)
    2. [v] Pastikan _Code Coverage_ kalian 100%


### Additional

1. Membuat halaman yang menampilkan data lengkap teman 
    1. [ ] Halaman dibuka setiap kali user mengklik salah satu teman pada halaman yang menampilkan daftar teman
    1. [ ] Tambahkan google maps yang menampilkan alamat teman pada halaman informasi detail (hint: https://developers.google.com/maps/documentation/javascript/)
1. Berkas ".env" untuk menyimpan username dan password, dapat menyebabkan akun anda terbuka untuk orang yang memiliki 
   akses ke repository bila berkas tersebut ter-push ke repository.
   Hal ini sangat tidak baik dan bisa memalukan karena dapat membuka rahasia/privacy anda sendiri.
    1. [v] Pastikan kerahasiaan dan privacy anda. Ubah mekanisme penyimpanan dan pengambilan bila diperlukan. 