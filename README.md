![Coffeeine Display](https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/photo/2022/05/20/2240932928.jpg)

# Coffeeine
--- Need caffeine? Time for Coffeeine ☕---<br>
Link to Coffeeine : [https://coffeeine.adaptable.app/main/](https://coffeeine.adaptable.app/main/)

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
    Pertama, saya membuat suatu proyek Django baru yang diawali dengan menginisiasi direktori baru. Karena tema aplikasi yang saya pilih adalah pengelolaan biji kopi di _coffee shop_ dengan nama Coffeeine, saya menginisiasi suatu direktori lokal bernama `coffeeine`.<br>
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
        Karena proyek coffeeine sudah dibuat, saya melakukan konfigurasi proyek tersebut dengan memberikan setiap _hosts_ akses ke aplikasi _web_ dengan menambahkan bintang di `ALLOWED_HOSTS` di `settings.py`:<br>
        ```
        ALLOWED_HOSTS = ["*"]
        ```
        Setelah semua proses dilakukan, saya menambahkan `.gitignore` agar Git tidak perlu melacak beberapa berkas sehingga tidak memberatkan proses kerja komputer.
