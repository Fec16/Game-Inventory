### Jason Game Inventory
---
#### Nama: Jason Kent Winata
#### NPM: 2206081313
#### Link: - <br>
---
### Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
   + Buat direktori baru dengan nama `game_inventory` .
   + Buka command prompt dan jalankan perintah berikut. <br>
     ```
     python -m venv env
     ```
     Aktifkan virtual environment dengan perintah berikut.
     ```
     env\Scripts\activate.bat
     ```
   + Buat berkas requirements.txt dan tambahkan beberapa dependencies.
     ```
     django
     gunicorn
     whitenoise
     psycopg2-binary
     requests
     urllib3
     ```
   + Pasang dependencies dengan perintah berikut.
     ```
     pip install -r requirements.txt
     ```
   + Buka file `settings.py`, pada `ALLOWED_HOSTS` tambahkan `"*"` kedalam list, ini bertujuan agar semua host dapat mengakses aplikasi web.
   + + Buat aplikasi baru dengan nama `main` dalam proyek game_inventory.
     ```
     python manage.py startapp main
     ```
     Akan terbentuk folder baru yang bernama `main` dan isinya kumpulan file yang muncul saat pertama kali membuat django app.
   + Daftarkan aplikasi `main` ke dalam `INSTALLED_APPS` yang ada pada file `settings.py` di direktori utama.
     ```
     INSTALLED_APPS = [
     ...,
     'main',
     ...
     ]
     ```
   + Buat direktori baru bernama `templates` di dalam direktori aplikasi `main` 
   + Buat file yang diberi nama `main.html` di dalam folder tersebut.
   + Contoh implementasi `main.html` bisa dlihat di [sini](https://github.com/Fec16/game-inventory/blob/main/main/templates/main.html).
   + Pada file `models.py` tambahkan class `Item` yang memiliki attribute `name`, `amount`, `type`, `quality`, `description`, dan `id` yang contohnya bisa dilihat di [sini](https://github.com/Fec16/game-inventory/blob/main/main/models.py).
   + Setiap melakukan perubahan pada file `models.py` kita perlu melakukan **migration** dengan menjalankan perintah berikut.
     ```
     python manage.py makemigrations
     python manage.py migrate
     ``` 
   + Buka berkas `views.py` pada berkas aplikasi `main` dan tambahkan:
     ```
     from django.shortcuts import render
     ```
   + Tambahkan fungsi `show_main` di bawah import:
     ```
     def show_main(request):
    	context = {
        	'name': 'Jason Kent Winata',
        	'class': 'PBP F'
    	}

     return render(request, "main.html", context)
     ```
     + Konfigurasi *routing* urls dengan membuat file `urls.py` di `main` dan isi dengan perintah berikut.
     ```
     from django.urls import path
     from main.views import show_main

     urlpatterns = [
         path('', show_main, name='show_main'),
     ]
     ```
   + Pada `urls.py` di `game_inventory` bukan `main` tambahkan import:
     ```
     from django.urls import path, include
     ```
   + Pada list `urlpatterns` tambahkan:
     ```
     path('main/', include('main.urls')),
     ```
   + Jalankan perintah `python manage.py runserver` dan buka link http://localhost:8000/main/ di browser manapun. Jika tampilan sudah sesuai main.html, selamat anda telah berhasil!
   + Terakhir lakukan pengecekan attribute-attribute pada models. Buka file `tests.py` pada direktori `main` dan implementasikan sesuai contoh [berikut](https://github.com/Fec16/game-inventory/blob/main/main/tests.py)
   + Jalankan tes dengan menggunakan perintah berikut.
     ```
     python manage.py test
     ```
   + Jika tes berhasil, akan mengeluarkan informasi berikut.
     ```
     ----------------------------------------------------------------------
     Ran 1 test in 0.001s

     OK
     Destroying test database for alias 'default'...
     ```
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. <br>
![bagan_django_ppt](https://github.com/Fec16/game-inventory/assets/118716513/2c814343-96f0-4e42-8820-ab54947a201e)

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
   + Kita menggunakan virtual environment untuk memastikan bahwa dependencies setiap proyek terisolasi. Hal ini penting karena proyek-proyek yang berbeda dapat menggunakan dependencies yang berbeda, dan kita perlu mencegah agar dependencies tersebut tidak bertabrakan. Dengan menggunakan virtual environment, kita dapat memastikan keamanan proyek kita.
   + Kita dapat membuat aplikasi web berbasis Django tanpa virtual environment, tetapi tidak dianjurkan untuk alasan tersebut.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya! <br>
   + **MVC (Model-View-Controller)** <br>
     MVC adalah konsep architecture yang digunakan untuk mengimplementasikan interface pengguna dan memfokuskan pada pemisahan representasi data dari komponen-komponen yang berinteraksi atau memproses data.
   + **MVT (Model-View-Template)** <br>
     MVT adalah konsep architecture yang mirip dengan MVC namun Controller sudah diurus oleh framework yang kita gunakan, dalam hal ini maka Controller sudah diurus oleh Django.
   + **MVVM (Model-View-ViewModel)** <br>
     MVVM adalah konsep architecture yang terstruktur untuk memisahkan logika program dengan control interface pengguna.
---
### Tugas 3
