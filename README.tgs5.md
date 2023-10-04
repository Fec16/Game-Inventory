### Jason Game Inventory
---
#### Nama: Jason Kent Winata
#### NPM: 2206081313 <br>
---
### Tugas 5

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    + **Element Selector**, Memilih elemen HTML berdasarkan nama elemennya.

    ```css
    p {
    color: blue;
    }
    ```

    + **Id selector**, Memilih elemen dengan id tertentu.

    ```css
    #header {
    background-color: blue;
    }
    ```

    + **Class Selector**, Memilih elemen dengan class tertentu.
    ```css
    .btn-primary {
    background-color: blue;
    }
    ```

2. Jelaskan HTML5 Tag yang kamu ketahui.
    + '`<header>`' mendefinisikan bagian atas dari sebuah halaman atau bagian dari sebuah elemen. Biasanya digunakan untuk judul, logo, navigasi, atau elemen-elemen penting lainnya di bagian atas halaman.

    + `<nav>` mendefinisikan bagian navigasi dari sebuah halaman web. Ini dapat berisi tautan ke berbagai halaman dalam situs web.

    + `<article>` mengelompokkan konten yang mandiri dan berdiri sendiri, seperti posting blog, artikel berita, atau konten yang dapat dibagikan secara independen.

    + `<section>` mengelompokkan konten berdasarkan tema atau subjek tertentu. Ini membantu dalam pengorganisasian halaman web menjadi bagian yang lebih terstruktur.

    + `<aside>` mengidentifikasi konten yang terkait tetapi tidak penting untuk inti dari halaman. Biasanya digunakan untuk sidebar atau elemen lain yang bisa ditempatkan di samping konten utama.

3. Jelaskan perbedaan antara margin dan padding.
    + Margin dan Padding merupakan properti CSS yang berfungsi untuk mengatur tata letak antar elemen HTML.
    + Margin digunakan untuk mengatur ruang di antara elemen tersebut dengan elemen-elemen lain di sekitarnya
    + Padding digunakan untuk mengatur jarak antara konten elemen tersebut dengan batas atau tepi elemen tersebut. 

    <img src= />


4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    + **Bootstrap** memiliki gaya desain yang sudah ditentukan sebelumnya dengan komponen UI yang telah dirancang dengan baik. Ini berarti Anda dapat memiliki tampilan yang konsisten tanpa perlu banyak kustomisasi.
        + Membutuhkan tampilan yang cepat dan konsisten tanpa banyak kustomisasi.
        + Menghemat waktu dan tidak perlu mengelola banyak kelas utilitas.
        + Sangat paham Bootstrap dan ingin memanfaatkannya.
    + **Tailwind** adalah framework yang berfokus pada utilitas. Itu berarti Anda membangun tampilan Anda dengan menggabungkan kelas-kelas utilitas ke dalam elemen HTML Anda. Anda memiliki lebih banyak kendali terhadap tampilan akhir, tetapi perlu melakukan lebih banyak pekerjaan kustomisasi.
        + Mendesain tampilan dan ingin membuat tampilan yang sangat kustom.
        + Memiliki waktu untuk menyesuaikan setiap elemen tampilan secara mendalam.
        + Menghasilkan file CSS yang lebih kecil dan mengoptimalkan kinerja halaman.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    + Pada direktori `game_invetory/settings.py` tambahkan
    ```
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
    STATIC_URL = 'static'
    ```
    + Pada direktori `game_inventory/main/templates/login.html` dan `game_inventory/main/templates/register.html` tambahkan kode CSS
    ```
    <style>
        body {
            background-color: #E4002B; 
        }
        .login-box {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
        }
    </style>
    ```

    + Pada direktori `game_inventory/main/templates/main.html` tambahkan kode CSS
    ```
    <style>
    body {
        margin: 0;
        padding: 0;
        font-family: Monospace, sans-serif;
    }

    /* Header */
    h1 {
        font-size: 24px;
        color: #E4002B; /* Updated color to #E4002B */
    }

    /* Cards */
    .card {
        border: 1px solid #E4002B; /* Updated border color */
        padding: 10px;
        margin: 10px;
        background-color: #fff1e2;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
        border-radius: 5px;
    }

    .card:last-child {
        background-color: #FFD700; 
        color: #000; 
    }

    /* Buttons */
    button {
        background-color: #E4002B; /* Updated background color */
        color: white;
        border: none;
        padding: 5px 10px;
        cursor: pointer;
    }

    /* "Add New Product" and "Logout" buttons */
    button.add-new-product, button.logout {
        background-color: #009933; 
    }

    /* Last login message */
    h5 {
        color: #777;
    }

    /* Style links */
    a {
        text-decoration: none;
        color: #E4002B; 
    }

    a:hover {
        text-decoration: underline;
        color: #E4002B; 
    }
    </style>
    ```

    + Pada direktori `game_inventory/main/templates/create_item.html` tambahkan kode CSS
    ```
    <style>
    /* Reset some default styles */
    body {
        margin: 0;
        padding: 0;
        font-family: Monospace, sans-serif;
    }

    /* Style the header */
    h1 {
        font-size: 24px;
        color: #E4002B; /* Updated color to #E4002B */
    }

    /* Style the table */
    table {
        border-collapse: collapse;
        width: 100% ;
        
    }

    table, th, td {
        border: 1px solid #E4002B; 
    }

    th, td {
        padding: 8px;
        text-align: left;
    }

    /* Style buttons */
    input[type="submit"] {
        background-color: #E4002B;
        color: white;
        border: none;
        padding: 5px 10px;
        cursor: pointer;
    }
    </style>
    ```


    + Bonus: pada `main.html` tambahkan kode berikut
    ```
    .card:last-child {
    background-color: #FFD700; 
    color: #000; 
    }
    ```