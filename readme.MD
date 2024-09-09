- cara mengimplementasikan checklist secara step-by-step
1. Buat sebuah direktori baru dan lakukan git init agar direktorinya menjadi git lokal
2. Buat dan aktifkan environment yang berguna untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada pada komputer (lokal)
3. Buat dan install dependencies (framework. library, dll) yang mempermudah pembuatan website
4. Jalankan proyek django 
5. Buat aplikasi main dan masukkan 'main' ke dalam INSTALLED_APPS di settings.py, hal ini berguna agar aplikasi main terdaftar pada proyeknya
6. Agar aplikasi main dapat diakses di browser, perlu dilakukan routing dengan cara membuat urls.py di direktori main. isi urls.py dengan kode/script yang diperlukan
7. Buat model pada aplikasi main, dengan nama class Product. class ini berisi attribute name, price, pack_category, level_category, dan description. Masing-masing atribut memiliki tipe data/field yang berbeda
8. Pada views.py, buat
