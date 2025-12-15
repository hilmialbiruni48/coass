# 🏥 CoAss - Covid Assistant

**CoAss (Covid Assistant)** adalah aplikasi web berbasis Django yang berfungsi sebagai asisten pribadi untuk pasien yang terpapar Covid-19. Aplikasi ini membantu pasien dalam proses penyembuhan dengan menyediakan fitur reminder, tracking kesehatan, dan pencatatan harian.

---

## 📋 Daftar Isi

- [Tentang Aplikasi](#-tentang-aplikasi)
- [Fitur Utama](#-fitur-utama)
- [Tech Stack](#-tech-stack)
- [Struktur Project](#-struktur-project)
- [Cara Menjalankan](#-cara-menjalankan)
  - [Prerequisites](#prerequisites)
  - [Instalasi](#instalasi)
  - [Menjalankan Server](#menjalankan-server)
- [Penggunaan](#-penggunaan)
- [Tim Pengembang](#-tim-pengembang)
- [Lisensi](#-lisensi)

---

## 📖 Tentang Aplikasi

Aplikasi ini dibuat untuk membantu para pejuang Covid-19 dalam masa penyembuhan dengan track record yang terstruktur. Latar belakang pembuatan aplikasi ini adalah pengalaman salah satu anggota kelompok yang pernah terpapar virus Covid-19 dan menyadari pentingnya adanya rutinitas dan perekaman data secara teratur untuk melihat progress tiap harinya.

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| 🔐 **Authentication** | Sistem login dan signup untuk user |
| 💊 **Reminder Obat** | Pengingat jadwal konsumsi obat harian |
| 🍽️ **Reminder Makan & Minum** | Pengingat jadwal makan dan tracking asupan air |
| 🏃 **Reminder Aktivitas** | Pengingat aktivitas seperti olahraga, berjemur, istirahat (dengan timer) |
| 🌡️ **Catatan Kesehatan** | Pencatatan suhu tubuh, saturasi, denyut jantung, tensi, gula darah |
| 🧪 **Riwayat SWAB** | Pencatatan tanggal, hasil, dan CT value test swab |
| 📝 **Jurnal Harian** | Catatan keluhan yang dirasakan setiap hari |

---

## 🛠️ Tech Stack

| Teknologi | Versi/Keterangan |
|-----------|------------------|
| **Backend** | Django 5.x |
| **Database** | SQLite (local) / PostgreSQL (production) |
| **Frontend** | HTML, CSS, JavaScript |
| **UI Framework** | Bootstrap 4, Crispy Forms |
| **Static Files** | WhiteNoise |

---

## 📁 Struktur Project

```
coass/
├── Authentication/        # Modul login & signup
├── Catatan_Kesehatan/     # Modul catatan kesehatan
├── Daily_Journal/         # Modul jurnal harian
├── Reminder_Aktivitas/    # Modul reminder aktivitas
├── Reminder_Makan_Minum/  # Modul reminder makan & minum
├── Reminder_Obat/         # Modul reminder konsumsi obat
├── Riwayat_SWAB/          # Modul riwayat test swab
├── main/                  # Halaman utama & landing page
├── co_ass/                # Konfigurasi Django project
│   ├── settings.py        # Pengaturan project
│   ├── urls.py            # URL routing utama
│   └── wsgi.py            # WSGI configuration
├── static/                # File static (CSS, JS, images)
├── templates/             # Template HTML global
├── manage.py              # Django management script
├── requirements.txt       # Dependencies Python
└── db.sqlite3             # Database SQLite (auto-generated)
```

---

## 🚀 Cara Menjalankan

### Prerequisites

Pastikan sudah terinstall di komputer Anda:
- **Python 3.8+** ([Download Python](https://www.python.org/downloads/))
- **pip** (biasanya sudah terinstall bersama Python)
- **Git** (opsional, untuk clone repository)

### Instalasi

1. **Clone atau download repository ini:**

   ```bash
   git clone https://github.com/username/coass.git
   cd coass
   ```

2. **(Opsional) Buat virtual environment:**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   pip install crispy-bootstrap4
   ```

4. **Jalankan migrasi database:**

   ```bash
   python manage.py migrate
   ```

5. **(Opsional) Buat superuser untuk akses admin:**

   ```bash
   python manage.py createsuperuser
   ```

### Menjalankan Server

```bash
python manage.py runserver
```

Buka browser dan akses: **http://127.0.0.1:8000/**

---

## 💡 Penggunaan

1. **Registrasi/Login**: Buat akun baru melalui halaman signup atau login jika sudah punya akun
2. **Halaman Utama**: Setelah login, Anda akan melihat dashboard dengan akses ke semua fitur
3. **Reminder Obat**: Tambahkan jadwal obat dengan nama obat, waktu konsumsi, dan durasi
4. **Reminder Aktivitas**: Atur jadwal aktivitas dengan opsi timer
5. **Catatan Kesehatan**: Catat data kesehatan harian (suhu, saturasi, dll)
6. **Riwayat SWAB**: Simpan hasil test swab PCR/Antigen
7. **Jurnal Harian**: Tulis keluhan yang dirasakan setiap hari

### Akses Admin Panel

Untuk mengakses Django admin panel:
1. Buat superuser (lihat langkah instalasi)
2. Akses **http://127.0.0.1:8000/admin/**
3. Login dengan kredensial superuser

---

## 👥 Tim Pengembang

**TK PBP Django - Kelompok B03**

| NIM | Nama | Modul |
|-----|------|-------|
| 2006482445 | Zidan Amukti Rajendra | Reminder Makan & Minum |
| 2006481953 | Amanda Putri Khairunnisa | Riwayat SWAB |
| 2006463843 | Hilmi Al-biruni | Reminder Obat |
| 2006464184 | Karlina Rana Salsabila | Catatan Kesehatan |
| 2006485945 | Raditya Hanif Yudha Prathama | Jurnal Harian |
| 2006464461 | Muhammad Athif | Halaman Utama |
| 2006481972 | Danela Syafika Desideria | Reminder Aktivitas |

---

## 📄 Lisensi

Project ini dilisensikan di bawah [The Unlicense](LICENSE).

---

## 📞 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'crispy_bootstrap4'`
```bash
pip install crispy-bootstrap4
```

### Error: `request.is_ajax()` AttributeError
Jika menggunakan Django 4.0+, pastikan semua file `views.py` sudah diupdate untuk menggunakan:
```python
if request.headers.get('x-requested-with') == 'XMLHttpRequest':
```
sebagai pengganti `request.is_ajax()` yang sudah deprecated.

### Database Error
Hapus file `db.sqlite3` dan jalankan ulang migrasi:
```bash
del db.sqlite3  # Windows
rm db.sqlite3   # Linux/macOS
python manage.py migrate
```

---

<p align="center">
  Made with ❤️ by Tim B03 - PBP 2021
</p>
