# Laporan Proyek Machine Learning - Rangga Wibisana Putra Pamungkas

## Domain Proyek
### Latar Belakang
Di dunia digital yang serba cepat saat ini, di mana pekerjaan jarak jauh dan kolaborasi virtual telah menjadi norma, kebutuhan akan perangkat kerja yang efisien dan andal menjadi lebih penting dari sebelumnya. Di antara perangkat ini, laptop menajadi salah satu perangkat yang sangat diperlukan untuk memfasilitasi produktivitas, kreativitas, dan konektivitas. Namun, dengan banyaknya pilihan laptop yang tersedia di pasaran, memilih laptop dengan yang tepat berdasarkan fitur atau spesifikasinya bisa menjadi hal yang menyulitkan. Tantangan ini telah mendorong munculnya proyek-proyek yang bertujuan untuk memprediksi harga laptop, dengan memanfaatkan algoritme pembelajaran mesin untuk membantu konsumen dalam membuat keputusan pembelian yang tepat.

Dengan memanfaatkan kekuatan teknik pembelajaran mesin seperti analisis regresi, kita dapat menganalisis data harga historis dan fitur produk untuk mengembangkan model prediktif. Model-model ini tidak hanya membantu konsumen dalam membuat keputusan pembelian yang tepat, tetapi juga membantu peritel dan produsen dalam strategi penetapan harga dan manajemen inventaris. Oleh karena itu, proyek prediksi harga laptop ini menjawab kebutuhan penting akan perangkat kerja yang dapat meningkatkan produktivitas dengan merampingkan proses pengambilan keputusan dalam memilih laptop dengan harga dan fitur yang tepat.

  Referensi: [A. D. Siburian, “Laptop Price Prediction with Machine Learning Using Regression Algorithm”, JUSIKOM PRIMA, vol. 6, no. 1, pp. 87-91, Sep. 2022.](https://doi.org/10.34012/jurnalsisteminformasidanilmukomputer.v6i1.2850)

## Business Understanding

Tidak seperti emas yang harga jual dan belinya mengacu pada harga perdagangan emas dunia, harga laptop dipengaruhi oleh beberapa fitur atau spesifikasi. Fitur tersebut antara lain, kecepatan prosesor, ukuran RAM, ukuran penyimpanan, hingga ukuran layar. Tidak adanya acuan harga laptop seperti acuan harga emas menyebabkan peritel atau perusahaan memerlukan sistem untuk memprediksi harganya. Tentu saja semua bisnis mengejar profit. Oleh karena itu, penting bagi perusahaan untuk mengetahui dan dapat memprediksi harga laptop di pasar. Prediksi akan digunakan untuk membantu peritel dan produsen dalam strategi penetapan harga dan manajemen inventaris, sehingga dengan menentukan berapa harga beli yang pantas untuk laptop dengan karakteristik tertentu perusahaan bisa mendapatkan profit sebesar mungkin.

### Problem Statements

Berdasarkan kondisi yang telah diuraikan sebelumnya, diperlukan pengembangan sebuah sistem prediksi harga laptop untuk menjawab permasalahan berikut:
- Dari serangkaian fitur yang ada, fitur apa yang paling berpengaruh terhadap harga diamonds?
- Berapa harga pasar diamonds dengan karakteristik atau fitur tertentu?  

### Goals
Untuk  menjawab pertanyaan tersebut, akan dikembangkan sebuah predictive modelling dengan tujuan atau goals sebagai berikut:
- Mengetahui fitur yang paling berkorelasi dengan harga laptop.
- Membuat model machine learning yang dapat memprediksi harga laptop seakurat mungkin berdasarkan fitur-fitur yang ada.

### Solution statements
 Untuk mencapai goals diatas yaitu mendapatkan model terbaik untuk memprediksi harga, pengembangan model akan menggunakan beberapa algoritma machine learning yaitu K-Nearest Neighbor, Random Forest, AdaBoost, serta Linear Regression Algorithm. Dari keempat model ini, akan dipilih satu model yang memiliki nilai kesalahan prediksi terkecil. Dengan kata lain, kita akan membuat model seakurat mungkin, yaitu model dengan nilai kesalahan sekecil mungkin.

## Data Understanding
Membuat model prediktif dengan machine learning tentu memerlukan data. Dataset yang akan kita gunakan pada projek kali ini adalah Laptop Price Dataset. Dataset ini merupakan dataset sintetis yang dibuat untuk mensimulasikan fitur-fitur yang umumnya terkait dengan harga laptop. Dataset ini mencakup fitur-fitur seperti merek, kecepatan prosesor, ukuran RAM, kapasitas penyimpanan, ukuran layar, dan berat. Dataset ini dapat diunduh melalui [Kaggle | Laptop Price Prediction](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

### Variabel-variabel pada Laptop Price dataset adalah sebagai berikut:
- Brand             : Represents the laptop brand, with options including Dell, HP, Lenovo, Asus, and Acer.
- Processor_Speed   : Indicates the speed of the laptop's processor, generated uniformly between 1.5 and 4.0 GHz.
- RAM_Size          : Represents the random selection of RAM sizes, including 4GB, 8GB, 16GB, and 32GB.
- Storage_Capacity  : Simulates different storage capacities with options of 256GB, 512GB, and 1000GB (1TB).
- Screen_Size       : Represents the size of the laptop screen, randomly generated between 11 and 17 inches.
- Weight            : Indicates the weight of the laptop in kilograms, simulated uniformly between 2.0 and 5.0 kg.
- Price             : Simulates the laptop prices based on a linear relationship with the features, including some added noise to mimic real-world variations.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi
