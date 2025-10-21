# 🕵️‍♂️ Steganografi Gambar Berbasis LSB (Python)

Aplikasi ini memungkinkan pengguna menyembunyikan pesan teks rahasia ke dalam gambar (format PNG) menggunakan teknik Least Significant Bit (LSB).
Dibangun dengan Python menggunakan library Pillow dan Tkinter untuk antarmuka sederhana yang interaktif.

📦 Fitur Utama

🖼️ Pilih gambar dari komputer untuk dijadikan media.

✍️ Masukkan teks rahasia untuk disisipkan.

💾 Simpan gambar hasil penyisipan dengan aman.

🔍 Baca kembali pesan rahasia dari gambar hasil.

💡 Berbasis metode LSB yang mudah dan cepat digunakan.

⚙️ Teknologi yang Digunakan

Python 3.x

Pillow (PIL Fork) – manipulasi gambar.

Tkinter – GUI sederhana untuk memilih file dan input teks.

os, sys – pengelolaan file dasar.

🚀 Cara Menggunakan
1️⃣ Instalasi

Pastikan Python sudah terinstal, lalu jalankan:

pip install pillow

2️⃣ Jalankan Aplikasi
python lsb_steganografi_gui.py

3️⃣ Proses Encoding

Klik “Pilih Gambar” untuk memilih file gambar (contoh: foto_asli.png).

Masukkan pesan rahasia di kolom teks (misalnya: Data Rahasia Operasi X).

Klik “Simpan Gambar Tersisip”, hasil akan disimpan dengan nama foto_tersisip.png.

4️⃣ Proses Decoding

Klik “Pilih Gambar Rahasia” dan pilih file hasil (foto_tersisip.png).

Klik “Baca Pesan”, teks rahasia akan ditampilkan di layar.

📄 Dokumentasi Proyek
🔹 File Asli dan File Hasil
Jenis File	Nama File	Deskripsi
Gambar Asli	foto_asli.png	Media awal tanpa data tersembunyi
Gambar Hasil	foto_tersisip.png	Gambar dengan pesan teks disisipkan ke bit paling rendah
🔹 Alasan Pemilihan Metode

Metode Least Significant Bit (LSB) dipilih karena:

Implementasinya sederhana dan cepat.

Tidak mengubah tampilan visual gambar secara signifikan.

Cocok untuk data teks berukuran kecil hingga sedang.

🔹 Dampak terhadap Ukuran & Kualitas Visual

Ukuran file: Hampir tidak berubah signifikan karena hanya 1 bit per piksel yang dimodifikasi.

Kualitas visual: Perubahan tidak terlihat secara kasat mata, sehingga gambar tampak identik dengan aslinya.

🔹 Analisis Keamanan
Aspek	Analisis
Potensi Deteksi	Rendah, karena perubahan piksel sangat kecil. Namun, analisis statistik atau alat forensik khusus bisa mendeteksi pola aneh.
Kekuatan	Aman untuk komunikasi rahasia non-publik yang tidak melewati kompresi. Mudah diterapkan.
Kelemahan	Rentan rusak bila file dikompresi (misal ke JPG) atau diubah ukurannya. Tidak memiliki enkripsi internal, sehingga pesan bisa dibaca jika seseorang tahu cara decoding.
🔐 Rencana Pengembangan (Next Version)

Menambahkan enkripsi AES sebelum penyisipan teks.

Menyediakan dukungan format JPEG dan BMP.

Menambahkan autentikasi pengguna untuk menjaga privasi pesan.

Fitur deteksi otomatis apakah gambar mengandung pesan rahasia.

📚 Lisensi

Proyek ini dirilis di bawah lisensi MIT License — bebas digunakan untuk penelitian, edukasi, atau pengembangan aplikasi keamanan digital.

👨‍💻 Pengembang

Aditya Maulana

Apakah kamu ingin saya tambahkan contoh screenshot GUI aplikasi (misal jendela pemilihan gambar dan hasil decoding) ke dalam README ini biar tampilannya lebih profesional di GitHub?
