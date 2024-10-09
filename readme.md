Syauqi Muhammad Yasman\
2306275752\
PBP D

# Tugas 2
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat repository di github kemudian clone repository tersebut
2. Mengaktifkan virtual environment
3. Menginstall Django dan requirements lainnya
4. Membuat proyek dan menambah izinkan localhost
5. Membuat aplikasi main
6. Membuat model dan migrasi
7. Mengonfigurasi view dan url
8. Membuat template
### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan request klien Django](https://github.com/user-attachments/assets/8a0853b0-0018-4088-be57-54d16b5a9a10)
Pengguna dengan web browser akan meminta sebuah request melalui urls.py, kemudian urls.py akan memenuhi permintaan pengguna, apakah pengguna hanya meminta views atau juga dengan model, jika pengguna juga meminta model, maka models.py akan mengambilkan data yang berada di database. Kemudian data tersebut ditampilkan pada oleh views.py ke dalam berkas html.

### Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai version control. Di mana git bekerja untuk menyimpan seluruh perubahan yang terjadi ketika kita sedang mengembangkan sebuah perangkat lunak. Dengan menggunakan git, kita dapat melakukan rollback jika terjadi sebuah kesalahan besar di tengah pengembangan perangkat lunak dengan mudah, karena versi-versi sebelumnya telah disimpan oleh git.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django menggunakan bahasa pemrograman Python sebagaimana yang kita pelajari pada mata kuliah Dasar-dasar Pemrograman 1. Selain itu, Django juga memiliki komunitas yang besar, sehingga tersedia banyak dukungan yang beredar di internet terkait masalah-masalah yang sering terjadi khususnya bagi seorang permula.

### Mengapa model pada Django disebut sebagai ORM?
Django disebut sebagai ORM karena memungkinkan developer untuk memetakan objek Python ke dalam tabel-tabel di database relasional, sehingga interaksi dengan database dapat dilakukan tanpa menulis query SQL secara langsung.

# Tugas 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan untuk pengiriman sebuah data baik dari klien ke server maupun server ke klien. Dengan implementasi data delivery pada sebuah web platform, kita dapat membuat interaksi dua arah dari klien ke server dan sebaliknya. Contohnya adalah klien menambahkan sebuah produk ke server dan server menampilkan produk-produk yang tersedia ke klien.
### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Keduanya memiliki kelebihan dan kekurangannya masing-masing, JSON memiliki keterbatasan tipe data dibandingkan dengan XML, XML mendukung tipe data binary dan timestamp sementara JSON tidak. Namun, JSON memiliki strukturnya yang lebih mudah dipahami dan memiliki waktu parsing lebih cepat daripada XML. Dari keterbatasan tipe data yang didukung oleh JSON, dan mungkin jarang digunakan, dibandingkan dengan struktur yang simpel dan kecepatannya, menjadikan JSON lebih mudah digunakan dalam pengembangan ketimbang XML, sehingga membuatnya dapat lebih populer.
### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi method tersebut adalah untuk memverifikasi apakah input yang diisi oleh pengguna sesuai dengan apa yang telah kita rancang pada model. Hal tersebut dilakukan untuk mencegah terjadinya error karena perbedaan tipe data.
### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CRSF Token merupakan token random yang sulit ditebak dan digunakan untuk memverifikasi apakah sebuah tindakan yang dilakukan berasal benar-benar dari pengguna. Tanpa adanya CRSF Token, penyerang dapat membuat request tanpa persetujuan pengguna ke sebuah website yang memiliki kerentanan CRSF. Hal tersebut dapat dilakukan penyerang melalui website berbahaya yang berusaha mengirimkan request ke suatu website yang sedang menjalankan session kita.

Tanpa token:
```
http://www.mybank.com/transfer?to=123456&amount=10000
```
Dengan token:
```
http://www.mybank.com/transfer?to=123456&amount=10000&token=31415926535897932384626433832795028841971
```
Dengan token CRSF, penyerang tidak bisa menebak token tersebut, sehingga request yang dikirimkan penyerang ditolak.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
1. Membuat base.html
2. Menambahkan base.html template ke settings
3. Membuat main.html melakukan extend terhadap base.html
4. Menambahkan uuid ke model sebagai key
5. Menjalankan migrasi baru
6. Membuat form input
7. Menampilkan data di main
8. Membuat pengembalian data xml dan json

