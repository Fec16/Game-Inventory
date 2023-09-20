### Jason Game Inventory
---
#### Nama: Jason Kent Winata
#### NPM: 2206081313
#### Link: - <br>
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
   + /create-item/ <br>
    ![create-item](https://github.com/Fec16/game-inventory/assets/118716513/af5f4774-6c17-44f8-b6da-248966c5d8f2)

   + /json/ <br>
    ![json](https://github.com/Fec16/game-inventory/assets/118716513/86445911-33ed-4378-9058-3d033c68ffc1)

   + /xml/ <br>
    ![xml](https://github.com/Fec16/game-inventory/assets/118716513/68d48880-6728-42ae-b544-f9fbbd8d9dfa)

   + /json/48384ed1-5587-481a-8d69-826ce287eef8 <br>
    ![json-id](https://github.com/Fec16/game-inventory/assets/118716513/3026a89f-998c-4afc-a6e9-db0b864075fb)


   + /xml/99072892-9bff-4075-8df7-354872ea4dd1 <br>
    ![xml-id](https://github.com/Fec16/game-inventory/assets/118716513/e7048e61-7d02-46b9-a993-b5fb878bd731)
