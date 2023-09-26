### Jason Game Inventory
---
#### Nama: Jason Kent Winata
#### NPM: 2206081313 <br>
---
### Tugas 4
1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya? <br>
   + Django `UserCreationForm` adalah salah satu *built-in form* yang disediakan oleh Django. Penggunaan dan cara kerjanya kurang lebih sama seperti `ModelForm`. <br>
   + Kelebihan: `UserCreationForm` mempermudah dan mempercepat pembuatan form *user*. Pengembang tidak perlu lagi membuat models seputar user dan dapat langsung menyimpannya ke dalam database. <br>
   + Kekurangan: `UserCreationForm` tidak sepenuhnya *customizable*. Selain itu, `UserCreationForm` tidak punya fitur autentikasi lanjutan misalnya 2FA. <br>
   
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
   + Autentikasi adalah proses verifikasi, memeriksa dan memastikan identitas pengguna. Langkah ini memastikan bahwa pengguna adalah orang yang sebenarnya dari user yang mereka klaim. <br>
   + Otorisasi adalah proses yang terjadi setelah autentikasi tujuannya untuk menentukan hak akses apa yang dimiliki oleh pengguna yang telah diautentikasi. <br>
   + Keduanya penting karena autentikasi dan otorisasi dapat menjamin keamanan, kontrol akses, privasi pengguna dalam aplikasi yang ada. Selain itu, tentunya hal ini sejalan dengan aturan hukum dan regulasi keamanan data. <br>
   
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? <br>
   + Cookies adalah penyimpanan data sederhana yang digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien atau pengguna. <br>
   + Cookies digunakan untuk menyimpan data pengguna dalam sebuah file secara permanen atau semenara. <br>
   + Cookies memiliki variabel name, value, domain website, path pada domain tersebut, tanggal expired, size cookie, dan sebagainya. Django juga menyediakan metode bawaan untuk mengatur dan mengambil cookies. <br>
   
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? <br>
   + Karena cookies disimpan pada sisi pengguna, tingkat keamanannya tergantung pengguna itu sendiri. Tetapi penggunaan cookies membawa beberapa risiko, misalnya penyimpanan data sensitif dalam cookies yang sebenarnya sangat berbahaya. Cookies dengan mudah dapat di-*copy* dan ditiru, akibatnya dapat timbul *cookie stealing*.
   
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   + Mengimplementasikan fungsi registrasi, login, dan logout.
      + Dengan `UserCreationForm` implementasinya menjadi lebih mudah. Pada berkas `views.py` tambahkan kode import berikut
      ```
      ...
      from django.shortcuts import redirect
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages
      from django.contrib.auth import authenticate, login, logout
      from django.contrib.auth.decorators import login_required
      ```
      + Selanjutnya, tambahkan kode berikut pada berkas `views.py` untuk fungsi registrasi, login, dan logout
      ```
      def register(request):
         form = UserCreationForm()

         if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)

      @login_required(login_url='/login')
      def show_main(request):
      ...

      def login_user(request):
         if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main")) 
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response
            else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
         context = {}
         return render(request, 'login.html', context)

      def logout_user(request):
         logout(request)
         response = HttpResponseRedirect(reverse('main:login'))
         response.delete_cookie('last_login')
         return response
      ```
      + Buat dua template berkas `html` dan implementasikan seperti berikut: [register.html](https://github.com/Fec16/game-inventory/blob/main/main/templates/register.html) dan [login.html](https://github.com/Fec16/game-inventory/blob/main/main/templates/login.html)
      + Dalam berkas `urls.py` pada `main` tambahkan
      ```
      urlpatterns = [
      ...
      path('register/', register, name='register'), 
      path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
      ...
]
      ```

   + Membuat dua akun pengguna dengan masing-masing tiga dummy data
      + Buat User menjadi bagian dari models agar tiap akun memiliki datanya masing-masing, caranya akan dibahas di bawah.

   + Menghubungkan model Item dengan User dan menerapkan cookies informasi last login.
      + Pada `models.py` di direktori `main` tambahkan:
      ```
      ...
      from django.contrib.auth.models import User

      class Item(models.Model):
         user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
      ```
      + Selanjutnya pada `views.py` di direktori `main` edit function `show_main` dan `create_item`:
      ```
      def show_main(request):
         items = Item.objects.filter(user=request.user)
         item_sum = 0
         for item in items:
            item_sum += item.amount

         context = {
            'name': request.user.username,
            'class': 'PBP F',
            'items' : items,
            'message': f"You have {item_sum} items in the shelf",
            'last_login': request.COOKIES['last_login'],
         }

         return render(request, "main.html", context)
      ```
      ```
      def create_item(request):
         form = ItemForm(request.POST or None)

         if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))

         context = {'form': form}
      return render(request, "create_item.html", context)
      ```
      + Kita menyisipkan cookie pada response untuk memberi tau browser client variabel yang akan disimpan. Sedangkan untuk mengambil nilai cookies kita tambahkan kode  `last_login = request.COOKIES['last_login']`.
      + Tambahkan juga pada berkas `main.html` kode berikut
      ```
      ...
      <h5>Sesi terakhir login: {{ last_login }}</h5>
      ...
      ```