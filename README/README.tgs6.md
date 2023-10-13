### Jason Game Inventory
---
#### Nama: Jason Kent Winata
#### NPM: 2206081313 <br>
---
### Tugas 6

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    + Dalam synchronous programming, tugas-tugas dieksekusi secara berurutan, satu per satu, tanpa memulai tugas baru sebelum tugas sebelumnya selesai. Ini berarti program akan berhenti atau terblokir jika ada tugas yang membutuhkan waktu lama untuk diselesaikan dan dapat menghambat responsivitas program.
    + Sedangkan dalam asynchronous programming, tugas-tugas dieksekusi tanpa harus menunggu tugas sebelumnya selesai. Program dapat melanjutkan eksekusi tugas lainnya sambil menunggu tugas asinkron selesai. Hal ini meningkatkan responsivitas program, terutama dalam konteks seperti penggunaan jaringan atau I/O yang lambat.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    + Paradigma event-driven programming adalah pendekatan pemrograman di mana program merespons peristiwa atau *events* yang terjadi dalam aplikasi atau lingkungan eksternal. Dalam JavaScript dan AJAX berarti menanggapi peristiwa seperti klik mouse, pengiriman permintaan HTTP, atau menerima respons dari server.
    + Contoh penerapannya adalah menggunakan event listener untuk menanggapi tindakan pengguna seperti mengklik tombol atau mengirim permintaan AJAX saat sebuah form disubmit.

3. Jelaskan penerapan asynchronous programming pada AJAX.
    + AJAX (Asynchronous JavaScript and XML) secara khusus dirancang untuk penerapan asynchronous programming dalam pengembangan web. Ketika Anda mengirim permintaan AJAX, Anda tidak harus menunggu respons dari server sebelum melanjutkan eksekusi kode JavaScript lainnya. Anda dapat mengatur callback functions yang akan dieksekusi ketika respons dari server diterima, memungkinkan aplikasi web Anda untuk tetap responsif.

4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
    + Fetch API adalah API JavaScript bawaan yang menyediakan antarmuka untuk mengirim permintaan HTTP asinkron ke server. Ia lebih modern, ringan, dan memiliki dukungan untuk Promise, yang mempermudah penanganan permintaan asinkron.
    + jQuery adalah library JavaScript yang memiliki banyak fitur, termasuk fasilitas AJAX. Namun, ia bisa menjadi lebih besar dalam ukuran dan memiliki overhead untuk penggunaan AJAX.
    + Menurut saya, Fetch API adalah pilihan yang lebih baik karena ia lebih ringan, lebih modern, dan merupakan bagian dari JavaScript standar. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.

    + **AJAX GET:** Ubahlah kode cards data item agar dapat mendukung AJAX GET.

    + Lakukan pengambilan task menggunakan AJAX GET.

    ```
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
    ```
    + **AJAX POST:** Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.

    data-bs-toggle="modal": data Bootstrap yang digunakan untuk menunjukkan bahwa tombol ini akan mengontrol modul pop-up;
    data-bs-target="#exampleModal": atribut data Bootstrap yang menentukan elemen target (dalam hal ini adalah modul pop-up dengan ID "exampleModal") yang akan ditampilkan saat tombol diklik;


    + Modal di-trigger dengan menekan suatu tombol pada halaman utama. Saat penambahan item berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya.

```
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
      <div class="modal-content">
          <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">Order New Pokemon Card!</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
              <form id="form" onsubmit="return false;">
                  {% csrf_token %}
                  <div class="mb-3">
                      <label for="name" class="col-form-label" style="color: #181818;">Name: (Dropdown Box)</label>
                      <select class="form-control" id="name" name="name">
                        {% for choice in cards %}
                            <option value="{{ choice.name }}">{{ choice.name }}</option>
                        {% endfor %}
                    </select>
                  </div>
                  <div class="mb-3">
                      <label for="amount" class="col-form-label"style="color: #181818;">Amount:</label>
                      <input type="number" class="form-control" id="amount" name="amount"></input>
                  </div>
                  <div class="mb-3">
                      <label for="description" class="col-form-label" style="color: #181818;">Description:</label>
                      <textarea class="form-control" id="description" name="description"></textarea>
                  </div>
              </form>
          </div>
          <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
          </div>
        </div>
  </div>
</div>
```

```
function addProduct() {
    fetch("{% url 'main:add_product_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshProducts)

    document.getElementById("form").reset()
    return false
}

document.getElementById("button_add").onclick = addProduct
```

dengan `document.getElementById("button_add").onclick = addProduct` maka button dengan id button_add akan menjalankan function addProduct ketika ditekan buttonnya yang akan merest form ketika sudah ditekan

    + Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.

Pada fungsi ini akan mengambil data dari method POST pada fungsi sebelumnya dari modal, dengan get, kemudian akan membuat produk baru seperti pada tugas sebelumnya

```
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        type = request.POST.get("type")
        quality = request.POST.get("quality")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, type=type, quality=quality, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

    + Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
pada path ini akan merouting create product ajax dari fungsi views untuk digunakan pada main.html

    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete_product_ajax/<int:item_id>/', delete_product_ajax, name='delete_product_ajax'),    

    + Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.

dihubungkan dengan function add product dengan memberikan fungsi pada button dengan ajax
```
function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }

document.getElementById("button_add").onclick = addProduct

- [X] Melakukan perintah collectstatic.

`python manage.py collectstatic` dan dikumpulan semua file static pada suatu file 

- [X] Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE

```
 async function deleteItem(itemId) {
      alert("Hello!");
      fetch(`delete_item_ajax/${itemId}/`, {
          method: "DELETE",
          
      }).then(refreshItems)
      return false
  }
```
```
 async function deleteItem(itemId) {
      const url = `/delete_product_ajax/${itemId}`;  // Use backticks for string interpolation
      fetch(url, {
          method: "DELETE",
      }).then(refreshProducts);

      return false;
    }
```

```
@csrf_exempt
def delete_product_ajax(request, item_id):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(pk=item_id)
            product.delete()
            response_data = {'message': 'DELETED'}
            status_code = 201
            return HttpResponse(b"DELETED", status=201)
        except:
            return HttpResponseNotFound()

    return HttpResponseNotFound()
```

```
path('delete_product_ajax/<int:item_id>/', delete_product_ajax, name='delete_product_ajax'),  
```

<a align="center" href="http://jason-kent-tugas.pbp.cs.ui.ac.id" >View Site</a>
