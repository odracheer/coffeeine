![Coffeeine Display](https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/photo/2022/05/20/2240932928.jpg)

# Coffeeine
--- Need caffeine? Time for Coffeeine ☕---<br>
Link to Coffeeine 🔗: [https://coffeeine.adaptable.app/main/](https://coffeeine.adaptable.app/main/)

# **Ricardo Palungguk Natama - 2206082700 - PBP C**

# Tugas 2 PBP
## Soal :
1. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

## Jawaban :
1. Untuk mengimplementasikan _checklist_ di atas secara _step-by-step_, saya akan menjabarkan setiap poin satu per satu.
    * **Membuat sebuah proyek Django baru**<br>
    Pertama, saya membuat suatu proyek Django baru yang diawali dengan menginisiasi direktori baru. Karena tema aplikasi yang saya pilih adalah pengelolaan biji kopi di _coffee shop_ dengan nama Coffeeine, saya menginisiasi suatu direktori lokal yang menjadi direktori utama bernama `coffeeine`.<br>
    Setelah itu, saya menggunakan _command prompt_ untuk menjalankan _virtual environment_. Hal ini penting agar _package_ dan _dependencies_ lain tidak bertabrakan versi dengan versi yang ada di dalam komputer saya. Untuk melakukannya, kita perlu membuat _virtual environment_ dengan menjalankan kode berikut:<br>
        ```
        python -m venv env
        ```
        Untuk mengaktifkannya, kita menggunakan perintah berikut:<br>
        ```
        env\Scripts\activate.bat
        ```
        Jika sudah aktif, input terminal akan diawali dengan `(env)`. Setelah itu, kita bisa lanjut ke tahap pemasangan _dependencies_. Saya membuat _file_ `requirements.txt` dan menambahkan _dependencies_ yang diperlukan sebagai berikut:<br>
        ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
        Tahap selanjutnya adalah menginstalasi _dependencies_ dengan perintah berikut:<br>
        ```
        pip install -r requirements.txt
        ```
        Sehabis proses instalasi, saya membuat proyek Django dengan nama `coffeeine` menggunakan perintah berikut:<br>
        ```
        django-admin startproject coffeeine .
        ```
        Karena proyek `coffeeine` sudah terbuat, hal ini menciptakan suatu direktori proyek baru dengan nama `coffeeine` di dalam direktori utama `coffeeine`. Saya melakukan konfigurasi proyek tersebut dengan memberikan setiap _hosts_ akses ke aplikasi _web_ dengan menambahkan bintang di `ALLOWED_HOSTS` di `settings.py`:<br>
        ```
        ALLOWED_HOSTS = ["*"]
        ```
        Setelah semua proses dilakukan, saya menambahkan `.gitignore` agar Git tidak perlu melacak beberapa berkas sehingga tidak memberatkan proses kerja komputer.<br>

    * **Membuat aplikasi dengan nama `main` pada proyek tersebut.**<br>
    Langkah awal yang harus dilakukan adalah menyalakan _virtual environment_ dengan menjalankan _command prompt_ di dalam direktori utama `coffeeine`. Saya menggunakan perintah:<br>
        ```
        env\Scripts\activate.bat
        ```
        Posisi kita sudah di dalam _virtual environment_. Oleh karena itu, kita dapat membuat aplikasi baru dengan nama `main` di dalam proyek `coffeeine`. Saya menjalankan perintah berikut untuk membuat aplikasi tersebut:<br>
        ```
        python manage.py startapp main
        ```
        Setelah dijalankan, suatu direktori baru bernama `main` akan terbentuk di dalam direktori utama. Agar aplikasi `main` dapat terdaftar di dalam proyek, kita harus mengubah isi `settings.py` yang ada di dalam direktori proyek dengan menambahkan isi variabel `INSTALLED_APPS`. Kode yang saya jalankan sebagai berikut:<br>
        ```
        INSTALLED_APPS = [
            ...,
            'main',
            ...
        ]
        ```
        Alhasil, aplikasi `main` sudah terdaftar di dalam proyek `coffeeine`.<br>
    
    * **Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.**<br>
    Ketika saya mencoba melakukan _routing_ URL terhadap proyek agar dapat menjalankan aplikasi `main`, saya menambahkan fungsi `include` dari `django.urls` ke dalam _file_ `urls.py` yang ada di dalam direktori proyek `coffeeine`. Kode yang dimasukkan:<br>
        ```
        ...
        from django.urls import path, include
        ...
        ```
        Menggunakan fungsi yang diimpor, saya menambahkan rute URL di dalam variabel `urlpatterns` untuk mengarahkan tampilan saya ke aplikasi `main`:<br>
        ```
        urlpatterns = [
            ...
            path('main/', include('main.urls')),
            ...
        ]
        ```
        Untuk mengecek apakah proses tersebut sudah berhasil, saya menjalankan server dari proyek Django dengan perintah `python manage.py runserver`. Terakhir, saya membuka [http://localhost:8000/main/](http://localhost:8000/main/) dan memastikan tampilan `main` sudah dapat dijalankan.<br>
    
    * **Membuat model pada aplikasi `main` dengan nama `Item`**<br>
    Untuk membuat model pada aplikasi `main` dengan nama `Item`, saya membuat suatu _Class_ di dalam _file_ `models.py`. _Class_ ini melakukan inheritance terhadap `models.Model`. Perintah yang saya jalankan sebagai berikut:<br>
        ```
        from django.db import models

        class Item(models.Model):
            name = models.CharField(max_length=255)
            price = models.IntegerField()
            amount = models.IntegerField()
            description = models.TextField()
        ```
        Di dalam _file_ tersebut, saya membuat 3 atribut wajib (name, amount, dan description) serta 1 atribut tambahan (price). Setelah itu, saya melakukan migrasi model agar Django dapat melacak perubahan pada model _database_. Kode yang saya jalankan:<br>
        ```
        python manage.py makemigrations
        ```
        Ini dilakukan untuk membuat suatu berkas migrasi yang belum diaplikasikan ke _database_. Hal ini penting karena apabila tidak dilakukan, dapat terjadi _error_ saat melakukan kode selanjutnya, yakni:<br>
        ```
        python manage.py migrate
        ```
        Kode ini akan mengeksekusi perubahan model dari berkas migrasi ke dalam _database_.<br>

    * **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**<br>
    Pertama-tama, saya membuka _file_ `views.py` yang ada di dalam direktori `main`. Selanjutnya, saya mengubah isi _file_ tersebut dengan menambahkan fungsi `render` dari `django.shortcuts` yang bertujuan untuk melakukan _render_ terhadap template HTML agar dapat ditampilkan. Kode yang dijalankan:<br>
        ```
        from django.shortcuts import render
        ```
        Jika sudah diimpor, maka kita dapat melanjutkan proses penambahan fungsi `show_main` di bawah impor tersebut. Berikut kodenya:<br>
        ```
        def show_main(request):
            context = {
                'name': 'Ricardo Palungguk Natama',
                'class': 'PBP C'
            }
            return render(request, "main.html", context)
        ```
        Fungsi tersebut akan digunakan untuk mengatur permintaan HTTP sehingga tampilannya sesuai. Selain itu, kata kunci `name` diberikan value `Ricardo Palungguk Natama` sesuai nama saya dan `class` diberikan value `PBP C`. Fungsi ini akan me-_render_ tampilan dari `main.html` yang ada di direktori `templates`. Setelah mengubah kode di dalam `views.py`, saya mengubah beberapa kode yang ada di `main.html` menjadi seperti berikut:<br>
        ```
        ...
        <h5>Name: </h5>
        <p>{{ name }}<p>
        <h5>Class: </h5>
        <p>{{ class }}<p>
        ...
        ```
        Kode yang ada di `views.py` sebelumnya akan digunakan _value_-nya di dalam `main.html` sehingga tercipta tampilan dengan nama dan kelas saya. Tujuan dibuatnya proses seperti ini karena Django menerapkan MVT (Model-View-Template) sehingga `View` akan menjadi perantara bagi `Template` untuk mengakses _database_ `Model`.<br>

    * **Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**<br>
    Untuk membuat _routing_ yang memetakan fungsi yang telah dibuat di `views.py`, saya membuat suatu _file_ bernama `urls.py` di dalam direktori `main` yang sudah dibuat sebelumnya. Setelah _file_ terbuat, saya mengisi _file_ kosong tersebut dengan kode berikut:<br>
        ```
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
        Kode ini bermaksud untuk mengimpor `path` dari `django.urls` agar bisa membuat suatu pola URL. Di sisi lain, saya juga mengimpor `show_main` dari `main.views` untuk memberikan tampilan kepada pengguna ketika terjadi _request_ terhadap URL dari pengguna. Selain itu, saya membuat variabel `app_name` untuk menunjukkan nama unik pada pola URL dengan nama dari aplikasinya, yakni `main`.<br>
    
    * **Melakukan _deployment_ ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**<br>
    Sebelum melakukan _deployment_, saya menyiapkan terlebih dahulu sebuah repositori di GitHub yang bernama `coffeeine`. Repositori ini dihubungkan dengan direktori utama `coffeeine` yang sebelumnya sudah diinisiasi serta dikonfigurasi. Setelah itu, saya melakukan `add`, `commit`, dan `push` dari direktori lokal ke dalam repositori GitHub. Selanjutnya, saya membuat `New App` di Adaptable dan mengkoneksikannya dengan repositori `coffeeine` yang ada di GitHub. Lalu, saya menggunakan `Python App Template` dan `PostgreSQL` serta mengkonfigurasi versi python yang saya punya. Setelahnya, saya memasukkan `python manage.py migrate && gunicorn coffeeine.wsgi` pada bagian Start Command. Karena konfigurasi telah selesai, saya memasukkan nama aplikasi `coffeeine` dan mencentang bagian `HTTP Listener on PORT`. Terakhir, saya meng-klik `Deploy App` untuk memproses `_deployment_`. Akhirnya, aplikasi selesai di-_deploy_ dan dapat diakses melalui link [https://coffeeine.adaptable.app/main/](https://coffeeine.adaptable.app/main/).<br>
    <br>
2. Empty.<br>
    <br>
3. Empty.<br>
    <br>
4. MVC, MVT, dan MVVM adalah pola arsitektur yang biasa digunakan dalam pengembangan suatu perangkat lunak. Masing-masing pola memiliki caranya sendiri dalam mengatur data dan tampilan kepada _user_. Berikut penjelasannya:<br>
    * **MVC** <br>
    MVC merupakan singkatan dari _Model-View-Controller_. Ini adalah pola arsitektur yang paling umum digunakan pada saat ini. _Model_ merupakan komponen yang bertanggung jawab dalam mengelola data dan _business logic_ dari aplikasi yang dibuat. _View_ merupakan komponen yang mengatur tampilan kepada _user_ dan menerima _input_ dari mereka. Controller merupakan komponen yang mengatur logika dari aplikasi serta menjadi perantara _Model_ dan _View_. Jika _View_ menerima _input_ dari _user_, maka _Controller_ lah yang akan mengelola _input_ tersebut.

    * **MVT** <br>
    MVT merupakan singkatan dari _Model-View-Template_. Pola arsitektur ini sering digunakan saat pemrogram ingin menggunakan _framework_ seperti Django Python. Di sini, _Model_ merupakan komponen yang bertanggung jawab untuk mengelola data dan mengatur akses ke data. _View_ merupakan komponen yang mengontrol logika bisnis dan melakukan _render_ terhadap template. _View_ akan menerima HTTP _request_ dan mengembalikan HTTP _responses_. _Template_ merupakan komponen yang mengatur tampilan kepada _user_. _Template_ pada dasarnya berisi _markup_ HTML yang melakukan _render_ tampilan.

    * **MVVM** <br>
    MVVM merupakan singkatan dari _Model-View-ViewModel_. MVVM menjadi pola arsitektur yang melonggarkan hubungan antar komponen karena dari satu komponen ke komponen lainnya tidak terhubung secara langsung. Di MVVM, _Model_ merupakan komponen yang mengelola data dan logika bisnisnya. Lalu, _View_ merupakan komponen yang tidak memiliki logika bisnis, hanya mengatur tampilan yang terhubung dengan _user_ (XML). _ViewModel_ merupakan komponen yang memproses segala data, logika, serta _input_ dari user. Ini mengambil data dari _Model_, mengolahnya, dan menyediakan data yang siap digunakan oleh _View_. Proses yang ada di UI kebanyakan terjadi di sini.

    * **Perbedaan MVC, MVT, MVVM**<br>
    Ketiganya memiliki kegunaan yang mirip di komponen _Model_. Akan tetapi, komponen lainnya saling membedakan fungsionalitasnya. MVC dan MVT mirip, namun MVC menggunakan komponen _View_-nya untuk memberikan tampilan kepada _user_ sementara MVT menggunakan komponen _Template_ untuk mengatur tampiilan kepada _user_. MVVM juga melakukan hal yang mirip dengan MVC dalam hal pengaturan tampilan, yakni menggunakan _View_. Untuk mengolah datanya dari _Model_, MVC menggunakan _Controller_, MVT menggunakan _View_, dan MVVM menggunakan _ViewModel_. Selain beberapa hal tadi, perbedaan lainnya adalah MVC dan MVT umumnya digunakan sebagai kerangka kerja, tetapi MVVM biasanya digunakan untuk pengembangan aplikasi berbasis UI yang kompleks seperti aplikasi _mobile_.