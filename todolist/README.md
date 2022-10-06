## Tautan Aplikasi Heroku
[https://assignment-pbp-2022.herokuapp.com/todolist/](http://assignment-pbp-2022.herokuapp.com/todolist/)<br>

## Jawaban Pertanyaan
### Tugas 4
1. Kegunaan `{% csrf_token %}` pada elemen `<form>` adalah untuk menjaga user dari serangan **Cross-site Request Forgery**,
   yaitu ketika *attacker* menggunakan *authenticated state* user untuk mengubah *request* user.
   `{% csrf_token %}` akan men-*generate* token pada bagian server saat *rendering page* HTML. 
   Kemudian, server akan mengecek kembali token yang di-*generate* tadi untuk setiap *request* yang dibuat *user*. Jika *request* yang dibuat tidak 
   memiliki token tersebut, *request* tidak akan dieksekusi

2. Ya, kita dapat merender `<form>` secara manual. <br>
   - Pertama, kita perlu membuat *instance* dari suatu form di `views.py`. Form bisa berupa *built-in forms* yang ada di module ataupun class buatan.
     *instance* tadi disimpan di dalam suatu variabel, misalnya `form`.
   - Kemudian, tambahkan *instance form* tadi ke context html
     ```
     ...
     context = {'form' : form} #sesuaikan dengan variabel form yang dibuat
     return render(request, 'xxx.html', context) #sesuaikan dengan target html
     ```
   - Pada file target html tadi (pada contoh sebelumnya `xxx.html`), buat elemen form baru menggunakan tag `<form></form>`
     ```
     <form method="POST">
        {% csrf_token %}
        {{form}}
        <input type="submit" value=Submit">
     </form>
     ```
   - Untuk merapikan tampilan, kita dapat menggunakan *tag* HTML `<div></div>` dan `<label></label>`
     untuk membungkus atribut-atribut yang ada di `form` tadi.

3. - User menginput data melalui HTML page (`./todolist/create-task`)
   - Melalui fungsi `create_task` di `views.py`, form membuat object `Task` baru.
   - Laman `./todolist` akan menampilkan tabel yang berisi task **khusus milik user tersebut**. Hal ini dilakukan 
     dengan mem-filter kumpulan object Task yang ada dengan `Task.objects.filter(user=req.user)` dan disimpan ke suatu variabel (untuk kasus saya `task`).
   - Variabel `task` tadi ditambahkan ke variabel `context` dengan key sebagai berikut `'tasks' : task` 
   - Key `'tasks'` yang menyimpan kumpulan task milik user akan diiterasi untuk ditampilkan di tabel pada file `todolist.html` (laman `./todolist`)

4. - Dibuat aplikasi baru `todolist` dengan menjalankan *command* `python manage.py startapp todolist`. 
     Kemudian, aplikasi `todolist` didaftarkan ke dalam variabel `INSTALLED_APPS` di `./project_django/settings.py`
   - Di folder `todolist`, ditambahkan file `urls.py` yang berisi `app_name` dan `url_patterns`. Variabel `url_patterns` berisi kumpulan *path* aplikasi `todolist`. 
     Kemudian, *path* aplikasi `todolist` (`./todolist/urls.py`) ditambahkan ke dalam `url_patterns` di `./project_django/urls.py`
   - Di `./todolist/models.py`, dibuat sebuah *class* `Task` yang memiliki atribut seperti di soal. Karena akan dibuat form untuk membuat *task* baru, 
     ditambahkan *class* lain bernama `CreateTaskForm` yang meng-*extend* `forms.ModelForm`
     ```
     class Task(models.Model):
         user = models.ForeignKey(
                User,
                models.SET_NULL,
                blank=True,
                null=True
                )
         date = models.DateField()
         title = models.CharField(max_length=255)
         description = models.TextField()
   
     class CreateTaskForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = ('title', 'description')
            widgets = {'description' : forms.Textarea()}
     ```
   - Untuk mengimplementasikan form registrasi, dibuat fungsi `user_register` di `./todolist/views.py` yang akan menghasilkan object *user*.
     Form yang digunakan adalah `UserCreationForm`, yang sudah tersedia di library Django. Implementasi fungsi `register` akan disimpan di target html `register.html`.
   - Untuk mengimplementasikan login, dibuat fungsi `user_login` di `./todolist/views.py`. *Credentials* user, seperti username dan password, akan diambil menggunakan method `request.POST.get(...)` dan dicocokkan dengan *database* user menggunakan fungsi `autheticate`. 
     Setiap user login, web akan menyimpan *cookie* login. Implementasi login ini akan disimpan di target HTML `login.html`.
   - Untuk mengimplementasikan logout, dibuat fungsi `user_login` di `./todolist/views.py`. Fungsi `logout` akan menerima parameter `request`. Setiap user logout, 
     *cookie* yang disimpan saat user login akan dihapus.  Implementasi logout ini akan disimpan di target HTML `logout.html`.
   - Untuk mengimplementasikan create-task, dibuat fungsi `create_task` di `./todolist/views.py`. Fungsi ini akan membuat *instance* dari CreateTaskForm dan meminta `title` serta `description` dari *task* yang akan dibuat.
     Kemudian, akan dibuat object Task baru dari data yang diisi di form tadi. Implementasi create_task ini akan disimpan di target HTML `create-task.html`.
   - Akan dibuat *routing* untuk keempat *page* di atas dengan menambahkan URL di `url_patterns` pada `./todolist/urls.py`

### Tugas 5
1. - Inline CSS: Menuliskan *style* CSS di dalam tag HTML yang ingin dikustomisasi
   - In(ternal)-file: *Style* CSS ditulis di dalam file yang sama dengan HTML dan dibungkus dengan *tag* `<style></style>`. 
 Untuk mereferensikan jenis kustomisasi yang diinginkan, ditambahkan atribut *class="#"* di dalam tag HTML tersebut,
 dengan `#` sebagai nama CSS selector yang sudah didefinisikan di dalam *in-file* CSS tadi
   - External: *Style* CSS dituliskan di file terpisah yang memiliki ekstensi `.css` (misalnya, `styles.css`). 
 File HTML akan mengambil referensi dari `style.css` tersebut dengan menuliskan `<link rel="stylesheet" href="styles.css">`

2. - `<!DOCTYPE>`: Mendefinisikan tipe dokumen
   - `<a>`: Membuat sebuah hyperlink
   - `<head>`: Di dalam tag ini terdapat informasi metadata/informasi dokumen
   - `<body>`: Di dalam tag ini terisi konten dari dokumen
   - `<button>`: Membuat elemen tombol
   - (dan masih banyak lagi.. :D)

3. - `.class`: Mengambil semua elemen yang memiliki kelas `class="<nama_kelas>"`
   - `element`: Mengambil semua elemen yang sesuai, misalnya `h1`

4. - Kustomisasi halaman *login*, *register*, serta *create-task* menggunakan CSS sendiri dan *library* bootstrap
   - Kustomisasi halaman *todolist* dengan membuat *cards* per objek *task* menggunakan CSS sendiri dan *library* bootstrap
   - Elemen *class* dari *library* Bootstrap dikustomisasi (*override*) secara in-file dan in-line