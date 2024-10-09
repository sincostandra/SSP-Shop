# Deployment : 
http://utandra-nur-sspshop.pbp.cs.ui.ac.id/

## Tugas 5
<details>
Pertanyaan  

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!  
JavaScript memungkinkan elemen-elemen pada halaman web untuk merespons aksi pengguna (seperti klik, input, atau scroll) tanpa perlu memuat ulang halaman (Event Driven dan Asinkronus), selain itu Dengan AJAX, JavaScript memungkinkan pengambilan dan pengiriman data dari server tanpa perlu memuat ulang seluruh halaman, sehingga meningkatkan efisiensi dan kecepatan.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?  
await digunakan untuk menunggu hasil dari operasi asynchronous (seperti fetch()). Ketika menggunakan await, kode berikutnya tidak akan dieksekusi sampai promise yang dihasilkan oleh fetch() diselesaikan (resolved atau rejected). Jika tidak mengguanakan await saat memanggil fetch, maka kode setelah fetch akan tetap jalan dan berpotensi mengalami error karena fetchnya belum selesai.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?  
Decorator csrf_exempt membuat Django tidak perlu mengecek keberadaan csrf_token pada POST request yang dikirimkan ke view/fungsi. Kita perlu mematikan csrfnya karena AJAX tidak secara otomatis menyertakan token CSRF (Tidak seperti formulir HTML tradisional yang secara otomatis menyertakan token CSRF).
Namun, penggunaannya harus hati-hati karena dapat membuat view rentan terhadap serangan CSRF.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?   
Melakukan pembersihan data hanya di frontend tidak cukup karena kode JavaScript di sisi klien bisa dimanipulasi oleh pengguna atau peretas, sehingga tidak bisa dianggap sepenuhnya aman. Oleh karena itu, sangat penting melakukan pembersihan di backend untuk memastikan bahwa data yang masuk ke sistem adalah valid, terlepas dari apakah pengguna telah melakukan bypass terhadap validasi input di frontend atau tidak.  


Implementasi  


1. AJAX GET
Lakukan import csrf_exempt dan require_POST dari django.views.decorators, Decorator csrf_exempt akan membuat django tidak cek keberadaan csrf_token karena biasanya ajax tidak generate token itu. Decorator require_POST membuat fungsinya hanya bisa diakses ketika pengguna mengirimkan POST request ke fungsi tsb. Jadi formnya tidak bisa diakses user lain

Di file views.py buat sebuah fungsi yang menerima parameter request dengan nama create_product_ajax. Untuk setiap field lakukan request.POST.get dan return HttpRespone(b"CREATE", status = 201).  

Lakukan routing di urls.py  

Langkah selanjutya menghapus variabel yang menerima products dari user dan memindahkannya ke show_json, karena dari sekarang, pengambilan objek-objek product diambil dari endpoint /json  

Hapus juga script html untuk menampilkan card productnya dan ganti dengan sebuah tag baru dengan id product_cards  

Buat blok script js baru di main.html, isi script tsb dengan async function yang akan mengambil (parse) data produk dari json, tambahkan juga async function baru di script dengan nama refreshProducts, fungsi ini akan me-refresh data products secara asinkronus (pastikan fungsi ini mengimplementasikan await)

2. AJAX POST
Tambahkan script untuk membuat Modal di main.html di bawah div dengan id product_cards, tambahkan juga function untuk membuat class modal karena dari vanilla tailwind css tidak menyediakan built-in modal  

Tambahkan button untuk menambahkan data via ajax, buat fungsi di script js dengan nama addProduct, function ini akan menyimpan data ke json dan akan close modal ketika inputnya berhasil  

Tambahkan juga event listener untuk masing-masing button pada modal  

3. XSS  
Tambahkan strip tags setiap pada function create_product_ajax di views.py, strip tags ini akan digunakan untuk setiap fields nonnumerik agar menghindari XSS dari peretas tambahkan juga function clean di masing-masing field pada file forms.py. Bersihkan data dengan DOMPurify untuk melakukan pembersihan di frontend  
</details>












