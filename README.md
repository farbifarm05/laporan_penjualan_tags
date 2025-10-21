# Modul Odoo: Laporan Penjualan Tags

Modul ini memperluas fungsionalitas laporan Analisis Penjualan (Sales Analysis) standar Odoo dengan menambahkan kolom kustom baru untuk "Tags" dan "Nama Produk Bersih".

---

## Fitur Utama

Modul ini menambahkan dua kolom baru ke model `sale.report` (Sales Analysis Report):

1.  **Tags (`x_sale_tags`)**
    * Menampilkan semua *sales tags* (dari modul CRM) yang terkait dengan Sales Order.
    * Data tags diambil menggunakan `string_agg` dari `crm.tag` yang terhubung ke `sale.order`.
    * Untuk data yang berasal dari Point of Sale (PoS), kolom ini akan kosong (NULL) karena PoS tidak memiliki relasi standar ke *sales tags*.

2.  **Nama Produk Bersih (`product_name_only`)**
    * Menampilkan nama produk (dari `product.template`) tanpa awalan kode referensi internal.
    * Contoh: Jika nama produk Anda adalah `[SKU001] Produk Hebat`, kolom ini hanya akan menampilkan `Produk Hebat`.
    * Jika produk tidak memiliki referensi internal di namanya, nama produk akan ditampilkan seperti aslinya.

---

## Prasyarat (Dependencies)

Modul ini bergantung pada modul-modul berikut:
* `sale_management`
* `pos_sale` (Untuk memastikan laporan tetap kompatibel dengan data PoS)
* `crm` (Dibutuhkan untuk mengakses model `crm.tag`)

---

## Instalasi

1.  Letakkan folder `laporan_penjualan_tags` ini ke dalam direktori `addons` Odoo Anda.
2.  Restart server Odoo Anda.
3.  Masuk ke Odoo sebagai Administrator.
4.  Aktifkan Mode Developer (Developer Mode).
5.  Pergi ke menu **Apps**.
6.  Klik **Update Apps List**.
7.  Cari modul **"Laporan Penjualan Tags"** dan klik tombol **Install**.

---

## Cara Penggunaan

Setelah modul terinstal, tidak ada konfigurasi tambahan yang diperlukan.

1.  Pergi ke menu **Sales > Reporting > Sales**.
2.  Secara default, Anda akan melihat tampilan Pivot. Ubah ke **List View** (ikon daftar/tabel).
3.  Anda akan melihat kolom baru **"Tags"** dan **"Nama Produk"** (yang telah diganti) di dalam daftar.
4.  Jika kolom tersebut tidak langsung terlihat, Anda dapat menambahkannya secara manual melalui ikon tiga titik vertikal di ujung kanan header tabel dan mencentang kolom tersebut.

---

## Penulis

* Fakhrul Rosyid
