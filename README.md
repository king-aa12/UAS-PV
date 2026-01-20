# Aplikasi Penjualan Pulsa Desktop (PyQt5)

README TERPADU – SOURCE CODE & FILE EXECUTABLE (.EXE)

---

## 1. Pendahuluan

Aplikasi Penjualan Pulsa adalah aplikasi desktop berbasis **Python** dan **PyQt5** yang digunakan untuk mencatat transaksi penjualan pulsa secara terkomputerisasi. Aplikasi ini membantu menghitung harga dan keuntungan secara otomatis, menyimpan data transaksi ke database, serta menampilkan laporan dalam bentuk tabel dan grafik.

Aplikasi ini dikembangkan sebagai **Final Project Praktikum Pemrograman Visual** di Politeknik Negeri Pontianak.

---

## 2. Masalah yang Diselesaikan

Permasalahan yang sering terjadi pada penjualan pulsa manual:

* Kesalahan perhitungan harga dan keuntungan
* Data transaksi tidak tersimpan rapi
* Sulit membuat rekap laporan
* Tidak ada grafik perkembangan penjualan

Aplikasi ini hadir untuk mengotomatisasi seluruh proses tersebut.

---

## 3. Fitur Utama

### 3.1 Transaksi Pulsa

* Pilih provider
* Input nomor HP (validasi 10–13 digit)
* Pilih nominal pulsa
* Hitung harga otomatis
* Hitung keuntungan otomatis
* Konfirmasi sebelum simpan

### 3.2 Data Transaksi

* Menampilkan seluruh transaksi dalam tabel
* Data tersimpan permanen di database SQLite

### 3.3 Laporan & Grafik

* Total keuntungan keseluruhan
* Rekap per provider
* Grafik jumlah transaksi per provider

---

## 4. Teknologi yang Digunakan

| Komponen       | Teknologi   |
| -------------- | ----------- |
| Bahasa         | Python 3.x  |
| GUI Framework  | PyQt5       |
| Grafik         | PyQtChart   |
| Database       | SQLite      |
| Packaging      | PyInstaller |
| Sistem Operasi | Windows     |

---

## 5. Struktur Folder Proyek

```
project/
│
├── main.py              # File utama program
├── pulsa.db            # Database SQLite (otomatis dibuat)
├── app_icon.ico        # Ikon aplikasi
├── Inter-Regular.ttf   # Font (opsional)
├── README.md           # Dokumentasi proyek
└── dist/
    └── AplikasiPenjualanPulsa.exe
```

---

## 6. Cara Menjalankan dari SOURCE CODE

### 6.1 Persiapan

Pastikan Python sudah terinstall:

```bash
python --version
```

### 6.2 Install Library

```bash
pip install pyqt5 pyqtchart
```

### 6.3 Menjalankan Program

```bash
python main.py
```

---

## 7. Cara Instal & Menjalankan FILE .EXE

Bagian ini digunakan jika aplikasi sudah dalam bentuk **file executable (.exe)**.

### 7.1 Syarat Sistem

* Sistem Operasi: Windows 10 / 11
* Tidak memerlukan Python terinstall

### 7.2 Cara Instal

1. Salin file:

   ```
   AplikasiPenjualanPulsa.exe
   ```
2. Letakkan di folder mana saja
3. Klik dua kali file `.exe`

Aplikasi siap digunakan tanpa instalasi tambahan.

---

## 8. Cara Menggunakan Aplikasi

### 8.1 Melakukan Transaksi

1. Buka aplikasi
2. Pilih provider pulsa
3. Masukkan nomor HP
4. Pilih nominal pulsa
5. Sistem menghitung harga otomatis
6. Klik tombol **Proses / Simpan**
7. Konfirmasi transaksi

Data akan otomatis tersimpan.

---

### 8.2 Melihat Data Transaksi

1. Buka tab **Data Transaksi**
2. Semua transaksi akan tampil dalam tabel
3. Data diambil langsung dari database

---

### 8.3 Melihat Laporan & Grafik

1. Buka tab **Laporan**
2. Lihat:

   * Total keuntungan
   * Rekap per provider
   * Grafik transaksi

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

File hasil build berada di:

```
dist/AplikasiPenjualanPulsa.exe
```

---

## 11. Troubleshooting

**Aplikasi tidak bisa dibuka**

* Pastikan file `.exe` tidak terhapus antivirus

**Library tidak ditemukan saat run source**

* Jalankan kembali:

  ```bash
  pip install pyqt5 pyqtchart
  ```

**Database tidak muncul**

* Pastikan file `pulsa.db` berada satu folder dengan `main.py` atau `.exe`

---

## 12. Identitas Pengembang

* Nama  : Aria Pajarizki
* Mata Kuliah : Praktikum Pemrograman Visual
* Dosen : Safri Adam, S.Kom., M.Kom.
* Institusi : Politeknik Negeri Pontianak

---

## 13. Lisensi

Proyek ini dibuat untuk keperluan akademik dan pembelajaran.

Bebas digunakan dan dikembangkan kembali untuk tujuan pendidikan.

---

## 14. Penutup

Dokumentasi ini menjelaskan penggunaan aplikasi baik dari sisi **source code** maupun **file executable (.exe)**. Dengan README ini, pengguna dapat langsung menjalankan, menginstal, serta memahami alur kerja aplikasi dengan mudah.

Terima kasih telah menggunakan Aplikasi Penjualan Pulsa 
