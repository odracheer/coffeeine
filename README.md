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
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
            ```
            Fungsi yang saya buat untuk JSON:<br>
            ```
            def show_json_by_id(request, id):
                data = Product.objects.filter(pk=id)
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")
            ```

    * **Membuat _routing_ URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.**<br>
    Untuk membuat _routing_ URL untuk masing-masing `views`, langkah yang perlu dilakukan cukup singkat. Hal yang saya lakukan adalah mengimpor semua fungsi yang sudah dibuat sebelumnya ke dalam _file_ `urls.py` yang ada di direktori `main`. Kode yang saya masukkan sebagai berikut:<br>
        ```
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
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