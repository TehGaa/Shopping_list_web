# Link Heroku
https://katalog-lab2-pbp.herokuapp.com/katalog/

# Bagan 
![Bagan](https://github.com/TehGaa/Tugas_2_pbp/blob/main/katalog/Bagan%20Tugas%202.drawio.png "Bagan Request Client Django")

# Kenapa memakai virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
Penggunaan *virtual environment* dikarenakan dalam pengerjaan beberapa proyek, terdapat beberapa *library* pada satu proyek yang versinya berbeda dengan proyek lainnya. Dengan digunakannya *virtual environment*, kita dapat menggunakan *library*-*library* dalam versi tertentu tanpa memengaruhi versi *library* untuk proyek lainnya. Kita tetap dapat menggunakan aplikasi web berbasi Django tanpa menggunakan virtual environment.


# Penjelasan poin 1-4
poin 1: Saya membuat fungsi bernama shows_katalog pada views.py yang bertujuan untuk mengembalikan HTTPS response dari request yang diminta. Response terdiri atas django         template yang telah disisipi *value-value* oleh list context. Salah satu isi dari context merupakan hasil import model CatalogItem dari models.py yang semua             *object*-nya telah dijadikan queryset. Isi lainnya dari context adalah nama dan npm.

poin 2: Saya membuat routing yang diawali dengan penambahan path pada urlpatterns di urls.py proyek django. Path tersebut dibuat agar mengikutsertakan urls.py yang ada           pada folder katalog. Kemudian saya menambahkan path default pada urls.py di folder katalog kemudian membuat path mengarah ke fungsi views yang telah saya buat           yaitu show_katalog.

poin 3: Saya memulai memetakan data ke template dengan menyunting file template terlebih dahulu. Suntingan yang saya lakukan adalah dengan menambahkan *curly brackets*           untuk pemasukkan *value* dari context, seperti nama dan npm. Kemudian saya menambahkan for loop pada django template agar dapat menampilkan seluruh data                 CatalogItem pada database.

poin 4: Saya melakukan deploy dengan menambahkan repository secrets berupa HEROKU_API_KEY dan HEROKU_API_NAME dari akun heroku saya serta aplikasi heroku yang sudah saya         persiapkan untuk tugas 2 pbp ini. Kemudian saya mengulang seluruh workflow yang sempat *failed* sehingga deploy dari dpl.yml dapat berhasil.

