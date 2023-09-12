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
        Untuk mengaktifkannya, kita menggunakan peintah berikut:<br>
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
    Ketika saya mencoba melakukan _routing_ URL terhadap proyek, saya membuat suatu file bernama `urls.py` di dalam direktori `main` yang sudah dibuat sebelumnya. Setelah file terbuat, saya mengisi file kosong tersebut dengan kode berikut:<br>
        ```
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
        Kode ini bermaksud untuk mengimpor `path` dari `django.urls` agar bisa membuat suatu pola URL. Di sisi lain, saya juga mengimpor `show_main` dari `main.views` untuk memberikan tampilan kepada pengguna ketika terjadi _request_ terhadap URL dari pengguna. Selain itu, saya membuat variabel `app_name` untuk menunjukkan nama unik pada pola URL dengan nama dari aplikasinya, yakni `main`.<br>
        
        Setelah proses tersebut dilakukan, saya menambahkan fungsi `include` dari `django.urls` ke dalam file `urls.py` yang ada di dalam direktori proyek `coffeeine`. Kode yang dimasukkan:<br>
        ```
        ...
        from django.urls import path, include
        ...
        ```
        Menggunakan fungsi yang diimpor, saya menambahkan rute URL di dalam variabel `urlpatterns` untuk mengarahkan tampilan saya ke `main`:<br>
        ```
        urlpatterns = [
            ...
            path('main/', include('main.urls')),
            ...
        ]
        ```
        Untuk mengecek apakah proses tersebut sudah berhasil, saya menjalankan server dari proyek Django dengan perintah `python manage.py runserver`. Terakhir, saya membuka [http://localhost:8000/main/](http://localhost:8000/main/) dan memastikan tampilan `main` sesuai.

    
    





