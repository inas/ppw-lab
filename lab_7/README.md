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



# Login SSO
buat objek CSUIhelper(). untuk menggunakan api csui, user harus login dulu. username dan password diambil dengan cara
    
    root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
    env = environ.Env(DEBUG=(bool, False),)
    environ.Env.read_env(env_file=root('sso.env'))
    API_MAHASISWA_LIST_URL = "https://api.cs.ui.ac.id/siakngcs/mahasiswa-list/"


    class CSUIhelper:
        class __CSUIhelper:

            // fungsi ini mengambil value yang disimpan dalam env kemudian merequest token.
            def __init__(self):
                self.username = env("SSO_USERNAME")
                self.password = env("SSO_PASSWORD")
                self.client_id = 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG'
                self.access_token = self.get_access_token(self.username,self.password)

            // fungsi ini merequest token dari api.
            def get_access_token(self, username, password):
                try:
                    url = "https://akun.cs.ui.ac.id/oauth/token/"

                    payload = "username=" + username + "&password=" + password + "&grant_type=password"
                    headers = {
                        'authorization': "Basic WDN6TmtGbWVwa2RBNDdBU05NRFpSWDNaOWdxU1UxTHd5d3U1V2VwRzpCRVFXQW43RDl6a2k3NEZ0bkNpWVhIRk50Ymg3eXlNWmFuNnlvMU1uaUdSVWNGWnhkQnBobUU5TUxuVHZiTTEzM1dsUnBwTHJoTXBkYktqTjBxcU9OaHlTNGl2Z0doczB0OVhlQ3M0Ym1JeUJLMldwbnZYTXE4VU5yTEFEMDNZeA==",
                        'cache-control': "no-cache",
                        'content-type': "application/x-www-form-urlencoded"
                    }

                    response = requests.request("POST", url, data=payload, headers=headers)

                    return response.json()["access_token"]
                except Exception:
                    raise Exception("username atau password sso salah, input : [{}, {}] {}".format(username, password, os.environ.items()))

            def get_client_id(self):
                return self.client_id

            // memasukkan access token dan clientid ke dalam dict
            def get_auth_param_dict(self):
                dict = {}
                acces_token = self.get_access_token(self.username,self.password)
                client_id = self.get_client_id()
                dict['access_token'] = acces_token
                dict['client_id'] = client_id

                return dict

            // melakukan requet untuk mendapatkan dat amahasiswa, lalu mngubah response menjadi JSON. mahasiswa_list mengambil results.
            def get_mahasiswa_list(self):
                response = requests.get(API_MAHASISWA_LIST_URL,
                                        params={"access_token": self.access_token, "client_id": self.client_id})
                mahasiswa_list = response.json()["results"]
                return mahasiswa_list

        instance = None

        def __init__(self):
            if not CSUIhelper.instance:
                CSUIhelper.instance = CSUIhelper.__CSUIhelper()

# fungsi index
yang dilakukan pada index adalah:
1. meminta list mahasiswa dari api. >>> mahasiswa_list = csui_helper.instance.get_mahasiswa_list()
2. mengambil semua object di models >>> friend_list = Friend.objects.all()
3. meminta akses token >>>     auth = csui_helper.instance.get_auth_param_dict()
4. "Get the value of a GET variable with name 'page', and if it doesn't exist, return 1".  >>>     page = request.GET.get('page',1)
5. fungsi paginator >>>  paginate_data = paginate_page(page, mahasiswa_list)

    def paginate_page(page, data_list):
        paginator = Paginator(data_list, 20) // param data_list: queryset/list, per page
        try:
            data = paginator.page(page) 
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

         # Get the index of the current page
        index = data.number - 1

         # This value is maximum index of pages, so the last page - 1
        max_index = len(paginator.page_range)

         # calculate where to slice the list
        start_index = index if index >= 10 else 0
        end_index = 10 if index < max_index - 10 else max_index

        page_range = list(paginator.page_range)[start_index:end_index]
        paginate_data = {'data':data, 'page_range':page_range}
        return paginate_data
        

6. ambil objek list mahasiswa yang sudah dipaginate >>> mahasiswa = paginate_data['data']

7. render


// QUESTION: kenapa cuma 100 mahasiswa yang ditampilin? gimana kalo maunya nampilin mahasiswa dalam satu halaman aja?


# html
1. Untuk setiap objek di mahasiswa_list bakal dibikin elemen beserta button add friend. button akan menjalankan method ajax yang menerima parameter nama dan npm. param akan dipass ke data. Request akan dikirim ke '{% url "lab-7:add-friend" %}'. 

    def add_friend(request):
        if request.method == 'POST':
            name = request.POST['name']
            npm = request.POST['npm']
            taken = Friend.objects.filter(npm=npm).exists()
            if (not taken):
                friend = Friend(friend_name=name,npm=npm)
                friend.save()
            data = model_to_dict(friend)
            return HttpResponse(data)

fungsi add mengambil name dan npm dari data yang dikirim. cek apakah ada objek dengan npm sama. jika tidak ada maka buat objek friend, simpan ke databse

2. atur pagination

    <div class="pagination">
        <span class="step-links">
            {% if mahasiswa_list.has_previous %}
                <a href="?page={{ mahasiswa_list.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ mahasiswa_list.number }} of {{ mahasiswa_list.paginator.num_pages }}
            </span>

            {% if mahasiswa_list.has_next %}
                <a href="?page={{ mahasiswa_list.next_page_number }}">next</a>
            {% endif %}
        </span>
    </div>

3. untuk friend_list, ambil tiap objek friend lalu buat elemen.