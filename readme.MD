Deployment :
http://utandra-nur-sspshop.pbp.cs.ui.ac.id/


TUGAS 1

- Cara mengimplementasikan checklist secara step-by-step
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

- Bagan Client  
[Bagan Client](https://drive.google.com/file/d/1xPmsC1JxE5CGiZgdL6ru9CsByWVBobBs/view)


- fungsi git dalam pengembangan perangkat lunak  
Git adalah tools version control, yang memungkinkan developer untuk melacak perubahan kode dari waktu ke waktu (version kontrol), berkolaborasi sesama developer (kolaborasi), membuat/mengetes fitur baru tanpa memengaruhi fitur utama (branching), dan dengan platform git online (misal, GitHub) bisa dimanfaatkan sebagai backup kode

- Alasan Django dipilih sebagai pembelajaran  
Django sudah menyediakan banyak fitur bawaan yang memudahkan pengembang, seperti autentikasi, manajemen basis data, dan sistem routing. Framework ini juga menggunakan pola arsitektur yang jelas (MVT), yang membantu pemula memahami bagaimana komponen web bekerja sama.  
Selain itu, bahasa yang digunakan pada Django adalah python yang sangat ramah bagi pemula (secara spesifik mahasiswa fasilkom juga sdh cukup familiar dengan python (DDP-1)). Hal ini membuat pembelajar lebih cepat paham apa yang dilakukan kodenya.  
Dan yang terakhirm karena komunitas framework Django sudah sangat besar sehingga banyak tersedia tutorial ataupun pertanyaan yang terjawab

- Mengapa model pada Django disebut sebagai ORM  
ORM (Object-Relational Mapping) adalah teknik yang digunakan untuk menghubungkan sistem berbasis objek (seperti program Python) dengan basis data relasional. ORM memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan objek dan metode dari bahasa pemrograman tanpa harus menulis kode SQL secara manual.  
Dalam Django, data dikelola melalui model, yang merepresentasikan struktur tabel di basis data. Model ini didefinisikan menggunakan kelas Python, di mana setiap atribut pada kelas tersebut mencerminkan kolom dalam tabel. Django secara otomatis menangani berbagai tugas terkait basis data, seperti pembuatan tabel, pembacaan, pembaruan, dan penghapusan data berdasarkan definisi model.  
Maka dari itu Django disebut ORM (Object-Relational Mapping) karena Django menggunakan teknik ORM untuk menghubungkan model berbasis objek Python dengan tabel-tabel dalam basis data relasional.



TUGAS 2

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam membuat suatu platform, tentunya kita pasti akan mengirimkan data dari sebuah tech stack ke tech stack yang lain. Proses pengiriman data ini yang kita kenal sebagai data delivery. Proses ini sangat krusial karena memungkinkan komponen-komponen yang menggunakan tech stack yang berbeda dapat saling berinteraksi dan bertukar informasi. Dengan adanya data delivery, setiap komponen dalam platform dapat menjalankan fungsinya secara optimal. Misalnya, data produk yang tersimpan di database dapat dikirimkan ke frontend untuk ditampilkan pada halaman produk, atau data produk yang diinputkan oleh pengguna di frontend dapat dikirimkan ke backend untuk diproses lebih lanjut.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Kedua format tersebut memiliki kekurangan dan kelebihan masing-masing. Format data JSON memiliki keunggulan seperti formatnya yang sederhana, mudah dipahami, dan juga lebih cepat. Sedangkan XML cocok pada data yang kompleks dan membutuhkan validasi data yang sangat ketat.
Namun, dalam konteks pengembangan web, menurutku JSON lebih unggul karena formatnya lebih sederhana, ringkas, dan sintaksnya mirip dengan objek JavaScript sehingga sangat cocok untuk pengembangan web. Selain itu format JSON sangat fleksibel karena dapat digunakan dalam banyak bahasa pemrograman (hal ini membuat data delivery menjadi lebih mudah). Alasan-alasan itu juga yang membuat JSON lebih populer ketimbang XML.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method ini berfungsi sebagai exception handling ketika user/client menginput form tidak sesuai formatnya. Hal ini penting dilakukan agar kita mencegah data yang tidak sesuai masuk ke dalam database kita. Selain itu, user juga akan mendapatkan notif/pesan ketika dia salah input data sehingga akan menurunkan risiko masalah kedepannya.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token sangat penting saat membuat form di aplikasi Django kita untuk melindungi pengguna dari serangan Cross-Site Request Forgery (CSRF). Tanpa CSRF token, web kita rentan terhadap serangan di mana penyerang bisa memanipulasi aksi pengguna yang sudah login tanpa sepengetahuan mereka. Misalnya, jika seorang pelanggan yang sudah login web kita tanpa sengaja mengunjungi web berbahaya, penyerang bisa membuat script yang secara otomatis mengirim permintaan untuk menambahkan barang ke keranjang belanja, mengubah alamat pengiriman, atau bahkan melakukan pembelian. Tanpa CSRF token, server web kita tidak bisa membedakan antara permintaan yang sah dari web kita sendiri dengan permintaan palsu dari web berbahaya, karena keduanya membawa cookie sesi yang valid. CSRF token mencegah hal ini dengan memastikan bahwa setiap permintaan POST (seperti menambah ke keranjang atau checkout) harus menyertakan token unik yang hanya diketahui oleh server kita dan halaman form yang sah, sehingga permintaan dari web lain akan ditolak karena tidak memiliki token yang valid, melindungi user/client kita dari transaksi yang tidak diinginkan atau manipulasi akun.

5. Implementasi step-by-step

a. Sebelum membuat form registrasi, perlu membuat sebuah skeleton yang berfungsi sebagai kerangka views dari web kita. Kerangka ini bertujuan memastikan adanya konsistensi dan memperkecil terjadinya redundasi kode. Impelementasinya dengan membuat dir baru ('templates') pada dir utama, kemudian isi dir tsb dengan file base.html yang berfungsi sebagai template untuk yang lain. Kemudian masukkan direktori templates ini ke dalam variabel TEMPLATES yang ada di settings.py. Setelah itu, file-file yang berfungsi sebagai tampilan web perlu meng-extends base.html

b. Pada models.py, kita perlu mengubah primary key dari integer menjadi UUID. caranya dengan menambahkan atribut baru yaitu id dengan tipe data UUIDField pada class product, hal ini bertujuan untuk meningkatkan keamanan data agar data yg disimpan pada DB tidak dapat diakses oleh sembarang user

C. Buat file baru yg (forms.py) untuk membuat struktur form yang dapat menerima data Product baru, setelah itu pada views.py kita perlu import formsnya agar tampilan form dapat ditampilkan

D. Di views.py, Buat method baru yang menerima parameter request, memvalidasi input form, menyimpan input ke database, dan ngereturn tampilan create_product.html

E. Masih di views.py, Tambahkan tiap produk yg sdh diinput di form ke dalam context agar dapat ditampilkan di main.html

F. pada urls.py, import fungsi create_product dan masukkan url pattern apa yg ingin dimasukkan ketika mau membuka formnya

G. Buat file create_product.html sebagai tampilan ketika user sedang add product, dan modifikasi main.html untuk mendisplay product yang sudah diinput



POSTMAN

![e11f556b-3ea5-40e5-8d17-80ffb414dd6e](https://github.com/user-attachments/assets/87fef678-ce48-4346-87eb-5e0764fff3c1)
![3a6408b6-2f8e-4ffb-8fa6-8ba0cede9ddc](https://github.com/user-attachments/assets/2a4fa79d-cd71-4102-bdf7-6debf8e8f355)
![ee7cda68-a743-4178-947f-265970c7e26e](https://github.com/user-attachments/assets/17092805-ef66-4bd9-925c-58547a432361)
![ea02c635-c113-4205-a99d-04741cad2ad2](https://github.com/user-attachments/assets/abb99262-bcd9-4706-9ed1-a358d40b22ae)