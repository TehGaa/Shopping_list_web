# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Asynchronous programming merupakan metode yang memungkinkan pengerjaan dua atau lebih operasi tanpa harus menunggu salah satu selesai terlebih dahulu. Asynchronous berguna dalam hal meningkatkan tingkat responsif dan mengurangi load halaman.

Synchronous programming merupakan metode yang mengharuskan urutan dalam pengeksekusian operasi sehingga dalam mengerjakan dua operasi atau lebih, salah satu operasi harus selesai terlebih dahulu kemudian yang lain baru dikerjakan. Synchronous digunakan oleh programmer karena penggunaan metode "tradisional" lebih memudahkan search engine untuk mencari website tersebut.

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
Event-Driven Programming merupakan paradigma di mana alur program berjalan sesuai dengan "event" yang diberikan oleh user. Event tersebut dapat berupa tekan tombol, gerakan mouse, ketikan keyboard, dll. Contoh penerapan Event-Driven Programming pada tugas ini adalah button ```Get Data``` yang akan meng-trigger ajax request sehingga data dari server dapat dikembalikan ke user.

# Jelaskan penerapan asynchronous programming pada AJAX
Penerapan asynchronous programming pada AJAX dapat dilihat pada salah satu kegunaan AJAX yaitu user dapat berkomunikasi dengan server, seperti menulis dan mengambil data, tanpa perlu untuk melakukan refresh halaman. Hal tersebut dimungkinkan karena AJAX mengirimkan ```XMLHttpRequest``` ke server secara terpisah dari operasi utama sehingga sukses dan tidak suksesnya request ini tidak memengaruhi operasi utama halaman.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas

## Mengubah tugas 4 yang telah dibuat sebelumnya menjadi menggunakan AJAX
Hal yang harus dilakukan pertama kali adalah melakukan link dengan CDN jquery AJAX.

### AJAX GET
#### Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON
View baru dibuat dengan nama ```json``` yang isinya akan mengembalikan seluruh task menggunakan object manager dengan filter user.
#### Buatlah path ```/todolist/json yang mengarah``` ke view yang baru kamu buat
Path ditambahkan pada ```urls.py``` di folder todolist dengan route 'json/', fungsi view 'json', dan nama dari path 'json'.
#### Lakukan pengambilan task menggunakan AJAX GET
Pengambilan task dengan ajax get dilakukan dengan membuat fungsi untuk melakukan request AJAX dengan method 'GET' kemudian response yang diberikan akan menggantikan data-data yang sebelumnya ada pada halaman user.

### AJAX POST
#### Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task
Pembuatan diawali dengan membuat suatu modal untuk menampilkan suatu pop up form yang dimanfaatkan sebagai pengisian task baru oleh user. Tombol untuk menampilkan modal tersebut dibuat dengan nama ```Add Task```.
#### Buatlah view baru untuk menambahkan task baru ke dalam database
View baru dibuat dengan nama ```add``` yang isinya akan membuat object baru dari model ```Task``` sesuai input yang diberikan user pada modal.
#### Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat
Path ditambahkan pada ```urls.py``` di folder todolist dengan route 'add/', fungsi view 'add', dan nama dari path 'add'.
#### Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
Tombol ```Save changes``` yang ada di dalam modal akan meng-trigger fungsi yang akan mengembalikan request AJAX dengan url 'add/' dan method 'POST' dengan data yang dikirimkan bersama request berupa isian dari form. Pengambilan data form dilakukan dengan menggunakan reference jquery dari form dikombinasikan bersama method .val() dan .trim().
#### Tutup modal setelah penambahan task telah berhasil dilakukan.
Penutupan modal dilakukan setelah AJAX request berhasil kemudian menggunakan potongan kode reference jquery dari form dikombinasikan bersama method .modal('hide').
#### Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page
Refresh halaman utama secara asinkronus dilakukan dengan menggunakan fungsi yang telah dijelaskan sebelumnya untuk melakukan AJAX GET request. 
