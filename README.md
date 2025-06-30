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

## 📊 Data Understanding
### 🗂️ Dataset Overview
#### 📋 Informasi Umum Dataset
- **Nama Dataset**: Anime Recommendations Database
- **Sumber Data**: [Kaggle - Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database)
- **Format File**: 2 file CSV (anime.csv, rating.csv)
- **Ukuran Total**: ~120 MB
- **Periode Data**: Data anime dari MyAnimeList.net hingga tahun 2017
- **Jumlah Total Records**: 
  - anime.csv: 12,294 records
  - rating.csv: 7,813,737 records

> 📥 **Download Dataset**: Mengingat ukuran file yang besar (~114MB untuk rating.csv), dataset lengkap tersedia di [Google Drive](https://drive.google.com/file/d/17-uftcMsdaXXQr8BM_goNvPlSTw0s8Zp/view?usp=sharing).

### 🎯 Deskripsi Dataset
Dataset ini berisi informasi komprehensif tentang anime dan rating pengguna yang dikumpulkan dari platform MyAnimeList.net. Dataset terdiri dari dua file utama yang saling terhubung melalui `anime_id`, memungkinkan analisis mendalam tentang preferensi pengguna dan karakteristik anime untuk membangun sistem rekomendasi yang akurat dan personal.

---

### 📁 Struktur Data dan Variabel

<div align="center">

| 🎬 **Data Anime** | 👥 **Interaksi Pengguna** | 🎯 **Statistik Utama** |
|:---:|:---:|:---:|
| **12,294** anime unik | **7.8 juta+** rating pengguna | **73 ribu+** pengguna aktif |
| **43** genre unik | **Rentang rating:** 1-10 | **Rating rata-rata:** 6.47/10 |
| **6** tipe anime | **Kelengkapan data:** 99%+ | **Genre teratas:** Comedy |

</div>

#### 🎬 **File 1: anime.csv**
Dataset ini berisi informasi metadata tentang anime yang menjadi dasar untuk sistem rekomendasi berbasis konten.

| Variabel     | Tipe Data | Deskripsi                                                                 | Data Hilang | Keterangan |
|-------------|-----------|---------------------------------------------------------------------------|-------------|------------|
| `anime_id`  | Integer   | ID unik untuk setiap anime (mengacu pada myanimelist.net)                | 0 (0%)      | Kunci Utama |
| `name`      | String    | Nama lengkap anime                                                        | 0 (0%)      | Lengkap Semua |
| `genre`     | String    | Daftar genre anime, dipisahkan koma                                       | 62 (0,50%)  | Multi-nilai |
| `type`      | String    | Tipe anime (TV, Movie, OVA, ONA, Special, Music)                         | 25 (0,20%)  | Kategori |
| `episodes`  | String    | Jumlah episode (1 jika movie, "Unknown" jika tidak diketahui)            | 0 (0%)      | Tipe Campuran |
| `rating`    | Float     | Rata-rata rating dari seluruh user (skala 1-10)                          | 230 (1,87%) | Variabel Target |
| `members`   | Integer   | Jumlah anggota komunitas yang memasukkan anime ini ke dalam list mereka   | 0 (0%)      | Metrik Popularitas |

#### 👥 **File 2: rating.csv**
Dataset ini berisi interaksi pengguna-anime yang menjadi inti untuk sistem rekomendasi kolaboratif.

| Variabel    | Tipe Data | Deskripsi                                                                 | Rentang Nilai    | Data Hilang | Keterangan |
|------------|-----------|---------------------------------------------------------------------------|------------------|-------------|------------|
| `user_id`  | Integer   | ID unik pengguna (acak, tidak dapat diidentifikasi)                      | 1 - 73.516     | 0 (0%)      | Kunci Asing |
| `anime_id` | Integer   | ID anime yang dirating oleh user (kunci asing ke anime.csv)              | 1 - 34.519     | 0 (0%)      | Kunci Asing |
| `rating`   | Integer   | Nilai rating yang diberikan user (-1 jika user menonton tapi tidak rating)| -1, 1-10      | 0 (0%)      | Variabel Target |

---

### 🔍 Analisis Kualitas Data

#### 📈 **Penilaian Kualitas Data**

<div align="center">

| **Dataset** | **Kelengkapan** | **Konsistensi** | **Akurasi** | **Validitas** | **Status** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **anime.csv** | 98,1% ✅ | Tinggi ✅ | Terverifikasi ✅ | Baik ✅ | 🟢 Bersih |
| **rating.csv** | 100% ✅ | Tinggi ✅ | Terverifikasi ✅ | Sempurna ✅ | 🟢 Bersih |

</div>

#### 🛠️ **Kebutuhan Preprocessing Data**

<div align="center">

| **Jenis Masalah** | **Jumlah** | **Dampak** | **Solusi** |
|:---:|:---:|:---:|:---:|
| Genre Hilang | 62 baris | Rendah | Imputasi atau Hapus |
| Tipe Hilang | 25 baris | Rendah | Imputasi "Tidak Diketahui" |
| Rating Hilang | 230 baris | Sedang | Pertimbangkan Eksklusi |
| Rating -1 | ~1,2 juta baris | Tinggi | Tangani sebagai "Ditonton" |

</div>

**Insight Kualitas Data:**
- Dataset `anime.csv` sangat bersih dengan data hilang minimal (<2%)
- Dataset `rating.csv` sempurna tanpa data hilang
- Tidak ditemukan duplikasi signifikan (hanya 1 baris duplikat di rating.csv)
- Konsistensi pemetaan ID antara kedua dataset terjaga dengan baik
- **Catatan Khusus**: Rating -1 menunjukkan pengguna menonton tanpa memberikan rating (bukan data hilang)

---

### 📊 Exploratory Data Analysis (EDA)

#### 🎨 **Analisis Univariat: Fitur Utama untuk Sistem Rekomendasi**

![Univariate Analysis](img/univariate_analysis.png)

Dari analisis univariat yang telah dilakukan, ditemukan insight penting:

<div align="center">

```
🎭 POPULARITAS GENRE         📺 PREFERENSI FORMAT         ⭐ DISTRIBUSI RATING
┌─────────────────────┐      ┌─────────────────────┐      ┌─────────────────────┐
│ 1. Comedy    (4.645)│      │ Serial TV     30,8% │      │ Rata-rata     6,47  │
│ 2. Action    (2.949)│      │ OVA          27,0%  │      │ Median        6,57  │
│ 3. Adventure (2.348)│      │ Movie        20,1%  │      │ Modus         8,00  │
│ 4. Fantasy   (2.309)│      │ Special      11,4%  │      │ Std Dev       1,18  │
│ 5. Sci-Fi    (2.070)│      │ ONA           4,5%  │      │ Rentang    1,67-10  │
└─────────────────────┘      └─────────────────────┘      └─────────────────────┘
```

</div>

**Insight Utama dari Analisis Univariat:**
- 🎭 **Keragaman Genre**: 43 genre unik dengan **Comedy** mendominasi sebagai favorit (1.844+ anime).
- 📺 **Preferensi Format**: **Serial TV** menjadi format paling populer (30,9% dari total anime).
- ⭐ **Distribusi Kualitas**: Rating terdistribusi normal dengan sedikit bias positif (rata-rata 6,47, median 6,57).
- 👥 **Perilaku Pengguna**: Rating pengguna menunjukkan **bias positif** dengan rating **8/10** paling sering diberikan (21,8%).

#### 🔄 **Analisis Multivariat Fase 1: Insight Sistem Rekomendasi Berbasis Konten**
![Multivariate Phase 1](img/multivariate_analysis_phase1.png)

Analisis hubungan antar variabel konten mengungkap:

<div align="center">

| **Metrik** | **Nilai** | **Insight** | **Implikasi** |
|:---:|:---:|:---:|:---:|
| 🏆 **Genre Teratas berdasar Rating** | Shounen (7,06) | Anime aksi & petualangan berkualitas tinggi | Sinyal konten kuat |
| 📉 **Genre Rating Terendah** | Kids (6,11) | Target audiens mempengaruhi rating | Preferensi berdasar usia |
| 🔗 **Korelasi Popularitas-Kualitas** | 0,388 | Anime populer cenderung berkualitas | Kebijaksanaan massa |
| 📺 **Format Terbaik** | TV (6,90) | Serial lebih disukai dari film/OVA | Format berpengaruh |

</div>

**Insight Mendalam:**
- **Dampak Genre**: **Shounen** mendominasi dengan rating tertinggi (7,06) - genre ini populer karena menyajikan cerita **zero-to-hero** seperti "Big Three" (*Naruto*, *One Piece*, *Bleach*)
- **Kualitas Format**: **Serial TV** unggul dalam kualitas dengan konsistensi penceritaan yang lebih baik
- **Efek Popularitas**: Korelasi positif (0,388) menunjukkan anime populer memang cenderung berkualitas tinggi

#### 🤝 **Analisis Multivariat Fase 2: Insight Sistem Rekomendasi Kolaboratif**

![Multivariate Phase 2](img/multivariate_analysis_phase2.png)

Analisis perilaku pengguna dan interaksi kolaboratif mengungkap:

<div align="center">

| **Metrik Perilaku Pengguna** | **Nilai** | **Pola Distribusi** | **Dampak Rekomendasi** |
|:---:|:---:|:---:|:---:|
| 🔗 **Konsistensi Pengguna-Kualitas** | Korelasi 0,411 | Kesepakatan kuat dengan rating resmi | Reliabilitas tinggi |
| 📊 **Rata-rata Aktivitas Pengguna** | 91,1 rating/pengguna | Distribusi ekor panjang | Tantangan cold start |
| 🎯 **Median Aktivitas Pengguna** | 45,0 rating/pengguna | Mayoritas pengguna kasual | Segmentasi user |
| 🏅 **Aktivitas Pengguna Teratas** | 3.747 rating | Penggemar anime super aktif | Pengguna berpengaruh |
| 📈 **Rata-rata Popularitas Anime** | 640,6 rating/anime | Distribusi sangat miring | Bias popularitas |
| 📊 **Median Popularitas Anime** | 57,0 rating/anime | Long-tail distribution | Tantangan discovery |
| 🏆 **Anime Paling Populer** | 34.226 rating | Efek blockbuster | Daya tarik mainstream |

</div>

**Genre Paling Disukai (Rating 8-10):**

<div align="center">

| **Ranking** | **Genre** | **Rating Tinggi** | **Persentase** | **Insight** |
|:---:|:---:|:---:|:---:|:---:|
| 🥇 | Comedy | 1.866.974 | 22,3% | Genre utama preferensi user |
| 🥈 | Action | 1.663.690 | 19,9% | Aksi tetap favorit mainstream |
| 🥉 | Romance | 1.224.042 | 14,6% | Emosional connection tinggi |
| 4️⃣ | Drama | 1.139.835 | 13,6% | Storytelling mendalam |
| 5️⃣ | Supernatural | 1.046.932 | 12,5% | Fantasy & mistis populer |

</div>

**Insight Kolaboratif:**
- **Konsistensi**: Korelasi 0,411 antara rating pengguna dan rating resmi menunjukkan pengguna menilai secara konsisten
- **Pola Aktivitas**: Distribusi ekor panjang dengan mayoritas pengguna kasual (median 45 rating) namun ada kelompok **pengguna fanatik** yang sangat aktif (hingga 3.747 rating)
- **Preferensi Genre**: **Comedy** mendominasi dengan 1,87 juta rating tinggi, diikuti **Action** dan **Romance**, mencerminkan preferensi mainstream yang mengutamakan hiburan dan emosi
- **Matrix Sparsity**: Sangat tinggi (99,08%) dengan coverage hanya 0,92%, menunjukkan tantangan cold start yang signifikan dan kebutuhan strategi khusus untuk pengguna baru
- **Distribusi Popularitas**: Sangat timpang dengan median anime hanya menerima 57 rating, sementara anime populer bisa mencapai 34.226 rating

**Dampak untuk Sistem Rekomendasi:**
- Perlu strategi **penanganan sparsity** yang robust
- **Segmentasi pengguna** berdasarkan aktivitas (kasual vs fanatik)
- **Bias genre** Comedy-Action-Romance harus diimbangi dengan diversity
- **Cold start mitigation** menggunakan content-based fallback

---

### 🎯 Statistik Utama untuk Sistem Rekomendasi

#### 📈 **Kesiapan Sistem Rekomendasi Berbasis Konten**

<div align="center">

| **Fitur** | **Statistik** | **Kualitas** | **Kekuatan Rekomendasi** |
|:---:|:---:|:---:|:---:|
| 🎬 **Cakupan Anime** | 12.294 judul unik | ✅ Komprehensif | Keragaman tinggi |
| 🎭 **Keragaman Genre** | 43 genre unik | ✅ Kategorisasi kaya | Pencocokan detail |
| 📊 **Spektrum Rating** | Rentang 1,67 - 10,0 | ✅ Rentang kualitas penuh | Penyaringan kualitas |
| 👥 **Rentang Popularitas** | 5 - 1 juta+ anggota | ✅ Popularitas beragam | Niche hingga mainstream |

</div>

#### 🔄 **Kesiapan Sistem Rekomendasi Kolaboratif**

<div align="center">

| **Metrik** | **Volume** | **Kualitas** | **Kesesuaian Algoritma** |
|:---:|:---:|:---:|:---:|
| 🔢 **Total Interaksi** | 7.813.737 rating | ✅ Skala masif | Faktorisasi Matriks |
| 👤 **Pengguna Aktif** | 73.516 pengguna unik | ✅ Komunitas besar | CF berbasis pengguna |
| ⭐ **Distribusi Rating** | 1-10 dengan bias positif | ✅ Preferensi jelas | Implisit/Eksplisit |
| 🎯 **Kepadatan Matriks** | ~0,92% sparse | ⚠️ Sparsitas tipikal | Perlu reduksi dimensi |

</div>

---
## 📊 Data Preparation

Tahapan persiapan data merupakan langkah awal yang esensial dalam membangun sistem rekomendasi yang optimal.
Pada tahap ini, data dikondisikan agar siap digunakan dalam proses pemodelan, baik untuk pendekatan content-based maupun collaborative filtering. Proses mencakup pembersihan data, rekayasa fitur, normalisasi numerik, hingga transformasi teks genre menjadi representasi numerik. Setiap langkah dirancang untuk memastikan kualitas, efisiensi, dan keterandalan sistem rekomendasi yang akan dikembangkan di tahap berikutnya.

---

### 🧹 **1. Penanganan Data yang Hilang**

#### 📋 **Analisis Awal Kualitas Data**

<div align="center">

| **Dataset**      | **Total Records** | **Data Hilang** | **Persentase** | **Status Kualitas** |
|:----------------:|:-----------------:|:---------------:|:--------------:|:-------------------:|
| 🎬 **anime.csv** | 12,294            | 317             | 2,58%          | 🟢 **Excellent**     |
| 👥 **rating.csv**| 7,813,737         | 1,476,496       | 18,9%          | 🟡 **Good**          |

</div>

#### 🎯 **Detail Data Hilang per Fitur**

Analisis lebih mendalam menunjukkan distribusi missing values pada setiap fitur:

<div align="center">

| **Fitur**                      | **Jumlah Hilang** | **Persentase** | **Dampak**    | **Strategi**     |
|:------------------------------:|:-----------------:|:--------------:|:-------------:|:----------------:|
| 🎭 **Genre**                   | 62                | 0,50%          | 🔴 **Lumayan** | Hapus            |
| ⭐ **Rating**                  | 230               | 1,87%          | 🔴 **Lumayan** | Hapus            |
| 📺 **Type**                    | 25                | 0,20%          | 🟡 **Kecil**   | Isi dengan nilai |
| 🆔 **Anime_ID, Name, Members** | 0                  | 0%            | ✅ **Bersih**  | -                |

</div>

#### 🛠️ **Strategi Pembersihan Terstruktur**

**Alasan Teknik yang Dipilih:**

Pendekatan pembersihan data dilakukan secara strategis dan terukur berdasarkan dampak setiap fitur terhadap performa sistem rekomendasi:

<div align="center">

| **Tipe Data**         | **Teknik Pembersihan**  | **Alasan**                                            | **Hasil**         |
|:---------------------:|:-----------------------:|:----------------------------------------------------:|:-----------------:| 
| 🎭 **Genre Kosong**   | **Hapus**               | Core feature untuk content-based filtering            | Integritas sistem |
| ⭐ **Rating Kosong**  | **Hapus**               | Indikator kualitas utama untuk rekomendasi            | Akurasi prediksi  |
| 📺 **Type Kosong**    | **Isi dengan nilai**    | Feature pelengkap, tidak kritis                       | Preservasi data   |
| 🚫 **Rating -1**      | **Saring**              | Sinyal tidak informatif untuk collaborative filtering | Interaksi bersih  |

</div>

**Alasan mengapa diperlukan:**

- **Genre dan Rating** adalah fitur kritis yang tidak bisa diimputasi tanpa bias
- **Menghapus data** lebih aman daripada menggunakan estimasi yang tidak akurat
- **Rating -1** menunjukkan user tidak memberikan penilaian, sehingga tidak informatif untuk model

#### ✅ **Hasil Pembersihan Data**

<div align="center">

| **Fase**     | **Dataset** | **Sebelum**  | **Sesudah** | **Pengurangan** | **Peningkatan Kualitas** |
|:------------:|:-----------:|:------------:|:-----------:|:---------------:|:------------------------:|
| **Awal**     | Anime       | 12,294       | 12,017      | -277            | 🟢 **99,8% Bersih**      |
| **Bersih**   | Rating      | 7,813,737    | 6,337,146   | -1,476,591      | 🟢 **100% Valid**        |

</div>

---

### 🎨 **2. Rekayasa Fitur untuk Sistem Berbasis Konten**

#### 🔍 **Ekstraksi dan Transformasi Genre menggunakan TF-IDF**

**Alasan mengapa diperlukan** Genre dalam dataset tersimpan sebagai teks yang dipisah koma (misal: "Action, Adventure, Comedy"). Untuk sistem machine learning, kita perlu mengkonversi teks menjadi representasi numerik yang dapat dipahami algoritma

<div align="center">

| **Tahap**           | **Input**            | **Proses**                     | **Output**         | **Manfaat**        |
|:-------------------:|:--------------------:|:------------------------------:|:------------------:|:------------------:|
| 🔍 **Persing**      | Teks genre mentah    | String Splitting dan Cleaning  | 43 genre unik      | Identifikasi Fitur |
| 📊 **Analisis**     | 43 Genre             | Penghitungan Frekuensi         | Distribusi Genre   | Pemahaman Data     |
| 🎯 **Transformasi** | Raw Text             | TF-IDF Vectorization           | Matriks Numerik    | Siap Untuk ML      |
| 🔄 **Optimasi**     | Sparase Matrix       | Dense Representation           | Feature Numerik    | Efiseinsi Komputasi|

</div>

#### 🏷️ Hasil TF-IDF Vectorization

<div align="center">

| **Metrik TF-IDF** | **Nilai**    | **Manfaat**            | **Keunggulan Teknis**                   | 
|:-----------------:|:------------:|:----------------------:|:---------------------------------------:|
| 🎯 Matrix Shape   | 12,017 x 43   | Representasi Lengkap. | Setiap anime memiliki vektor genre       |
| 🔢 Sparsity       | ~85%          | Efisiensi Memori      | Sebagian besar anime punya sedikit genre |
| 📈 Feature Range  | 0.0 - 1.0     | Normalisasi Otomatis  | Konsisten untuk similarity calculation   |
| 🎪 Genre Coverage | 43 Genre Unik | Comprehensive         | Menangkap keragaman konten anime         |


</div>

#### ⚙️ **Perhitungan Cosine Similarity**

**Alasan mengapa diperlukan:** Untuk sistem content-based filtering, kita perlu mengukur kemiripan antar anime berdasarkan genre. Cosine similarity dipilih karena efektif untuk data sparse dan tidak terpengaruh magnitude.

**Teknik yang diterapkan:** Menghitung cosine similarity antar anime berdasarkan matriks TF-IDF yang telah dibuat sebelumnya.

<div align="center">

| **Metrik Similarity** | **Nilai** | **Interpretasi** | **Kegunaan** |
|:---:|:---:|:---:|:---:|
| 🔄 **Matrix Size** | 12,017 uftcMsdaXXQr8BM_goNvPlSTw0s8Zp 12,017 | Similarity antar semua anime | Base untuk rekomendasi |
| 📊 **Range** | 0.0 - 1.0 | 0=tidak mirip, 1=identik | Mudah interpretasi |
| 🎯 **Mean Similarity** | ~0.12 | Anime umumnya berbeda | Rekomendasi akan beragam |
| 🔝 **Max Similarity** | 1.0 | Ada anime dengan genre identik | Perfect match possible |

</div>

---

### 🤝 **3. Persiapan Data untuk Collaborative Filtering**

#### 📊 **Pembangunan User-Item Matrix**

**Alasan mengapa diperlukan:** Collaborative filtering memerlukan matriks interaksi user-anime yang dense untuk menemukan pola preferensi. Data mentah terlalu sparse (99.08%) sehingga perlu filtering untuk meningkatkan kualitas sinyal.

**Teknik yang diterapkan:** Filtering data berdasarkan aktivitas user dan popularitas anime untuk mengurangi sparsity dan meningkatkan efisiensi komputasi.

#### 🎯 **Strategi Anti-Sparsity**

**Masalah yang diselesaikan:**
- **Original sparsity: 99.08%** - Terlalu jarang untuk pembelajaran yang efektif
- **Cold start problem** - User/anime baru tanpa riwayat
- **Computational efficiency** - Matriks terlalu besar untuk diproses

<div align="center">

| **Jenis Filter** | **Ambang Batas** | **Logika** | **Yang Dipertahankan** | **Metrik Kualitas** |
|:---:|:---:|:---:|:---:|:---:|
| 👤 **User Aktif** | ≥20 rating/user | Perilaku konsisten | 47,153 users | 🟢 **Reliable patterns** |
| 🎬 **Anime Populer** | ≥50 rating/anime | Validasi komunitas | 5,172 anime | 🟢 **Strong signals** |
| 🔗 **Interaksi Final** | Quality subset | Data informatif | 6,101,496 pairs | 🟢 **2.50% density** |

</div>

#### 🎪 **Analisis Dampak Optimasi**

<div align="center">

| **Metrik** | **Sebelum Optimasi** | **Setelah Optimasi** | **Peningkatan** | **Manfaat** |
|:---:|:---:|:---:|:---:|:---:|
| 📊 **Kepadatan Matriks** | 0.92% | 2.50% | +172% | 🔥 **Sinyal lebih kuat** |
| ⚡ **Efisiensi Komputasi** | Baseline | ~15x faster | +1,500% | 🚀 **Training lebih cepat** |
| 🎯 **Kualitas Prediksi** | Noisy | Clean signals | Significant | ✨ **Model lebih akurat** |
| 💾 **Memory Usage** | 47K × 5K matrix | Manageable size | -95% | 🛡️ **Resource efficient** |

</div>

---

### 📏 **4. Normalisasi Fitur Numerik**

#### 🎼 **MinMaxScaler untuk Harmonisasi Data**

**Alasan mengapa diperlukan:** Fitur numerik seperti rating (1-10) dan members (5-1M+) memiliki skala yang sangat berbeda. Tanpa normalisasi, fitur dengan nilai besar akan mendominasi perhitungan similarity.

**Teknik yang diterapkan:** Menggunakan MinMaxScaler untuk menormalisasi fitur rating dan members ke rentang [0,1].

<div align="center">

| **Fitur** | **Rentang Asli** | **Rentang Setelah Scaling** | **Distribusi** | **Dampak** |
|:---:|:---:|:---:|:---:|:---:|
| ⭐ **Rating** | 1.67 - 10.0 | 0.00 - 1.00 | ✅ **Preserved** | Bobot setara dengan genre |
| 👥 **Members** | 5 - 1,013,917 | 0.00 - 1.00 | ✅ **Preserved** | Tidak mendominasi similarity |

</div>

#### 🔬 **Mengapa MinMaxScaler?**

<div align="center">

| **Aspek** | **MinMaxScaler** | **StandardScaler** | **Keuntungan** |
|:---:|:---:|:---:|:---:|
| 📊 **Output Range** | [0,1] Fixed | Unbounded | Predictable dan interpretable |
| 🎯 **Distribusi** | Shape preserved | Gaussian assumption | Tidak mengubah pola asli |
| 🔄 **Reversibility** | Simple inverse | Complex inverse | Mudah di-decode |
| 🎪 **Compatibility** | Perfect for cosine | May cause issues | Optimal untuk similarity metrics |

</div>

---

### ✅ **5. Validasi Kualitas Data**

#### 🔍 **Checkpoint Kontrol Kualitas**

Setiap tahap preparation divalidasi untuk memastikan integritas dan kesiapan data untuk modeling:

<div align="center">

| **Aspek Validasi** | **Pemeriksaan** | **Hasil** | **Status** | **Dampak** |
|:---:|:---:|:---:|:---:|:---:|
| 🔢 **Data Types** | Konsistensi format | ✅ **Correct** | 🟢 **Pass** | Model compatibility |
| 📏 **Value Ranges** | Scaling [0,1] verification | ✅ **Verified** | 🟢 **Pass** | Similarity computation |
| 🕳️ **Missing Values** | Zero tolerance check | ✅ **Clean** | 🟢 **Pass** | Algorithm stability |
| 🎯 **Feature Matrix** | ML-ready format | ✅ **Structured** | 🟢 **Pass** | Training readiness |

</div>

#### 📈 **Ringkasan Dataset Final**

<div align="center">

| **Sistem** | **Records** | **Fitur** | **Kepadatan** | **Kualitas** | **Status** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 🎨 **Content-Based** | 12,017 anime | 43 TF-IDF features + 2 numeric | 100% | ✅ **Production Ready** | 🚀 **Ready** |
| 🤝 **Collaborative** | 6.1M interactions | 47K users × 5K anime | 2.50% | ✅ **Highly Optimized** | 🚀 **Ready** |

</div>

---

### 🎯 **Kesimpulan Data Preparation**

**Teknik yang Berhasil Diterapkan:**

1. **Missing Value Handling** - Strategic removal dan imputation
2. **TF-IDF Vectorization** - Text-to-numeric transformation untuk genre
3. **Cosine Similarity Computation** - Similarity matrix untuk content-based
4. **Data Filtering** - Anti-sparsity strategy untuk collaborative filtering
5. **MinMax Normalization** - Feature scaling untuk konsistensi

**Manfaat yang Dicapai:**

- ✅ **Content-based system**: 100% dense feature matrix siap untuk similarity computation
- ✅ **Collaborative system**: Sparsity berkurang dari 99.08% ke 2.50%
- ✅ **Computational efficiency**: Memory usage turun 95%, speed naik 1,500%
- ✅ **Model accuracy**: Clean signals untuk prediksi yang lebih akurat

**Data preparation ini memastikan kedua sistem rekomendasi memiliki foundation yang solid untuk memberikan rekomendasi anime yang akurat dan relevan.**
