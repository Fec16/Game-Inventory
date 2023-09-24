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
1. Apa perbedaan antara form POST dan form GET dalam Django? <br>
    + Method POST akan mengirimkan data atau nilai langsung ke action untuk ditampung, tanpa menampilkan pada URL. 
    + Method GET akan menampilkan data/nilai pada URL, kemudian akan ditampung oleh action.

    + **Compare GET vs. POST** diambil dari [W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp "W3Schools") <br>

|Type|GET|POST|
|---|---|---|                                                                                              
| BACK button / Reload | Harmless | Data will be re-submitted (the browser should alert the user that the data are about to be re-submitted) |
| Bookmarked | Can be dibookmarked | Cannot be bookmarked |
| Cached | Can be cached | Not cached |
| Encoding type | application/x-www-form-urlencoded | application/x-www-form-urlencoded or multipart/form-data. Use multipart encoding for binary data |
| History | Parameters remain in browser history | Parameters are not saved in browser history |
| Restrictions on data length | Yes, when sending data, the GET method adds the data to the URL; and the length of a URL is limited (maximum URL length is 2048 characters) | No restrictions |
| Restrictions on data type | Only ASCII characters allowed | No restrictions. Binary data is also allowed |
| Security | GET is less secure compared to POST because data sent is part of the URL | POST is a little safer than GET because the parameters are not stored in browser history or in web server logs |
| Visibility | Data is visible to everyone in the URL | Data is not displayed in the URL |

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <br>
    + HTML adalah landasan utama dari webpage yang bertugas menjelaskan bagaimana data-data akan ditampilkan.
    + XML dan JSON menyimpan dan mengirim data dalam transaksi data antar server.
    + **Compare JSON Vs. XML** diambil dari [W3Schools](https://www.geeksforgeeks.org/difference-between-json-and-xml/ "W3Schools") <br>

|JSON|XML|
|---|---| 
| It is JavaScript Object Notation | It is Extensible markup language |
| It is based on JavaScript language | It is derived from SGML |
| It is a way of representing objects | It is a markup language and uses tag structure to represent data items |
| It supports array | It doesn’t supports array |
| Its files are very easy to read as compared to XML | Its documents are comparatively difficult to read and interpret |
| It doesn’t use end tag | It has start and end tags |
| It is less secured | It is more secured than JSON |
| It doesn’t supports comments | It supports comments |
| It supports only UTF-8 encoding | It supports various encoding | 

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <br>
    + **Sederhana dan Mudah Dibaca**: JSON menggunakan format teks yang mudah dibaca oleh manusia. Struktur data JSON terdiri dari pasangan key-value yang mirip sehingga mudah dipahami dan dikelola.
    + **Terbuka dan Standar**: JSON adalah format data terbuka sehingga memiliki standar terbuka yang dapat digunakan secara bebas oleh semua orang.
    + **Dukungan oleh Banyak Layanan Web**: Banyak layanan web dan API populer saat ini menggunakan JSON sebagai format pertukaran data, sehingga memudahkan integrasi antara aplikasi dengan layanan pihak ketiga.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
    + Jalankan virtual environment untuk menghindari project bertabrakan dengan dependencies lain. <br>
    ```
    env\Scripts\activate.bat
    ```
    + Buat folder `templates` di root folder dan di dalamnya buat berkas `base.html`. Untuk contoh berkas dapat dilihat di [sini](https://github.com/Fec16/game-inventory/blob/main/templates/base.html). <br>
    + Buka `settings.py` lalu ke variable `TEMPLATES` dan sesuaikan dengan potongan kode berikut. <br>
    ```
    ...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
            'APP_DIRS': True,
            ...
        }
    ]
    ...
    ```
    + Pada folder main buat berkas baru `forms.py`. <br>
    ```
    from django.forms import ModelForm
    from main.models import Item

    class ItemForm(ModelForm):
      class Meta:
        model = Item
        fields = ["name", "amount", "price", "description", "category"]
    ````
    + Pada folder `templates` di direktori `main`, buat berkas baru bernama `create_item.html` <br>
    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Item</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Item"/>
                </td>
            </tr>
        </table>
    </form>
    
    {% endblock %}
    ```
    + Pada berkas `views.py` di direktori `main`, tambahkan berikut: <br> 
     ```
     from django.http import HttpResponseRedirect, HttpResponse
     from main.forms import ProductForm
     from django.urls import reverse
     from django.core import serializers
     from main.models import Item
     ```
     + Sesuaikan function `show_main` pada `views.py` seperti potongan kode berikut: <br> 
     ```
     def show_main(request):
        item = Item.objects.all()

        context = {
           'name': 'Jason Kent Winata',
           'class': 'PBP F',
           'items' : items,
           'message': "You have successfully added a new item: " + items[1].name,
        }

        return render(request, "main.html", context)
     ```
     + Selanjutnya, tambahkan 5 function pada `views.py`
     ```
     # Function untuk menampilkan create_item.html
     def create_item(request):
        form = ItemForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
          form.save()
          return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)

     def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

     def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

     def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

     def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```
     + Pada file `urls.py` di `main`, tambahkan import function seperti ini: <br> 
     ```
      from django.urls import path
      from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
      
      app_name = 'main'
      
      urlpatterns = [
          path('', show_main, name='show_main'),
          path('create-item', create_item, name='create_item'),
          path('xml/', show_xml, name='show_xml'),
          path('json/', show_json, name='show_json'),
          path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
          path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), 
      ]
     ```

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md. <br>
   + /create-item <br>
    
   + /json/ <br>
    
   + /xml/ <br>
    
   + /json/- <br>
    
   + /xml/- <br>
    
