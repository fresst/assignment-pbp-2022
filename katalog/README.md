## Link Aplikasi Heroku
[https://assignment-pbp-2022.herokuapp.com/](https://assignment-pbp-2022.herokuapp.com/)<br>
[https://assignment-pbp-2022.herokuapp.com/katalog/](https://assignment-pbp-2022.herokuapp.com/katalog/)

## Jawaban Pertanyaan
1. Bagan *request client*<br>
![mvt-diagram](https://user-images.githubusercontent.com/89509266/190100337-cc86d070-2513-4c70-8838-d4d9af53b0d8.jpg)<br>
*Client* mengirim HTTP *request* yang diterima *framework* Django. Selanjutnya, *request* tersebut dikirim ke **URLs** (`urls.py`) untuk dialihkan ke **Views** (`views.py`) yang diminta.
Views ini akan menerima *request object*, kemudian mengambil data melalui **Model** (`models.py`) dan mengembalikan *response object* (HTTP *response*) dalam bentuk **Template** HTML.
Model berkaitan langsung dengan database.

2. *Virtual environment* digunakan untuk mengisolasi *dependencies* suatu *project* dari *dependencies* global.<br>
   Kita tetap bisa membuat *project* Django tanpa menggunakan *virtual environment*. Namun, itu berarti *project* lain juga terpengaruh dengan *packages* yang dipasang.
   Penggunaan *virtual environment* dianjurkan supaya perubahan *dependencies project* tertentu tidak memengaruhi pengaturan proyek lain.

3.  - Membuat fungsi `def show_catalog(req)` di `../katalog/views.py` yang menerima 1 parameter berupa request `req`. HTTP *response* berupa berkas HTML `katalog.html`.
    - Membuat routing di `../katalog/urls.py` dan di `../project_django/urls.py` agar aplikasi bisa ditampilkan 
      di url `https://assignment-pbp-2022.herokuapp.com/katalog`
    - Data dari `initial_catalog_data.json` diambil dan disimpan `class CatalogItem(models.Model)` yang terdapat pada `../katalog/models.py`.
       Selanjutny fungsi `show_catalog` akan memetakan data yang diambil dari `CatalogItem`, kemudian ditempatkan ke dalam HTML.
    - *Deployment* dilakukan dengan membuat aplikasi baru bernama "assignment-pbp-2022", kemudian memasukkan API key Heroku ke Secrets repository.