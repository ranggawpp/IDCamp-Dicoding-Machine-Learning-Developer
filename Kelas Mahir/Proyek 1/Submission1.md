# Laporan Proyek Machine Learning - Rangga Wibisana Putra Pamungkas

## Domain Proyek

### Latar Belakang

Di dunia digital yang serba cepat saat ini, di mana pekerjaan jarak jauh dan kolaborasi virtual telah menjadi norma, kebutuhan akan perangkat kerja yang efisien dan andal menjadi lebih penting dari sebelumnya. Di antara perangkat ini, laptop menajadi salah satu perangkat yang sangat diperlukan untuk memfasilitasi produktivitas, kreativitas, dan konektivitas. Namun, dengan banyaknya pilihan laptop yang tersedia di pasaran, memilih laptop yang tepat berdasarkan fitur atau spesifikasinya bisa menjadi hal yang menyulitkan. Tantangan ini telah mendorong munculnya proyek-proyek yang bertujuan untuk memprediksi harga laptop, dengan memanfaatkan algoritme pembelajaran mesin untuk membantu konsumen dalam membuat keputusan pembelian yang tepat.

Dengan memanfaatkan kekuatan teknik pembelajaran mesin seperti analisis regresi, kita dapat menganalisis data harga historis dan fitur produk untuk mengembangkan model prediktif. Model-model ini tidak hanya membantu konsumen dalam membuat keputusan pembelian yang tepat, tetapi juga membantu peritel dan produsen dalam strategi penetapan harga dan manajemen inventaris. Oleh karena itu, proyek prediksi harga laptop ini menjawab kebutuhan penting akan perangkat kerja yang dapat meningkatkan produktivitas dengan merampingkan proses pengambilan keputusan dalam memilih laptop dengan harga dan fitur yang tepat.

  Referensi: [A. D. Siburian, “Laptop Price Prediction with Machine Learning Using Regression Algorithm”, JUSIKOM PRIMA, vol. 6, no. 1, pp. 87-91, Sep. 2022.](https://doi.org/10.34012/jurnalsisteminformasidanilmukomputer.v6i1.2850)

## Business Understanding

Tidak seperti emas yang harga jual dan belinya mengacu pada harga perdagangan emas dunia, harga laptop dipengaruhi oleh beberapa fitur atau spesifikasi. Fitur tersebut antara lain, kecepatan prosesor, ukuran RAM, ukuran penyimpanan, hingga ukuran layar. Tidak adanya acuan harga laptop seperti acuan harga emas menyebabkan peritel atau perusahaan memerlukan sistem untuk memprediksi harganya. Tentu saja semua bisnis mengejar profit. Oleh karena itu, penting bagi perusahaan untuk mengetahui dan dapat memprediksi harga laptop di pasar. Prediksi akan digunakan untuk membantu peritel dan produsen dalam strategi penetapan harga dan manajemen inventaris, sehingga dengan menentukan berapa harga beli yang pantas untuk laptop dengan karakteristik tertentu perusahaan bisa mendapatkan profit sebesar mungkin.

### Problem Statements

Berdasarkan kondisi yang telah diuraikan sebelumnya, diperlukan pengembangan sebuah sistem prediksi harga laptop untuk menjawab permasalahan berikut:

- Dari serangkaian fitur yang ada, fitur apa yang paling berpengaruh terhadap harga laptop?
- Berapa harga pasar laptop dengan karakteristik atau fitur tertentu?  

### Goals

Untuk  menjawab pertanyaan tersebut, akan dikembangkan sebuah predictive modelling dengan tujuan atau goals sebagai berikut:

- Mengetahui fitur yang paling berkorelasi dengan harga laptop.
- Membuat model machine learning yang dapat memprediksi harga laptop seakurat mungkin berdasarkan fitur-fitur yang ada.

### Solution statements

Untuk mencapai goals diatas yaitu mendapatkan model terbaik untuk memprediksi harga, pengembangan model akan menggunakan beberapa algoritma machine learning yaitu K-Nearest Neighbor, Random Forest, AdaBoost, serta Linear Regression Algorithm. Dari keempat model ini, akan dipilih satu model yang memiliki nilai kesalahan prediksi terkecil. Dengan kata lain, kita akan membuat model seakurat mungkin.

## Data Understanding

Membuat model prediktif dengan machine learning tentu memerlukan data. Dataset yang akan kita gunakan pada projek kali ini adalah Laptop Price Dataset. Dataset ini merupakan dataset sintetis yang dibuat untuk mensimulasikan fitur-fitur yang umumnya terkait dengan harga laptop. Dataset ini mencakup fitur-fitur seperti merek, kecepatan prosesor, ukuran RAM, kapasitas penyimpanan, ukuran layar, dan berat. Dataset ini dapat diunduh melalui [Kaggle | Laptop Price Prediction](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

## Exploratory Data Analysis

### Deskripsi Variabel

Data yang digunakan ini berformat CSV (Comma-Separated Values) dan memiliki 1.000 data dengan 7 fitur. Terdapat tiga jenis data dalam dataset ini, yaitu satu fitur bertipe objek, dua fitur bertipe integer (int64), dan empat fitur bertipe desimal atau float (float64).

<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 1.png">
<br> Gambar 1
</p>

Variabel-variabel pada Laptop Price dataset adalah sebagai berikut:

- Brand             : Mewakili merek laptop, dengan pilihan termasuk Dell, HP, Lenovo, Asus, dan Acer.
- Processor_Speed   : Menunjukkan kecepatan prosesor laptop, yang dihasilkan secara seragam antara 1,5 dan 4,0 GHz.
- RAM_Size          : Mewakili pilihan ukuran RAM, termasuk 4GB, 8GB, 16GB, dan 32GB.
- Storage_Capacity  : Mensimulasikan kapasitas penyimpanan yang berbeda dengan opsi 256GB, 512GB, dan 1000GB (1TB).
- Screen_Size       : Mewakili ukuran layar laptop, dibuat secara acak antara 11 dan 17 inci.
- Weight            : Menunjukkan berat laptop dalam kilogram, disimulasikan secara seragam antara 2,0 hingga 5,0 kg.
- Price             : Mensimulasikan harga laptop berdasarkan hubungan linier dengan fitur-fiturnya, termasuk beberapa noise tambahan untuk meniru variasi dunia nyata.

<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 2.png">
<br> Gambar 2
</p>

Kemudian dengan menggunakan fungsi describe() kita dapatkan informasi statistik pada masing-masing fitur, antara lain:

- Count adalah jumlah sampel pada data.
- Mean adalah nilai rata-rata.
- Std adalah standar deviasi.
- Min yaitu nilai minimum setiap kolom.
- 25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama.
- 50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- 75% adalah kuartil ketiga.
- Max adalah nilai maksimum.

### Missing Value dan Outliers

Dataset ini tidak memiliki nilai hilang (missing value) dan tidak terdapat outlier pada fitur-fitur numeriknya, seperti pada fitur kecepatan prosesor dan fitur lainnya.

<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 3.png">
<br> Gambar 3
</p>

### Univariate Analysis

#### Categorical Features

Pada dataset ini terdapat satu fitur kategorikal yaitu fitur Brand, pada fitur Brand ini terdapat 5 kategori Brand dengan sebaran data yang cukup merata berada di kisaran 20%.

<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 4.png">
<br> Gambar 4
</p>

#### Numerical Features

<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 5.png">
<br> Gambar 5
</p>

Pada Gambar 5 di atas, melalui histogram dari setiap fitur tersebut kita dapatkan informasi sebagai berikut:
- Pada fitur Processor Speed, Screen Size dan Weight dapat kita lihat sebaran datanya yang cukup variatif. Processor Speed tersebar antara 1.5 hingga 4.0, Screen Size tersebar dari 11 hingga 17, serta pada Weight data tersebar dari 2.0 hingga 5.0.
- Pada fitur RAM Size sebaran data terbagi menjadi RAM 4, 8, 16 dan 32. Data terbanyak berada pada RAM 32.
- Pada fitur Storage capacity sebaran data terbagi menjadi 256, 512 dan 1000. Data terbanyak berada pada Storage Capacity 256.
- Pada fitur Price dapat kita lihat harga laptop sangan dipengaruhi oleh storage capacity, harga laptop menjadi terbagi tiga rentang seperti pada storage capacity.

### Multivariate Analysis

#### Categorical Features

Dengan mengamati rata-rata harga relatif terhadap fitur Brand, rata-rata harga cenderung mirip. Rentangnya berada antara 18000 hingga 20000. Sehingga, fitur Brand memiliki pengaruh atau dampak yang kecil terhadap rata-rata harga.

<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 6.png">
<br> Gambar 6
</p>

#### Numerical Features

<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 7.png">
<br> Gambar 7
</p>

## Data Preparation

Dalam Data preparation dilakukan beberapa langkah dan metode supaya model yang dibangun berjalan dengan baik yaitu,

- Encoding Fitur Kategori
<br>One hot encoding adalah teknik mengubah data kategorik menjadi data numerik dimana setiap kategori menjadi kolom baru dengan nilai 0 atau 1. Fitur yang akan diubah menjadi numerik pada proyek ini adalah Area Type, City, Furnishing Status, dan Tenant Preferred.

- Membagi Dataset
<br>Train test split aja proses membagi data menjadi data latih dan data validasi. Data train akan digunakan untuk membangun model, sedangkan data uji akan digunakan untuk menguji performa model. Pada proyek ini dataset sebesar 3696 dibagi menjadi 3511 untuk data latih dan 185 untuk data validasi. Dengan rasio 95% data pada data train dan 5% pada data validasi.

- Standarisasi
<br>Model yang dibangun akan memiliki performa lebih baik dan bekerja lebih cepat jika dimodelkan dengan data seragam yang memiliki skala relatif sama. Salah satu teknik normalisasi yang digunakan pada proyek ini adalah Standarisasi dengan sklearn.preprocessing.StandardScaler.

## Modeling

Digunakan empat algoritma atau Model machine learning untuk menyelesaikan permasalahan di atas yaitu

- Linear Regression
<br>Linear Regression adalah salah

- KNeighbors Regressor
<br>KNN adalah algoritma yang relatif sederhana dibandingkan dengan algoritma lain. Algoritma KNN menggunakan ‘kesamaan fitur’ untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam set pelatihan.

KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif). Nah, itulah mengapa algoritma ini dinamakan K-nearest neighbor (sejumlah k tetangga terdekat). KNN bisa digunakan untuk kasus klasifikasi dan regresi.

- RandomForest Regressor
<br>Algoritma random forest adalah salah satu algoritma supervised learning. Ia dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Random forest juga merupakan algoritma yang sering digunakan karena cukup sederhana tetapi memiliki stabilitas yang mumpuni.

Random forest merupakan salah satu model machine learning yang termasuk ke dalam kategori ensemble (group) learning. Apa itu model ensemble? Sederhananya, ia merupakan model prediksi yang terdiri dari beberapa model dan bekerja secara bersama-sama. Ide dibalik model ensemble adalah sekelompok model yang bekerja bersama menyelesaikan masalah. Sehingga, tingkat keberhasilan akan lebih tinggi dibanding model yang bekerja sendirian. Pada model ensemble, setiap model harus membuat prediksi secara independen. Kemudian, prediksi dari setiap model ensemble ini digabungkan untuk membuat prediksi akhir.

- AdaBoost Regression.
<br>Seperti namanya, boosting, algoritma ini bertujuan untuk meningkatkan performa atau akurasi prediksi. Caranya adalah dengan menggabungkan beberapa model sederhana dan dianggap lemah (weak learners) sehingga membentuk suatu model yang kuat (strong ensemble learner). Algoritma boosting muncul dari gagasan mengenai apakah algoritma yang sederhana seperti linear regression dan decision tree dapat dimodifikasi untuk dapat meningkatkan performa.

Dari keempat algoritma ini kemudian akan dipilih salah satu algoritma dengan nilai metrik evaluasi terbaik yang menunjukkan bahwa algoritma tersebut adalah yang terbaik.

## Evaluation
<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 8.png">
<br> Gambar 8
</p>
<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 9.png">
<br> Gambar 9
</p>
<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 10.png">
<br> Gambar 10
</p>
<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 11.png">
<br> Gambar 11
</p>

Mean Absolute Error (MAE): The MAE value indicates the average absolute difference between predicted and actual values. A smaller MAE suggests better model performance.
Mean Squared Error (MSE): The MSE is the average of the squared differences between predicted and actual values. A smaller MSE suggests the model is better at responding to data variability.
Coefficient of Determination (R-squared or R2): The R2 value that approaching 1, indicates that the model very effectively explains the variation in the data. A higher R2 value indicates better performance in explaining variability.

## Kesimpulan
<p align='center'>
<img title="a title" alt="Alt text" src="./img/Gambar 12.png">
<br> Gambar 12
</p>

Based on the modeling that has been conducted, regression analysis has been successfully performed using a machine learning approach, where the features 'Processor_Speed' becomes the most influential feature on 'Price'.
Considering all the evaluation metrics above, it can be concluded that linear regression model has excellent performance. This is supported by MAE, MAPE, MSE, RMSE, and R2 values that are very close to optimal. The model seems to be well-suited to the data used and capable of providing accurate predictions.