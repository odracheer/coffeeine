![Coffeeine Display](https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/photo/2022/05/20/2240932928.jpg)

# Coffeeine
--- Need caffeine? Time for Coffeeine ☕---<br>
Link to Coffeeine 🔗: [https://coffeeine.adaptable.app/main/](https://coffeeine.adaptable.app/main/)

# **Ricardo Palungguk Natama - 2206082700 - PBP C**

<details>
<summary>Tugas 2 PBP</summary>

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

2. Berikut adalah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responsnya<br>
    ![Bagan](https://i.imgur.com/UaDPTdS.png)
    
    Penjelasan:<br>
    Bagan tersebut menjelaskan kaitan `urls.py`, `views.py`, `models.py`, dan berkas `HTML` di dalam suatu alur. Alurnya dimulai dari _Client_ yang melakukan _request_ ke Django. Setelahnya, Django akan melakukan _mapping_ ke URL yang sesuai. Untuk melakukan hal itu, Django akan memilih URL yang diinginkan di `urls.py` karena _file_ tersebut menyimpan seluruh URL yang ada di proyek. Setelah menemukan URL yang di-_request_ _Client_, kemudian _request_ tersebut akan diteruskan ke `views.py`. Di dalam MVT, terdapat 3 komponen utama yaitu _Model-View-Template_. `views.py` menjadi komponen _View_ di dalam MVT. `views.py` akan melakukan interaksi dengan `models.py` untuk mengambil data yang dibutuhkan karena `views.py` tidak bisa mengakses _database_ secara langsung. `models.py` menjadi perantara `views.py` untuk mengakses _database_. Hal ini dikarenakan `models.py` berperan sebagai komponen _Model_ di pola arsitektur MVT proyek ini. Setelah `models.py` mengambil data yang dibutuhkan, ia akan memberikan data tersebut kepada `views.py` untuk diolah dan dioper ke `templates.py` dalam bentuk berkas `html`. Berkas `html` yang sudah diberikan akan di-_render_ oleh `templates.py` karena `templates.py` merupakan komponen _Template_ di kasus ini. Terakhir, alurnya akan diakhiri dengan `templates.py` mengalihkan tampilan ke Django dan Django menyajikan tampilan yang sudah di-_render_ kepada _Client_.<br>
    <br>

3. _Virtual environment_ memainkan peran penting dalam pengembangan suatu proyek aplikasi web yang berbasis Django. Dengan bantuan _virtual environment_, kita dapat membuat isolasi proyek yang mandiri. Hasl ini sangat berguna jika kita memiliki banyak proyek. Isolasi proyek ini turut memengaruhi _dependencies_ dan _package_ Python yang ikut terisolasi sehingga akan terhindar dari konflik apabila terdapat lebih dari satu proyek Django dan setiap proyeknya menggunakan versi yang berbeda (baik _package_ maupun _dependencies_).<br>
Meskipun begitu, suatu aplikasi web berbasis Django tetap bisa dibuat tanpa menggunakan sebuah _virtual environment_. Akan tetapi, hal ini tidak disarankan karena terdapat kemungkinan konflik/_error_ apabila terdapat penggunaan versi _package_ atau _dependencies_ yang berbeda pada tahap pengembangan. Selain itu, ada kemungkinan versi dari _package_ atau _dependencies_ proyek lain akan terganti jika kita tidak menggunakan _virtual environment_. Dengan kata lain, penggunaan _virtual environment_ sangat penting di dalam pengembangan suatu proyek aplikasi web yang berbasis Django.<br>
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

## Bonus Tugas 2
Selain test dari template/tutorial 1, saya juga menambahkan test lain yang berguna untuk mengecek unit models.py yang telah saya buat. Test berjalan dengan lancar.

</details>

<details>
<summary>Tugas 3 PBP</summary>

# Tugas 3 PBP
## Soal :
1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
4. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

## Jawaban :
1. Setelah mencari sumber informasi yang menjelaskan tentang form `POST` dan form `GET` di PPT dan internet, saya akan menjabarkan perbedaan antara form `POST` dan form `GET` dalam Django di tabel berikut:

    | Perbedaan               | POST                             | GET                             |
    |-------------------------|------------------------------------------|---------------------------------| 
    | Kegunaan                | POST _request_ digunakan untuk mengirim data ke server| GET _request_ digunakan untuk membaca/menerima data dari web server |
    | Pemanggilan Method      | POST menggunakan $_POST | GET menggunakan $_GET |
    | Batas Karakter          | Tidak ada batasan ukuran yang ketat dalam jumlah data yang dapat dikirimkan | Panjang URL yang dapat digunakan terbatas sampai 2047 karakter |
    | Keamanan                | Lebih aman untuk data sensitif karena data tidak terlihat dalam URL | Kurang aman karena data terlihat dalam URL dan dapat dengan mudah dilihat oleh pihak ketiga |
    | HTTP Status Code        | Jika POST _request_ berhasil, maka server akan mengembalikan kode status HTTP 201 | Jika GET _request_ berhasil, maka server akan mengembalikan kode status HTTP 200 (OK) |
    | _Input_ Data            | Biasanya, _input_ data dilakukan melalui form | Biasanya, _input_ data dilakukan melalui link |

<br>

2. Dalam konteks pengiriman data, terdapat beberapa perbedaan utama antara XML, JSON, dan HTML. Perbedaan tersebut akan saya jabarkan dalam bentuk tabel:

    | Perbedaan           | XML                        | JSON                              | HTML                        |
    |---------------------|----------------------------|-----------------------------------|-----------------------------|
    | Struktur Data       | Hierarkis, berbasis tag     | Berbasis pasangan "key-value"     | Hierarkis, berbasis tag     |
    | Tujuan Utama        | Pertukaran data antara sistem yang berbeda dan dukungan banyak bahasa | Pertukaran data antara server dan aplikasi web, umum dalam pengembangan aplikasi web modern | Tidak digunakan untuk pertukaran data, digunakan untuk membuat tampilan dan struktur halaman web |
    | Keterbacaan manusia | Lebih sulit dibaca manusia | Mudah dibaca oleh manusia | Relatif mudah dibaca oleh manusia karena dirancang untuk menafsirkan dan menyusun teks, gambar, dan materi lain di web |
    | Ekstensibilitas     | Sangat ekstensibel dengan DTD atau XML Schema | Kurang ekstensibel, struktur data lebih sederhana | Tidak ekstensibel, aturan dan elemen sudah ditentukan |

<br>

3. JSON sering digunakan dalam pertukaran data antara aplikasi modern karena beberapa hal, yaitu:
    * JSON adalah format data yang ringan dan efisien. JSON terdiri dari teks biasa. Hal ini membuat data lebih mudah untuk dikirimkan melalui jaringan. JSON juga berukuran lebih kecil daripada format data lain, seperti XML, serta mendukung pengambilan data parsial. Artinya, aplikasi web dapat mengambil hanya bagian dari data yang dibutuhkan sehingga menghemat _bandwidth_ dan waktu.
    * JSON mudah dibaca oleh manusia dan mesin. JSON menggunakan struktur yang sederhana dan mudah dipahami, baik oleh manusia maupun mesin. Hal ini membuat JSON lebih mudah digunakan untuk pengembangan aplikasi web modern.
    * JSON didukung oleh berbagai bahasa pemrograman. JSON didukung oleh berbagai bahasa pemrograman, termasuk JavaScript, Python, Java, dan C++. Hal ini membuat JSON lebih mudah untuk digunakan dalam berbagai aplikasi web.

<br>

4. Untuk mengimplementasikan _checklist_ di atas secara _step-by-step_, saya akan menjabarkan setiap poin satu per satu.
    * **Membuat input `form` untuk menambahkan objek model pada app sebelumnya.**<br>
    Sebelum membuat input `form`, saya masuk ke `urls.py` yang ada di dalam folder `coffeeine` untuk mengubah _path_ `main/` menjadi `''` dengan kode berikut:<br>
        ```
        urlpatterns = [
            path('', include('main.urls')),
            path('admin/', admin.site.urls),
        ]
        ```
        Hal ini penting agar lebih sesuai dengan konvensi yang ada. Karena `urlpatterns` sudah diubah, kita harus membuat suatu _skeleton_ yang berfungsi sebagai kerangka _views_ sehingga mengurangi redundansi kode. Pertama, saya membuat _folder_ `templates` di dalam direktori utama. Di dalamnya, saya membuat suatu _file_ dengan nama `base.html` yang menjadi kerangka umum halaman web. Saya mengisi _file_ tersebut dengan kode berikut: <br>
        ```
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta
                    name="viewport"
                    content="width=device-width, initial-scale=1.0"
                />
                {% block meta %}
                {% endblock meta %}
            </head>

            <body>
                {% block content %}
                {% endblock content %}
            </body>
        </html>
        ```
        Setelah itu, saya membuka `settings.py` yang ada di direktori proyek `coffeeine` untuk mengganti isi variabel TEMPLATES dengan kode berikut:<br>
        ```
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'],
                'APP_DIRS': True,
                ...
            }
        ]
        ```
        Setelah semua proses tersebut dilakukan, saya baru memulai membuat form input. Awalnya, saya membuat _file_ dengan nama `forms.py` di direktori `main`. Berikut adalah kode yang saya gunakan:<br>
        ```
        from django.forms import ModelForm
        from main.models import Item

        class ItemForm(ModelForm):
            class Meta:
                model = Item
                fields = ["name", "price", "amount", "description"]
        ```
        Tahapan selanjutnya adalah membuat fungsi baru untuk menambahkan Item dengan nama `create_item` yang memiliki parameter `request`. Tetapi, sebelumnya kita harus mengimpor beberapa fungsi di bagian paling atas:<br>
        ```
        from django.http import HttpResponseRedirect
        from main.forms import ItemForm
        from django.urls import reverse
        from main.models import Item #Ga ada di tutorial
        ```
        Jika sudah, maka kita langsung ke bagian pembuatan fungsi. Kode yang saya gunakan:<br>
        ```
        def create_item(request):
            form = ItemForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "create_item.html", context)
        ```
        Selain itu, tak lupa saya mengubah fungsi `show_main` yang sebelumnya pernah dibuat dengan kode berikut:<br>
        ```
        def show_main(request):
            items = Item.objects.all()

            context = {
                'name': 'Ricardo Palungguk Natama', 
                'class': 'PBP C', 
                'items': items
            }

            return render(request, "main.html", context)
        ```
        Setelah mengubah fungsi-fungsi yang ada di dalam `views.py`, saya mengimpor fungsi `create_item` ke `urls.py` di _folder_ `main` seperti berikut:<br>
        ```
        from main.views import show_main, create_item
        ```
        Selain itu, saya juga menambahkan _path_ baru ke dalam `urlpatterns` di _file_ tersebut:<br>
        ```
        path('create-item', create_item, name='create_item'),
        ```
        Sebelum ke tahap final, saya membuat _file_ HTML baru dengan nama `create_item.html` di direktori `main/templates`. Kode yang saya gunakan:<br>
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
        Pada tahapan terakhir, saya mengubah isi `main.html` yang ada di direktori `main/templates` dengan kode berikut:<br>
        ```
        {% extends 'base.html' %}

        {% block content %}
            <h1>Coffeeine Page</h1>

            <h5>Name:</h5>
            <p>{{name}}</p>

            <h5>Class:</h5>
            <p>{{class}}</p>

            {% with total_items=items|length %}
                <p>Anda menyimpan {{ total_items }} jenis kopi pada aplikasi ini</p>
            {% endwith %}

        <table>
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Amount</th>
                <th>Description</th>
            </tr>

            {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}

            {% for item in items %}
                <tr>
                    <td>{{item.name}}</td>
                    <td>{{item.price}}</td>
                    <td>{{item.amount}}</td>
                    <td>{{items.description}}</td>
                </tr>
            {% endfor %}
        </table>

        <br />

        <a href="{% url 'main:create_item' %}">
            <button>
                Add New Item
            </button>
        </a>

        {% endblock content %}
        ```

    * **Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML _by ID_, dan JSON _by ID_.**<br>
    Untuk menambahkan 5 fungsi `views`, saya melakukan beberapa langkah sesuai dengan format:<br>
        * HTML<br>
        Pertama-tama, saya membuat `base.html` yang berfungsi sebagai kerangka halaman web di _folder_ `templates` dalam direktori utama. Lalu, saya juga mengubah `main.html` dengan melakukan _extends_ terhadap `base.html`. Setelah itu, saya membuat _file_ `forms.py` di direktori `main`. Ketiga hal ini sudah dilakukan di _checklist_ sebelumnya sehingga saya akan fokus ke _file_ `views.py` yang ada di direktori `main`. Saya mengimpor `Item` dari `main.models` dengan kode berikut:<br>
            ```
            from main.models import Item
            ```
            Setelah melakukan hal tersebut, saya mengubah fungsi `show_main` yang sudah pernah dibuat sebelumnya menjadi seperti ini:<br>
            ```
            def show_main(request):
                items = Item.objects.all()

                context = {
                    'name': 'Ricardo Palungguk Natama', 
                    'class': 'PBP C', 
                    'items': items
                }

                return render(request, "main.html", context)
            ```
        
        * XML dan JSON<br>
        Pertama-tama, saya membuka `views.py` yang ada di direktori `main`. Lalu, saya menambahkan beberapa impor seperti berikut:<br>
            ```
            from django.http import HttpResponse
            from django.core import serializers
            ```
            Setelah melakukan impor, saya membuat fungsi masing-masing untuk `XML` dan `JSON`. Kedua fungsi tersebut menerima parameter `request` dan di dalamnya terdapat variabel `data` untuk menyimpan hasil _query_ dari seluruh data yang ada di `Item`. Hal yang membedakan kedua fungsi parameter `serialize` dan parameter `content_type`. Fungsi yang saya buat untuk XML:<br>
            ```
            def show_xml(request):
                data = Item.objects.all()
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            ```
            Fungsi yang saya buat untuk JSON:<br>
            ```
            def show_json(request):
                data = Item.objects.all()
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            ```

        * XML _by ID_ dan JSON _by ID_<br>
        Pertama-tama, saya membuka `views.py` yang ada di direktori `main`. Lalu, saya menambahkan beberapa impor seperti berikut:<br>
            ```
                from django.http import HttpResponse
                from django.core import serializers
            ```
            Setelah melakukan impor, saya membuat fungsi masing-masing untuk `XML by ID` dan `JSON by ID`. Kedua fungsi tersebut menerima parameter `request` dan `id`. Di dalamnya terdapat variabel `data` untuk menyimpan hasil _query_ dari data dengan ID tertentu yang ada di `Item`. Sama seperti sebelumnya, hal yang membedakan kedua fungsi parameter `serialize` dan parameter `content_type`. Fungsi yang saya buat untuk XML:<br>
            ```
            def show_xml_by_id(request, id):
                data = Item.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            ```
            Fungsi yang saya buat untuk JSON:<br>
            ```
            def show_json_by_id(request, id):
                data = Item.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            ```

    * **Membuat _routing_ URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.**<br>
    Untuk membuat _routing_ URL untuk masing-masing `views`, langkah yang perlu dilakukan cukup singkat. Hal yang saya lakukan adalah mengimpor semua fungsi yang sudah dibuat sebelumnya ke dalam _file_ `urls.py` yang ada di direktori `main`. Kode yang saya masukkan sebagai berikut:<br>
        ```
        from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
        ```
        Sehabis itu, saya menambahkan beberapa _path_ URL baru ke dalam `urlpatterns`. _Path_ yang saya tambahkan:<br>
        ```
        urlpatterns = [
            ...
            path('xml/', show_xml, name='show_xml'), 
            path('json/', show_json, name='show_json'),
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
            ...
        ]
        ```
        Dengan demikian, kita dapat menjalankan server dan `localhost:8000` untuk melihat data dengan format yang kita inginkan. Jika kita ingin melihat data dalam format XML, kita bisa menjalankan `http://localhost:8000/xml`. Namun, kita dapat menjalankan `http://localhost:8000/xml/[ID]` apabila ingin melihat data dengan format XML secara spesifik berdasarkan IDnya. Di samping itu, kita juga bisa melihat data dalam format JSON dengan menjalankan `http://localhost:8000/json`. Untuk melihat data dengan format JSON secara spesifik berdasarkan ID, kita bisa menjalankan `http://localhost:8000/json/[ID]`. Untuk HTML, kita cukup menjalankan `http://localhost:8000` karena pada dasarnya data sudah dalam bentuk HTML. Namun, jika kita ingin melihat format HTML secara spesifik, disarankan untuk menggunakan Postman agar data dalam format HTML terlihat.
    
    <br>

    * **Mengakses kelima URL di poin 2 menggunakan Postman, membuat _screenshot_ dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md.`**<br>
    Berikut adalah hasil akses URL pada Postman dalam bentuk _screenshot_:<br>
        * HTML<br>
        ![HTML image](https://i.imgur.com/tEP2ECA.png)
        * XML<br>
        ![XML image](https://i.imgur.com/2jQd29U.png)
        * JSON <br>
        ![JSON image](https://i.imgur.com/5nTPsYK.png)
        * XML _by_ ID<br>
        ![XML by ID image](https://i.imgur.com/wfFIdsl.png)
        * JSON _by_ ID<br>
        ![JSON by ID image](https://i.imgur.com/z13OnOM.png)

## Bonus Tugas 3
Saya telah menambahkan pesan "Anda menyimpan X jenis kopi pada aplikasi ini" dan saya juga menyesuaikan konteksnya dengan `jenis kopi` karena saya membuat aplikasi kopi.

## Referensi Tugas 3
* Alexandromeo. (2016, November 6). _Perbedaan Method POST dan GET Beserta Fungsinya._ Makinrajin. Retrieved September 17, 2023, from https://makinrajin.com/blog/perbedaan-post-dan-get/
* Ramadhan, R. (n.d.). _Penjelasan Singkat tentang POST & GET Django._ GitHub Gist. Retrieved September 17, 2023, from https://gist.github.com/rririanto/442f0590578ca3f8648aeba1e25f8762
* Lane, R. (2023, May 17). _What's the Relationship Between XML, JSON, HTML and the Internet?_ DeltaXML. Retrieved September 17, 2023, from https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/
* Jaiswal, A. (n.d.). _JSON: Introduction, Benefits, Applications, and Drawbacks._ Turing. Retrieved September 17, 2023, from https://www.turing.com/kb/what-is-json

</details>

<details>
<summary>Tugas 4 PBP</summary>

# Tugas 4 PBP
## Soal :
1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
3. Apa itu _cookies_ dalam konteks aplikasi _web_, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
4. Apakah penggunaan _cookies_ aman secara default dalam pengembangan _web_, atau apakah ada risiko potensial yang harus diwaspadai?
5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

## Jawaban :
1. UserCreationForm adalah salah satu dari banyak _built-in form_ yang disediakan oleh Django. UserCreationForm digunakan untuk membuat formulir pendaftaran atau registrasi pengguna (_user registration form_) dalam aplikasi _web_ yang dibangun dengan Django. _Form_ ini secara khusus dirancang untuk memudahkan pembuatan dan validasi data yang diperlukan saat membuat akun pengguna baru. `UserCreationForm` mempunyai kelebihan dan kekurangan dalam penggunaannya. Kelebihan `UserCreationForm` adalah sebagai berikut:<br>
    * Penggunaan yang Mudah: `UserCreationForm` memudahkan pengembang _web_ dalam membuat _form_ pendaftaran dengan cepat. Dengan hanya beberapa baris kode, kita dapat membuat _form_ pendaftaran dengan mudah.
    * Validasi Otomatis: _Form_ ini mencakup validasi bawaan untuk memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan aturan yang ditetapkan, seperti penggunaan kata sandi yang cukup kuat dan unik.
    * Integrasi dengan Model Pengguna Django: Form ini terintegrasi dengan model pengguna bawaan Django (User), yang berarti Anda tidak perlu merancang basis data atau logika pengolahan data tambahan untuk menyimpan informasi pengguna baru. Semua ini diurus oleh Django.<br>

    Namun, ada beberapa kekurangan dari `UserCreationForm`:<br>
    * Tidak Terlalu Fleksibel: Meskipun `UserCreationForm` cocok untuk penggunaan umum, dalam beberapa kasus, `UserCreationForm` mungkin perlu penyesuaian dengan kebutuhan khusus aplikasi yang dibuat. Ini bisa menjadi lebih rumit dan memerlukan penyesuaian yang lebih besar.
    * Tidak Dapat Dikonfigurasi dengan Mudah: Beberapa aplikasi memerlukan lebih banyak data pengguna selain nama dan alamat email. Dalam hal ini, `UserCreationForm` akan lebih sulit digunakan karena perlu menambahkan bidang tambahan ke formulir sehingga memerlukan penyesuaian tambahan.
    * Tampilan Bawaan Tidak Selalu Sesuai: Tampilan bawaan dari `UserCreationForm` mungkin tidak sesuai dengan desain atau tampilan yang diinginkan untuk situs _web_. Kita perlu melakukan penyesuaian untuk mencocokkan penampilan _web_.

<br>

2. Autentikasi adalah proses verifikasi identitas pengguna. Autentikasi memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah orang yang mereka klaim. Dalam konteks Django, autentikasi biasanya melibatkan verifikasi bahwa pengguna telah memasukkan informasi login yang benar, seperti nama pengguna dan kata sandi. Di sisi lain, Otorisasi adalah proses menentukan hak akses pengguna terhadap sumber daya atau fitur tertentu dalam aplikasi. Proses ini menentukan apa yang dapat atau tidak dapat dilakukan oleh pengguna setelah mereka berhasil diautentikasi. Keduanya penting karena keduanya bertanggung jawab dalam memastikan keamanan dan kontrol dalam aplikasi _web_. Tanpa autentikasi, siapa pun dapat mengakses aplikasi, bahkan jika mereka bukan pengguna yang sah. Tanpa otorisasi, pengguna yang sudah diautentikasi dapat memiliki akses yang tidak terkendali ke seluruh aplikasi sehingga dapat mengancam keamanan dan privasi data.

<br>

3. Mengutip dari Kaspersky, _cookies_ adalah potongan kecil data yang disimpan pada perangkat pengguna saat mereka berinteraksi dengan situs _web_. Cookies adalah salah satu cara penting untuk mengelola sesi pengguna dan menyimpan informasi sementara di sisi klien (_browser_ pengguna) selama mereka berinteraksi dengan aplikasi _web_. Dalam konteks aplikasi web, _cookies_ digunakan untuk berbagai tujuan, termasuk otentikasi, pelacakan sesi, dan penyimpanan preferensi pengguna. Django menggunakan _cookies_ untuk mengelola data sesi pengguna. Ketika pengguna pertama kali mengunjungi aplikasi _web_, Django mengirimkan _cookie_ ke _browser_ pengguna yang berisi ID sesi. Setiap kali pengguna melakukan _request_ ke aplikasi web, Django memeriksa cookie untuk ID sesi. Jika ID sesi ditemukan, Django menggunakan ID sesi untuk mengidentifikasi sesi pengguna. Django menggunakan informasi sesi untuk memberikan pengalaman pengguna yang lancar. Setelah sesi kadaluwarsa, cookies sesi akan dihapus dan pengguna perlu melakukan otentikasi lagi jika perlu.

<br>

4. Penggunaan _cookies_ dalam pengembangan web memiliki potensi risiko yang harus diwaspadai. Berikut adalah beberapa risiko potensial yang terkait dengan penggunaan _cookies_:<br>
    * Pelanggaran Privasi: _Cookies_ dapat digunakan untuk melacak aktivitas pengguna di situs _web_. Jika tidak diatur dengan benar, _cookies_ ini dapat mengumpulkan informasi pribadi tentang pengguna tanpa izin, di mana hal ini merupakan pelanggaran privasi.
    * _Cookie Theft_: Jika _cookies_ yang berisi data otentikasi atau informasi sensitif lainnya dicuri oleh pihak yang tidak berwenang, ini dapat digunakan untuk mendapatkan akses yang tidak sah ke akun pengguna. Oleh karena itu, penting untuk mengenkripsi _cookie_ yang berisi data sensitif.
    * _Session Hijacking_: Dalam serangan _session hijacking_, penyerang mencuri ID sesi pengguna dan menggunakannya untuk mendapatkan akses ke akun pengguna tanpa perlu mencuri _cookie_. Ini dapat terjadi jika ID sesi tidak cukup aman atau tidak dienkripsi.
    * _Cross-Site Scripting_ (XSS): Serangan XSS dapat mengakibatkan _cookies_ pengguna dieksploitasi oleh penyerang. Jika penyerang dapat menyisipkan skrip berbahaya ke dalam situs web yang dilihat oleh pengguna, skrip itu dapat mencuri _cookies_ dan mengirimkannya ke penyerang.

    Oleh karena itu, gunakan _cookies_ secara bertanggung jawab. Informasi disimpan dalam _cookies_ apabila benar-benar diperlukan saja. Lakukan enkripsi _cookies_ untuk melindungi informasi pribadi yang disimpan dalam _cookies_. Izin pengguna juga harus didapatkan sebelum menyimpan _cookies_ yang berisi informasi pribadi.

<br>

5. Untuk mengimplementasikan _checklist_ di atas secara _step-by-step_, saya akan menjabarkan setiap poin satu per satu.
    * **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**<br>
    Pertama-tama, saya membuat fungsi registrasi terlebih dahulu. Saya membuka `views.py` yang ada di direktori `main` lalu menambahkan impor sebagai berikut:<br>
        ```
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        ```
        Saya mengimpor fungsi `redirect` dan `messages` serta _built-in form_ `UserCreationForm` dari Django untuk membuat formulir pendaftaran pengguna ke dalam aplikasi _web_. Fungsi yang tersisa akan digunakan untuk menghubungkan data dengan _cookie_ serta membuat fungsi `login` dan `logout` berdasarkan _cookie_ pengguna.Setelah itu, saya membuat fungsi `register` di bawahnya yang berisi kode berikut:<br>
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
        ```
        Setelah itu, kita perlu membuat suatu _file_ HTML yang akan memberikan tampilan kepada pengguna dengan nama `register.html` di dalam direktori `main/templates`. Saya mengisi _file_ tersebut dengan kode berikut:<br>
        ```
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
            
            <h1>Register</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}

        </div>  

        {% endblock content %}
        ```
        Selanjutnya, saya membuka `urls.py` yang ada di direktori `main`. Saya mengimpor kode `from main.views import register` dan menambahkan _path url_ `path('register/', register, name='register'),` ke dalam `urlpatterns` agar halaman _register_ dapat diakses oleh pengguna. Tahapan berikutnya adalah membuat fungsi `login`. Saya kembali membuka `views.py` untuk menambahkan impor `from django.contrib.auth import authenticate, login`. Setelah itu, saya membuat fungsi `login_user` menggunakan fungsi `authenticate` dan `login` yang sebelumnya diimpor dengan kode berikut:<br>
        ```
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
        ```
        Saya kembali membuat sebuah _file_ baru dengan nama `login.html` sebagai `templates` yang akan ditampilkan ke pengguna. Lalu, saya mengisi _file_ tersebut dengan kode berikut:<br>
        ```
        {% extends 'base.html' %}

        {% block meta %}
            <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

        </div>

        {% endblock content %}
        ```
        Langkah terakhir dalam membuat fungsi `login` adalah mengimpor `from main.views import login_user` ke dalam `views.py` yang ada di direktori `main` dan menambahkan _path url_ `path('login/', login_user, name='login'),` ke dalam `urlpatterns`. Setelah itu, saya membuat fungsi `logout`. Langkah-langkah yang dilakukan hampir sama dengan kedua fungsi sebelumnya. Pertama, saya mengimpor kode `from django.contrib.auth import logout` dan membuat fungsi `logout_user` yang menerima parameter `request`. Fungsi ini diisi dengan kode:<br>
        ```
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        ```
        Berikutnya, saya membuka _file_ `main.html` dan menambahkan kode berikut setelah _hyperlink tag_ untuk _Add New Item_:<br>
        ```
        <a href="{% url 'main:logout' %}">
            <button>
                Logout
            </button>
        </a>
        ```
        Terakhir, saya membuka `urls.py` di direktori `main`. Saya melakukan impor `from main.views import logout_user` dan menambahkan _path url_ `path('logout/', logout_user, name='logout'),` ke dalam `urlpatterns` seperti sebelumnya. Untuk memastikan ketiga fungsi ini bisa bekerja dengan efektif, saya mengimpor `from django.contrib.auth.decorators import login_required`. Lalu, saya menambahkan kode `@login_required(login_url='/login')` di atas fungsi `show_main` agar pengguna diwajibkan untuk melakukan _login_ terlebih dahulu sebelum mengakses halaman `main`.
    
    <br>
    
    * **Membuat dua akun pengguna dengan masing-masing tiga _dummy_ data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**<br>
    Untuk membuat akun pengguna, saya melakukan _register_ terlebih dahulu dengan pergi ke halaman `register`. Setelah melakukan _register_ _username_ dan _password_, saya mengulangi langkah tersebut sehingga menghasilkan dua akun yang berbeda. Akun pertama bernama `ricardo` dengan _password_ `pbp12345`. Akun kedua bernama `riland` dengan _password_ yang sama, yakni `pbp12345`. Kemudian, saya melakukan _login_ ke salah satu akun. Setelah itu, halaman saya dipindahkan ke `main` di mana saya bisa menambahkan `Item`. Selanjutnya, saya menambahkan 3 `Item` baru ke akun tersebut. Saya juga melakukan hal yang sama terhadap akun yang lainnya. Alhasil, saya telah menambahkan 3 _dummy_ data ke setiap akun pengguna. Berikut adalah dokumentasinya:<br>
    ![Kopi Ricardo](https://i.imgur.com/hXs0p7I.png)
    ![Kopi Ricardo](https://i.imgur.com/v5XLlyP.png)

    <br>

    * **Menghubungkan model `Item` dengan `User`.**<br>
    Untuk menghubungkan model `Item` dengan `User`, langkah awal yang saya lakukan adalah membuka `models.py`. Lalu, saya mengimpor `from django.contrib.auth.models import User` dan menambahkan kode berikut di dalam _file_ `models.py`:<br>
        ```
        class Item(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
        ```
        Hal ini dilakukan untuk mengasosiasikan sebuah user dengan produk melalui suatu _relationship_. Setelah itu, saya membuka `views.py` di direktori `main` untuk mengubah fungsi `create_item` menjadi seperti ini:<br>
        ```
        def create_product(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return HttpResponseRedirect(reverse('main:show_main'))
        ```
        Setelah itu, saya mengubah fungsi `show_main` dengan mengganti isi context dengan _key_ 'name' menjadi `'name': request.user.username,`. Karena saya mengubah `models.py`, selanjutnya saya melakukan migrasi. Saya menjalankan `env\Scripts\activate.bat` di _Command Prompt_ dan menuliskan kode `python manage.py makemigrations` untuk melacak semua perubahan. Pada saat terjadi _error_, saya menuliskan `1` sebagai _default value_ bagi `field user` pada semua _row_ yang telah dibuat pada _database_. Lalu, saya mengetik `1` lagi untuk menetapkan user dengan ID `1` pada model yang sudah ada. Terakhir, saya melakukan migrasi dengan mengeksekusi perintah `python manage.py migrate`.

    <br>

    * **Menampilkan detail informasi pengguna yang sedang `logged in` seperti `username` dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.**<br>
    Pertama-tama, saya membuka `views.py` di direktori `main`. Karena sebelumnya saya sudah mengimpor `HttpResponseRedirect`, `reverse`, dan `datetime`, saya akan lanjut ke tahapan selanjutnya yakni mengubah isi fungsi `login_user` di blok `if user is not None`:<br>
        ```
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        ```
        Selanjutnya, saya menambahkan `context` di dalam fungsi `show_main` dengan kode `'last_login': request.COOKIES['last_login']`. Sehabis itu, saya bisa membuat fungsi `logout_user` menjadi seperti berikut:
        ```
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        ```
        Karena _cookies_ sudah di-_setting_, selanjutnya saya membuka `main.html` dan menambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` di antara tabel dan tombol _logout_. Lalu, kita tinggal melakukan _refresh_ apabila server sudah dijalankan sebelumnya. Untuk melihat data _cookies_ `last login`, kita bisa melakukan _inspect element_ dan mengecek di bagian `Application/Storage`. Kita hanya perlu melakukan klik terhadap `Cookies` lalu kita bisa melihat data _cookies_ yang tersedia.

## Referensi Tugas 4
* What Are Internet Cookies and What Do They Do? (n.d.). Kaspersky. Retrieved September 26, 2023, from https://www.kaspersky.com/resource-center/definitions/cookies

</details>

<details>

<summary>Tugas 5 PBP</summary>

# Tugas 5 PBP
## Soal :
1. Jelaskan manfaat dari setiap _element selector_ dan kapan waktu yang tepat untuk menggunakannya.
2. Jelaskan HTML5 Tag yang kamu ketahui.
3. Jelaskan perbedaan antara _margin_ dan _padding_.
4. Jelaskan perbedaan antara _framework_ CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).

## Jawaban :
1. Setiap _element selector_ memiliki manfaat dan waktu penggunaannya masing-masing. Berikut adalah penjelasannya:

    * <strong><em>Universal Selector </em>(`*`)</strong><br>
        * Manfaat: Universal selector digunakan untuk memilih semua elemen dalam dokumen HTML.<br>
        * Waktu yang Tepat: _Selector_ ini berguna jika kita ingin menerapkan suatu _style_ dasar ke seluruh elemen.<br>
        
    * <strong><em>Element Type Selector </em>(`p`, `h1`, `div`, etc.)</strong><br>
        * Manfaat: _Element type selector_ digunakan untuk memilih elemen berdasarkan jenis atau nama elemennya (seperti paragraf, judul, atau _container_ elemen/div). <br>
        * Waktu yang Tepat: _Selector_ ini berguna jika kita ingin menerapkan _style_ tertentu terhadap satu atau beberapa jenis elemen dalam dokumen.<br>
    
    * <strong><em>Class Selector </em>(`.class-name`)</strong><br>
        * Manfaat: _Class Selector_ digunakan untuk memilih elemen berdasarkan kelas yang diberikan pada elemen tersebut. Dengan _selector_ ini, kita bisa menerapkan _style_ yang sama terhadap beberapa elemen yang memiliki kelas yang sama.<br>
        * Waktu yang Tepat: _Selector_ ini berguna jika kita ingin membuat _style_ yang sama terhadap elemen-elemen dengan kelas yang sama, tetapi tidak ingin memengaruhi elemen-elemen lain.<br>

    * <strong><em>ID Selector </em>(`#element-id`)</strong><br>
        * Manfaat: _ID selector_ digunakan untuk memilih elemen berdasarkan ID uniknya. Oleh karena itu, kita dapat menerapkan _style_ terhadap satu elemen khusus.<br>
        * Waktu yang Tepat: _Selector_ ini berguna ketika kita ingin menargetkan elemen tertentu untuk penerapan suatu _style_ atau perilaku khusus.<br>

    * <strong><em>Grouping Selector </em>(`h1, h2, h3`, etc.)</strong><br>
        * Manfaat: _Grouping Selector_ digunakan untuk memilih beberapa elemen secara bersamaan sehingga tidak perlu melakukan _styling_ yang berulang terhadap beberapa elemen yang memiliki _style_ yang sama. Penggunaan _selector_ ini dapat mengurangi redundansi kode.<br>
        * Waktu yang Tepat: _Selector_ ini berguna ketika kita ingin menargetkan beberapa elemen untuk penerapan _style_ yang sama.<br>

    <br>

2. Berikut adalah penjelasan mengenai beberapa HTML5 Tag yang saya ketahui:
    * `<header>` = Tag ini digunakan untuk mendefinisikan header atau bagian atas halaman _web_.
    * `<nav>` = Tag ini digunakan untuk menandakan bagian halmaman yang berisi menu navigasi.
    * `<table>` = Tag ini digunakan untuk menspesifikasikan tabel dalam halaman.
    * `<br>` = Tag ini digunakan untuk memberikan spasi untuk satu _line_.
    * `<!DOCTYPE>` = Tag ini digunakan untuk mendefinisikan tipe dokumen
    * `<button>` = Tag ini digunakan untuk menspesifikasikan tombol/_button_ dalam halaman.
    * `<h1>-<h6>` = Tag ini digunakan untuk mengatur header berukuran 1-6
    * `<p>` = Tag ini digunakan untuk menjelaskan paragraf dalam suatu halaman _web_.
    * `<footer>` = Tag ini digunakan untuk mendefinisikan _footer_ atau bagian bawah halaman _web_.
    * `<details>-<summary>` = Tag ini digunakan untuk membuat elemen yang dapat dibuka-tutup, di mana `<details>` adalah konten yang disembunyikan dan `<summary>` adalah judul dari konten tersebut.

    <br>

3. Perbedaan antara _margin_ dan _padding_ saya jabarkan dalam tabel berikut:<br>

    | Aspek         | Margin                                        | Padding                                          |
    |---------------|-----------------------------------------------|--------------------------------------------------|
    | **Definisi**  | _Margin_ adalah ruang di luar elemen HTML, di antara elemen tersebut dan elemen-elemen lain di sekitarnya. | _Padding_ adalah ruang di dalam elemen HTML, di antara batas elemen dan kontennya sendiri. |
    | **Nilai**     | Dapat berupa nilai negatif atau angka desimal. | Tidak mengizinkan nilai negatif. |
    | **Penyusunan**| Dapat diatur ke "_auto_."                       | Tidak dapat diatur ke "_auto_." |
    | **Pengaruh Terhadap Tampilan** | Tidak dipengaruhi oleh _style_ elemen seperti warna latar belakang. | Dipengaruhi oleh _style_ elemen seperti warna latar belakang. |

    <br>

4. Perbedaan antara _framework_ CSS Tailwind dan Bootstrap saya jabarkan dalam tabel berikut:

    | Fitur                                     | Bootstrap                                       | CSS Tailwind                                     |
    |-------------------------------------------|-------------------------------------------------|--------------------------------------------------|
    | **Popularitas**                           | Salah satu _framework_ HTML, CSS, & JS paling populer digunakan untuk membuat aplikasi responsif yang berfokus pada perangkat _mobile_. | _Framework_ CSS paling populer digunakan untuk membuat _interface_ pengguna yang fleksibel. |
    | **Tema dan _Template_**                   | Menyediakan tema dan _template_ siap pakai.        | Tidak menyediakan tema atau _template_ siap pakai.        |
    | **Kelas Utilitas**                        | Menawarkan kelas-kelas utilitas yang unik.      | Menggunakan kelas-kelas utilitas secara ekstensif. |
    | **Konsistensi Aplikasi**                  | Aplikasi yang dibuat dengan Bootstrap umumnya serupa karena sudah memiliki _template_ bawaan. | Aplikasi dan situs _web_ yang dibuat dengan Tailwind CSS bersifat unik dan fleksibel. |
    | **Kematangan**                            | _Framework_ yang lebih tua yang dikenal karena responsif dan efisiensinya sehingga menghemat banyak waktu pengembang. | Framework yang lebih baru dan masih terus berkembang. |
    | **Ukuran File**                           | Memerlukan ukuran _file_ yang lebih besar.       | Memerlukan ukuran _file_ yang lebih kecil.          |
    | **Perusahaan Terkenal yang Menggunakan** | Twitter, LinkedIn, Spotify, StackShare.         | MAKE IT, Superchat, Hashnode, Livestorm.          |
    | **Kemudahan Belajar**                     | Memiliki kurva pembelajaran yang lebih curam karena memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia | Memiliki pembelajaran yang lebih cepat untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan. |

    Waktu yang tepat untuk menggunakan Bootstrap adalah ketika kita ingin membangun tampilan situs _web_ dengan komponen yang sudah ada karena Bootstrap sudah menyediakan _template_ untuk digunakan. Selain itu, Bootstrap digunakan ketika proyek yang dibuat membutuhkan desain yang konsisten dan tidak memerlukan penyesuaian tingkat tinggi. Di sisi lain, CSS Tailwind digunakan ketika tingkat kustomisasi yang tinggi dan mengontrol setiap aspek desain. Penggunaan CSS Tailwind juga biasa dilakukan pada saat kita ingin mengutamakan ukuran _file_ CSS yang kecil dan memaksimalkan fleksibilitas dalam merancang tampilan yang unik.

    <br>

5. Untuk mengimplementasikan _checklist_ di atas secara _step-by-step_, saya akan menjabarkan setiap poin satu per satu.
    * <strong>Kustomisasi halaman _login_, _register_, dan tambah inventori semenarik mungkin.</strong><br>
    Pertama-tama, saya menambahkan isi `base.html` dengan Bootstrap agar saya bisa mengakses fitur-fiturnya. Kode yang saya gunakan:
        ```
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1">
                {% block meta %}
                {% endblock meta %}
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
                <link rel="stylesheet" type="text/css" href="style.css">
            </head>

            <body>
                {% block content %}
                {% endblock content %}
            </body>
        </html>
        ```
        Lalu, saya mengubah tampilan beberapa file `.html` yang ada di folder saya. Saya menggunakan _styling_ terhadap tulisan saya dengan CSS dan Bootstrap Package. Untuk bagian `login.html` dan `register.html`, saya menggunakan _container_ `card`.<br>
        * `login.html`
            ```
            {% extends 'base.html' %}

            {% block meta %}
                <title>Login</title>
            {% endblock meta %}

            {% block content %}

            <style>
                .navbar {
                    background-color: #000;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 20px 50px;
                    margin-bottom: 40px;
                }

                .navbar-brand img {
                    width: 80px; 
                    height: 80px;
                    margin-right: 10px; 
                }

                .navbar-brand {
                    font-size: 60px;
                    font-family: "EB Garamond", serif;
                    color: #ffffff;
                    text-align: center;
                    padding-top: 10px;
                }

                .navbar-brand:hover {
                    color: #ffffff;
                }

                .btn-primary {
                    background-color: green;
                    background-color: green;
                    margin-bottom: 15px;
                }

                .btn-primary:hover, .btn-primary:active, .btn-primary:focus {
                    background-color: darkgreen;
                    border-color: darkgreen;
                }

                p {
                    margin-top: 10px;
                }

            </style>

                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#">
                            <img src="https://i.imgur.com/S4xLOxr.png" alt="Logo" class="d-inline-block align-text-top">
                            Coffeeine.
                        </a>
                    </div>
                </nav>

                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-md-6">
                            <div class="card">
                                <div class="card-header">
                                    <h1 class="text-center">Login</h1>
                                </div>
                                <div class="card-body">
                                    <form method="POST" action="">
                                        {% csrf_token %}
                                        <div class="form-group mb-3">
                                            <label for="username">Username:</label>
                                            <input type="text" name="username" id="username" class="form-control" placeholder="Username">
                                        </div>
                                        <div class="form-group mb-3">
                                            <label for="password">Password:</label>
                                            <input type="password" name="password" id="password" class="form-control" placeholder="Password">
                                        </div>
                                        <div class="form-group text-center">
                                            <input class="btn btn-primary" type="submit" value="Login">
                                        </div>
                                    </form>
                                    {% if messages %}
                                        <ul class="list-group">
                                            {% for message in messages %}
                                                <li class="list-group-item">{{ message }}</li>
                                            {% endfor %}
                                        </ul>
                                    {% endif %}
                                    <p>Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            {% endblock content %}
            ```
        * `register.html`
            ```
            {% extends 'base.html' %}

            {% block meta %}
                <title>Register</title>
            {% endblock meta %}

            {% block content %}  

            <style>
                .navbar {
                    background-color: #000;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 20px 50px;
                    margin-bottom: 40px;
                }

                .navbar-brand img {
                    width: 80px; 
                    height: 80px;
                    margin-right: 10px; 
                }

                .navbar-brand {
                    font-size: 60px;
                    font-family: "EB Garamond", serif;
                    color: #ffffff;
                    text-align: center;
                    padding-top: 10px;
                }

                .navbar-brand:hover {
                    color: #ffffff;
                }

                .btn-primary {
                    background-color: green;
                    border-color: green;
                    margin-bottom: 15px;
                }

                .btn-primary:hover, .btn-primary:active, .btn-primary:focus {
                    background-color: darkgreen;
                    border-color: darkgreen;
                }

                p {
                    margin-top: 10px;
                }

            </style>

                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#">
                            <img src="https://i.imgur.com/S4xLOxr.png" alt="Logo" class="d-inline-block align-text-top">
                            Coffeeine.
                        </a>
                    </div>
                </nav>

                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-md-6">
                            <div class="card">
                                <div class="card-header text-center"><h1>Register</h1></div>
                                <div class="card-body">
                                    <form method="POST">
                                        {% csrf_token %}
                                        <div class="form-group mb-3">
                                            {{ form.username.label_tag }}
                                            {{ form.username }}
                                        </div>
                                        <div class="form-group mb-3">
                                            {{ form.email.label_tag }}
                                            {{ form.email }}
                                        </div>
                                        <div class="form-group mb-3">
                                            {{ form.password1.label_tag }}
                                            {{ form.password1 }}
                                        </div>
                                        <div class="form-group mb-3">
                                            {{ form.password2.label_tag }}
                                            {{ form.password2 }}
                                        </div>
                                        <div class="form-group text-center">
                                            <input class="btn btn-primary" type="submit" name="submit" value="Register">
                                        </div>
                                    </form>
                                    {% if messages %}
                                        <ul class="list-group">
                                            {% for message in messages %}
                                                <li class="list-group-item">{{ message }}</li>
                                            {% endfor %}
                                        </ul>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            {% endblock content %}
            ```
    
    * <strong>Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan _approach_ lain seperti menggunakan `Card`.</strong><br>
    Saya melakukan kustomisasi bentuk dan warna tabel pada halaman `main.html`. Saya juga mengubah beberapa `button` yang digunakan dan mengganti tulisan saat _user_ mengakses _web_. Selain itu, saya juga melakukan kustomisasi `create_item.html` dan `edit.item.html` dengan menggunakan _container_ `Card`. Berikut kodenya:<br>

        * `main.html`
            ```
            {% extends 'base.html' %}

            {% block content %}

            <style>
                .navbar {
                    background-color: #000;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 20px 50px;
                    margin-bottom: 40px;
                }

                .navbar-brand img {
                    width: 80px; 
                    height: 80px;
                    margin-right: 10px; 
                }

                .navbar-brand {
                    font-size: 60px;
                    font-family: "EB Garamond", serif;
                    color: #ffffff;
                    text-align: center;
                    padding-top: 10px;
                }

                .navbar-brand:hover {
                    color: #ffffff;
                }

                .btn-primary, .btn-primary:hover, .btn-primary:active, .btn-primary:focus {
                    background-color: green;
                    margin-bottom: 15px;
                }

                table {
                    width: 100%;
                    border-collapse: collapse;
                }

                button {
                    padding: 6px 12px;
                    background-color: green;
                    border: none;
                    color: white;
                    cursor: pointer;
                    margin-right: 5px;
                }

                button.edit {
                    background-color: green;
                    border-radius: 10px;
                    text-align: center;
                }

                button.edit:hover, button.edit:active, button.edit:focus {
                    background-color: darkgreen;
                    border-radius: 10px;
                }

                button.delete {
                    background-color: black;
                    border-radius: 10px;
                    text-align: center;
                }

                button.delete:hover, button.delete:active, button.delete:focus {
                    background-color: #2b2a2a;
                    border-radius: 10px;
                }

                td {
                    border: 1px solid #dddddd;
                    padding: 8px;
                    text-align: left; 
                }

                th {
                    background-color: #f2f2f2;
                    text-align: center;
                    padding: 8px;
                }   

                tr:hover {
                    background-color: #ddd;
                }

                /* Stil teks di textarea */
                textarea {
                    width: 100%;
                    padding: 6px 12px;
                    border: 1px transparent;
                    resize:both;
                    background-color: #ddd;
                }

                textarea:hover {
                    background-color: #ddd;
                }

                h5 {
                    font-size: 24px; /* Sesuaikan dengan ukuran yang Anda inginkan */
                    text-align: center;
                    margin-bottom: 10px; /* Jarak antara h5 dan p */
                }

                p {
                    font-size: 18px; /* Sesuaikan dengan ukuran yang Anda inginkan */
                    text-align: center;
                    margin-bottom: 20px; /* Jarak antara p dan elemen berikutnya */
                }

                .button-container {
                    text-align: center;
                    margin-top: 10px; /* Sesuaikan dengan jarak atas yang Anda inginkan */
                    margin-bottom: 10px;
                }

                .custom-button {
                    background-color: green;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    cursor: pointer;
                    margin: 5px;
                    border-radius: 5px;
                }

                .custom-button:hover, .custom-button:active, .custom-button:focus {
                    background-color: darkgreen;
                }

                .logout-button {
                    background-color: black;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    cursor: pointer;
                    margin: 5px;
                    border-radius: 5px;
                }

                .logout-button:hover, .logout-button:focus, .logout-button:active {
                    background-color:#2b2a2a;
                }

            </style>

                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#">
                            <img src="https://i.imgur.com/S4xLOxr.png" alt="Logo" class="d-inline-block align-text-top">
                            Coffeeine.
                        </a>
                    </div>
                </nav>

                <h5 class="custom-heading">Halo {{name}} dari kelas {{class}}!</h5>

                {% with total_items=items|length %}
                    <p>☕ Anda menyimpan {{ total_items }} jenis kopi pada aplikasi ini ☕</p>
                {% endwith %}

                <table>
                    <tr>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Amount</th>
                        <th>Description</th>
                        <th>Edit</th>
                    </tr>

                    {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}

                    {% for item in items %}
                        <tr>
                            <td>{{ item.name }}</td>
                            <td>{{ item.price }}</td>
                            <td>{{ item.amount }}</td>
                            <td><textarea rows="4" cols="40" readonly style="resize:none;">{{ item.description }}</textarea></td>
                            <td>
                                <a href="{% url 'main:edit_item' item.pk %}">
                                    <button class="edit">Edit</button>
                                </a>
                                <a href="{% url 'main:delete_item' item.pk %}" onclick="return confirm('Apakah anda yakin ingin menghapus barang ini?')">
                                    <button class="delete">Delete</button>
                                </a>
                            </td>
                        </tr>
                    {% endfor %}
                </table>

                <h5 style="margin-top: 20px;">Sesi terakhir login: {{ last_login }}</h5>
                <br />

                <div class="button-container text-center">
                    <a href="{% url 'main:create_item' %}">
                        <button class="custom-button">
                            Add New Item
                        </button>
                    </a>
                    <a href="{% url 'main:logout' %}" onclick="return confirm('Apakah Anda yakin ingin logout?');">
                        <button class="custom-button logout-button">
                            Logout
                        </button>
                    </a>
                </div>

            {% endblock content %}
            ```
        * `create.item_html`
            ```
            {% extends 'base.html' %}

            {% block meta %}
                <title>Add New Coffee</title>
            {% endblock meta %}

            {% block content %}
            <style>
                .navbar {
                    background-color: #000;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 20px 50px;
                    margin-bottom: 40px;
                }

                .navbar-brand img {
                    width: 80px; 
                    height: 80px;
                    margin-right: 10px; 
                }

                .navbar-brand {
                    font-size: 60px;
                    font-family: "EB Garamond", serif;
                    color: #ffffff;
                    text-align: center;
                    padding-top: 10px;
                }

                .navbar-brand:hover {
                    color: #ffffff;
                }

                .btn-primary {
                    background-color: green;
                    border-color: darkgreen;
                    margin-bottom: 15px;
                }

                .btn-primary:hover, .btn-primary:active, .btn-primary:focus {
                    background-color: darkgreen;
                    border-color: darkgreen;
                }

                .btn-secondary {
                    background-color: black;
                    margin-bottom: 15px;
                }

                .btn-secondary:hover, .btn-secondary:active, .btn-secondary:focus {
                    background-color: #2b2a2a;
                }

                .card-header {
                    text-align: center;
                }

            </style>

                <nav class="navbar navbar-expand-lg">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#">
                            <img src="https://i.imgur.com/S4xLOxr.png" alt="Logo" class="d-inline-block align-text-top">
                            Coffeeine.
                        </a>
                    </div>
                </nav>

                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-md-6">
                            <div class="card">
                                <div class="card-header"><h1>Add Your New Coffee</h1></div>
                                <div class="card-body">
                                    <form method="POST">
                                        {% csrf_token %}
                                        <table class="table">
                                            {{ form.as_table }}
                                            <tr>
                                                <td></td>
                                                <td>
                                                    <input class="btn btn-primary" type="submit" value="Add Coffee">
                                                    <a class="btn btn-secondary" href="{% url 'main:show_main' %}">Cancel</a>
                                                </td>
                                            </tr>
                                        </table>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            {% endblock content %}
            ```
        * `edit_item.html`
            ```
            {% extends 'base.html' %}

            {% block meta %}
                <title>Edit Coffee</title>
            {% endblock meta %}

            {% block content %}
            <style>
                .navbar {
                    background-color: #000;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 20px 50px;
                    margin-bottom: 40px;
                }

                .navbar-brand img {
                    width: 80px; 
                    height: 80px;
                    margin-right: 10px; 
                }

                .navbar-brand {
                    font-size: 60px;
                    font-family: "EB Garamond", serif;
                    color: #ffffff;
                    text-align: center;
                    padding-top: 10px;
                }

                .navbar-brand:hover {
                    color: #ffffff;
                }

                .btn-primary, .btn-primary:active, .btn-primary:focus {
                    background-color: green;
                    border-color: green;
                    margin-bottom: 15px;
                }

                .btn-primary:hover{
                    border-color: darkgreen;
                    background-color: darkgreen;
                }

                .btn-secondary {
                    background-color: black;
                    margin-bottom: 15px;
                }

                .btn-secondary:hover, .btn-secondary:active, .btn-secondary:focus{
                    background-color: #2b2a2a;
                }

                .card-header {
                    text-align: center;
                }

            </style>

            <nav class="navbar navbar-expand-lg">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">
                        <img src="https://i.imgur.com/S4xLOxr.png" alt="Logo" class="d-inline-block align-text-top">
                        Coffeeine.
                    </a>
                </div>
            </nav>

            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-header"><h1>Your Coffee</h1></div>
                            <div class="card-body">
                                <form method="POST">
                                    {% csrf_token %}
                                    <table class="table">
                                        {{ form.as_table }}
                                        <tr>
                                            <td></td>
                                            <td>
                                                <input class="btn btn-primary" type="submit" value="Submit Changes">
                                                <a class="btn btn-secondary" href="{% url 'main:show_main' %}">Cancel</a>
                                            </td>
                                        </tr>
                                    </table>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {% endblock content %}
            ```
    <br>
## Referensi Tugas 5
* _CSS Selectors._ (n.d.). W3Schools. Retrieved October 3, 2023, from https://www.w3schools.com/css/css_selectors.asp
* _HTML5 - Tags Reference._ (n.d.). Tutorialspoint. Retrieved October 3, 2023, from https://www.tutorialspoint.com/html5/html5_tags.htm
* Jain, S. (2023, June 5). _CSS Padding vs Margin._ GeeksforGeeks. Retrieved October 3, 2023, from https://www.geeksforgeeks.org/css-padding-vs-margin/
* Kumari, R. (2023, September 12). _Tailwind CSS Vs Bootstrap._ Tutorialspoint. Retrieved October 4, 2023, from https://www.tutorialspoint.com/tailwind-css-vs-bootstrap


</details>

<details>
<summary>Tugas 6 PBP</summary>

# Tugas 6 PBP
## Soal :
1. Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.
2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _event-driven programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
3. Jelaskan penerapan _asynchronous programming_ pada AJAX.
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada _library_ jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas _secara step-by-step_ (bukan hanya sekadar mengikuti tutorial).

## Jawaban :
1. Berikut adalah perbedaan antara _asynchronous programming_ dengan _synchronous programming_:<br>

    | Fitur / Konsep                         | Pemrograman Sinkron                                  | Pemrograman Asinkron                             |
    | -------------------------------------- | ---------------------------------------------------- | ------------------------------------------------ |
    | **Urutan Eksekusi**                    | Berurutan dan Blocking                               | Tidak Berurutan dan Non-blocking                 |
    | **Blocking vs. Non-blocking**          | Memproses dengan cara blokir                         | Memproses tanpa menghentikan eksekusi program    |
    | **Contoh Kasus Penggunaan**            | Tugas sederhana, perhitungan                         | Operasi I/O, jaringan, responsivitas aplikasi    |
    | **Konkurensi dan Paralelisme**         | Tidak memanfaatkan multi-core                        | Bisa memanfaatkan multi-core                     |
    | **Model Pemrograman**                  | Linear, mudah dipahami                               | Kontrol alur yang lebih kompleks                 |
    | **Alur Pemrograman Berbasis Platform** | Aplikasi berjalan secara berurutan, kurang responsif | Responsif, manajemen sumber daya yang lebih baik |

<br>

2. Paradigma "_event-driven programming_" adalah suatu pendekatan dalam pemrograman di mana program merespons peristiwa (_events_) yang terjadi, seperti tindakan pengguna, perubahan keadaan, atau pesan yang diterima. Istilah "_event_" dalam konteks ini mengacu pada situasi atau kondisi yang memicu reaksi atau pemrosesan tertentu dalam program. Pendekatan ini sering digunakan dalam pengembangan aplikasi yang melibatkan antarmuka pengguna (UI) interaktif, pemrosesan _asynchronous_, dan komunikasi dengan sumber eksternal seperti server atau perangkat lain. Penerapannya dalam tugas ini adalah ...........

<br>

3. Penerapan _asynchronous programming_ pada AJAX memungkinkan kita untuk membuat permintaan ke server web secara asinkron. Artinya, kita tidak perlu menunggu respon dari server sebelum melanjutkan eksekusi program yang berbeda. Hal ini sangat berguna untuk menjaga antarmuka pengguna tetap responsif dan menghindari pengalaman blok yang mungkin muncul dengan permintaan sinkron. Selain itu, kita harus mendefinisikan _event handlers_ untuk menangani respons dari server saat permintaan AJAX selesai. Dengan cara ini, kita dapat menentukan apa yang harus dilakukan program ketika data dari server telah diterima, baik itu menampilkan data ke pengguna, memproses data lebih lanjut, atau melakukan tindakan lain. Setelah mendefinisikan _event handlers_, kita perlu membuat _callback functions_ dalam AJAX untuk menentukan bagaimana menangani respons dari server. _Callback functions_ ini akan dijalankan setelah permintaan selesai.

<br>

4. Dalam pengembangan _web_, kita memerlukan AJAX (Asynchronous JavaScript and XML) untuk mengambil atau mengirim data dari dan ke server tanpa perlu melakukan _refresh_ ulang seluruh halaman. Ada dua teknologi yang biasa digunakan untuk melakukan AJAX,yakni Fetch API dan jQuery. Berikut adalah perbandingan antara kedua teknologi ini:<br>

    | Fitur / Aspek          | Fetch API                              | jQuery                                      |
    | ---------------------- | -------------------------------------- | ------------------------------------------- |
    | Ketersediaan           | Bawaan di _browser_ modern             | Membutuhkan pustaka tambahan                |
    | Gaya Pengkodean        | Promise-based, lebih modern            | Callback-based, lebih tradisional           |
    | Kompatibilitas         | Lebih rendah di _browser_ lama         | Lebih kuat untuk _browser_ lama             |
    | Berat                  | Lebih ringan                           | Lebih berat                                 |
    | Manipulasi DOM         | Terfokus pada permintaan HTTP          | Menyediakan utilitas DOM                    |
    | Performa               | Dapat lebih cepat dalam beberapa kasus | Bergantung pada implementasi AJAX jQuery    |
    | Komunitas dan Dukungan | Tren menuju Fetch API                  | Masih banyak proyek yang menggunakan jQuery |

    Kedua teknologi ini memiliki keunggulan dan kelemahan masing-masing. Pilihan tergantung pada konteks proyek dan preferensi individu. Menurut pendapat pribadi saya, Fetch API lebih baik dibandingkan jQuery untuk penerapan AJAX. Fetch API adalah teknologi yang lebih modern, ringan, dan memberikan lebih banyak kendali. Dengan penggunaan Promises, Fetch API memungkinkan penanganan permintaan asinkron yang lebih baik dan lebih mudah dibaca.

<br>

5. Untuk mengimplementasikan _checklist_ di atas secara _step-by-step_, saya akan menjabarkan setiap poin satu per satu.
    * **AJAX GET**<br>
        Pertama-tama, saya membuat fungsi di `views.py` dengan nama `get_item_json` yang memiliki parameter `request`. Fungsi ini saya buat untuk mengambil data `Item` berdasarkan _user_. Berikut kode yang saya masukkan:<br>
        ```
        def get_item_json(request):
            item = Item.objects.filter(user = request.user)
            return HttpResponse(serializers.serialize('json', item))
        ```
        Setelah membuat fungsi tersebut, saya membuat tampilan data yang sebelumnya tabel menjadi _cards_. Untuk melakukannya, saya membuka `main.html` lalu menghapus tabel dan menggantinya dengan kode berikut:<br>
        ```
        <div class="cards-container"></div>
        ```
        Karena saya sudah membuat fungsi tersebut, saya membuat _path_ agar fungsi tersebut dapat diakses oleh `main.html`. Saya memasukkan path di `urls.py` dengan perintah berikut:<br>
        ```
        from main.views import get_item_json
        ...
        path('get-item/', get_item_json, name='get_item_json'),
        ```
        Sehabis itu, saya membuat tag `<script>` dan membuat fungsi _asynchronous_ `getItems` dan `refreshItems`. Fungsi `getItems` ditujukan untuk mengambil data `Item` milik _user_ dengan AJAX GET, sementara `refreshItems` dibuat untuk menampilkan `Item` apa saja yang dimiliki oleh _user_. Berikut kode yang saya tambahkan untuk membuat kedua fungsi tersebut:<br>
        * `getItems()`
            ```
            async function getItems() {
                return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
            }
            ```
        * `refreshItems()`
            ```
            async function refreshItems() {
                const items = await getItems();
                const cardsContainer = document.querySelector(".cards-container");
                cardsContainer.innerHTML = "";

                items.forEach((item) => {
                    const card = document.createElement("div");
                    card.className = "card";
                    card.innerHTML = `
                    <header class="card-header">
                        <h5 class="card-title">${item.fields.name}</h5>
                    </header>
                    <div class="card-body">
                        <p class="card-text">Price: ${item.fields.price}</p>
                        <p class="card-text">Amount: ${item.fields.amount}</p>
                        <p class="card-description">Description: ${item.fields.description}</p>
                        </div>
                    <div class="card-footer">
                        <a href="/edit-item/${item.pk}" class="btn btn-primary">Edit</a>
                        {% csrf_token %}
                            <button class="btn btn-secondary" onclick="incrementAmount(${item.pk})">+</button>
                            <button class="btn btn-secondary" onclick="decrementAmount(${item.pk})">-</button>
                            <a href="#" class="btn btn-danger" onclick="confirmDelete(${item.pk}); return false;">Delete</a>
                    </div>
                    `;
                    cardsContainer.appendChild(card);
                });
            }

            refreshItems()
            ```
            Lalu, saya mengatur berbagai macam _styling_ dari _cards_ di bagian tag `<style>`. Setelah saya melakukan semua langkah tersebut, saya sudah bisa mengambil task dengan AJAX GET.

    <br>

    * **AJAX POST**<br>
        Untuk menerapkan AJAX POST di kode saya, saya membuat _modal_ pada awalnya. Saya menambahkan _modal_ tersebut di `main.html` dengan menuliskan kode berikut:<br>
        ```
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add Your New Coffee</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name"></input>
                            </div>
                            <div class="mb-3">
                                <label for="price" class="col-form-label">Price:</label>
                                <input type="number" class="form-control" id="price" name="price"></input>
                            </div>
                            <div class="mb-3">
                                <label for="amount" class="col-form-label">Amount:</label>
                                <input type="number" class="form-control" id="amount" name="amount"></input>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" id="button_delete"data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Coffee</button>
                    </div>
                </div>
            </div>
        </div>
        ```
        Di bagian `views.py`, saya membuat fungsi agar bisa menambahkan `Item` melalui _modal_. Saya mengimpor `HttpResponseNotFound` dan membuat fungsi `add_item_ajax` dengan parameter `request` untuk menambahkan `Item` menggunakan AJAX. Kita juga harus menggunakan @csrf_exempt agar memastikan data hanya datang dari _website_ kita. Berikut kodenya:<br>
        ```
        from django.http import HttpResponseNotFound
        from django.views.decorators.csrf import csrf_exempt
        ...
        @csrf_exempt
        def add_item_ajax(request):
            if request.method == 'POST':
                name = request.POST.get("name")
                price = request.POST.get("price")
                amount = request.POST.get("amount")
                description = request.POST.get("description")
                user = request.user

                new_item = Item(name=name, price=price, amount=amount, description=description, user=user)
                new_item.save()

                return HttpResponse(b"CREATED", status=201)

            return HttpResponseNotFound()
        ```
        Setelah membuat fungsinya, saya menambahkan path berdasarkan ketentuan soal, yaitu `/create-ajax/`, ke dalam `urls.py` yang ada di direktori proyek. Berikut kodenya:<br>
        ```
        ...
        from main.views import add_item_ajax
        ...
        path('create-ajax/', add_item_ajax, name='add_item_ajax'),
        ```
        Langkah terakhir, saya membuat function baru di tag `<script>` agar bisa mengimplementasikan AJAX POST. Saya membuat function dengan nama `addItem()`. Kode yang saya gunakan sebagai berikut:<br>
        ```
        function addItem() {
            fetch("{% url 'main:add_item_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshItems)

            document.getElementById("form").reset()
            return false
        }
        document.getElementById("button_add").onclick = addItem
        ```
        Setelah melakukan beberapa langkah ini, saya sudah bisa mengimplementasikan penambahan `Item` baru dengan AJAX POST.
    
    <br>

    * **Melakukan perintah `collectstatic`**<br>
        Untuk melakukan perintah `collectstatic`, saya membuka `settings.py` dan menambahkan kode berikut di bawah `STATIC_URL = '/static/'`:<br>
        ```
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        ```
        Setelah itu, saya membuka `Command Prompt` untuk menjalankan `collectstatic` dengan perintah berikut:<br>
        ```
        python manage.py collectstatic
        ```

## Bonus Tugas 6
Saya membuat bonus untuk tugas 6 dengan menambahkan beberapa kode berikut. Pertama-tama, saya membuat fungsi `delete_item_ajax` di `views.py` dengan kode berikut:<br>
```
@csrf_exempt
def delete_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponse(b"DELETED", status=201)
```
Setelah itu, saya membuat _path_ ke fungsi tersebut di `urls.py`. Saya menambahkan _path_ ini:<br>
```
path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
```
Karena saya sudah menambahkan _path_ tersebut, saya sudah bisa mengaksesnya dari `main.html`. Langkah selanjutnya adalah saya membuat fungsi _asynchronous_ untuk mengecek apakah _user_ benar-benar ingin menghapus `Item` tersebut dan fungsi _synchronous_ jika _user_ ingin lanjut menghapus. Berikut kodenya:<br>
```
async function confirmDelete(id) {
    if (confirm('Apakah Anda yakin ingin menghapus item ini?')) {
        deleteItem(id);
    }
}

function deleteItem(id) {
    fetch("/delete-item-ajax/?/".replace("?", id), {
        method: "POST"
    }).then(refreshItems)

    document.getElementById("form").reset()
    return false
}
```
Terakhir, saya membuat _delete button_ di dalam fungsi `refreshItems` untuk menjalankan `confirmDelete(id)` pada saat diklik seperti berikut:<br>
```
<a href="#" class="btn btn-danger" onclick="confirmDelete(${item.pk}); return false;">Delete</a>
```

## Referensi Tugas 6
* _Event-Driven Programming._ (n.d.). Tutorialspoint. Retrieved October 12, 2023, from https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_eventdriven_programming.htm
* Pangestu, G. (n.d.). _Asynchronous vs Synchronous Programming_. BINUS UNIVERSITY. Retrieved October 12, 2023, from https://binus.ac.id/malang/2022/05/asynchronous-vs-synchronous-programming/
* _What is an asynchronous request in AJAX ?_ (2019, March 9). GeeksforGeeks. Retrieved October 12, 2023, from https://www.geeksforgeeks.org/what-is-an-asynchro

</details>