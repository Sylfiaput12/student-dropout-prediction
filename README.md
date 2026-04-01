# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah menghasilkan banyak lulusan dengan reputasi yang baik. Namun, masih terdapat permasalahan serius terkait tingginya jumlah mahasiswa yang tidak menyelesaikan pendidikannya (dropout).

Tingginya angka dropout menjadi tantangan besar bagi institusi karena dapat berdampak pada kualitas pendidikan, reputasi, serta efektivitas proses pembelajaran. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi sejak dini mahasiswa yang berpotensi mengalami dropout agar dapat diberikan bimbingan khusus.

Dalam proyek ini, dilakukan analisis data mahasiswa serta pembangunan model machine learning untuk memprediksi status mahasiswa (Dropout, Enrolled, atau Graduate). Selain itu, dibuat dashboard interaktif untuk membantu pihak institusi dalam memahami pola data dan memonitor performa mahasiswa

### Permasalahan Bisnis

Permasalahan bisnis yang ingin diselesaikan dalam proyek ini adalah:

- Tingginya jumlah mahasiswa yang mengalami dropout.
- Kesulitan dalam mengidentifikasi mahasiswa yang berpotensi dropout secara dini.
- Kurangnya insight terkait faktor-faktor yang memengaruhi status mahasiswa.
- Belum adanya sistem monitoring berbasis data untuk mendukung pengambilan keputusan

### Cakupan Proyek

Cakupan proyek ini meliputi:

- Analisis dan eksplorasi data mahasiswa.
- Data preprocessing (data splitting, handling imbalanced data, encoding, dan scaling).
- Pembangunan model machine learning untuk klasifikasi status mahasiswa.
- Evaluasi performa model.
- Pengembangan prototype aplikasi prediksi menggunakan Streamlit.
- Pembuatan dashboard analisis menggunakan Tableau.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup environment:

```
conda create - name final_student python=3.9
conda activate final_student

pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib

```

## Business Dashboard

Dashboard dibuat menggunakan Tableau untuk membantu pihak Jaya Jaya Institut dalam memahami kondisi mahasiswa secara menyeluruh.

Dashboard menampilkan:

- Total mahasiswa
- Persentase Dropout, Graduate, dan Enrolled
- Analisis berdasarkan:
  - Gender
  - Age
  - Admission Grade
  - Course
  - Marital Status
  - Scholarship
  - Tuition Status
  - Inflation Rate

Dashboard ini memudahkan pihak institusi dalam mengidentifikasi pola dan faktor yang memengaruhi risiko dropout, sehingga dapat digunakan sebagai dasar pengambilan keputusan.

Link Dashboard Tableu Public :

https://public.tableau.com/views/JayaJayaInstitutAnalysisDashboardDropOut/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Menjalankan Sistem Machine Learning

Prototype sistem dikembangkan menggunakan Streamlit untuk memprediksi status mahasiswa secara interaktif.

Fitur yang digunakan dalam model:

- Gender
- Course
- Age at Enrollment
- Debtor
- Marital Status
- Scholarship Holder
- Tuition Fees Up to Date
- Admission Grade
- Inflation Rate

Cara menjalankan:

```
streamlit run app.py
```

Setelah aplikasi dijalankan, pengguna dapat memasukkan data mahasiswa dan sistem akan memberikan hasil prediksi berupa:

- Dropout
- Enrolled
- Graduate

## Conclusion

Berdasarkan hasil analisis dan pemodelan, faktor yang paling berpengaruh terhadap status mahasiswa adalah faktor akademik dan finansial, seperti admission grade, status pembayaran tuition fees, serta kondisi keuangan (debtor).

Model yang dibangun menggunakan algoritma Random Forest menghasilkan akurasi sebesar 55%, yang menunjukkan performa masih dalam kategori moderat. Model mampu mengklasifikasikan kelas Dropout dan Graduate dengan cukup baik, namun masih mengalami kesulitan dalam mengidentifikasi kelas Enrolled.

Secara keseluruhan, proyek ini berhasil memberikan insight yang berguna bagi institusi dalam memahami faktor risiko dropout serta menyediakan sistem prediksi awal yang dapat digunakan sebagai alat bantu pengambilan keputusan.

Beberapa insight penting yang diperoleh dari analisis antara lain:

1. Mahasiswa yang tidak membayar biaya kuliah tepat waktu memiliki risiko dropout yang jauh lebih tinggi.
2. Mahasiswa tanpa beasiswa cenderung memiliki tingkat dropout yang lebih tinggi dibandingkan penerima beasiswa.
3. Performa akademik pada semester pertama merupakan indikator kuat dalam menentukan kemungkinan dropout.
4. Terdapat perbedaan risiko dropout berdasarkan gender dan usia mahasiswa.
5. Beberapa program studi memiliki tingkat dropout yang lebih tinggi dibandingkan yang lain.

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Mengembangkan program bantuan finansial bagi mahasiswa dengan risiko ekonomi tinggi.
- Memberikan pendampingan akademik khusus bagi mahasiswa dengan nilai masuk (admission grade) rendah.
- Melakukan monitoring berkala terhadap mahasiswa dengan risiko dropout.
- Mengembangkan model dengan fitur tambahan atau algoritma lain untuk meningkatkan performa prediksi.
- Mengintegrasikan dashboard dan sistem prediksi ke dalam sistem internal institusi untuk monitoring real-time.
