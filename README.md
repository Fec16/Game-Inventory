### Jason Game Inventory
---
#### Nama: Jason Kent Winata
#### NPM: 2206081313
#### Link: - <br>
---
### Pertanyaan untuk Tugas 2
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
