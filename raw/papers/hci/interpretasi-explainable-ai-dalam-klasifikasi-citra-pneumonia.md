---
title: "INTERPRETASI EXPLAINABLE AI DALAM KLASIFIKASI CITRA PNEUMONIA"
authors: "ERIK DWI PRASETYA"
year: 2026
citations: 0
paper_type: "primary"
domain: "hci"
fetched: "2026-11-08T06:26:08.391690"
doi: ""
openalex_id: "https://openalex.org/W7219562637"
source_api: "openalex"
---

# INTERPRETASI EXPLAINABLE AI DALAM KLASIFIKASI CITRA PNEUMONIA

**著者**: ERIK DWI PRASETYA
**年**: 2026 | **被引用数**: 0
**タイプ**: primary | **分野**: HCI

## Abstract

Pneumonia merupakan penyakit serius pada paru-paru yang memiliki tingkat kematian tinggi secara global, terutama pada kelompok usia rentan. Diagnosis pneumonia umumnya dilakukan menggunakan citra x-ray yang memerlukan analisis ahli medis dengan waktu yang cukup lama. Penggunaan deep learning untuk klasifikasi citra medis menghadapi tantangan black box yang menghambat kepercayaan tenaga medis terhadap hasil prediksi model. Penelitian ini bertujuan mengimplementasikan arsitektur VGG16 untuk klasifikasi citra pneumonia dan menerapkan metode Explainable AI (XAI) menggunakan Grad-CAM++ untuk memberikan interpretasi visual terhadap keputusan model. Penelitian menggunakan dataset publik "Chest X-Ray Images (Pneumonia)" dari Kaggle dengan total 5.856 citra yang terdiri dari 1.583 citra normal dan 4.273 citra pneumonia. Metodologi penelitian meliputi preprocessing data dengan penyeragaman dimensi, augmentasi data, dan stratified k-fold cross validation. Pendekatan studi ablasi dua tahap dilakukan untuk mengidentifikasi kontribusi setiap komponen metodologi terhadap performa model. Model VGG16 dimodifikasi dengan fine-tuning arsitektur dan penerapan class weighting untuk mengatasi ketidakseimbangan dataset. Hasil penelitian menunjukkan model final (Eksperimen 3) mencapai akurasi 95,57%, recall 98,13%, precision 95,89%, F1-score 97,00%, dan AUC 97,93%. Model berhasil menekan kasus false negative menjadi 8 dari 238 kasus pneumonia, yang krusial dalam konteks medis untuk menghindari salah diagnosis. Implementasi Grad-CAM++ berhasil menghasilkan visualisasi heatmap yang menunjukkan area penting pada citra paru-paru yang menjadi dasar keputusan model. Perbandingan penggunaan lapisan konvolusi menunjukkan bahwa lapisan terakhir (Block5_conv3) menghasilkan representasi fitur yang paling abstrak dan terfokus pada kondisi klinis paru-paru. Penelitian ini membuktikan bahwa kombinasi arsitektur VGG16 yang dimodifikasi dengan metode XAI Grad-CAM++ dapat menghasilkan model klasifikasi pneumonia dengan performa tinggi dan interpretasi yang baik. Model yang dikembangkan memiliki potensi sebagai decision support system untuk membantu tenaga medis dalam diagnosis pneumonia yang lebih cepat dan akurat, meskipun masih memerlukan validasi lanjut oleh ahli radiologi. Seluruh eksperimen dari penelitian ini disimpan pada situs https://github.com/ED-Prasetya/dataset_imbalance.
