# Implementasi Algoritma Genetika - Knapsack Problem

Proyek ini mengimplementasikan **Algoritma Genetika (GA)** untuk menyelesaikan permasalahan klasik **Knapsack Problem**. Tujuannya adalah memilih kombinasi barang yang memiliki total nilai (fitness) tertinggi tanpa melebihi kapasitas beban maksimal tas.

## 📋 Struktur Proyek

Proyek ini terdiri dari beberapa modul Python yang masing-masing menangani tahapan spesifik dalam algoritma genetika:

1.  **`main.py`**: File utama yang mengatur alur eksekusi algoritma, mulai dari inisialisasi hingga visualisasi hasil.
2.  **`inisiasipopulasi.py`**: Bertanggung jawab untuk membangkitkan populasi awal secara acak.
3.  **`evaluasifitness.py`**: Berisi logika untuk menghitung nilai fitness (total harga) dan menangani batasan kapasitas (penalty jika melebihi kapasitas).
4.  **`selection.py`**: Mengimplementasikan metode seleksi orang tua, seperti *Roulette Wheel Selection* dan *Tournament Selection*.
5.  **`crossover.py`**: Menangani proses persilangan gen (*One-point*, *Two-point*, dan *Uniform crossover*) untuk menghasilkan keturunan baru.
6.  **`mutation.py`**: Melakukan mutasi pada genetik anak untuk menjaga variasi populasi (*Swap*, *Inversion*, dan *Uniform mutation*).

## ⚙️ Parameter Algoritma

Dalam implementasi ini, parameter yang digunakan adalah:
- **Jumlah Generasi**: 50
- **Jumlah Populasi**: 20
- **Probabilitas Crossover**: 0.5
- **Probabilitas Mutasi**: 0.1
- **Kapasitas Tas**: 50 unit bobot

## 🚀 Cara Menjalankan

Pastikan Anda telah menginstal pustaka `matplotlib` untuk visualisasi:
```bash
pip install matplotlib
```

Jalankan skrip utama:
```bash
python main.py
```

## 📊 Hasil Visualisasi

Setelah program selesai dijalankan, grafik perkembangan fitness terbaik di setiap generasi akan ditampilkan dan disimpan secara otomatis sebagai `fitness_plot.png`.

![Perkembangan Fitness](fitness_plot.png)

## 💡 Penjelasan Alur Algoritma

1.  **Inisialisasi**: Membuat sekumpulan individu (kromosom) acak yang merepresentasikan barang yang diambil (1) atau tidak (0).
2.  **Evaluasi**: Menghitung total nilai barang untuk setiap individu. Jika total bobot melebihi kapasitas, fitness diberikan nilai 0.
3.  **Seleksi**: Memilih individu terbaik untuk menjadi orang tua menggunakan metode *Roulette Wheel*.
4.  **Crossover**: Menggabungkan gen dari dua orang tua untuk menciptakan individu baru (anak).
5.  **Mutasi**: Mengubah sedikit bagian dari kromosom anak secara acak untuk menghindari optimasi lokal (stuck pada hasil yang kurang maksimal).
6.  **Iterasi**: Proses ini diulang sebanyak jumlah generasi yang ditentukan hingga ditemukan solusi optimal.
