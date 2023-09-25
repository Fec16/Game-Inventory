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