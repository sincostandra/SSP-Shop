Deployment :
http://utandra-nur-sspshop.pbp.cs.ui.ac.id/

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