# finalproject23si3

## Nama Project: Auth API Project

## Deskripsi 
Aplikasi ini merupakan sistem autentikasi sederhana berbasis web menggunakan Flask. Aplikasi menyediakan fitur utama seperti registrasi pengguna, login, dan melihat data profil pengguna. Aplikasi ini dibuat untuk memenuhi kebutuhan Final Project mata kuliah Software Testing dengan fokus pada implementasi automated testing dan Continuous Integration (CI).

Fitur utama:
- Register (mendaftarkan user baru)
- Login (autentikasi user)
- Profile (melihat daftar user) 

## Cara Menjalankan Aplikasi
1. Clone repository: git clone https://github.com/Faline/finalproject23si3.git
2. Masuk ke folder project: cd auth-api
3. Aktifikan virtual environment: venv\Scripts\activate
4. Install dependencies: pip install -r requirements.txt
5. Jalankan aplikasi: python app/app.py
6. Buka di browser: http://127.0.0.1:5000

## Cara Menjalankan Testing
- Menjalankan semua test: pytest
- Menjalankan test dengan coverage: pytest --cov=app

## Startegi Pengujian
### 1. Unit Testing
Unit testing dilakukan untuk menguji fungsi-fungsi utama dalam aplikasi secara terpisah, terutama pada:
- Validasi input (email dan password)
- Proses registrasi user
- Proses login user

### 2. Integration Testing
Integration testing dilakukan untuk menguji alur sistem secara keseluruhan, seperti:
- Register > Login > Profile
- Login dengan password yang salah
- Register user lalu akses profile
Tujuan integration test adalah memastikan bahwa setiap komponen dapat bekerja dengan baik ketika digabungkan.

### 3. Test Coverage
Pengujian dilakukan dengan menggunakan pytest-cov unruk mengukur tingkat coverage kode. Hasil coverage: 86%

### 4. Continuous Integration (CI)
Aplikasi ini menggunakan GitHub Actions untuk menjalankan testing secara otomatis setiap kali terjadi:
- Push
- Pull request
Pipeline CI mencakup:
- Install dependencies
- Menjalankan unit dan integration test
- Menghasilkan laporan coverage
