# Laporan Proyek Machine Learning Terapan - Sistem Rekomendasi Anime
## Project Overview

Industri anime mengalami pertumbuhan yang sangat pesat dalam dekade terakhir, dengan nilai pasar global diperkirakan akan melampaui USD 48 miliar pada tahun 2030. Pada tahun 2023, industri anime mencatatkan pendapatan sebesar 3,3465 triliun yen, angka terbesar dalam sejarah dengan lebih dari 51% pendapatan berasal dari luar Jepang (Kumparan Bisnis, 2025; Seputar Otaku, 2025). Fenomena ini didorong oleh semakin besarnya basis penggemar global, termasuk di Indonesia yang memiliki komunitas anime yang sangat besar.

Seiring dengan ledakan jumlah judul anime baru yang mencapai lebih dari 300 judul TV pada tahun 2023, penonton menghadapi tantangan besar dalam memilih tontonan yang sesuai dengan preferensi mereka. Banyaknya pilihan justru menciptakan "paradoks kelimpahan", di mana pengguna merasa kewalahan dan kesulitan menemukan anime yang benar benar relevan. Kebanyakan pengguna masih mengandalkan rekomendasi dari forum atau tokoh tertentu yang cenderung bias pada judul judul populer, pendekatan yang tidak efisien dan tidak dapat diskalakan.

Untuk mengatasi tantangan tersebut, proyek ini bertujuan membangun sistem rekomendasi anime berbasis content-based filtering yang dapat membantu pengguna menemukan anime yang sesuai dengan preferensi mereka. Pendekatan ini memanfaatkan kemiripan konten seperti genre, deskripsi, dan karakteristik anime untuk memberikan rekomendasi yang dipersonalisasi. Penelitian terdahulu menunjukkan bahwa sistem rekomendasi untuk anime dapat dikembangkan melalui pendekatan content-based filtering dan collaborative filtering, dengan integrasi kedua metode memberikan hasil yang optimal (Putri & Faisal, 2023).

Penerapan sistem rekomendasi ini tidak hanya meningkatkan pengalaman pengguna dalam menemukan anime yang sesuai dengan selera mereka, tetapi juga membuka peluang bagi studio anime untuk menjangkau audiens yang lebih luas. Dengan demikian, sistem ini berpotensi mengurangi dominasi judul judul mainstream dan mendorong eksplorasi terhadap anime yang kurang dikenal namun berkualitas, sehingga menciptakan ekosistem anime yang lebih inklusif dan beragam.

### Referensi

Kumparan Bisnis. (2025). Industri Game dan Anime Diprediksi Melejit, Capai USD 467 Miliar di 2027. *Kumparan*. https://kumparan.com/kumparanbisnis industri-game-dan-anime-diprediksi-melejit-capai-usd-467-miliar-di-2027-24LsLjWy2yh

Putri, H. D., & Faisal, M. (2023). Analyzing the Effectiveness of Collaborative Filtering and Content-Based Filtering Methods in Anime Recommendation Systems. *Jurnal Komtika*, 7(2), 124-133. https://journal.unimma.ac.id/index.php/komtika/article/view/9219

Seputar Otaku. (2025). Ketika Pasar Global Mengalahkan Jepang: Peluang atau Tantangan untuk Masa Depan Anime. *Seputar Otaku*. https://seputarotaku.com/article/535/ketika-pasar-global-mengalahkan-jepang-apa-artinya-untuk-masa-depan-anime

---
## Business Understanding
### Problem Statements

Berdasarkan latar belakang yang telah dijelaskan, permasalahan yang dapat dirumuskan adalah:

1. **Bagaimana cara membantu pengguna menemukan anime yang sesuai dengan preferensi mereka di tengah banyaknya pilihan yang tersedia?**
2. **Bagaimana cara mengurangi ketergantungan pengguna pada rekomendasi manual yang bias dan tidak efisien?**
3. **Bagaimana cara memberikan rekomendasi anime yang akurat berdasarkan karakteristik konten dan pola preferensi pengguna?**

### Goals

Tujuan yang ingin dicapai dari proyek ini adalah:

1. **Membangun sistem rekomendasi anime** yang dapat memberikan saran tontonan yang relevan dan personal kepada pengguna.
2. **Mengimplementasikan model machine learning** yang dapat menganalisis preferensi pengguna secara otomatis.
3. **Meningkatkan pengalaman pengguna** dalam discovery anime dengan mengurangi waktu pencarian.

### Solution Approach

Untuk mencapai tujuan tersebut, proyek ini akan menggunakan **pendekatan hybrid** yang menggabungkan dua metode sistem rekomendasi:

1. **Content-Based Filtering**
   - Menganalisis karakteristik anime seperti genre, rating, dan deskripsi
   - Memberikan rekomendasi berdasarkan kemiripan konten dengan anime yang disukai pengguna
   - Keunggulan: Tidak memerlukan data pengguna lain, dapat menangani cold start problem

2. **Collaborative Filtering**
   - Menganalisis pola rating dan preferensi dari pengguna dengan selera serupa
   - Memberikan rekomendasi berdasarkan "wisdom of the crowd"
   - Keunggulan: Dapat menemukan pola tersembunyi dan memberikan rekomendasi yang tidak terduga

Pendekatan hybrid ini dipilih karena dapat mengatasi kelemahan masing masing metode dan memberikan rekomendasi yang lebih akurat serta beragam dibandingkan menggunakan satu metode saja.