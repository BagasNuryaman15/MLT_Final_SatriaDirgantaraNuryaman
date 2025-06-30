# %% [markdown]
# # **Proyek Recommendations System: [Anime Recommendations Database]**

# %% [markdown]
# - **Nama:** Satria Dirgantara Nurayaman
# - **Email:** satriadirgantaranuryaman@gmail.com
# - **ID Dicoding:** Satria Dirgantara Nuryaman

# %% [markdown]
# ## **Import Library**

# %%
# Manipulation Data
import pandas as pd
import numpy as np
import re

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Data Preprocessing
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Reccommender System
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# TensorFlow
import tensorflow as tf

# Evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Configurations
import warnings 
warnings.filterwarnings('ignore')
plt.style.use('seaborn-v0_8-whitegrid')

# %% [markdown]
# ## **Data Loading**

# %%
# Load Anime.csv file
anime_df = pd.read_csv('Data/anime.csv')
anime_df.head()

# %%
# Load Rating.csv file
rating_df = pd.read_csv('Data/rating.csv')
rating_df.head()

# %%
# Ambil sample 100.000 baris secara acak
df_sample = rating_df.sample(n=10000, random_state=42)

# Simpan file ke data
df_sample.to_csv('Data/rating_sample.csv', index=False)

# %% [markdown]
# - Disini karena data rating.csv asli berukuran lebih dari 100mb maka aku memutuskan untuk melakukan sampling data sebanyak 100.000 baris, agar bisa di perlihatkan pada github.

# %% [markdown]
# ## **Exploratory Data Analysis (EDA)**

# %% [markdown]
# ### **Deskripsi Variable**
# 
# **Anime.csv:**
# | Kolom      | Deskripsi                                                                 |
# |------------|--------------------------------------------------------------------------|
# | anime_id   | ID unik untuk setiap anime (mengacu pada myanimelist.net)                |
# | name       | Nama lengkap anime                                                       |
# | genre      | Daftar genre anime, dipisahkan koma                                      |
# | type       | Tipe anime (TV, Movie, OVA, dll)                                         |
# | episodes   | Jumlah episode (1 jika movie)                                            |
# | rating     | Rata-rata rating dari seluruh user (skala 1-10)                          |
# | members    | Jumlah anggota komunitas yang memasukkan anime ini ke dalam grup mereka  |
# 
# **Rating.csv**
# | Kolom    | Deskripsi                                                                 |
# |----------|--------------------------------------------------------------------------|
# | user_id  | ID unik pengguna (acak, tidak dapat diidentifikasi)                      |
# | anime_id | ID anime yang dirating oleh user (mengacu pada anime_id di anime.csv)    |
# | rating   | Nilai rating yang diberikan user (skala 1-10, -1 jika tidak memberi rating)|

# %% [markdown]
# ### **Informasi Umum**

# %%
# Informasi singkat tentang dataset anime
print(f'Jumlah Baris dan Kolom anime_df adalah: {anime_df.shape}')
print(f'\n Informasi Tentang Dataset Anime :')

# Menampilkan informasi dasar
anime_df.info()

# %% [markdown]
# Berdasarkan hasil eksplorasi awal: 
# - Dataset anime terdiri dari **12.294** baris dan **7** fitur utama. 
# - Dataset ini juga terdiri dari **3** fitur bertipe data numerik seperti `anime_id`, `rating`, dan juga `members`, dan **4** bertipe data object seperti `name`, `genre`, `type`, dan juga `episodes`.
# - Sebagian besar data sudah lengkap, namun terdapat beberapa nilai kosong pada kolom `genre`, `type`, dan `rating`. Hal ini perlu diperhatikan pada tahap data preparation agar tidak mempengaruhi hasil rekomendasi. 
# 
# Secara umum, dataset ini sudah sangat representatif untuk membangun sistem rekomendasi berbasis konten dan kolaboratif.

# %%
# Informasi singkat tentang dataset rating
print(f'Jumlah Baris dan Kolom rating_df adalah: {rating_df.shape}')
print(f'\nInformasi Tentang Dataset Rating :')

# Menampilkan informasi dasar
rating_df.info()

# %% [markdown]
# Berdasarkan hasil eksplorasi awal ditemukan bahwa:
# - Dataset rating terdiri dari **7.813.737** baris dan **3** fitur utama, yaitu user_id, anime_id, dan rating. Seluruh data pada rating.csv bertipe numerik dan tidak ditemukan nilai kosong. 
# - Tapi, jumlah data yang sangat besar ini dapat menimbulkan tantangan komputasi, terutama pada proses training model collaborative filtering. 
# 
# Jika nanti proses komputasi sangat lambat, maka rencananya kita bakal mengambil sebanyak **1 - 2 juta sampel saja**.

# %% [markdown]
# ### **Ringkasan Statistik**

# %%
# Ringkasan statistik deskriptif untuk anmie_df
print('\nStatistik Deskriptif untuk anime_df:')

# Fitur Numerik
print('\nFitur Numerik:')
display(anime_df.describe())

# Fitur Kategorikal
print('\nFitur Kategorikal:')
display(anime_df.describe(include='object'))

# %% [markdown]
# Dari ringkasan statistik dataset `anime_df`, terdapat beberapa hal menarik yang dapat dicatat:
# 
# - Untuk fitur numerik:
#   - **Rating** anime memiliki rata rata **6.47** dari skala **10**, dengan nilai minimum **1.67** dan maksimum **10.0**, menunjukkan adanya sebaran kualitas dari yang sangat rendah hingga sangat tinggi.
#   - **Members**, yang merepresentasikan popularitas, sangat bervariasi, dengan median sebesar **1.550** ribu, namun ada anime yang mencapai lebih dari **1 juta anggota**, menunjukkan distribusi yang sangat tidak merata (right-skewed).
#   
# - Untuk fitur kategorikal:
#   - Terdapat **12.292 judul anime unik** dari **12.294 data**, menunjukkan nyaris tidak ada duplikasi nama.
#   - Genre paling sering muncul adalah **Hentai**, dengan **823 kemunculan**, sedangkan jenis penayangan paling dominan adalah **TV** (3787 data).
#   - Fitur `episodes` memiliki **187 nilai unik**, dengan episode `1` paling umum muncul (5677 kali), mengindikasikan bahwa pengguna sering menonton anime Movie atau mungkin OVA dan Special Episode.
# 
# Secara keseluruhan, dataset ini merepresentasikan dunia anime dengan sangat beragam, baik dari segi rating, popularitas, genre, hingga format tayangan.

# %%
# Ringkasan statistik dari dataset rating_df
print('\nStatistik Deskriptif untuk rating_df:')
rating_df.describe()

# %% [markdown]
# Dari ringkasan statistik deskriptif rating_df kita menemukan:
# 
# - Dataset ini mencatat lebih dari **7,8 juta interaksi** antara pengguna dan anime. Rata rata rating berada di angka **6.14**, dengan median **7.0**, menandakan kecenderungan pengguna atau penonton memberi nilai cukup positif. 
# 
# - Nilai rating berkisar dari **-1 hingga 10**, di mana **-1** kemungkinan besar berarti belum memberikan penilaian. Penyebaran rating cukup lebar, dengan standar deviasi **3.72**, menunjukkan adanya variasi opini yang tinggi. 
# 
# Secara keseluruhan, data ini menggambarkan sistem rating yang aktif dan sangat bervariasi, pondasi yang sangat kaya untuk membangun sistem rekomendasi.

# %% [markdown]
# ### **Identifikasi Missing Values dan Duplikasi**

# %%
# Identifikasi Missing Values dan Duplikasi anime_df
missing_values_anime = anime_df.isnull().sum()
missing_values_anime_percentage = (missing_values_anime / len(anime_df)) * 100
duplicates_anime = anime_df.duplicated().sum()

# Membuat DataFrame untuk missing_anime_df
missing_anime_df = pd.DataFrame({
    'Jumlah Missing Values': missing_values_anime,
    'Persentasi Missing Values': missing_values_anime_percentage,
    'Jumlah Duplikasi': duplicates_anime
}).sort_values(by='Jumlah Missing Values', ascending=False)

# Menampilkan DataFrame missing_anime_df
display(missing_anime_df)

# %% [markdown]
# - Secara keseluruhan, dataset `anime_df` tergolong bersih. Hanya terdapat sedikit missing values pada kolom `rating` (1.87%), `genre` (0.50%), dan `type` (0.20%). Sisanya lengkap 100%.
# - Tidak ditemukan **data duplikat** di seluruh kolom, termasuk `anime_id` dan `name`, yang berarti tiap entri mewakili satu anime yang unik.
# 
# 

# %%
# Identifikasi Missing Values dan Duplikasi rating_df
missing_values_anime = rating_df.isnull().sum()
missing_values_anime_percentage = (missing_values_anime / len(rating_df)) * 100
duplicates_anime = rating_df.duplicated().sum()

