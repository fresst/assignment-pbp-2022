## Tautan Aplikasi Heroku
[https://assignment-pbp-2022.herokuapp.com/mywatchlist/](https://assignment-pbp-2022.herokuapp.com/mywatchlist/)<br>
[https://assignment-pbp-2022.herokuapp.com/mywatchlist/html/](https://assignment-pbp-2022.herokuapp.com/mywatchlist/html/)<br>
[https://assignment-pbp-2022.herokuapp.com/mywatchlist/xml/](https://assignment-pbp-2022.herokuapp.com/mywatchlist/xml/)<br>
[https://assignment-pbp-2022.herokuapp.com/mywatchlist/json/](https://assignment-pbp-2022.herokuapp.com/mywatchlist/json/)

## Jawaban Pertanyaan
1. - HTML didesain terutama untuk ditampilkan di web browser, sedangkan XML dan JSON digunakan untuk menyimpan dan mentransfer data
   - Data yang disimpan di JSON berbentuk pasangan *key*/nama dan *value*, sedangkan data yang disimpan di XML berupa *value* dibungkus di dalam *tag* yang berisi *key*
   - Dokumen XML harus memiliki *root element* (klasifikasi tertinggi), sedangkan JSON dan HTML tidak harus memiliki *root element*
   - JSON relatif lebih mudah digunakan daripada XML

2. *Data delivery* penting karena data yang dibuat manusia perlu diproses oleh mesin. Tiap proses memerlukan jenis data yang berbeda.
   Misalnya, HTTP meminta sebuah *page* HTML, maka mesin akan memproses file yang ditulis dalam **HTML**. Misalnya (lagi), HTTP meminta *request* data,
   maka data akan mengembalikan file XML atau JSON. Di sinilah pentingnya peran *data delivery*.
   

3. - Membuat aplikasi django, **mywatchlist**, dengan perintah `python manage.py startapp mywatchlist` di *directory* tugas pbp. 
     Kemudian, tambahkan nama aplikasi tadi ke dalam variabel `INSTALLED_APPS` di file `settings.py` yang berada di *directory* `project-django`.
   - Melakukan *routing* di berkas `urls.py` dan menambahkan *script* sesuai yang ada di Lab 1 PBP (tentunya dengan menyesuaikan `app_name` dan `urlpatterns`).
     Kemudian, cantumkan `path('mywatchlist/', include('mywatchlist.urls')),` ke dalam variabel `urlpatterns` di file `urls.py` pada `project_django`.
   - Di dalam file `models.py` pada folder `mywatchlist`, ditambahkan *class* baru yang bernama `MyWatchList` yang meng-*extend* `models.Model`.
     Class `MyWatchList` memiliki atribut seperti yang tertera seperti pada instruksi.
     ```
     class MyWatchList(models.Model):
         watched = models.BooleanField()
         title = models.CharField(max_length=255)
         rating = models.DecimalField( 
                     default=1,
                     max_digits=3,
                     decimal_places=2,
                     validators=[
                         MinValueValidator(Decimal('1.00')),
                         MaxValueValidator(Decimal('5.00'))
                     ]              
                 )
         release_date = models.DateField()
         review = models.TextField()
     ```
     Variabel `watched` menerima *value* `true` dan `false` (Boolean), `title` menerima string teks yang panjangnya tidak lebih dari 255 character,
     `rating` menerima desimal pada range 1-5 dengan presisi 2 angka di belakang titik, `release_date` menerima string tanggal yang formatnya di-set `default`,
     dan `review` menerima teks yang ukurannya lebih panjang daripada `title`.

## Tangkapan Layar Postman
##### Link ../mywatchlist/html:
![postman-html](https://user-images.githubusercontent.com/89509266/191427802-b469f175-836d-4254-a583-3b00e1362584.jpg)<br>

##### Link ../mywatchlist/xml:
![postman-xml](https://user-images.githubusercontent.com/89509266/191428141-17aae277-dd33-48d9-a0d1-6e0cf7cf4d79.jpg)<br>

##### Link ../mywatchlist/json:
![postman-json](https://user-images.githubusercontent.com/89509266/191428219-c7e59a0f-a56f-4450-8b80-f16290cb0eed.jpg)<br>