[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ZXimSQGf)

Tugas Menengah
Hasil kerja
Tugas ini akan menguji pemahaman Anda tentang menghubungkan aplikasi Flask ke database MySQL dan mengimplementasikan operasi dasar CRUD (Buat, Baca, Perbarui, Hapus). Selain itu, Anda akan menjelajahi metode autentikasi berbasis sesi menggunakan Flask-login Flask-JWT-Exended. Dan
Tugas
1. Pengaturan Basis Data:
   A. Buat database MySQL untuk proyek ini.
   B. Rancang dan terapkan tabel database untuk menyimpan data pengguna, termasuk nama pengguna, email, peran (hanya tersedia peran Pengguna dan Admin), dan kata sandi (di-hash dengan aman).
   C. Merancang dan mengimplementasikan tabel database untuk menyimpan data ulasan, termasuk deskripsi, email, dan rating (antara 1-5)
2. Aplikasi & Ketergantungan Flask:
   A. Siapkan aplikasi Flask baru.
   B. Instal dependensi berikut:
      Saya. Labu
        ii. SQLAlkimia
            aku aku aku. Flask-Login (untuk otentikasi berbasis sesi)
            iv. MySQL Connector Python (untuk menghubungkan ke MySQL)
3. Koneksi Basis Data:
   A. Konfigurasikan aplikasi Flask Anda untuk terhubung ke database MySQL menggunakan URI koneksi.
4. Pembuatan Model:
   A. Buat file model yang mewakili struktur data pengguna menggunakan SQLAlchemy.
   B. Tentukan bidang untuk nama pengguna, email, dan kata sandi (di-hash menggunakan algoritma hashing yang aman seperti bcrypt).
5. Pengambilan dan Tampilan Data:
   A. Ambil semua data pengguna dari database.
   B. Menampilkan data pengguna dalam tabel yang diformat dengan baik di halaman web.
6. Otentikasi Berbasis Sesi:
   A. Menerapkan fungsi login dan logout pengguna menggunakan Flask-Login.
   B. Simpan informasi pengguna dengan aman dalam sesi.
   C. Lindungi rute tertentu yang memerlukan otentikasi pengguna.

7. Daftar Endpoint dan Permintaan Wajib

|Endpoint     |Methods      |Request Body                            |Additional Info|
| ----------- | :---------: | ----------:                            |----------:    |
| /login      | GET         | -                                      |              -|
| /login      | POST        | email - string                         | Kembalikan kode status 200 jika berhasil |
| /review     | GET         | -                                      | Harus dapat diakses dari peran Admin saja.|    
|-            |-            | -                                      | Kembalikan kode status 403 jika otentikasi gagal| 
| /review     | POST        | description - string rating - integer  | Harus dapat diakses dari peran user saja|
|-            | -           |-                                       | Kembalikan kode status 403 jika otentikasi gagal|


Hasil yang diharapkan
Fungsi Aplikasi:
   - Pengguna dapat mengambil daftar pengguna.
   - Pengguna dapat mendaftar akun dengan nama pengguna, email, dan kata sandi.
   - Pengguna terdaftar dapat masuk dan mengakses fungsi tambahan.
   - Pengguna yang berwenang (misalnya admin) dapat membuat, memperbarui, dan       menghapus data ulasan (fitur bonus).
   - Pengguna dapat keluar dari aplikasi.
Teknis Implementasi:
   - Aplikasi ini menggunakan Flask sebagai kerangka web.
   - Aplikasi terhubung ke database MySQL dan berinteraksi dengan data pengguna melalui model SQLAlchemy.
   - Rute dilindungi berdasarkan status otentikasi pengguna.

   Skill set
   Database Connection
   Flask Authentication