# Membuat DataFrame untuk missing_rating_df
missing_rating_df = pd.DataFrame({
    'Jumlah Missing Values': missing_values_anime,
    'Persentasi Missing Values': missing_values_anime_percentage,
    'Jumlah Duplikasi': duplicates_anime
}).sort_values(by='Jumlah Missing Values', ascending=False)

# Menampilkan DataFrame missing_rating_df
display(missing_rating_df)

# %% [markdown]
# - Dataset rating_df sangat bersih, tidak ada missing values yang teridentifikasi, tapi hanya aja duplikasi data saja dengan jumlah hanya 1.

# %% [markdown]
# ### **Univariate Visualization**

# %%
# Univariate Visualization - 4 Visualisasi Kunci untuk Recommendation System

# Setup figure dengan 4 subplot
fig, ax = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Univariate Analysis: Key Features for Recommendation System', fontsize=16, fontweight='bold')

# Preprocessing genre data
all_genres = []
for genres in anime_df['genre'].dropna():
    genre_list = [g.strip() for g in str(genres).split(',')]
    all_genres.extend(genre_list)

genre_counts = pd.Series(all_genres).value_counts().head(15)

# 1. Top 15 Genre Distribution - Content-Based Filtering Insight
bars = ax[0, 0].bar(range(len(genre_counts)), genre_counts.values, color='skyblue', edgecolor='navy', alpha=0.7)
ax[0, 0].set_title('Top 15 Genre Distribution\n(Content-Based Filtering Insight)', fontweight='bold', fontsize=12)
ax[0,0].set_xlabel('Genre', fontweight='bold')
ax[0,0].set_ylabel('Frequency', fontweight='bold')
ax[0,0].set_xticks(range(len(genre_counts)))
ax[0,0].set_xticklabels(genre_counts.index, rotation=45, ha='right')

# Menambahkan annotasi di atas bar
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax[0,0].text(bar.get_x() + bar.get_width()/2., height + 20,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=9)

ax[0,0].grid(axis='y', alpha=0.3)

# 2. Distribusi Rating Anime - Kualitas Konten

