# Link Aplikasi Heroku
link : https://katalog-lab2-pbp.herokuapp.com/todolist

# Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
Kegunaan dari ```{% csrf_token}``` pada elemen form adalah mencegah serangan dari luar. Seperti namanya, django mencegah adanya upaya peretasan berjenis cross site request forgery (CSRF). Yang terjadi ketika potongan kode ```{% csrf_token %}``` tidak ada pada elemen form adalah halaman dari response tidak akan terbentuk dan mengembalikan pesan error ```Forbidden CSRF token missing```.

# Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }}```)?
Kita dapat membuat form secara manual langsung pada template html-nya. Hal ini dilakukan dengan cara membuat tag form kemudian mengisi dengan tag input dengan type text. Hal ini akan otomatis membuat ```field``` untuk mengisikan data yang kita mau. Kemudian, kita memerlukan input kedua yaitu submit button agar dapat menjalankan action yang diharapkan ketika sudah mengisi form.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML
Ketika kita menekan submit button untuk menjalankan action pada form, data yang telah ditulis oleh pengguna akan dibungkus pada HttpRequest dengan metod POST. Kemudian, kita perlu untuk menyiapkan suatu object baru (bisa form atau yang lain) untuk disisipkan data yang telah kita terima dari form. Kemudian, kita perlu untuk menjalankan method ```save()``` pada object tersebut agar object yang kita buat tersimpan di database. Untuk menampilkan data kita pada template HTML, kita perlu menambahkan context yang sesuai dengan menggunakan object manager pada fungsi ```render```. Kemudian, kita perlu untuk menulikan variabel django yang sesuai dengan key di context pada template sehingga data bisa ditampilkan dengan baik.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
### Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya
Pembuatan aplikasi baru dilakukan dengan menjalankan perintah ```python manage.py startapp todolist```

### Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Penambahan path dilakukan dengan menuliskan function ```path``` dengan parameter berupa path ```todolist/``` dan include urls yang ada pada aplikasi todolist pada ```urls.py``` di project django

### Membuat sebuah model Task
Pembuatan sebuah model ```Task``` dilakukan dengan cara membuat class baru bernama ```Task``` pada models.py di todolist dengan atribut-atribut yang diminta, seperti user (object berupa ForeignKey User), title (object berupa CharField), date (object berupa DateField), dan description(object berupa CharField).

### Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik
Pengimplementasian form registrasi dilakukan dengan cara membuat template dari halaman untuk registrasi terlebih dahulu. Kemudian, kita membuat view yang tepat untuk mengembalikan HttpResponse yang telah di-render bersama-sama dengan template dan context (berisi django form). Kemudian, kita perlu menambahkan kondisi ketika terdapat request kembali dengan method POST, maka kita perlu untuk membuat django form dengan parameter request.POST. Kita juga perlu untuk mengecek apakah form yang baru saja kita buat valid atau tidak. Apabila valid, maka kita dapat melakukan save dengan method ```save()``` pada object form tersebut. Kemudian, kita disarankan untuk melakukan redirect ke halaman lain.

Pengimplementasian form login dilakukan dengan cara membuat template dari halaman untuk login terlebih dahulu. Kemudian, kita membuat view yang tepat untuk mengembalikan HttpResponse yang telah di-render bersama-sama dengan template dan context (berisi django form). Kemudian, kita perlu menambahkan kondisi ketika terdapat request kembali dengan method POST, maka kita perlu untuk mengambil data-data dari request.POST. Kemudian, kita perlu untuk menjalankan fungsi ```authenticate()```. Apabila user terautentikasi, maka kita dapat menjalankan fungsi ```login()``` dengan parameter HttpRequest dan user yang sudah di autentikasi. Kemudian, kita perlu untuk melakukan setting cookie sehingga session id dapat tersimpan. Setelah itu, kita disarankan untuk melakukan redirect ke halaman lain.

Pengimplementasian form logout dilakukan dengan cara membuat input submit button pada template yang diinginkan (misalnya pada template untuk show_todolist). Submit button tersebut mengarah ke view function ```logout_user()``` untuk dijalankan function ```logout()``` yang gunanya untuk menghapus id yang telah di log in dan data session nya. Kemudian, kita juga perlu untuk menghapus semua cookie pada request. Setelah itu, kita disarankan untuk melakukan redirect ke halaman lain.

### Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task
Pembuatan halaman utama dilakukan pada template html yang sesuai. Template diisi dengan django variable yang dapat menerima username pengguna dan data, seperti task, judul task, dan deskripsi task, untuk table. Kemudian, template juga diisi dengan tombol tambah task baru yang mengarah ke url untuk create task dan logout yang mengarah ke url logout user. 

### Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task
Pembuatan halaman untuk pembuatan task dilakukan pada template yang sesuai. Template diisi dengan django variable yang dapat menerima object form yang telah dikustomisasi dengan atribut judul dan deskripsi. Kemudian, kita membuat tombol submit untuk membuat object model ```Task``` dari data-data yang telah di-input pada form. Object tersebut kemudian kita simpan ke database.

### Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut: ```http://localhost:8000/todolist``` berisi halaman utama yang memuat tabel task, ```http://localhost:8000/todolist/login``` berisi form login, ```http://localhost:8000/todolist/register``` berisi form registrasi akun, ```http://localhost:8000/todolist/create-task``` berisi form pembuatan task, dan ```http://localhost:8000/todolist/logout``` berisi mekanisme logout
Routing dibuat dengan penambahan path yang sesuai pada urls.py di todolist. Path-path tersebut masing-masing harus sesuai dengan yang diharapkan pada tugas. Path-path yang telah dibuat diberi nama kemudian diarahkan ke fungsi view yang sesuai.

### Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Deployment dilakukan dengan melakukan commit serta push ke github atas perubahan berupa tugas yang telah dikerjakan. Github akan secara otomatis menjalankan dpl.yml dengan Procfile yang telah disediakan. Hal ini akan otomatis melakukan deploy ke heroku. Setelah dilakukan deploy, kita dapat mengakses aplikasi kita menggunakan link ```<nama aplikasi heroku>.herokuapp.com```.

### Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku
Pembuatan akun diawali dengan masuk ke link aplikasi heroku. Kemudian, kita perlu untuk melakukan dua kali registrasi sehingga terbentuk dua buah akun. Kemudian, kita perlu untuk melakukan login ke masing-masing akun kemudian melakukan penambahan task baru dengan menekan tombol ```Tambah Task Baru```.

---
# README Tugas 5<br>

# Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS merupakan kode-kode CSS yang ditulis langsung pada tag ```style``` di dalam suatu tag html. Kelebihan dari cara ini adalah mudah untuk dilakukan karena tidak perlu di link oleh file static lain. Kekurangan dari cara ini adalah ```style``` yang dibuat tidak dapat digunakan oleh komponen lain.

Internal CSS merupakan kode-kode CSS yang ditulis langsung pada tag ```style``` di dalam file html. Kelebihan dari cara ini adalah dapat digunakan untuk berbagai komponen. Kekurangan dari cara ini adalah tidak dapat digunakan pada file html lain.

External CSS merupakan kode-kode CSS yang ditulis dalam suatu file css tersendiri kemudian di-__link__ dengan file html. Kelebihan dari cara ini adalah dapat digunakan pada banyak file html. Kekurangan dari cara ini adalah halaman dapat menjadi berantakan apabila file gagal dipanggil.

# Jelaskan tag HTML5 yang kamu ketahui
- ```<button>``` digunakan untuk pembuatan sebuah button
- ```<div>``` digunakan apabila ingin membuat sebuah bagian untuk menempatkan komponen-komponen lainnya
- ```<p>``` digunakan apabila ingin membuat suatu paragraf

# Jelaskan tipe-tipe CSS selector yang kamu ketahui
- Element selector digunakan dengan cara memakai tag HTML. Tag tidak diawali apapun.
- ID selector digunakan dengan cara memakai ID suatu tag HTML. ID diawali dengan ```#```
- Class selector digunakan dengan cara memakai nama class. CLass diawali dengan ```.```

#  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

## Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:

### Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.
Kustomisasi dilakukan dengan menambahkan CSS dan CSS framework bootstrap pada templat-templat tersebut. Kustomisasi yang saya lakukan adalah dengan mengganti button dengan button primary dari bootstrap, mengganti background agar hover dengan css, dll.

### Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
Kustomisasi dengan mengganti seluruh table menjadi cards. Saya membuat ```div``` dengan class row kemudian di dalamnya akan di-looping sebanyak item yang ada pada ```context```. Kemudian setiap looping akan dibuat card baru dengan isi yang sesuai dengan atribut-atribut pada ```Task``` Django Model.

## Membuat keempat halaman yang dikustomisasi menjadi responsive.
Kustomisasi dilakukan dengan menambahkan media query agar gambar yang saya tempelkan dapat berubah-ubah ukurannya sesuai dengan ukuran layar pengguna.