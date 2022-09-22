# Link Aplikasi Tugas 3 PBP
Link : http://katalog-lab2-pbp.herokuapp.com/mywatchlist/

# Jelaskan perbedaan antara JSON, XML, dan HTML!
##### JSON
JSON merupakan salah satu metode dalam pengiriman data yang menggunakan string JSON untuk merepresentasikan objek-objek.
JSON merupakan sebuah representasi objek yang serupa dengan javascript dan biasanya berfokus untuk mengirimkan data.

##### XML
XML merupakan salah satu metode dalam pengiriman data yang menggunakan representasi node-tree dalam penyajiannya. 
XML merupakan sebuah _markup language_ yang berfokus dalam pengiriman data tanpa mementingkan tampilan dari data-data yang disajikan.

##### HTML
HTML merupakan salah satu metode dalam pengiriman data dalam bentuk suatu halaman yang berisikan _layout_ penyajian data.
HTML merupakan sebuah _markup language_ yang tidak hanya mengirimkan data, tetapi juga menegaskan struktur dari tampilan halaman web.

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian sebuah platform dikarenakan kita membutuhkan solusi untuk mengirimkan data ke server.
Data delivery juga diperlukan agar kita dapat menampilkan data-data ke dalam suatu halaman web.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
- **Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu**<br />
Pembuatan aplikasi diawali dengan menyalakan virtual environment kemudian penginstallan requirements.txt.
Kemudian, saya menjalankan perintah ```python manage.py startapp mywatchlist``` untuk membuat aplikasi bernama mywatchlist
Selanjutnya, saya menambahkan aplikasi mywatchlist ke dalam installed_apps yang berada pada settings proyek django

- **Menambahkan path mywatchlist sehingga pengguna dapat mengakses ```http://localhost:8000/mywatchlist```**<br />
Penambahan path dilakukan dengan mengakses directory mywatchlist kemudian menambahkan perintah ```path('mywatchlist/', include(mywatchlist.urls))```
Hal ini dilakukan agar terbentuk suatu routing untuk mengakses urls yang ada pada aplikasi mywatchlist

- **Membuat sebuah model ```MyWatchList```**<br />
Pembuatan model dilakukan dengan cara membuat class yang merupakan subclass dari ```models.Model```  serta atribut-atribut sesuai dengan yang diharapkan. 
Kemudian, saya membuat migrasi dengan perintah ```python manage.py makemigrations``` untuk menyiapkan model yang saya telah buat untuk dimigrasi.
Langkah terakhir adalah melakukan migrasi dari model dengan perintah ```python manage.py migrate```.

- **Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas**<br />
Penambahan data diawali dengan membuat folder fixtures pada directory mywatclist. Kemudian, saya membuat file ```JSON``` yang diisi oleh string-string untuk 
merepresentasikan objek-objek dari model yang telah dibuat. Kemudian, saya melakukan load data ke server dengan perintah 
```python manage.py loaddata <nama_file_json_pada_fixtures>```.

- **Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam HTML, XML, JSON**<br />
Fitur penyajian data dalam bentuk html, xml, dan json dilakukan dengan menambahkan fungsi view untuk masing-masing format. Untuk format HTML, 
saya menggunakan fungsi ```render``` untuk mengembalikan HTTPresponse yang telah disisipkan template ```html``` dan data-data dari model. Untuk format XML dan JSON, 
saya menggunakan fungsi ```HttpResponse``` untuk mengembalikan http response berupa objek-objek dari model yang telah diserialisasikan ke bentuk XML dan JSON.

- **Membuat routing sehingga data di atas dapat diakses melalui URL ```http://localhost:8000/mywatchlist/html```,
 ```http://localhost:8000/mywatchlist/xml```, dan ```http://localhost:8000/mywatchlist/json```**<br />
Routing dilakukan dengan penambahan 3 path pada urlpatterns yang berada di file ```urls.py``` di folder mywatchlist.
Path-path tersebut masing-masing mengarah ke fungsi view yang telah disiapkan sebelumnya.

- **Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet** <br />
Deployment dilakukan dengan menggunakan ```HEROKU_API_KEY``` dan ```HEROKU_API_NAME``` yang sudah ada pada tugas 2. Kemudian, 
saya menyunting file ```Procfile``` dengan menambahkan perintah ```python manage.py loaddata <nama_file_json_pada_fixtures``` agar data-data 
yang sudah saya siapkan dapat dimasukkan ke dalam server saat proses deploy.

# Bukti Screenshot dari Postman
### HTML
![HTML](https://github.com/TehGaa/Tugas_2_pbp/blob/main/mywatchlist/postman_html.png)

### XML
![XML](https://github.com/TehGaa/Tugas_2_pbp/blob/main/mywatchlist/postman_xml.png)

### JSON
![JSON](https://github.com/TehGaa/Tugas_2_pbp/blob/main/mywatchlist/postman_json.png)


