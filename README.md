# Aplikasi Penjualan Pulsa Desktop (PyQt5)

README – SOURCE CODE & FILE EXECUTABLE (.EXE)

---

## 1. Deskripsi Aplikasi

Aplikasi Penjualan Pulsa adalah aplikasi desktop berbasis **Python** dan **PyQt5** yang digunakan untuk mencatat transaksi penjualan pulsa secara otomatis. Aplikasi ini menyimpan data transaksi ke dalam database SQLite, menghitung harga dan keuntungan secara otomatis, serta menampilkan laporan dan grafik penjualan per provider.

Aplikasi ini dibuat sebagai **Final Project Praktikum Pemrograman Visual**.

---

## 2. Masalah yang Diselesaikan

Permasalahan pada pencatatan manual penjualan pulsa:

* Kesalahan perhitungan harga dan keuntungan
* Data transaksi tidak tersimpan rapi
* Sulit membuat laporan keuntungan
* Tidak ada grafik perkembangan penjualan

Aplikasi ini mengotomatisasi seluruh proses transaksi dan pelaporan.

---

## 3. Fitur Utama

### 3.1 Transaksi Pulsa

* Pilih provider (Telkomsel, Indosat, XL, Axis, Three, Smartfren)
* Input nomor HP dengan validasi (10–13 digit)
* Pilih nominal pulsa
* Harga otomatis (nominal + Rp3.000)
* Konfirmasi sebelum transaksi disimpan

### 3.2 Data Transaksi

* Menampilkan riwayat transaksi dalam tabel
* Data tersimpan permanen di database SQLite
* Tabel tidak bisa diedit langsung

### 3.3 Laporan & Grafik

* Total keuntungan keseluruhan
* Rekap transaksi per provider
* Grafik batang transaksi per provider

---

## 4. Teknologi yang Digunakan

| Komponen      | Teknologi   |
| ------------- | ----------- |
| Bahasa        | Python 3.x  |
| GUI Framework | PyQt5       |
| Grafik        | PyQtChart   |
| Database      | SQLite      |
| Packaging     | PyInstaller |
| OS            | Windows     |

---

## 5. Struktur File Proyek

```
project/
│
├── main.py              # Source code utama aplikasi
├── pulsa.db            # Database SQLite (dibuat otomatis)
├── app_icon.ico        # Ikon aplikasi
├── README.md           # Dokumentasi proyek
└── dist/
    └── AplikasiPenjualanPulsa.exe
```

---

## 6. Cara Menjalankan dari SOURCE CODE

### 6.1 Persiapan Lingkungan

Pastikan Python sudah terinstall:

```bash
python --version
```

### 6.2 Instal Library

```bash
pip install pyqt5 pyqtchart
```

### 6.3 Menjalankan Program

```bash
python main.py
```

Jika berhasil, jendela aplikasi akan muncul.

---

## 7. Cara Instal & Menjalankan FILE .EXE

Bagian ini digunakan jika aplikasi sudah dalam bentuk **file executable (.exe)**.

### 7.1 Syarat Sistem

* Sistem Operasi: Windows 10 / Windows 11
* Tidak memerlukan Python atau library tambahan

### 7.2 Cara Instal

1. Salin file:

   ```
   AplikasiPenjualanPulsa.exe
   ```
2. Letakkan di folder mana saja
3. Klik dua kali file `.exe`
4. Aplikasi langsung berjalan

---

## 8. Cara Menggunakan Aplikasi

### 8.1 Melakukan Transaksi

1. Buka aplikasi
2. Pilih **Provider**
3. Masukkan **Nomor HP**
4. Pilih **Nominal Pulsa**
5. Sistem menampilkan harga otomatis
6. Klik tombol **PROSES TRANSAKSI**
7. Konfirmasi transaksi

Data akan langsung tersimpan ke database.

---

### 8.2 Melihat Data Transaksi

1. Buka tab **Data Transaksi**
2. Seluruh transaksi akan tampil dalam tabel
3. Data diurutkan dari transaksi terbaru

---

### 8.3 Melihat Laporan & Grafik

1. Buka tab **Laporan**
2. Lihat:

   * Total keuntungan keseluruhan
   * Rekap keuntungan per provider
   * Grafik batang transaksi

---

## 9. Struktur Database

Database menggunakan SQLite dengan tabel `transaksi`:

| Field      | Tipe    | Keterangan      |
| ---------- | ------- | --------------- |
| id         | INTEGER | Primary key     |
| provider   | TEXT    | Nama provider   |
| no_hp      | TEXT    | Nomor HP        |
| nominal    | INTEGER | Nominal pulsa   |
| harga      | INTEGER | Harga jual      |
| keuntungan | INTEGER | Keuntungan      |
| tanggal    | TEXT    | Waktu transaksi |

Database otomatis dibuat saat aplikasi pertama kali dijalankan.

---

## 10. Cara Membuat File Executable (.EXE)

### 10.1 Install PyInstaller

```bash
pip install pyinstaller
```

### 10.2 Build Aplikasi

```bash
pyinstaller --noconsole --onefile --icon=app_icon.ico --name AplikasiPenjualanPulsa main.py
```

Hasil build berada di:

```
dist/AplikasiPenjualanPulsa.exe
```

---

## 11. Troubleshooting

**Aplikasi tidak bisa dibuka**

* Pastikan file `.exe` tidak diblokir antivirus

**Module PyQt5 tidak ditemukan**

* Jalankan kembali:

  ```bash
  pip install pyqt5 pyqtchart
  ```

**Database tidak muncul**

* Pastikan file `pulsa.db` berada satu folder dengan `main.py` atau `.exe`

---

## 12. Identitas Pengembang

* Nama : Aria Pajarizki
* Mata Kuliah : Praktikum Pemrograman Visual
* Dosen : Safri Adam, S.Kom., M.Kom.
* Institusi : Politeknik Negeri Pontianak

---

## 13. Lisensi

Proyek ini dibuat untuk keperluan akademik dan pembelajaran.

Bebas digunakan dan dikembangkan kembali untuk tujuan pendidikan.

---

## 14. Penutup

README ini menjelaskan penggunaan aplikasi baik dari sisi **source code** maupun **file executable (.exe)**. Dengan dokumentasi ini, pengguna dapat menjalankan, menginstal, dan memahami alur kerja aplikasi dengan mudah.

Terima kasih telah menggunakan Aplikasi Penjualan Pulsa 🚀