ax[0, 1].hist(anime_df['rating'].dropna(), bins=30, color='lightcoral', edgecolor='darkred', alpha=0.7)
ax[0, 1].axvline(anime_df['rating'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {anime_df["rating"].mean():.2f}')
ax[0, 1].axvline(anime_df['rating'].median(), color='orange', linestyle='--', linewidth=2, label=f'Median: {anime_df["rating"].median():.2f}')
ax[0, 1].set_title('Anime Rating Distribution\n(Content Quality Analysis)', fontweight='bold', fontsize=12)
ax[0, 1].set_xlabel('Rating (1-10)', fontweight='bold')
ax[0, 1].set_ylabel('Frequency', fontweight='bold')
ax[0, 1].legend()
ax[0, 1].grid(alpha=0.3)

# 3. Distribusi Type Anime
type_counts = anime_df['type'].value_counts()
wedges, texts, autotexts = ax[1, 0].pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%', 
                                   startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0'])
ax[1, 0].set_title('Anime Type Distribution\n(Format Preference Analysis)', fontweight='bold', fontsize=12)

# Styling pie chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# 4. Distribusi User Ratings (dari rating_df) - Collaborative Filtering Insight
user_rating_dist = rating_df[rating_df['rating'] != -1]['rating']


bars4 = ax[1, 1].bar(user_rating_dist.value_counts().sort_index().index, 
               user_rating_dist.value_counts().sort_index().values, 
               color='lightgreen', edgecolor='darkgreen', alpha=0.7)
ax[1, 1].set_title('User Rating Distribution\n(Collaborative Filtering Insight)', fontweight='bold', fontsize=12)
ax[1, 1].set_xlabel('User Rating (1-10)', fontweight='bold')
ax[1, 1].set_ylabel('Frequency', fontweight='bold')
ax[1, 1].set_xticks(range(1, 11))

# Antonasi di atas bar
total_ratings = len(user_rating_dist)
for bar in bars4:
    height = bar.get_height()
    percentage = (height / total_ratings) * 100
    ax[1, 1].text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{percentage:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=9)

ax[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# Tampilkan insights penting
print('='*60)
print('KEY INSIGHTS DARI UNIVARIATE ANALYSIS VISUALIZATION')
print('='*60)
print(f'- Total Keragaman Genre: {len(pd.Series(all_genres).unique())} Nilai Unik')
print(f'- Genre Paling Populer: {genre_counts.index[0]} ({genre_counts.iloc[0]} anime)')
print(f'- Rata rata rating anime: {anime_df["rating"].mean():.2f}/10')
print(f'- Preferensi Rating Pengguna: {user_rating_dist.mean():.2f} rata rata')
print(f'- Rating Users Paling Umum: {user_rating_dist.mode().iloc[0]}/10')
print(f'- Rating distribution skew: {"Positive bias" if user_rating_dist.mean() > 5.5 else "Negative bias"}')
print(f'- Tipe Paling Umum: {type_counts.index[0]} ({type_counts.iloc[0]} anime)')




# %% [markdown]
# Dari keempat visualisasi yang dilakukan di atas dan key insight yang diperoleh, kita menemukan bahwa:
# 
# - Preferensi pengguna terhadap konten anime sangat tercermin dari dominasi genre **_Comedy_**, yang menempati posisi teratas secara signifikan. Hal ini menunjukkan kecenderungan penonton terhadap tontonan yang **ringan dan menghibur**. Sementara itu, distribusi rating anime menunjukkan pola yang cukup seimbang, dengan **rata rata 6.47** dan **median 6.57**, mengindikasikan bahwa sebagian besar anime dinilai **cukup layak oleh komunitas**. Format **TV** menjadi tipe paling umum, menegaskan bahwa **serial** masih menjadi pilihan utama dalam industri anime dibanding format seperti OVA atau Movie.
# 
# - Dari sisi **interaksi pengguna**, rating yang diberikan menunjukkan kecenderungan yang **sangat positif**, dengan nilai **8/10** menjadi yang paling sering diberikan. Ini mengindikasikan adanya **bias positif** dalam perilaku pengguna, di mana mereka cenderung menilai lebih tinggi anime yang mereka tonton. Distribusi seperti ini memberi sinyal penting bagi pengembangan **sistem rekomendasi**, di mana **genre populer** dan **anime dengan rating tinggi** dapat menjadi **titik awal** dalam memberikan saran yang lebih **relevan dan memuaskan**.

# %% [markdown]
# ### **Multivariate Visualization**

# %%
# Setup figure dengan 3 subplot untuk Phase 1 Analysis
fig, ax = plt.subplots(1, 3, figsize=(20, 6))
fig.suptitle('Multivariate Analysis Phase 1: Content-Based Filtering Insights', fontsize=16, fontweight='bold')

# 1. Rating vs Genre Analysis (Boxplot)
# Preprocessing: Ambil top 10 genre untuk clarity
all_genres = []
anime_genre_mapping = []

for idx, genres in anime_df['genre'].dropna().items():
    genre_list = [g.strip() for g in str(genres).split(',')]
    for genre in genre_list:
        anime_genre_mapping.append({
            'anime_id': anime_df.loc[idx, 'anime_id'],
            'genre': genre,
            'rating': anime_df.loc[idx, 'rating']
        })

genre_rating_df = pd.DataFrame(anime_genre_mapping)
top_genres = genre_rating_df['genre'].value_counts().head(10).index

# Filter untuk top 10 genres
genre_rating_filtered = genre_rating_df[genre_rating_df['genre'].isin(top_genres)]

# Plot 1: Rating Distribution by Genre
sns.boxplot(data=genre_rating_filtered, x='genre', y='rating', ax=ax[0], palette='viridis')
ax[0].set_title('Rating Distribution by Top 10 Genres\n(Content Quality by Category)', fontweight='bold', fontsize=12)
ax[0].set_xlabel('Genre', fontweight='bold')
ax[0].set_ylabel('Rating (1-10)', fontweight='bold')
ax[0].tick_params(axis='x', rotation=45)
ax[0].grid(alpha=0.3)

# 2. Members vs Rating Correlation (Scatterplot)
# Filter outliers untuk visualization yang lebih baik
anime_filtered = anime_df[(anime_df['members'] < anime_df['members'].quantile(0.95)) & 
                         (anime_df['rating'].notna())]

scatter = ax[1].scatter(anime_filtered['members'], anime_filtered['rating'], 
                       alpha=0.6, c=anime_filtered['rating'], cmap='RdYlBu_r', s=30)
ax[1].set_title('Popularity vs Quality Analysis\n(Members vs Rating)', fontweight='bold', fontsize=12)
ax[1].set_xlabel('Members (Popularity)', fontweight='bold')
ax[1].set_ylabel('Rating (Quality)', fontweight='bold')

# Add trendline
z = np.polyfit(anime_filtered['members'], anime_filtered['rating'], 1)
p = np.poly1d(z)
ax[1].plot(anime_filtered['members'], p(anime_filtered['members']), "r--", alpha=0.8, linewidth=2)

# Add colorbar
plt.colorbar(scatter, ax=ax[1], label='Rating')
ax[1].grid(alpha=0.3)

# 3. Type vs Rating Analysis (Violin Plot)
anime_clean = anime_df[anime_df['rating'].notna() & anime_df['type'].notna()]
sns.violinplot(data=anime_clean, x='type', y='rating', ax=ax[2], palette='Set2')
ax[2].set_title('Rating Distribution by Anime Type\n(Format vs Quality)', fontweight='bold', fontsize=12)
ax[2].set_xlabel('Anime Type', fontweight='bold')
ax[2].set_ylabel('Rating (1-10)', fontweight='bold')
ax[2].tick_params(axis='x', rotation=45)
ax[2].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Analisis Korelasi dan Insights
print('='*50)
print('PHASE 1 MULTIVARIATE ANALYSIS INSIGHTS')
print('='*50)

# Correlation analysis
correlation = anime_df[['rating', 'members']].corr().iloc[0,1]
print(f'Korelasi Popularitas - Kualitas: {correlation:.3f}')

# Genre dengan rating tertinggi
avg_rating_by_genre = genre_rating_filtered.groupby('genre')['rating'].mean().sort_values(ascending=False)
print(f'Genre Rating Tertinggi: {avg_rating_by_genre.index[0]} (rata rata: {avg_rating_by_genre.iloc[0]:.2f})')
print(f'Genre Rating Terendah: {avg_rating_by_genre.index[-1]} (rata rata: {avg_rating_by_genre.iloc[-1]:.2f})')

# Type analysis
avg_rating_by_type = anime_clean.groupby('type')['rating'].mean().sort_values(ascending=False)
print(f'Tipe Terbaik berdasarkan Rating: {avg_rating_by_type.index[0]} (rata rata: {avg_rating_by_type.iloc[0]:.2f})')

# %% [markdown]
# Analisis ini menunjukkan bahwa kualitas anime sangat dipengaruhi oleh genre, popularitas, dan format penyajiannya:
# 
# - Genre **Shounen** muncul sebagai kategori dengan **rating rata rata tertinggi (7.06)**. Hal ini bukan kebetulan genre ini banyak digemari karena menyajikan cerita **penuh aksi, petualangan, dan perjuangan karakter zero to hero**, seperti yang ditampilkan dalam anime legendaris **"Big Three"**: *Naruto*, *One Piece*, *Bleach* dan bapak dari "**Big Three"** yaitu *Dragon Ball*. Popularitas mereka telah merevolusi industri anime dan memperluas basis penonton secara global.
# 
# - Sebaliknya, genre **Kids** menempati posisi terbawah dengan **rating rata rata 6.11**, mencerminkan perbedaan selera dan ekspektasi antara penonton anak anak dan dewasa.
# 
# - Dari sisi format, anime bertipe **TV** menjadi yang paling unggul secara kualitas dengan **rating rata rata 6.90**, menunjukkan bahwa **serialisasi** tetap menjadi format yang paling disukai penonton dibandingkan OVA, Movie, atau lainnya.
# 
# - Terdapat pula **korelasi positif sebesar 0.388** antara jumlah **members (popularitas)** dan **rating (kualitas)**. Ini mengindikasikan bahwa anime yang **lebih populer cenderung lebih disukai**, menjadikannya aspek penting dalam sistem rekomendasi berbasis content.
# 
# Dengan demikian, **genre populer**, **format serial**, dan **tingkat popularitas** menjadi komponen kunci dalam merancang sistem rekomendasi yang efektif dan memuaskan.

# %%
# Full Dataset Analysis - Multivariate Phase 2
rating_clean = rating_df[rating_df['rating'] != -1].copy()  
print(f'Dataset rating setelah remove unrated: {len(rating_clean):,} records')

# Merge dengan anime_df untuk mendapatkan informasi genre dan rating anime
merged_df = rating_clean.merge(anime_df[['anime_id', 'name', 'genre', 'rating', 'type']], on='anime_id', how='left')
merged_df = merged_df.dropna()  # Drop missing values setelah merge

print(f'Dataset gabungan FULL berhasil dibuat dengan {len(merged_df):,} interaksi user-anime')

# Setup figure untuk Full Dataset Analysis
fig, ax = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Multivariate Analysis Phase 2: Collaborative Filtering Insights (Full Dataset)', 
             fontsize=16, fontweight='bold')

# 1. User Rating vs Anime Rating (Quality Correlation) - FULL DATASET
ax[0, 0].scatter(merged_df['rating_y'], merged_df['rating_x'], alpha=0.1, s=0.5, rasterized=True)
ax[0, 0].set_title('User Rating vs Anime Quality\n(Collaborative vs Content Quality)', fontweight='bold', fontsize=12)
ax[0, 0].set_xlabel('Anime Rating (Official)', fontweight='bold')
ax[0, 0].set_ylabel('User Rating', fontweight='bold')
ax[0, 0].grid(alpha=0.3)

# Add correlation line
correlation_user_anime = merged_df[['rating_x', 'rating_y']].corr().iloc[0,1]
z = np.polyfit(merged_df['rating_y'], merged_df['rating_x'], 1)
p = np.poly1d(z)
ax[0, 0].plot(merged_df['rating_y'], p(merged_df['rating_y']), "r--", alpha=0.8, linewidth=2)
ax[0, 0].text(0.05, 0.95, f'Correlation: {correlation_user_anime:.3f}', 
              transform=ax[0, 0].transAxes, 
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.8), fontweight='bold')

# 2. User Activity Distribution (Rating Frequency per User) - FULL DATASET
user_activity = merged_df['user_id'].value_counts()
ax[0, 1].hist(user_activity, bins=100, color='lightblue', edgecolor='darkblue', alpha=0.7)
ax[0, 1].set_title('User Activity Distribution\n(Ratings per User)', fontweight='bold', fontsize=12)
ax[0, 1].set_xlabel('Number of Ratings per User', fontweight='bold')
ax[0, 1].set_ylabel('Frequency', fontweight='bold')
ax[0, 1].axvline(user_activity.mean(), color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {user_activity.mean():.1f}')
ax[0, 1].axvline(user_activity.median(), color='orange', linestyle='--', linewidth=2, 
                label=f'Median: {user_activity.median():.1f}')
ax[0, 1].legend()
ax[0, 1].grid(alpha=0.3)

# 3. Anime Popularity Distribution (Rating Frequency per Anime) - FULL DATASET
anime_popularity = merged_df['anime_id'].value_counts()
ax[1, 0].hist(anime_popularity, bins=100, color='lightcoral', edgecolor='darkred', alpha=0.7)
ax[1, 0].set_title('Anime Popularity Distribution\n(Ratings Received per Anime)', fontweight='bold', fontsize=12)
ax[1, 0].set_xlabel('Number of Ratings per Anime', fontweight='bold')
ax[1, 0].set_ylabel('Frequency', fontweight='bold')
ax[1, 0].axvline(anime_popularity.mean(), color='red', linestyle='--', linewidth=2,
                label=f'Mean: {anime_popularity.mean():.1f}')
ax[1, 0].axvline(anime_popularity.median(), color='orange', linestyle='--', linewidth=2,
                label=f'Median: {anime_popularity.median():.1f}')
ax[1, 0].legend()
ax[1, 0].grid(alpha=0.3)

# 4. Genre Preference Heatmap (Top 10 genres vs User Rating) - FULL DATASET
genre_ratings = []
for idx, row in merged_df.iterrows():
    if pd.notna(row['genre']):
        genres = [g.strip() for g in str(row['genre']).split(',')]
        for genre in genres:
            genre_ratings.append({'genre': genre, 'user_rating': row['rating_x']})

genre_rating_df = pd.DataFrame(genre_ratings)
top_10_genres = genre_rating_df['genre'].value_counts().head(10).index

# Create genre preference matrix
genre_preference = genre_rating_df[genre_rating_df['genre'].isin(top_10_genres)]
genre_matrix = genre_preference.groupby(['genre', 'user_rating']).size().unstack(fill_value=0)

# Normalize untuk percentage
genre_matrix_pct = genre_matrix.div(genre_matrix.sum(axis=1), axis=0) * 100

# Plot enhanced heatmap
im = ax[1, 1].imshow(genre_matrix_pct.values, cmap='YlOrRd', aspect='auto')
ax[1, 1].set_title('Genre vs User Rating Heatmap\n(Rating Distribution by Top 10 Genres)', fontweight='bold', fontsize=12)
ax[1, 1].set_xlabel('User Rating (1-10)', fontweight='bold')
ax[1, 1].set_ylabel('Genre', fontweight='bold')
ax[1, 1].set_xticks(range(len(genre_matrix_pct.columns)))
ax[1, 1].set_xticklabels(genre_matrix_pct.columns)
ax[1, 1].set_yticks(range(len(genre_matrix_pct.index)))
ax[1, 1].set_yticklabels(genre_matrix_pct.index)

# Add colorbar
plt.colorbar(im, ax=ax[1, 1], label='Percentage (%)')

plt.tight_layout()
plt.show()

# Full Dataset Insights
print('='*50)
print('PHASE 2 COLLABORATIVE FILTERING ANALYSIS INSIGHTS')
print('='*50)
print(f'- Korelasi User Rating vs Anime Quality: {correlation_user_anime:.3f}')
print(f'- Rata-rata aktivitas user: {user_activity.mean():.1f} rating per user')
print(f'- Median aktivitas user: {user_activity.median():.1f} rating per user')
print(f'- Rata-rata popularitas anime: {anime_popularity.mean():.1f} rating per anime')
print(f'- Median popularitas anime: {anime_popularity.median():.1f} rating per anime')
print(f'- User paling aktif memberikan: {user_activity.max():,} rating')
print(f'- Anime paling populer menerima: {anime_popularity.max():,} rating')

# Genre analysis
high_rating_genres = genre_rating_df[genre_rating_df['user_rating'] >= 8]['genre'].value_counts().head(5)
print('\nGenre paling disukai (rating 8-10):')
for i, (genre, count) in enumerate(high_rating_genres.items(), 1):
    print(f'{i}. {genre}: {count:,} rating tinggi')

# Data sparsity analysis
total_possible_interactions = merged_df['user_id'].nunique() * merged_df['anime_id'].nunique()
sparsity = (1 - len(merged_df) / total_possible_interactions) * 100
print(f'\nMatrix Sparsity: {sparsity:.2f}%')
print(f'Coverage: {100-sparsity:.2f}%')

# %% [markdown]
# Analisis ini menyoroti hubungan antara perilaku pengguna dan kualitas konten anime berdasarkan data interaksi yang sangat besar.
# 
# - Ditemukan **korelasi positif sebesar 0.411** antara **user rating** dan **rating resmi**, yang menunjukkan bahwa pengguna cukup konsisten dalam menilai kualitas anime. Ini memperkuat validitas penggunaan data interaksi pengguna dalam pendekatan collaborative filtering.
# 
# - Rata rata setiap pengguna memberikan **91 rating**, namun distribusinya mengikuti pola **long-tail** atau sebagian besar hanya memberi sedikit rating, dengan segelintir user yang sangat aktif, tercatat satu user bahkan memberikan **3.747 rating**. Ini mengindikasikan adanya kelompok (Fanatic) peningkat rating anime yang di sukai untuk membuat anime nya ada di papan atas IMDb dan juga MyAnimeList.
# 
# - Dari sisi anime, rata rata sebuah judul menerima **640 rating**, namun distribusi popularitas juga sangat timpang. Beberapa anime seperti yang paling populer tercatat menerima hingga **34.226 rating**, menunjukkan bahwa eksposur sangat tidak merata antar judul.
# 
# - Dalam distribusi rating berdasarkan genre, **Comedy** menjadi genre dengan **jumlah rating tinggi (8–10) terbanyak**, yakni lebih dari **1,1 juta rating**, diikuti oleh **Action**, **Romance**, dan **Drama**. Genre genre ini tidak hanya populer tetapi juga sangat disukai, menjadikannya pilar penting dalam sistem rekomendasi yang berbasis kolaborasi pengguna.
# 
# - Matrix sparsity sangat tinggi (**99.08%**), sehingga hanya sebagian kecil user yang memberi rating ke sebagian kecil anime.
# 
# Insight ini memberikan arah bahwa collaborative filtering dapat diperkuat dengan **mengidentifikasi pengguna aktif**, **mengelola bias popularitas**, serta memanfaatkan kekuatan genre favorit untuk memberikan rekomendasi yang lebih akurat dan memuaskan.

# %% [markdown]
# ## **Data Preparation**

# %% [markdown]
# ### **Penanganan Missing Values**

# %%
# Dataset anime
missing_anime = pd.DataFrame({
    'Jumlah Nilai Hilang': anime_df.isnull().sum(),
    'Persentase (%)': (anime_df.isnull().sum() / len(anime_df)) * 100
})
print('\nNilai Hilang pada Dataset Anime:')
display(missing_anime[missing_anime['Jumlah Nilai Hilang'] > 0])

# Dataset rating
rating_minus_one = (rating_df['rating'] == -1).sum()
print('\nDataset Rating:')
print(f'Nilai hilang: {rating_df.isnull().sum().sum()}')
print(f'Rating -1 (belum diberi nilai): {rating_minus_one:,} ({rating_minus_one/len(rating_df)*100:.2f}%)')

# 2. STRATEGI PEMBERSIHAN DATA
print('\nSTRATEGI & EKSEKUSI PEMBERSIHAN DATA')

# Membersihkan dataset anime
print('SEBELUM PEMBERSIHAN:')
print(f'Jumlah data anime: {len(anime_df):,}')
print(f'Jumlah data rating: {len(rating_df):,}')

# Menghapus nilai genre dan rating yang hilang, isi type yang hilang
anime_df_clean = anime_df.dropna(subset=['genre', 'rating']).copy()
anime_df_clean['type'].fillna('Unknown', inplace=True)

# Menghapus rating -1 (interaksi tanpa penilaian)
rating_df_clean = rating_df[rating_df['rating'] != -1].copy()

print('\nSETELAH PEMBERSIHAN:')
print(f'Jumlah data anime: {len(anime_df_clean):,} (berkurang {len(anime_df)-len(anime_df_clean):,})')
print(f'Jumlah data rating: {len(rating_df_clean):,} (berkurang {len(rating_df)-len(rating_df_clean):,})')

# 3. VALIDASI KUALITAS
print('\nVALIDASI KUALITAS')
print(f'Sisa nilai hilang pada data anime: {anime_df_clean.isnull().sum().sum()}')
print(f'Sisa nilai hilang pada data rating: {rating_df_clean.isnull().sum().sum()}')
print(f'Rentang nilai rating: {rating_df_clean["rating"].min()} - {rating_df_clean["rating"].max()}')
print(f'Jumlah anime yang digunakan bersama di kedua dataset: {len(set(rating_df_clean["anime_id"]).intersection(set(anime_df_clean["anime_id"]))):,}')

# %% [markdown]
# ### **Persiapan Data Untuk Content-Based Filtering**

# %% [markdown]
# #### **Persiapan Data genre untuk TF-IDF**

# %%
# Menyiapkan data untuk TF-IDF
data = anime_df_clean[['anime_id', 'name', 'genre', 'rating', 'members']].copy()

print(f'\nJumlah data siap untuk TF-IDF: {len(data):,}')
print('\nCONTOH DATA GENRE:')
for i, genre in enumerate(data['genre'].head(), 1):
    print(f'{i}. {genre}')

# Summarry statistics untuk data genre
print(f'\nSTATISTIK DATA:')
print(f'- Total anime: {len(data):,}')
print(f'- Genre unik rata-rata per anime: {data["genre"].str.count(",").mean() + 1:.1f}')
print(f'- Rating range: {data["rating"].min():.2f} - {data["rating"].max():.2f}')
print(f'- Members range: {data["members"].min():,} - {data["members"].max():,}')

# Analisis genre
total_genres = []
for genres in data['genre']:
    genre_list = [g.strip() for g in str(genres).split(',')]
    total_genres.extend(genre_list)

unique_genres = len(set(total_genres))
print(f'- Total genre unik dalam dataset: {unique_genres}')
print(f'- Rata-rata genre per anime: {len(total_genres)/len(data):.1f}')

# %% [markdown]
# #### **Pembangunan Vektor TF-IDF (Genre Vectorization)**

# %%
# Inisialisasi TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Melakukan perhitungan idf pada data genre
tfidf_vectorizer.fit(data['genre']) 

print('TF-IDF VECTORIZER BERHASIL DILATIH')
print(f'Jumlah fitur genre terdeteksi: {len(tfidf_vectorizer.get_feature_names_out())}')

# Membuat DataFrame untuk laporan
features = tfidf_vectorizer.get_feature_names_out()
tfidf_summary = pd.DataFrame({
    'No': range(1, len(features) + 1),
    'Genre': features,
    'Status': ['Terdeteksi'] * len(features)
})

print('\nRINGKASAN FITUR GENRE YANG TERDETEKSI:')
print(f'Total genre unik: {len(tfidf_summary)} genre')

# Hanya menampilkan sample DataFrame untuk laporan
print('\nSAMPLE FITUR GENRE (DataFrame Format):')
display(tfidf_summary.head(10))

print('\nDISTRIBUSI GENRE YANG TERDETEKSI:')
print(f'Genre pertama: {features[0]}')
print(f'Genre terakhir: {features[-1]}')
print(f'Sample genre populer: {", ".join(features[:5])}')

# %% [markdown]
# #### **Transformasi Genre Menjadi Matriks TF-IDF**

# %%
# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(data['genre']) 

print('TRANSFORMASI TF-IDF BERHASIL:')
print(f'Ukuran matrix: {tfidf_matrix.shape}')
print(f'Format: {tfidf_matrix.shape[0]} anime x {tfidf_matrix.shape[1]} genre features')

# Membuat DataFrame untuk visualisasi matrix sample
matrix_dense = tfidf_matrix.todense()
print('\nSAMPLE MATRIX TF-IDF (5 anime pertama):')
sample_matrix_df = pd.DataFrame(
    matrix_dense[:5],
    columns=tfidf_vectorizer.get_feature_names_out(),
    index=[f'Anime_{i+1}' for i in range(5)]
)

# Menampilkan hanya kolom yang memiliki nilai > 0 untuk sample pertama
non_zero_cols = sample_matrix_df.columns[sample_matrix_df.iloc[0] > 0][:10]  # Max 10 kolom
display(sample_matrix_df[non_zero_cols].round(4))

# Statistik dari matrix TF-IDF
print('\nSTATISTIK MATRIX TF-IDF:')
matrix_stats = pd.DataFrame({
    'Metrik': ['Sparsity (%)', 'Non-zero values', 'Max TF-IDF score', 'Mean TF-IDF score'],
    'Nilai': [
        f'{(1 - matrix_dense.sum() / matrix_dense.size) * 100:.2f}',
        f'{np.count_nonzero(matrix_dense):,}',
        f'{matrix_dense.max():.4f}',
        f'{matrix_dense.mean():.4f}'
    ]
})

display(matrix_stats)

# %% [markdown]
# #### **Visualisasi Sampling Matriks TF-IDF**

# %%
# Membuat DataFrame lengkap dari TF-IDF matrix
tfidf_df = pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tfidf_vectorizer.get_feature_names_out(),
    index=data['name']
)

print('SAMPLING MATRIX TF-IDF UNTUK VISUALISASI:')

# Sample 5 anime dan 10 genre secara acak
sample_visualization = tfidf_df.sample(10, axis=1).sample(5, axis=0)

print('SAMPLE MATRIX (5 anime X 10 genre):')
display(sample_visualization.round(4))

# Statistik sampling
print('\nSTATISTIK SAMPLING:')
sampling_stats = pd.DataFrame({
    'Metrik': ['Anime yang ditampilkan', 'Genre yang ditampilkan', 'Nilai rata-rata', 'Nilai maksimum'],
    'Nilai': [
        f'{sample_visualization.shape[0]} dari {tfidf_df.shape[0]}',
        f'{sample_visualization.shape[1]} dari {tfidf_df.shape[1]}',
        f'{sample_visualization.values.mean():.4f}',
        f'{sample_visualization.values.max():.4f}'
    ]
})
display(sampling_stats)

# %% [markdown]
# #### **Perhitungan Kemiripan Antar Anime (Cosine Similarity)**

# %%
# Menghitung cosine similarity berdasarkan TF-IDF matrix
cosine_sim = cosine_similarity(tfidf_matrix)

print('PERHITUNGAN COSINE SIMILARITY BERHASIL:')
print(f'Ukuran similarity matrix: {cosine_sim.shape}')
print(f'Format: {cosine_sim.shape[0]} x {cosine_sim.shape[1]} (anime vs anime)')

# Sample similarity matrix untuk visualisasi
print('\nSAMPLE SIMILARITY MATRIX (5x5):')
sample_similarity_df = pd.DataFrame(
    cosine_sim[:5, :5], 
    columns=[f'Anime_{i+1}' for i in range(5)],
    index=[f'Anime_{i+1}' for i in range(5)]
)
display(sample_similarity_df.round(4))

# Statistik similarity
print('\nSTATISTIK COSINE SIMILARITY:')
similarity_stats = pd.DataFrame({
    'Metrik': ['Minimum', 'Maximum', 'Mean', 'Std Dev'],
    'Nilai': [
        f'{cosine_sim.min():.4f}',
        f'{cosine_sim.max():.4f}', 
        f'{cosine_sim.mean():.4f}',
        f'{cosine_sim.std():.4f}'
    ]
})
display(similarity_stats)

# %% [markdown]
# ### **Persiapan Data untuk Collaborative Filtering**

# %% [markdown]
# #### **Pembangunan USER-ITEM MATRIX**

# %%
# 1. PEMBANGUNAN USER-ITEM MATRIX
print('\nMEMBANGUN USER-ITEM MATRIX:')

# Merge rating dengan anime data untuk mendapatkan nama anime
rating_with_anime = rating_df_clean.merge(
    anime_df_clean[['anime_id', 'name']], 
    on='anime_id', 
    how='inner'
)

print(f'Data gabungan rating x anime: {len(rating_with_anime):,} interaksi')
print(f'Unique users: {rating_with_anime["user_id"].nunique():,}')
print(f'Unique anime: {rating_with_anime["anime_id"].nunique():,}')

# 2. FILTERING DATA UNTUK EFISIENSI KOMPUTASI
print('\nFILTERING DATA UNTUK EFISIENSI:')

# Parameter filtering
min_user_ratings = 20  # User minimal kasih 20 rating
min_anime_ratings = 50  # Anime minimal dapat 50 rating

print(f'Filter kriteria:')
print(f'- Minimum rating per user: {min_user_ratings}')
print(f'- Minimum rating per anime: {min_anime_ratings}')

# Hitung aktivitas user dan popularitas anime
user_counts = rating_with_anime['user_id'].value_counts()
anime_counts = rating_with_anime['anime_id'].value_counts()

# Filter active users dan popular anime
active_users = user_counts[user_counts >= min_user_ratings].index
popular_anime = anime_counts[anime_counts >= min_anime_ratings].index

print(f'\nSebelum filtering:')
print(f'- Total users: {rating_with_anime["user_id"].nunique():,}')
print(f'- Total anime: {rating_with_anime["anime_id"].nunique():,}')
print(f'- Total interactions: {len(rating_with_anime):,}')

# Filter dataset
collaborative_data = rating_with_anime[
    (rating_with_anime['user_id'].isin(active_users)) &
    (rating_with_anime['anime_id'].isin(popular_anime))
].copy()

print(f'\nSetelah filtering:')
print(f'- Active users: {len(active_users):,}')
print(f'- Popular anime: {len(popular_anime):,}')
print(f'- Filtered interactions: {len(collaborative_data):,}')
print(f'- Data reduction: {(1 - len(collaborative_data)/len(rating_with_anime))*100:.1f}%')

# 3. ANALISIS KUALITAS DATA FILTERED
print('\nANALISIS KUALITAS DATA HASIL FILTERING:')

# Statistik detail
filtered_stats = pd.DataFrame({
    'Metrik': [
        'Rata-rata rating per user',
        'Rata-rata rating per anime', 
        'User paling aktif (max ratings)',
        'Anime paling populer (max ratings)',
        'Sparsity matrix (%)',
        'Coverage matrix (%)',
        'Efisiensi data (%)'
    ],
    'Nilai': [
        f'{collaborative_data.groupby("user_id").size().mean():.1f}',
        f'{collaborative_data.groupby("anime_id").size().mean():.1f}',
        f'{collaborative_data.groupby("user_id").size().max():,}',
        f'{collaborative_data.groupby("anime_id").size().max():,}',
        f'{(1 - len(collaborative_data)/(collaborative_data["user_id"].nunique() * collaborative_data["anime_id"].nunique()))*100:.2f}%',
        f'{(len(collaborative_data)/(collaborative_data["user_id"].nunique() * collaborative_data["anime_id"].nunique()))*100:.2f}%',
        f'{(len(collaborative_data)/len(rating_with_anime))*100:.1f}%'
    ]
})

display(filtered_stats)

# %% [markdown]
# #### **Encoding User dan Anime ID**

# %%
# Ambil data yang sudah difilter sebelumnya
df = collaborative_data.copy()

print(f'Dataset siap untuk collaborative filtering: {len(df):,} interactions')
print(f'Unique users: {df["user_id"].nunique():,}')
print(f'Unique anime: {df["anime_id"].nunique():,}')

# Bikin list unique user dan anime ID
user_ids = df['user_id'].unique().tolist()
anime_ids = df['anime_id'].unique().tolist()

print(f'\nTotal unique users: {len(user_ids):,}')
print(f'Total unique anime: {len(anime_ids):,}')

# Buat mapping dictionary untuk encode user dan anime jadi index (sesuai materi dicoding)
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

anime_to_anime_encoded = {x: i for i, x in enumerate(anime_ids)}
anime_encoded_to_anime = {i: x for i, x in enumerate(anime_ids)}

print('\nContoh encoding user:')
print(f'User {user_ids[0]} -> Index {user_to_user_encoded[user_ids[0]]}')
print(f'User {user_ids[1]} -> Index {user_to_user_encoded[user_ids[1]]}')

print('\nContoh encoding anime:')
print(f'Anime {anime_ids[0]} -> Index {anime_to_anime_encoded[anime_ids[0]]}')
print(f'Anime {anime_ids[1]} -> Index {anime_to_anime_encoded[anime_ids[1]]}')

# Apply encoding ke DataFrame
df['user'] = df['user_id'].map(user_to_user_encoded)
df['anime'] = df['anime_id'].map(anime_to_anime_encoded)

print('\nDataFrame setelah encoding:')
display(df[['user_id', 'user', 'anime_id', 'anime', 'rating']].head())

# Simpan info untuk modeling
num_users = len(user_ids)
num_anime = len(anime_ids)

print(f'\nINFO UNTUK NEURAL NETWORK:')
print(f'- Num users (vocabulary size): {num_users}')
print(f'- Num anime (vocabulary size): {num_anime}')
print(f'- Total interactions: {len(df):,}')

# %% [markdown]
# #### **Data Spliting untuk Neural Network**

# %%
# Normalize rating ke skala 0-1 untuk neural network
df['rating_normalized'] = (df['rating'] - 1) / 9  # dari 1-10 jadi 0-1

print(f'Rating asli range: {df["rating"].min()}-{df["rating"].max()}')
print(f'Rating normalized range: {df["rating_normalized"].min():.2f}-{df["rating_normalized"].max():.2f}')

# Shuffle data untuk randomness
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split data: 80% train, 20% test
train_size = int(0.8 * len(df_shuffled))
train_df = df_shuffled[:train_size].copy()
test_df = df_shuffled[train_size:].copy()

print(f'\nData splitting berhasil:')
print(f'- Training set: {len(train_df):,} interactions ({len(train_df)/len(df)*100:.1f}%)')
print(f'- Test set: {len(test_df):,} interactions ({len(test_df)/len(df)*100:.1f}%)')

# Prepare input arrays untuk TensorFlow
x_train = [train_df['user'].values, train_df['anime'].values]
y_train = train_df['rating_normalized'].values

x_test = [test_df['user'].values, test_df['anime'].values]
y_test = test_df['rating_normalized'].values

print(f'\nArrays untuk TensorFlow:')
print(f'- X_train: User array {x_train[0].shape}, Anime array {x_train[1].shape}')
print(f'- y_train: {y_train.shape}')
print(f'- X_test: User array {x_test[0].shape}, Anime array {x_test[1].shape}')
print(f'- y_test: {y_test.shape}')

# %% [markdown]
# ## **Modeling**

# %% [markdown]
# ### **Content-Based Filtering**

# %% [markdown]
# ### **Pembangunan Sistem Rekomendasi Content-Based Filtering**

# %%
def anime_recommendations(title, cosine_sim=cosine_sim, df=data, items=['name', 'genre', 'rating']):
    """
    Fungsi untuk memberikan rekomendasi anime berdasarkan kemiripan genre
    
    Parameters:
    -----------
    title : str
        Nama anime yang dijadikan referensi
    cosine_sim : array
        Matrix cosine similarity
    df : DataFrame
        Dataset anime
    items : list
        Kolom yang ingin ditampilkan dalam hasil
    
    Returns:
    --------
    DataFrame
        Top 10 rekomendasi anime dengan similarity score
    """
    # Mengambil indeks dari anime yang dipilih
    idx = df[df['name'] == title].index[0]
    
    # Mengambil skor kemiripan dengan semua anime
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Mengurutkan anime berdasarkan skor kemiripan
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Mengambil 10 anime teratas (selain anime input)
    sim_scores = sim_scores[1:11]
    
    # Mengambil indeks anime
    anime_indices = [i[0] for i in sim_scores]
    
    # Mengembalikan rekomendasi anime
    recommendations = df.iloc[anime_indices][items].copy()
    recommendations['similarity_score'] = [score[1] for score in sim_scores]
    
    return recommendations

print('CONTENT-BASED FILTERING MODEL BERHASIL DIBUAT!')
print(f'Model siap merekomendasikan dari {len(data):,} anime')
print(f'Berbasis {len(tfidf_vectorizer.get_feature_names_out())} fitur genre')

# %% [markdown]
# ### **Pembangunan Sistem Rekomendasi Collaborative Filtering**

# %% [markdown]
# #### **Neural Network Architecture**

# %%
# Build Neural Collaborative Filtering Model
class RecommenderNet(tf.keras.Model):
    def __init__(self, num_users, num_anime, embedding_size=64, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.num_users = num_users
        self.num_anime = num_anime
        self.embedding_size = embedding_size
        
        # User embedding layer
        self.user_embedding = tf.keras.layers.Embedding(
            num_users,
            embedding_size,
            embeddings_initializer='he_normal',
            embeddings_regularizer=tf.keras.regularizers.l2(1e-6)
        )
        
        # Anime embedding layer
        self.anime_embedding = tf.keras.layers.Embedding(
            num_anime,
            embedding_size,
            embeddings_initializer='he_normal',
            embeddings_regularizer=tf.keras.regularizers.l2(1e-6)
        )
        
        # Bias embeddings
        self.user_bias = tf.keras.layers.Embedding(num_users, 1)
        self.anime_bias = tf.keras.layers.Embedding(num_anime, 1)
        
        # Dropout untuk regularization
        self.dropout = tf.keras.layers.Dropout(0.2)
        
    def call(self, inputs):
        # Get embeddings
        user_vector = self.user_embedding(inputs[0])
        anime_vector = self.anime_embedding(inputs[1])
        
        # Get bias terms
        user_bias = self.user_bias(inputs[0])
        anime_bias = self.anime_bias(inputs[1])
        
        # Compute dot product
        dot_product = tf.reduce_sum(user_vector * anime_vector, axis=1, keepdims=True)
        
        # Add bias terms
        x = dot_product + user_bias + anime_bias
        
        # Apply dropout
        x = self.dropout(x)
        
        # Output with sigmoid activation (0-1 range)
        return tf.keras.activations.sigmoid(x)

# Instantiate model
model = RecommenderNet(num_users, num_anime)

print('NEURAL COLLABORATIVE FILTERING ARCHITECTURE BERHASIL DIBUAT!')
print(f'Model siap untuk {num_users:,} users dan {num_anime:,} anime')
print(f'Embedding size: 64 dimensions')
print(f'Regularization: L2 (1e-6) + Dropout (0.2)')

# %% [markdown]
# #### **Model Compilation**

# %%
# Model Compilation
model.compile(
    loss='mean_squared_error',
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    metrics=['mae', 'mse']
)

print('MODEL COMPILATION BERHASIL!')

# %% [markdown]
# #### **Model Training**

# %%
# QUICK FIX - Training cepat untuk deadline
history = model.fit(
    x_train, y_train,
    validation_data=(x_test, y_test),
    epochs=10,
    batch_size=2048,
    verbose=1
)

# %% [markdown]
# ### **Testing Model**

# %% [markdown]
# #### **Testing Content-Based Filtering Model**

# %%
def test_content_based_filtering_model():
    '''
    Fungsi pengujian profesional untuk model content-based filtering.
    Menguji berbagai anime dari genre dan kategori yang berbeda.
    '''
    print('=' * 60)
    print('PENGUJIAN MODEL CONTENT-BASED FILTERING DIMULAI!!!')
    print('=' * 60)

    test_scenarios = [
        {
            'anime_title': 'Gintama', 
            'category': 'Action/Comedy/Shounen', 
            'expected_genre': 'Comedy',
            'description': 'Anime shounen populer dengan unsur aksi dan komedi'
        },
        {
            'anime_title': 'Monster', 
            'category': 'Psychological/Thriller/Seinen', 
            'expected_genre': 'Thriller',
            'description': 'Serial thriller psikologis yang sangat terkenal'
        },
        {
            'anime_title': 'Berserk', 
            'category': 'Action/Fantasy/Horror/Seinen', 
            'expected_genre': 'Action',
            'description': 'Serial dark fantasy dengan unsur aksi yang kental'
        },
        {
            'anime_title': 'Initial D First Stage', 
            'category': 'Sports/Cars/Seinen', 
            'expected_genre': 'Sports',
            'description': 'Anime balapan mobil dengan tema olahraga dan seinen'
        },
        {
            'anime_title': 'Kill la Kill', 
            'category': 'Action/Comedy/School', 
            'expected_genre': 'Action',
            'description': 'Anime komedi aksi berlatar belakang sekolah'
        }
    ]

    test_results = []

    for i, scenario in enumerate(test_scenarios, 1):
        anime_title = scenario['anime_title']
        category = scenario['category']
        expected_genre = scenario['expected_genre']
        description = scenario['description']

        print('\nTAHAP PENGUJIAN KE - {}:'.format(i))
        print(f'Kasus Uji {i}: {anime_title}')
        print(f'Kategori: {category}')
        print(f'Deskripsi: {description}')
        print()

        try:
            if anime_title in data['name'].values:
                source_anime = data[data['name'] == anime_title].iloc[0]
                print(f'Properti Anime Asal:')
                print(f'  Judul: {source_anime["name"]}')
                print(f'  Genre: {source_anime["genre"]}')
                print(f'  Rating: {source_anime["rating"]:.2f}/10')
                print(f'  Jumlah Anggota: {source_anime["members"]:,}')

                # Buat rekomendasi
                recommendations = anime_recommendations(anime_title)
                print(f'\n10 Rekomendasi Teratas Berdasarkan Konten:')
                display(recommendations[['name', 'genre', 'rating', 'similarity_score']].round(3))

                avg_similarity = recommendations['similarity_score'].mean()
                max_similarity = recommendations['similarity_score'].max()
                min_similarity = recommendations['similarity_score'].min()
                avg_rating = recommendations['rating'].mean()
                similarity_variance = recommendations['similarity_score'].var()

                genre_matches = 0
                for _, rec in recommendations.iterrows():
                    if pd.notna(rec['genre']) and expected_genre.lower() in rec['genre'].lower():
                        genre_matches += 1

                genre_consistency = (genre_matches / len(recommendations)) * 100
                high_rating_count = (recommendations['rating'] >= 7.0).sum()
                rating_quality = (high_rating_count / len(recommendations)) * 100

                test_results.append({
                    'source_anime': anime_title,
                    'category': category,
                    'source_rating': source_anime['rating'],
                    'avg_similarity_score': avg_similarity,
                    'max_similarity_score': max_similarity,
                    'min_similarity_score': min_similarity,
                    'similarity_variance': similarity_variance,
                    'avg_recommended_rating': avg_rating,
                    'genre_consistency_pct': genre_consistency,
                    'rating_quality_pct': rating_quality,
                    'test_status': 'BERHASIL'
                })

                print(f'\nHasil Pengujian untuk "{anime_title}":')
                print(f'Metrik Kualitas:')
                print(f'  - Skor Kemiripan - Rata-rata: {avg_similarity:.3f}, Maksimum: {max_similarity:.3f}, Minimum: {min_similarity:.3f}')
                print(f'  - Rata-rata Rating Rekomendasi: {avg_rating:.2f}/10')
                print(f'  - Konsistensi Genre: {genre_consistency:.1f}%')
                print(f'  - Kualitas Rating Tinggi (≥7.0): {rating_quality:.1f}%')
                print(f'  - Status Uji: BERHASIL')

            else:
                print(f'Anime "{anime_title}" tidak ditemukan dalam dataset')
                similar_titles = data[data['name'].str.contains(anime_title.split()[0], case=False, na=False)]['name'].head(3)
                if len(similar_titles) > 0:
                    print('Alternatif judul serupa yang ditemukan:')
                    for idx, title in enumerate(similar_titles, 1):
                        print(f'  {idx}. {title}')
                else:
                    print('  Tidak ada judul serupa ditemukan')

                test_results.append({
                    'source_anime': anime_title,
                    'category': category,
                    'source_rating': None,
                    'avg_similarity_score': None,
                    'max_similarity_score': None,
                    'min_similarity_score': None,
                    'similarity_variance': None,
                    'avg_recommended_rating': None,
                    'genre_consistency_pct': None,
                    'rating_quality_pct': None,
                    'test_status': 'TIDAK_DITEMUKAN'
                })

        except Exception as e:
            print(f'Error saat menguji {anime_title}: {str(e)}')
            import traceback
            print(f'Detail error: {traceback.format_exc()}')

            test_results.append({
                'source_anime': anime_title,
                'category': category,
                'source_rating': None,
                'avg_similarity_score': None,
                'max_similarity_score': None,
                'min_similarity_score': None,
                'similarity_variance': None,
                'avg_recommended_rating': None,
                'genre_consistency_pct': None,
                'rating_quality_pct': None,
                'test_status': 'ERROR'
            })

    return pd.DataFrame(test_results)


content_test_results = test_content_based_filtering_model()

print('\n')
print('=' * 60)
print('RANGKUMAN HASIL PENGUJIAN')
print('='*60)
display(content_test_results)

success_rate = (content_test_results['test_status'] == 'BERHASIL').sum() / len(content_test_results) * 100
print('\nRINGKASAN KINERJA FILTERING BERBASIS KONTEN:')
print(f'  Tingkat Keberhasilan: {success_rate:.1f}%')

successful_tests = content_test_results[content_test_results['test_status'] == 'BERHASIL']
if len(successful_tests) > 0:
    print(f'  Rata-rata Skor Kemiripan: {successful_tests["avg_similarity_score"].mean():.3f}')
    print(f'  Rata-rata Rating Rekomendasi: {successful_tests["avg_recommended_rating"].mean():.2f}/10')
    print(f'  Rata-rata Konsistensi Genre: {successful_tests["genre_consistency_pct"].mean():.1f}%')
    print(f'  Rata-rata Kualitas Rating: {successful_tests["rating_quality_pct"].mean():.1f}%')

    best_test = successful_tests.loc[successful_tests['avg_similarity_score'].idxmax()]
    print(f'  Kasus Terbaik: {best_test["source_anime"]} (Kemiripan: {best_test["avg_similarity_score"]:.3f})')

print(f'\n  Sistem menunjukkan performa yang {"sangat baik" if success_rate >= 80 else "cukup baik" if success_rate >= 60 else "perlu ditingkatkan"}')

# %% [markdown]
# #### **Testing Collaborative Filtering Model**

# %%
# Fungsi untuk menghasilkan rekomendasi anime berdasarkan collaborative filtering
def get_anime_recommendations_collaborative(user_id, model, num_recommendations=5):
    '''
    Menghasilkan rekomendasi anime untuk pengguna tertentu menggunakan collaborative filtering
    '''
    try:
        # Langkah 1: Mengambil data pengguna
        user_data = collaborative_data[collaborative_data['user_id'] == user_id]
        if user_data.empty:
            return 'Pengguna tidak ditemukan dalam data'

        # Langkah 2: Mengambil daftar anime yang telah ditonton
        user_anime_list = user_data['anime_id'].values.tolist()
        all_anime_ids = collaborative_data['anime_id'].unique()
        unrated_anime = [anime_id for anime_id in all_anime_ids if anime_id not in user_anime_list]

        if len(unrated_anime) == 0:
            return 'Pengguna telah menonton seluruh anime dalam data'

        # Langkah 3: Pastikan user sudah masuk dalam pemetaan encoding
        if user_id not in user_to_user_encoded:
            return 'Pengguna tidak ditemukan dalam pemetaan encoding'

        user_encoded = user_to_user_encoded[user_id]

        # Langkah 4: Menyusun input prediksi untuk batch
        valid_anime_ids, valid_anime_encoded = [], []
        for anime_id in unrated_anime[:500]:  # Dibatasi untuk efisiensi
            if anime_id in anime_to_anime_encoded:
                valid_anime_ids.append(anime_id)
                valid_anime_encoded.append(anime_to_anime_encoded[anime_id])

        if not valid_anime_encoded:
            return 'Tidak ada anime valid untuk diprediksi'

        # Menyusun input batch
        user_input = np.full((len(valid_anime_encoded), 1), user_encoded, dtype=np.int32)
        anime_input = np.array(valid_anime_encoded, dtype=np.int32).reshape(-1, 1)

        # Melakukan prediksi
        pred_ratings = model.predict([user_input, anime_input], verbose=0).flatten()
        pred_ratings_scaled = pred_ratings * 9 + 1  # Normalisasi ke skala 1-10

        # Menyusun daftar prediksi
        predictions = list(zip(valid_anime_ids, pred_ratings_scaled))
        predictions.sort(key=lambda x: x[1], reverse=True)
        top_predictions = predictions[:num_recommendations]

        # Menyusun DataFrame hasil rekomendasi
        results = []
        for anime_id, pred_rating in top_predictions:
            anime_info = anime_df_clean[anime_df_clean['anime_id'] == anime_id]
            if not anime_info.empty:
                anime = anime_info.iloc[0]
                genre = anime['genre'] if pd.notnull(anime['genre']) else '-'
                genre_display = genre[:50] + '...' if len(genre) > 50 else genre

                results.append({
                    'anime_id': anime_id,
                    'name': anime['name'],
                    'genre': genre_display,
                    'predicted_rating': float(pred_rating),
                    'official_rating': float(anime['rating'])
                })

        return pd.DataFrame(results)

    except Exception as e:
        import traceback
        return f'Terjadi kesalahan: {str(e)}\nDetail: {traceback.format_exc()}'
    

def test_collaborative_filtering_model(model):
    '''
    Fungsi pengujian profesional untuk model collaborative filtering.
    Menguji berbagai user dengan preferensi yang berbeda.
    '''
    print('=' * 60)
    print('PENGUJIAN MODEL COLLABORATIVE FILTERING DIMULAI!!!')
    print('=' * 60)

    # Ambil sample user yang aktif untuk testing
    active_users = collaborative_data['user_id'].value_counts().head(10).index.tolist()
    
    test_results = []
    
    for i, user_id in enumerate(active_users[:5], 1):  # Test 5 users
        print(f'\nTAHAP PENGUJIAN KE - {i}:')
        print(f'Kasus Uji {i}: User ID {user_id}')
        print('-' * 50)
        
        try:
            # Dapatkan data historis user
            user_history = collaborative_data[collaborative_data['user_id'] == user_id]
            
            if len(user_history) > 0:
                print(f'Profil User {user_id}:')
                print(f'  Total Rating yang Diberikan: {len(user_history)}')
                print(f'  Rata-rata Rating: {user_history["rating"].mean():.2f}/10')
                print(f'  Rating Tertinggi: {user_history["rating"].max()}/10')
                print(f'  Rating Terendah: {user_history["rating"].min()}/10')
                
                # Tampilkan beberapa anime favorit user (rating >= 8)
                favorite_anime = user_history[user_history['rating'] >= 8].head(3)
                if len(favorite_anime) > 0:
                    print(f'\nBeberapa Anime Favorit User (Rating ≥8):')
                    for idx, row in favorite_anime.iterrows():
                        anime_info = anime_df_clean[anime_df_clean['anime_id'] == row['anime_id']]
                        if not anime_info.empty:
                            anime_name = anime_info.iloc[0]['name']
                            print(f'  - {anime_name} (Rating User: {row["rating"]}/10)')
                
                # Generate rekomendasi
                recommendations = get_anime_recommendations_collaborative(user_id, model, 10)
                
                if isinstance(recommendations, pd.DataFrame) and len(recommendations) > 0:
                    print(f'\n10 Rekomendasi Teratas untuk User {user_id}:')
                    display(recommendations[['name', 'genre', 'predicted_rating', 'official_rating']].round(3))
                    
                    # Hitung metrik kualitas
                    avg_predicted = recommendations['predicted_rating'].mean()
                    avg_official = recommendations['official_rating'].mean()
                    prediction_variance = recommendations['predicted_rating'].var()
                    
                    # Cek kualitas prediksi (realistic range)
                    realistic_predictions = ((recommendations['predicted_rating'] >= 1) & 
                                           (recommendations['predicted_rating'] <= 10)).sum()
                    prediction_quality = (realistic_predictions / len(recommendations)) * 100
                    
                    # Cek diversity genre
                    unique_genres = set()
                    for genre_str in recommendations['genre'].dropna():
                        if genre_str != '-':
                            genres = [g.strip() for g in str(genre_str).split(',')]
                            unique_genres.update(genres)
                    
                    genre_diversity = len(unique_genres)
                    
                    test_results.append({
                        'user_id': user_id,
                        'total_user_ratings': len(user_history),
                        'user_avg_rating': user_history['rating'].mean(),
                        'avg_predicted_rating': avg_predicted,
                        'avg_official_rating': avg_official,
                        'prediction_variance': prediction_variance,
                        'prediction_quality_pct': prediction_quality,
                        'genre_diversity': genre_diversity,
                        'test_status': 'BERHASIL'
                    })
                    
                    print(f'\nHasil Pengujian untuk User {user_id}:')
                    print(f'Metrik Kualitas:')
                    print(f'  - Rata-rata Rating Prediksi: {avg_predicted:.2f}/10')
                    print(f'  - Rata-rata Rating Resmi Anime: {avg_official:.2f}/10')
                    print(f'  - Variansi Prediksi: {prediction_variance:.3f}')
                    print(f'  - Kualitas Prediksi (1-10 range): {prediction_quality:.1f}%')
                    print(f'  - Keragaman Genre: {genre_diversity} genre unik')
                    print(f'  - Status Uji: BERHASIL')
                    
                else:
                    print(f'Gagal generate rekomendasi: {recommendations}')
                    test_results.append({
                        'user_id': user_id,
                        'total_user_ratings': len(user_history),
                        'user_avg_rating': user_history['rating'].mean(),
                        'avg_predicted_rating': None,
                        'avg_official_rating': None,
                        'prediction_variance': None,
                        'prediction_quality_pct': None,
                        'genre_diversity': None,
                        'test_status': 'GAGAL_REKOMENDASI'
                    })
            
            else:
                print(f'User {user_id} tidak memiliki data rating')
                test_results.append({
                    'user_id': user_id,
                    'total_user_ratings': 0,
                    'user_avg_rating': None,
                    'avg_predicted_rating': None,
                    'avg_official_rating': None,
                    'prediction_variance': None,
                    'prediction_quality_pct': None,
                    'genre_diversity': None,
                    'test_status': 'TIDAK_ADA_DATA'
                })
                
        except Exception as e:
            print(f'Error saat menguji User {user_id}: {str(e)}')
            import traceback
            print(f'Detail error: {traceback.format_exc()}')
            
            test_results.append({
                'user_id': user_id,
                'total_user_ratings': None,
                'user_avg_rating': None,
                'avg_predicted_rating': None,
                'avg_official_rating': None,
                'prediction_variance': None,
                'prediction_quality_pct': None,
                'genre_diversity': None,
                'test_status': 'ERROR'
            })
    
    return pd.DataFrame(test_results)

# EKSEKUSI TESTING COLLABORATIVE FILTERING
print('\nMEMULAI PENGUJIAN COLLABORATIVE FILTERING MODEL')
print('=' * 80)

# Jalankan test
collaborative_test_results = test_collaborative_filtering_model(model)

# LAPORAN HASIL LENGKAP
print('\n\nLAPORAN AKHIR PENGUJIAN COLLABORATIVE FILTERING')
print('=' * 80)

print('\nHasil Uji Collaborative Filtering:')
display(collaborative_test_results)

# Analisis performa
collab_success_rate = (collaborative_test_results['test_status'] == 'BERHASIL').sum() / len(collaborative_test_results) * 100
print(f'\n RINGKASAN KINERJA COLLABORATIVE FILTERING:')
print(f'  Tingkat Keberhasilan: {collab_success_rate:.1f}%')

successful_collab = collaborative_test_results[collaborative_test_results['test_status'] == 'BERHASIL']
if not successful_collab.empty:
    print(f'  Rata-rata Rating Prediksi: {successful_collab["avg_predicted_rating"].mean():.2f}/10')
    print(f'  Rata-rata Rating Resmi: {successful_collab["avg_official_rating"].mean():.2f}/10')
    print(f'  Variansi Prediksi Rata-rata: {successful_collab["prediction_variance"].mean():.3f}')
    print(f'  Kualitas Prediksi Rata-rata: {successful_collab["prediction_quality_pct"].mean():.1f}%')
    print(f'  Keragaman Genre Rata-rata: {successful_collab["genre_diversity"].mean():.1f} genre')
    
    # Best performing user
    best_user = successful_collab.loc[successful_collab['prediction_quality_pct'].idxmax()]
    print(f'  User Terbaik: {best_user["user_id"]} (Kualitas: {best_user["prediction_quality_pct"]:.1f}%)')

print(f'\nModel collaborative filtering menunjukkan performa yang {"sangat baik" if collab_success_rate >= 80 else "cukup baik" if collab_success_rate >= 60 else "perlu ditingkatkan"}')

# %% [markdown]
# ## **Evaluation**

# %%
print('FINAL EVALUATION SUMMARY')
print('=' * 60)

# Content-Based Results
print('\nCONTENT-BASED FILTERING PERFORMANCE:')
print(f'  Success Rate: 100%')
print(f'  Avg Similarity Score: 0.894/1.0')
print(f'  Avg Recommendation Rating: 7.73/10')
print(f'  Genre Consistency: 90%+')

# Collaborative Results  
print('\nCOLLABORATIVE FILTERING PERFORMANCE:')
print(f'  Success Rate: {collab_success_rate:.1f}%')
if not successful_collab.empty:
    print(f'  Avg Predicted Rating: {successful_collab["avg_predicted_rating"].mean():.2f}/10')
    print(f'  Avg Official Rating: {successful_collab["avg_official_rating"].mean():.2f}/10')
    print(f'  Prediction Quality: {successful_collab["prediction_quality_pct"].mean():.1f}%')

# Training Metrics
print('\nNEURAL NETWORK TRAINING METRICS:')
final_loss = history.history['loss'][-1]
final_val_loss = history.history['val_loss'][-1] 
final_mae = history.history['mae'][-1]
final_val_mae = history.history['val_mae'][-1]

print(f'  Final Training Loss: {final_loss:.4f}')
print(f'  Final Validation Loss: {final_val_loss:.4f}')
print(f'  Final Training MAE: {final_mae:.4f}')
print(f'  Final Validation MAE: {final_val_mae:.4f}')

# %% [markdown]
# Model rekomendasi yang dibangun berhasil menunjukkan performa yang sangat baik dari dua sisi utama, yaitu content-based filtering dan collaborative filtering. Pendekatan content-based menghasilkan rekomendasi yang konsisten secara genre dengan tingkat kemiripan tinggi (avg similarity score 0.894) dan rata-rata rating rekomendasi mencapai 7.73/10. Sementara itu, collaborative filtering yang didukung oleh model neural network sederhana mampu memberikan prediksi rating yang cukup akurat (MAE ~0.099), dengan rata-rata rating prediksi sebesar 7.63/10 dan tingkat keberhasilan pengujian mencapai 100%. 
# 
# Pemilihan arsitektur neural network yang relatif sederhana dilakukan secara sadar karena keterbatasan waktu menjelang deadline proyek. Fokus utama diarahkan pada efisiensi pembangunan pipeline, stabilitas model, serta kemudahan deployment tanpa mengorbankan akurasi secara signifikan. Dengan performa yang solid dari kedua pendekatan, sistem rekomendasi ini siap untuk digunakan pada tahap evaluasi lanjutan atau pengembangan skala produksi.

# %%



