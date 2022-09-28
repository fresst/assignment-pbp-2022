## Tautan Aplikasi Heroku
[https://assignment-pbp-2022.herokuapp.com/todolist/](http://assignment-pbp-2022.herokuapp.com/todolist/)<br>

## Jawaban Pertanyaan
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

3. 

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
    
         def __str__(self):
             return self.title

     class CreateTaskForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = ('title', 'description')
            widgets = {'description' : forms.Textarea()}
     ```