### Postman
#### XML
![Postman XML](https://github.com/user-attachments/assets/6c8404a7-5a15-4f2f-b12f-fa151e226784)
#### XML/id
![Postman XML with id](https://github.com/user-attachments/assets/c84eb116-dee2-48b2-8a16-448c8f3236dc)
#### JSON
![Postman JSON](https://github.com/user-attachments/assets/dc0c4212-e619-478c-b6c4-4249e647195f)
#### JSON/id
![Postman JSON with id](https://github.com/user-attachments/assets/b68875e1-e52f-4767-993c-1dc63ffef844)

# Tugas 4
### Apa perbedaan antara HttpResponseRedirect() dan redirect()
Dalam kasus HttpResponseRedirect() argumen pertama hanya dapat berupa url. Sementara redirect() yang pada akhirnya akan mengembalikan HttpResponseRedirect() dapat menerima model, tampilan, atau url sebagai argumen. Jadi redirect() sedikit lebih fleksibel ketimbang HttpResponseRedirect().
### Jelaskan cara kerja penghubungan model Product dengan User!
Model dengan Product dihubungkan dengan many-to-one relationships, di mana pada Product, terdapat sebuah key yang merujuk ke User sebagai pemilik. Misalkan kita memiliki 100 Product, dan terdapat 50 Product memiliki key 1, maka 50 Product tersebut terhubung ke User dengan id 1, sementara 50 Product lainnya memiliki key 2, maka sisa Product tersebut terhubung ke User dengan id 2.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
| Authentication                                                                                               | Authorization                                                                                              |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Proses memverifikasi identitas pengguna sebelum memberi mereka izin untuk mengakses sistem, akun, atau file. | Proses memverifikasi tingkat akses pengguna ke sistem, akun, atau file.                                    |
| Tujuan utamanya adalah untuk memverifikasi identitas pengguna.                                               | Tujuan utamanya adalah memastikan bahwa hanya pengguna yang berwenang yang dapat melakukan akses tertentu. |
| Contoh mekanismenya adalah nama pengguna dan kata sandi atau OTP (one time pin).                             | Contoh mekanismenya adalah Role-Based Access Control (RBAC).                                               |
Pada saat pengguna melakukan login, proses aunthentication dilakukan, fungsinya untuk memverifikasi identitas pengguna sebelum memberi izin untuk mengakses sistem (website).

Authentication pada Django diimplementasi menggunakan dekorator @login_required() yang menandakan bahwa halaman tersebut membutuhkan authentication sebelum halaman tersebut dapat diakses. Ketika pengakses telah mendapatkan session yang valid, barulah halaman tersebut dapat diakses. Sementara untuk authorization dapat dilakukan dengan menambahkan field role pada model user, role tersebut yang kemudian akan dicek sebelum menampilkan apa saja atau halaman apa yang dapat diakses oleh role tersebut.
### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan session yang diidentifikasi melalui cookie session ID. Cookie tersebut dikirim ke browser dan digunakan untuk mencocokkan pengguna dengan session yang disimpan di server.

Cookies dapat digunakan untuk berbagai keperluan seperti menyimpan preferensi pengguna, pelacakan aktivitas, shopping cart, dan token keamanan.

Tidak semua cookies aman, dan ada beberapa flag penting yang harus digunakan (seperti Secure, HttpOnly, dan SameSite) untuk memastikan bahwa cookies tidak dapat disalahgunakan oleh pihak ketiga atau dalam serangan keamanan seperti XSS atau CSRF.
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat fungsi untuk melakukan registrasi
2. Membuat template register form
3. Menambah register ke urls
4. Membuat fungsi untuk melakukan login 
5. Membuat template login form 
6. Menambah login ke urls
7. Membuat fungsi untuk melakukan logout
8. Menambahkan tombol logout di main
9. Menambahkan logout ke urls
10. Menambahkan Restriksi ke halaman create product
11. Menggunakan cookie ketika login dan logout
12. Menghubungkan user dengan model
13. Membuat migrasi baru
14. Membuat setingan untuk environtment production


### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. Inline Styles
```html
<div style="color: red;">Text</div>
```
2. ID Selector
```css
#myElement {
    color: blue;
}
```
3. Class, Attribute, dan Pseudo-classes Selector
```css
.myClass {
    color: green;
}

input[type=submit] {
    color: white;
}

button:hover {
    color: red;
}
```
4. Type Selector (Element Selector)
```css
div {
    color: yellow;
}
```
5. Universal Selector
```css
* {
    color: black;
}
```
### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Karena aplikasi web tidak hanya dibuka melalui satu tipe perangkat, aplikasi web dibuka melalui smartphone, laptop, desktop, dan lain-lain. Sehingga untuk mengakomodasi semua itu, diciptakanlah responsive website yang dapat menyesuaikan bentuknya terhadap jenis perangkat dan besar layar yang digunakan.

Contoh aplikasi yang sudah menerapkan responsive design:
1. Happy Farmer Shop
2. PBP Fasilkom UI
3. Google

Contoh aplikasi yang belum menerapkan responsice design:
1. SIAK NG
2. Open JDK
3. Google Docs
### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin: Ruang di luar elemen (memisahkan dari elemen lain).
```css
.element {
    margin: 20px;
}
```
- Border: Garis di sekitar elemen (membatasi elemen).
```css
.element {
    border: 2px solid black;
}
```
- Padding: Ruang di dalam elemen (antara konten dan border).
```css
.element {
    padding: 10px;
}
```
Implementasi gabungan:
```css
button {
    border: 2px solid black;
    margin-left: 10px;
    padding: 3px;
}
```
### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Tentu! Flexbox dan Grid Layout adalah dua model layout di CSS yang membantu dalam menyusun elemen di halaman web. Masing-masing memiliki karakteristik dan kegunaan tersendiri.

1. Flexbox (Flexible Box Layout)

Konsep:

Flexbox adalah model layout satu dimensi yang memungkinkan pengaturan elemen dalam baris atau kolom. Dengan flexbox, elemen dapat dengan mudah diatur agar responsif dan fleksibel, menyesuaikan ruang yang tersedia.

Kegunaan:

- Penataan Elemen: Cocok untuk mengatur elemen dalam satu dimensi, seperti menu navigasi atau tombol.
- Penataan Responsif: Elemen dapat tumbuh atau menyusut sesuai dengan ukuran kontainer.
- Alignment: Mempermudah pengaturan alignment dan distribusi ruang antar elemen.

2. Grid Layout

Konsep:
Grid Layout adalah model layout dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Ini memberi kontrol lebih besar atas tata letak elemen di halaman.

Kegunaan:
- Penataan Kompleks: Cocok untuk desain yang lebih kompleks, seperti grid gambar, tata letak halaman, atau dashboard.
- Pengaturan Kolom dan Baris: Memungkinkan pembuatan kolom dan baris yang dapat disesuaikan dengan ukuran kontainer.
- Spasi dan Area: Dapat mendefinisikan area grid untuk menempatkan elemen secara spesifik.
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Menambah middleware WhiteNoise
2. Menambah static url di settings
3. Membuat directory static dan global.css
4. Menambah link css di base.html
5. Mengimplementasikan Edit dan Delete

# Tugas 5

### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript memungkinkan untuk menambahkan interaktivitas ke halaman web. Pengguna dapat berinteraksi dengan elemen-elemen seperti tombol, form, menu, atau konten yang berubah dinamis, tanpa perlu memuat ulang halaman.

JavaScript mendukung Asynchronous programming, terutama dengan AJAX dan fetch(), memungkinkan aplikasi untuk mengambil atau mengirim data ke server tanpa perlu memuat ulang halaman.

JavaScript bekerja di hampir semua browser modern tanpa perlu konfigurasi tambahan. Ini membuatnya sangat kompatibel dan mempermudah pengembangan aplikasi yang dapat berjalan di berbagai platform, termasuk desktop, tablet, dan perangkat seluler.
### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
fetch merupakan fungsi asynchronous dan mengembalikan promise, yang artinya operasi pengambilan data dari server terjadi di latar belakang tanpa menghentikan eksekusi kode lain. Penggunaan await akan membuat javascript menunda eksekusi kode hingga promise yang dikembalikan oleh fetch terselesaikan. Oleh karena itu, jika tidak menggunakan await, kita hanya akan mendapatkan promise, karena data yang ambil oleh fetch belum selesai. 
### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Decorator csrf_exempt diperlukan ketika kita ingin menghindari pengecekan CSRF pada view yang akan dipanggil oleh AJAX POST request. Namun, penggunaannya perlu hati-hati, dan sebisa mungkin, sebaiknya tetap menerapkan CSRF protection dengan menyertakan CSRF token dalam setiap AJAX POST.
### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Bagian frontend merupakan bagian yang dilihat oleh client. Pada aplikasi web, client memiliki akses untuk memodifikasi bagian frontend itu sendiri, misalnya lewat developer tools. Hal ini bisa saja dimanfaatkan seseorang untuk menonaktifkan pembersihan input yang terdapat pada frontend. Jika tidak ada pembersihan ulang di backend, maka input yang diinputkan oleh seseorang yang menonaktifkan pembersihan input pada frontend akan masuk sebagai input yang valid. Berbeda halnya jika terdapat pembersihan input kembali di backend. Karena backend berjalan di server, maka client tidak memiliki akses untuk menonaktifkan pembersihan input tersebut. Sehingga, input yang masuk dapat diverifikasi kembali jika memang input tersebut berbahaya.
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Menambahkan pesan error pada login
2. Membuat fungsi baru pada views.py yang menangani form submit dari ajax
3. Menambahkan fungsi baru tersebut ke urls.py
4. Menambahkan filter pada show_xml dan show_json
5. Membuat tampilan product diambil menggunakan ajax
6. Membuat modal form untuk menambah data menggunakan ajax
7. Melakukan pembersihan input backend dan frontend