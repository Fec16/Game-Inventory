### Jason Game Inventory
---
#### Nama: Jason Kent Winata
#### NPM: 2206081313 <br>
---
### Tugas 4
1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
   Kelebihan dalam menggunakan `UserCreationForm` adalah kita tidak perlu menghandle lagi password yang tidak sesuai dengan ketentuan atau nama *user* yang duplikat, oleh karena itu sebagai *software engineer*, dengan adanya fitur ini sangat mempermudah hidup. <br>
   Kekurangan dalam menggunakan `UserCreationForm` mungkin ketika membuat akun, limitasi passwordnya sangat strict sehingga membuat *user* bingung mau bikin password apa.
   
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
   Autentikasi adalah proses verifikasi identitas pengguna. Ini memastikan bahwa pengguna yang mencoba mengakses aplikasi web adalah orang tepat. Sedangkan Otorisasi adalah proses yang mengatur akses pengguna terotentikasi ke sumber daya atau fungsi tertentu dalam aplikasi web. Ini menentukan apa yang dapat dilakukan oleh pengguna yang sudah terotentikasi. <br>
   Mereka berdua penting karena autentikasi dan otorisasi dapat memastikan bahwa aplikasi web menjadi aman, data sensitif terlindungi, dan *user* memiliki akses yang sesuai dengan function yang diberikan. <br>
   
3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   Cookie adalah informasi yang disimpan dalam web pengguna. Cookies digunakan untuk menyimpan data pengguna dalam sebuah file secara permanen (atau untuk jangka waktu tertentu). Cookies memiliki tanggal dan waktu kedaluwarsa dan akan dihapus secara otomatis ketika waktu kedaluwarsanya tiba. Django menyediakan metode bawaan untuk mengatur dan mengambil cookies. <br>
   
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
   
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).