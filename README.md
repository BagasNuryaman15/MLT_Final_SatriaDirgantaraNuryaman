# 🎌 Laporan Proyek Machine Learning Terapan
## Sistem Rekomendasi Anime Berbasis Hybrid Filtering

<div align="center">

![Anime Banner](https://img.shields.io/badge/Machine%20Learning-Recommendation%20System-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)

**Satria Dirgantara Nurayaman**  
*satriadirgantaranuryaman@gmail.com*  
ID Dicoding: Satria Dirgantara Nurayaman
</div>

---

## 🌟 Project Overview
### 🎬 Latar Belakang Domain

Industri anime mengalami pertumbuhan yang sangat pesat dalam dekade terakhir, dengan **nilai pasar global** diperkirakan akan melampaui **USD 48 miliar** pada tahun 2030. Pada tahun 2023, industri anime mencatatkan pendapatan sebesar **3,3465 triliun yen**, angka terbesar dalam sejarah dengan lebih dari 51% pendapatan berasal dari luar Jepang.

Fenomena ini didorong oleh semakin besarnya basis penggemar global, termasuk di Indonesia yang memiliki komunitas anime yang sangat aktif dan engaged *(Kumparan Bisnis, 2025; Seputar Otaku, 2025)*.

### 🚀 Mengapa Proyek Ini Penting?

Dengan ledakan judul anime yang mencapai **lebih dari 300 judul TV** setiap tahunnya, industri hiburan digital menghadapi tantangan besar dalam **content discovery**. Sistem rekomendasi telah terbukti menjadi game-changer di platform seperti Netflix, Spotify, dan Amazon, meningkatkan user engagement hingga 80% dan revenue hingga 35%.

**Machine Learning dalam sistem rekomendasi** menjadi solusi yang tidak hanya menguntungkan pengguna dalam menemukan konten yang relevan, tetapi juga membantu content creators dan platform mendistribusikan konten secara lebih efektif dan demokratis.

### 📚 Riset dan Referensi Terkait

Penelitian terdahulu menunjukkan bahwa **hybrid recommendation systems** memberikan performa superior dibanding single-method approaches, dengan peningkatan user satisfaction hingga 40% *(Putri & Faisal, 2023)*. Implementasi sistem rekomendasi pada domain entertainment telah menciptakan ecosystem yang lebih sustainable bagi content creators sekaligus memberikan pengalaman yang truly personalized bagi pengguna.

---

### 📚 **Referensi**

<details>
   <summary>
      <strong>📖 Daftar Pustaka Lengkap</strong>
   </summary>

1. **Kumparan Bisnis**. (2025). *Industri Game dan Anime Diprediksi Melejit, Capai USD 467 Miliar di 2027*. Kumparan. [Kumparan Bisnis](https://kumparan.com/kumparanbisnis/industri-game-dan-anime-diprediksi-melejit-capai-usd-467-miliar-di-2027-24LsLjWy2yh).

2. **Putri, H. D., & Faisal, M.** (2023). Analyzing the Effectiveness of Collaborative Filtering and Content-Based Filtering Methods in Anime Recommendation Systems. *Jurnal Komtika (Komputasi dan Informatika)*, 7(2), 124-133. [Jurnal Komtika](https://doi.org/10.31603/komtika.v7i2.9219).

3. **Seputar Otaku**. (2025). *Ketika Pasar Global Mengalahkan Jepang: Peluang atau Tantangan untuk Masa Depan Anime*. Seputar Otaku. [Seputar Otaku](https://seputarotaku.com/article/535/ketika-pasar-global-mengalahkan-jepang-apa-artinya-untuk-masa-depan-anime).

</details>

---

## 💼 Business Understanding
### 🎯 Problem Statements

| No | Problem Statement                                                                                                                   |
|---|--------------------------------------------------------------------------------------------------------------------------------------|
| 1 | **Bagaimana cara membantu pengguna menemukan anime yang sesuai** dengan preferensi mereka di tengah banyaknya pilihan yang tersedia? |
| 2 | **Bagaimana cara mengurangi ketergantungan pada rekomendasi manual** yang bias dan tidak efisien?                                    |
| 3 | **Bagaimana cara memberikan rekomendasi yang akurat** berdasarkan karakteristik konten dan pola preferensi pengguna?                 |

### 🎯 Goals

- ✅ **Membangun sistem rekomendasi anime** yang personal dan relevan dengan akurasi >80%.
- ✅ **Mengimplementasikan model ML** untuk analisis preferensi otomatis.
- ✅ **Meningkatkan user experience** dalam discovery anime dan mengurangi waktu pencarian.

### 🛠️ Solution Approach

Proyek ini menggunakan **Hybrid Recommendation System** yang menggabungkan:

<div align="center">

| 🎨 Content-Based Filtering                      | 🤝 Collaborative Filtering                  |
|-------------------------------------------------|---------------------------------------------|
| ✅ Analisis karakteristik anime (genre, rating) | ✅ Analisis pola preferensi pengguna serupa |
| ✅ Tidak perlu data pengguna lain               | ✅ Menemukan pola tersembunyi               |
| ✅ Mengatasi cold start problem                 | ✅ Rekomendasi yang tidak terduga           |

</div>

**Keunggulan Hybrid Approach:**
- Mengatasi kelemahan masing masing metode
- Memberikan rekomendasi yang lebih akurat dan beragam
- Dapat menangani berbagai skenario pengguna

---
