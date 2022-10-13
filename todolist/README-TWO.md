## Tautan Aplikasi Heroku
[https://assignment-pbp-2022.herokuapp.com/todolist/](http://assignment-pbp-2022.herokuapp.com/todolist/)<br>

## Jawaban Pertanyaan
1. - Asynchronous Programming: Proses suatu program dapat dilakukan bersamaan dengan proses lain
   - Synchronous Programming: Proses suatu program hanya dapat berjalan ketika proses dari program lain sudah selesai

2. Maksud dari *Event-Driven Programming* adalah proses yang dilakukan terjadi akibat suatu *event* atau peristiwa. <br>
   Contohnya, suatu fungsi bekerja jika suatu tombol X diklik.<br>
   Contoh penerapan *Event-Driven Programming* dalam tugas ini adalah tombol "Create Task" yang menginisiasi AJAX POST.

3. Penerapan *asynchronous programming* pada AJAX salah satunya adalah memperbarui suatu bagian webpage tanpa harus 
   me-*reload* keseluruhan web. AJAX hanya memperbarui informasi yang di-*update* ke server dan hanya mengembalikan informasi tadi.

4. GET<br>
   - Membuat fungsi baru di views, yaitu "get_todolist_json" yang mengembalikan semua task user dalam bentuk json.
   - Membuat path baru untuk fungsi tersebut, yaitu `/todolist/json`
   - Membuat `<script>` baru di dalam tag `<body>`untuk mengambil data dari `todolist/json` dan menampilkannya di HTML
   POST<br>
   - Membuat tombol `Add Task` dan membuat *class* modal baru yang berisi form
   - Membuat *view* `add_task` yang berisi fungsi untuk menambahkan views baru ke database. Setelah itu, dilakukan url routing pada `urls.py`
   - Form yang ada di dalam modal tadi disambungkan ke `add_task`
   - Setelah *task* baru berhasil dibuat, dibuat `<script>` yang me-refresh *task* baru.