## TUGAS 4
<details>
Pertanyaan  

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!  
    Urutan prioritas pengambilan CSS selector mengikuti specificity. Urutannya dari yang terendah hingga tertinggi:

    1. Elemen HTML (Type selectors)  
    2. Class selectors  
    3. ID selectors  
    4. Inline styles  
    5. !important.  

    Semakin spesifik selektor, semakin tinggi prioritasnya. Jika ada dua atau lebih selector yang memiliki tingkat specificity yang sama, aturan yang berada paling bawah dalam file CSS akan diambil.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!  
Responsive design memungkinkan sebuah aplikasi web untuk menyesuaikan tampilannya di berbagai perangkat dengan ukuran layar yang berbeda, seperti desktop, tablet, dan smartphone. Ini penting karena pengguna/client web kita diisi oleh mayoritas pengguna smartphone (sekitar 90%) (sumber: https://www.statista.com/statistics/1289755/internet-access-by-device-worldwide/) sehingga web kita menjadi lebih mudah diakses oleh mayoritas pengguna internet  
Contoh web/aplikasi yang responsive: x.com  
Contoh web/aplikasi yang belum responsive: pertamina.com  

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!  
Margin: Ruang di luar border elemen. sebagai pengatur jarak antara elemen dan elemen lain di sekitarnya.
Border: Garis di sekeliling elemen yang memisahkan padding dan margin. Kita dapat mengubah ketebalan, warna, dan jenisnya.
Padding: Ruang antara konten elemen dan border-nya. Padding memperbesar area dalam elemen tanpa menambah ukuran luar.

Implementasi margin, border, dan padding
```css
  div {
  margin: 20px; /* Jarak 20px dari elemen lain */
  border: 2px solid black; /* Border hitam 2px */
  padding: 15px; /* Jarak konten ke border sebesar 15px */
}
```
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!  
Flexbox: Layout yang lebih fleksibel untuk mengatur elemen dalam satu dimensi, baik secara horizontal atau vertikal. Kegunaannya adalah untuk memudahkan distribusi elemen dalam satu baris atau kolom dengan kontrol yang lebih baik untuk alignment dan space distribution.  
Grid Layout: Layout yang bekerja dalam dua dimensi, yaitu baris dan kolom.  Cocok unntuk membuat tata letak yang kompleks dengan area yang dapat dibagi-bagi secara rapi.

### Implementasi Step-by-step
- Static files django  
    Pada settings.py, kita perlu menambahkan STATIC_ROOT yang menentukan absolute path ke direktori static files ketika menjalankan perintah collectstatic pada proyek. STATIC_ROOT ini nantinya berguna untuk melakukan menyediakan path konten statis pada akses production (DEBUG=False pada settings.py).  
    Tambahkan middleware WhiteNoise sehingga Django dapat mengelola file statis secara otomatis dalam mode produksi (DEBUG=False) tanpa perlu konfigurasi yang kompleks.

- Menambahkan tailwind ke aplikasi  
    Pada base html, tambahkan tag <meta name="viewport"> agar halamanw eb menjadi responsive, setelah itu sambungkan template django dengan tailwind dengan memanfaatkan script CDN dari tailwind  

- Fitur Edit Product  
    Pada views.py Buat sebuah method yang mengambil objects product dengan id yang spesifik (pk = id), kemudian buat formnya menggunakan MoodEntryForm (dengan instance product yang kita definisikan tadi) dan cek apakah formnya valid. Jika valid, simpan input dan kembali ke show_main.   
    Buat berkas HTML pada main/templates sebagai tampilan ketika sedang mengedit product, tambahkan juga button untuk mengedit produk di main.html  
    Aur kembali juga urls.py agar urlnya dapat diakses oleh client

- Fitur Delete Product  
    Pada views.py Buat sebuah method yang mengambil objects product dengan id yang spesifik (pk = id), setelah itu panggil method delete (bawaan django), return page ke main page.   
    Tambahkan Button pada main.html dan lakukan routing pada urls.py  

- Navigation Bar  
    Buat berkas html dengan nama navbar.html di root /templates. Lakukan styling pada navbar dengan tailwind. Kemudian, tautkan navbar tersebut ke dalam main.html, create_mood_entry.html, dan edit_mood.html yang berada di subdirektori main/templates/ dengan menggunakan tags include

- Global css  
    Buat sebuah file global.css di /static/ss pada root dir, file ini berguna sebagai template style yang bisa kita gunakan kedepannya.  
    Untuk menambahkan template ini ke file yg lain, gunakan sintaks {% load static %}  

- Styling page login dan register
    Lakukan styling pada masing-masing page sesuai ide awal

- Styling create_product dan edit_product  
    Lakukan styling pada masing-masing page dan Lakukan extend/load base.html dan static css

- Styling Halaman Home  
    Buat sebuah berkas bernama card_info.html pada main/templates, berkas ini sebagai tampilan untuk info spt nama, kelas, dan shop_name

    Buat berkas card_product.html, berkas ini sebagai tampilan untuk masing-masing product.  

    Buat berkas gambar sebagai tampilan ketika produk belum ada, simpan berkas ini di static/image

    Pada main.html, masukkan semua berkas tadi sesuai styling yang dibuat.  
</details>
    
## TUGAS 3
<details>
### Pertanyaan
1. Perbedaan antara HttpResponseRedirect() dan redirect()  
Secara singkat, redirect() merupakan shortcut untuk langsung mengarahkan user atau client ke URL yang sesuai, sedangkan HttpResponeRedirect() merupakan versi yang lebih kompleks dari redirect() karena memberikan kontrol leih untuk melakukan modifikasi sebelum return (misal, kita bisa menggunakan method set_cookies)

2. Cara kerja penghubungan Product dengan User  
Pada models di app main, kita buat sebuah attribut baru pada model Product (misal bernama user), attribut ini diisi dengan field ForeignKey (ini akan memastikan bahwa Product hanya akan terasosiasikan dengan seorang User). Setelah itu, pada method create_product, kita jg harus memastikan value dari product.user adalah request.user

3. Authentication merupakan proses verifikasi identitas pengguna, ini bertujuan untuk memastikan bahwa user/client adalah benar sesuai klaim mereka (misal dari login username dan password). Sedangkan Authorization adalah proses untuk menentukan apa saja yang boleh dilakukan oleh user yang sudah diautentikasi (misal, melakukan penambahan produk).  
Authentication Django menggunakan sisten auth bawaan yang tersedia yaitu django.contrib.auth, dan untuk Authorization mmenggunakan django.contrib.auth.decorators
### Implementasi Authentication  
```python
from django.contrib.auth import authenticate, login, logout
    ...
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
    ...
```  
### Implementasi Authorization
```python
from django.contrib.auth.decorators import login_required
    ...
    @login_required(login_url='/login')
    def show_main(request):
        products = Product.objects.filter(user=request.user)
    ...
```

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Pada saat user/client berhasil login, Django membuat session yang disimpan di server, session ini memiliki session key yang unik dan dikirimkan ke browser dalam bentuk cookies. Setiap kali ada request, Django akan ngecek cookies (sessionid) apakah valid atau tidak.  
Kegunaan lain dari cookies adalah untuk menyimpan data yang tidak sensitif, seperti preferensi pengguna (tema, bahasa, dll). Namun, tidak semua coookies aman, misalnya cookies pada web yang tidak secure (hanya menggunakan http dan data yg dikirim tidak dienkripsi) akan sangat rentan terhadap pencurian data melalui Man-in-the-Middle attacks.

### Implementasi Step-by-step

- Form registrasi  
    Di dalam views.py, import UserCreationForm yang sudah disediakan oleh Django untuk memudahkan pembuatan dan dalam file yg saama buat sebuah method baru bernama register untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.  
    Setelah itu buat sebuah berkas HTML baru pada dir main/templates sebagai struktur tampilan ketika client mengakses url register. pastikan jg berkas ini mengeksten kerangka dari base.html.  
    Kemudian lakukan routing url pada urls.py agar dapat diakses pada web client/user

- Form Login  
    Mirip dengan registrasi, pada views.py kita perlu mengimport import authenticate, login, dan AuthenticationForm. Kemudian buat sebuah method bernama login_user (method ini akan memvalidasi input dari client/user dan jika valid, maka Django akan membuat session untuk client). kemudian buat file HTML baru bernama login.html untuk struktur tampilan ketika client login, dan lakukan routing pada urls.py

- Form Logout
    Lakukan hal yang sama sepertis sebelumnya, namun kali ini yg diimport adalah logout dan buat button pada main.html yang ketika dipencet akan mengarahkan user ke url logout, jangan lupa untuk melakukan routing pada urls.py  

- Restriksi akses  
    Setelah berhasil membuat forms register, login, dan logout. Sekarang client/user harus mempunyai akun agar dapat mengakses halaman main, maka dari itu kita perlu membatasi akses kepada user yg blm login. Implementasinya menggunakan dekorator @login_required. dekorator ini mengharuskan user/client untuk masuk (login) terlebih dahulu sebelum dapat mengakses suatu halaman main. Arahkan juga user ke halaman login jika usernya belum login  

- Menggunakan Data Dari Cookies untuk menampilkan username dan last login dari user  
    Pada views.py, tambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas. Pada method login_user, kita mengganti return dari yg awalnya redirect() menjadi HttpResponeRedirect() dan simpan responnya pada variabel respone, kemudian dari variabel respone kita panggil method set_cookie untuk membuat cookie last login dan menyimpannya pada variabel respone. kemudian pada method show_main, tambahkan key/attribute baru yg namanya last_login, key ini berisi value dari request.COOKIES['last_login'] yang berfungsi untuk menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web. Setelah itu kita perlu memodifikasi method logout_user dengan menambahkan response.delete_cookies() untuk menghapus cookies yang ada. Terakhir, tampilkan context last_login pada main.html  

- Menghubungkan Product dengan User  
pada models.py, lakukan import User dari django.contrib.auth.models, dan pada class Product buat sebuah attribut baru yg bernama user. attribut ini diisi dengan field ForeignKey (ini akan memastikan bahwa Product hanya akan terasosiasikan dengan seorang User). Setelah itu, pada method create_product, kita simpan user yang mengisi form create_product (request.user) pada variabael product.user. Kemudian pada method show main, modifikasi kode sehingga products hanya menerima Product sesuai usernya dengan cara Product.objects.filter(user=request.user). Kemudian ubah value context khususnya di key 'name', menjadi request.user.username agar username dapat ditampilkan di show_main
</details>

## TUGAS 2
<details>
### Pertanyaan
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?  
Dalam membuat suatu platform, tentunya kita pasti akan mengirimkan data dari sebuah tech stack ke tech stack yang lain. Proses pengiriman data ini yang kita kenal sebagai data delivery. Proses ini sangat krusial karena memungkinkan komponen-komponen yang menggunakan tech stack yang berbeda dapat saling berinteraksi dan bertukar informasi. Dengan adanya data delivery, setiap komponen dalam platform dapat menjalankan fungsinya secara optimal. Misalnya, data produk yang tersimpan di database dapat dikirimkan ke frontend untuk ditampilkan pada halaman produk, atau data produk yang diinputkan oleh pengguna di frontend dapat dikirimkan ke backend untuk diproses lebih lanjut.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  
Kedua format tersebut memiliki kekurangan dan kelebihan masing-masing. Format data JSON memiliki keunggulan seperti formatnya yang sederhana, mudah dipahami, dan juga lebih cepat. Sedangkan XML cocok pada data yang kompleks dan membutuhkan validasi data yang sangat ketat.
Namun, dalam konteks pengembangan web, menurutku JSON lebih unggul karena formatnya lebih sederhana, ringkas, dan sintaksnya mirip dengan objek JavaScript sehingga sangat cocok untuk pengembangan web. Selain itu format JSON sangat fleksibel karena dapat digunakan dalam banyak bahasa pemrograman (hal ini membuat data delivery menjadi lebih mudah). Alasan-alasan itu juga yang membuat JSON lebih populer ketimbang XML.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?  
Method ini berfungsi sebagai exception handling ketika user/client menginput form tidak sesuai formatnya. Hal ini penting dilakukan agar kita mencegah data yang tidak sesuai masuk ke dalam database kita. Selain itu, user juga akan mendapatkan notif/pesan ketika dia salah input data sehingga akan menurunkan risiko masalah kedepannya.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?  
CSRF token sangat penting saat membuat form di aplikasi Django kita untuk melindungi pengguna dari serangan Cross-Site Request Forgery (CSRF). Tanpa CSRF token, web kita rentan terhadap serangan di mana penyerang bisa memanipulasi aksi pengguna yang sudah login tanpa sepengetahuan mereka. Misalnya, jika seorang pelanggan yang sudah login web kita tanpa sengaja mengunjungi web berbahaya, penyerang bisa membuat script yang secara otomatis mengirim permintaan untuk menambahkan barang ke keranjang belanja, mengubah alamat pengiriman, atau bahkan melakukan pembelian. Tanpa CSRF token, server web kita tidak bisa membedakan antara permintaan yang sah dari web kita sendiri dengan permintaan palsu dari web berbahaya, karena keduanya membawa cookie sesi yang valid. CSRF token mencegah hal ini dengan memastikan bahwa setiap permintaan POST (seperti menambah ke keranjang atau checkout) harus menyertakan token unik yang hanya diketahui oleh server kita dan halaman form yang sah, sehingga permintaan dari web lain akan ditolak karena tidak memiliki token yang valid, melindungi user/client kita dari transaksi yang tidak diinginkan atau manipulasi akun.

### Implementasi step-by-step

a. Sebelum membuat form registrasi, perlu membuat sebuah skeleton yang berfungsi sebagai kerangka views dari web kita. Kerangka ini bertujuan memastikan adanya konsistensi dan memperkecil terjadinya redundasi kode. Impelementasinya dengan membuat dir baru ('templates') pada dir utama, kemudian isi dir tsb dengan file base.html yang berfungsi sebagai template untuk yang lain. Kemudian masukkan direktori templates ini ke dalam variabel TEMPLATES yang ada di settings.py. Setelah itu, file-file yang berfungsi sebagai tampilan web perlu meng-extends base.html

b. Pada models.py, kita perlu mengubah primary key dari integer menjadi UUID. caranya dengan menambahkan atribut baru yaitu id dengan tipe data UUIDField pada class product, hal ini bertujuan untuk meningkatkan keamanan data agar data yg disimpan pada DB tidak dapat diakses oleh sembarang user

C. Buat file baru yg (forms.py) untuk membuat struktur form yang dapat menerima data Product baru, setelah itu pada views.py kita perlu import formsnya agar tampilan form dapat ditampilkan

D. Di views.py, Buat method baru yang menerima parameter request, memvalidasi input form, menyimpan input ke database, dan ngereturn tampilan create_product.html

E. Masih di views.py, Tambahkan tiap produk yg sdh diinput di form ke dalam context agar dapat ditampilkan di main.html

F. pada urls.py, import fungsi create_product dan masukkan url pattern apa yg ingin dimasukkan ketika mau membuka formnya

G. Buat file create_product.html sebagai tampilan ketika user sedang add product, dan modifikasi main.html untuk mendisplay product yang sudah diinput



### POSTMAN  
XML
![e11f556b-3ea5-40e5-8d17-80ffb414dd6e](https://github.com/user-attachments/assets/87fef678-ce48-4346-87eb-5e0764fff3c1)

JSON
![3a6408b6-2f8e-4ffb-8fa6-8ba0cede9ddc](https://github.com/user-attachments/assets/2a4fa79d-cd71-4102-bdf7-6debf8e8f355)

XML by id
![ee7cda68-a743-4178-947f-265970c7e26e](https://github.com/user-attachments/assets/17092805-ef66-4bd9-925c-58547a432361)

JSON by id
![ea02c635-c113-4205-a99d-04741cad2ad2](https://github.com/user-attachments/assets/abb99262-bcd9-4706-9ed1-a358d40b22ae)
</details>

## TUGAS 1

<details>
### Pertanyaan
1. Fungsi git dalam pengembangan perangkat lunak  
Git adalah tools version control, yang memungkinkan developer untuk melacak perubahan kode dari waktu ke waktu (version kontrol), berkolaborasi sesama developer (kolaborasi), membuat/mengetes fitur baru tanpa memengaruhi fitur utama (branching), dan dengan platform git online (misal, GitHub) bisa dimanfaatkan sebagai backup kode

2. Alasan Django dipilih sebagai pembelajaran  
Django sudah menyediakan banyak fitur bawaan yang memudahkan pengembang, seperti autentikasi, manajemen basis data, dan sistem routing. Framework ini juga menggunakan pola arsitektur yang jelas (MVT), yang membantu pemula memahami bagaimana komponen web bekerja sama.  
Selain itu, bahasa yang digunakan pada Django adalah python yang sangat ramah bagi pemula (secara spesifik mahasiswa fasilkom juga sdh cukup familiar dengan python (DDP-1)). Hal ini membuat pembelajar lebih cepat paham apa yang dilakukan kodenya.  
Dan yang terakhirm karena komunitas framework Django sudah sangat besar sehingga banyak tersedia tutorial ataupun pertanyaan yang terjawab

3. Mengapa model pada Django disebut sebagai ORM  
ORM (Object-Relational Mapping) adalah teknik yang digunakan untuk menghubungkan sistem berbasis objek (seperti program Python) dengan basis data relasional. ORM memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan objek dan metode dari bahasa pemrograman tanpa harus menulis kode SQL secara manual.  
Dalam Django, data dikelola melalui model, yang merepresentasikan struktur tabel di basis data. Model ini didefinisikan menggunakan kelas Python, di mana setiap atribut pada kelas tersebut mencerminkan kolom dalam tabel. Django secara otomatis menangani berbagai tugas terkait basis data, seperti pembuatan tabel, pembacaan, pembaruan, dan penghapusan data berdasarkan definisi model.  
Maka dari itu Django disebut ORM (Object-Relational Mapping) karena Django menggunakan teknik ORM untuk menghubungkan model berbasis objek Python dengan tabel-tabel dalam basis data relasional.

### Cara mengimplementasikan checklist secara step-by-step
1. Buat sebuah direktori baru dan lakukan git init agar direktorinya menjadi git lokal
2. Buat dan aktifkan environment yang berguna untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada pada komputer (lokal)
3. Buat dan install dependencies (framework. library, dll) yang mempermudah pembuatan website
4. Jalankan proyek django 
5. Buat aplikasi main dan masukkan 'main' ke dalam INSTALLED_APPS di settings.py, hal ini berguna agar aplikasi main terdaftar pada proyeknya
6. Agar aplikasi main dapat diakses di browser, perlu dilakukan routing dengan cara membuat urls.py di direktori main. isi urls.py dengan kode/script yang diperlukan
7. Buat model pada aplikasi main, dengan nama class Product. class ini berisi attribute name, price, pack_category, level_category, dan description. Masing-masing atribut memiliki tipe data/field yang berbeda
8. Pada views.py, buat sebuah kode/logic yang akan returns sebuah render yang berisi context yang akan ditampilkan melalui templates
9. Setelah itu lakukan routing pada urls.py di directory/aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
10. Push ke PWS, dengan cara membuat proyek baru pada website, dan melakukan git remote add, setelah itu lakukan add commit and push
11. Buat readme.md

### Bagan Client  
![bagan](https://github.com/user-attachments/assets/54eccdf7-cc4d-4e54-bae7-339a34810116)

</details>