# Laporan Proyek Machine Learning - Rangga Wibisana Putra Pamungkas

## Domain Proyek
### Latar Belakang
Di dunia digital yang serba cepat saat ini, di mana pekerjaan jarak jauh dan kolaborasi virtual telah menjadi norma, kebutuhan akan perangkat kerja yang efisien dan andal menjadi lebih penting dari sebelumnya. Di antara alat-alat ini, laptop menonjol sebagai perangkat yang sangat diperlukan yang memfasilitasi produktivitas, kreativitas, dan konektivitas. Namun, dengan banyaknya pilihan laptop yang tersedia di pasaran, memilih laptop yang tepat yang menyeimbangkan antara performa, fitur, dan biaya bisa menjadi hal yang menakutkan. Tantangan ini telah mendorong munculnya proyek-proyek yang bertujuan untuk memprediksi harga laptop, dengan memanfaatkan algoritme pembelajaran mesin untuk membantu konsumen dalam membuat keputusan pembelian yang tepat.

Penelitian telah menunjukkan bahwa harga laptop dapat bervariasi secara signifikan berdasarkan berbagai faktor seperti merek, spesifikasi, dan tren pasar. Sebagai contoh, sebuah penelitian yang diterbitkan dalam Journal of Computer Science and Technology menemukan bahwa strategi penetapan harga yang digunakan oleh produsen laptop dipengaruhi oleh faktor-faktor seperti reputasi merek, inovasi teknologi, dan permintaan konsumen. Selain itu, penelitian yang dilakukan oleh perusahaan analisis pasar seperti Gartner dan IDC menunjukkan bahwa pasar laptop bersifat dinamis dan kompetitif, dengan harga yang berfluktuasi sebagai respons terhadap perubahan dinamika rantai pasokan, biaya komponen, dan preferensi konsumen.

Mengingat kompleksitas dan volatilitas pasar laptop, memprediksi harga laptop secara akurat telah menjadi upaya yang menantang namun penting. Dengan memanfaatkan kekuatan teknik pembelajaran mesin seperti analisis regresi dan jaringan saraf, para peneliti dan ilmuwan data dapat menganalisis data harga historis, tren pasar, dan fitur produk untuk mengembangkan model prediktif. Model-model ini tidak hanya membantu konsumen dalam membuat keputusan pembelian yang tepat, tetapi juga membantu peritel dan produsen dalam strategi penetapan harga dan manajemen inventaris. Oleh karena itu, proyek prediksi harga laptop ini menjawab kebutuhan penting akan alat kerja yang dapat meningkatkan produktivitas dengan merampingkan proses pengambilan keputusan dalam memilih laptop yang hemat biaya dan efisien.

Banyak orang yang membutuhkan perangkat kerja yang dapat meningkatkan produktivitas mereka, salah satu perangkat ini adalah laptop. Dalam situasi pasar saat ini, mereka tidak membeli laptop hanya berdasarkan harga saja. Mereka perlu memiliki laptop dengan spesifikasi yang sesuai dengan kebutuhannya untuk mendorong produktivitas. 

Memilih laptop dengan fitur yang tepat dengan harga yang pantas bisa menjadi hal yang melelahkan. Untuk mencegah pembelian laptop dengan harga yang terlalu mahal, diperlukan suatu cara untuk memprediksi harga laptop berdasarkan spesifikasi yang ditentukan. Dengan memahami dampak dari berbagai konfigurasi (CPU, RAM, penyimpanan, dll.) terhadap harga, pengguna dapat membuat pilihan yang lebih tepat sasaran yang sesuai dengan anggaran dan kebutuhan mereka.
Pada bagian ini, kamu perlu menuliskan latar belakang yang relevan dengan proyek yang diangkat.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Jelaskan mengapa dan bagaimana masalah tersebut harus diselesaikan
- Menyertakan hasil riset terkait atau referensi. Referensi yang diberikan harus berasal dari sumber yang kredibel dan author yang jelas.
  
  Referensi: [A. D. Siburian, “Laptop Price Prediction with Machine Learning Using Regression Algorithm”, JUSIKOM PRIMA, vol. 6, no. 1, pp. 87-91, Sep. 2022.](https://doi.org/10.34012/jurnalsisteminformasidanilmukomputer.v6i1.2850)

## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
    - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

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

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

