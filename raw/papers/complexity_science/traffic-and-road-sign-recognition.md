---
title: "Traffic and road sign recognition"
authors: "Hasan Fleyeh"
year: 2026
citations: 30
paper_type: "primary"
domain: "complexity_science"
fetched: "2026-06-26T06:00:48.811014"
doi: "https://doi.org/10.17869/enu.233020"
openalex_id: "https://openalex.org/W147800203"
source_api: "openalex"
---

# Traffic and road sign recognition

**著者**: Hasan Fleyeh
**年**: 2026 | **被引用数**: 30
**タイプ**: primary | **分野**: 複雑系科学

## Abstract

This thesis presents a system to recognise and classify road and traffic signs for the purpose of developing an inventory of them which could assist the highway engineers' tasks of updating and maintaining them. It uses images taken by a camera from a moving vehicle. The system is based on three major stages: colour segmentation, recognition, and classification. Four colour segmentation algorithms are developed and tested. They are a shadow and highlight invariant, a dynamic threshold, a modification of de la Escalera's algorithm and a Fuzzy colour segmentation algorithm. All algorithms are tested using hundreds of images and the shadow-highlight invariant algorithm is eventually chosen as the best performer. This is because it is immune to shadows and highlights. It is also robust as it was tested in different lighting conditions, weather conditions, and times of the day. Approximately 97% successful segmentation rate was achieved using this algorithm. Recognition of traffic signs is carried out using a fuzzy shape recogniser. Based on four shape measures - the rectangularity, triangularity, ellipticity, and octagonality, fuzzy rules were developed to determine the shape of the sign. Among these shape measures octangonality has been introduced in this research. The final decision of the recogniser is based on the combination of both the colour and shape of the sign. The recogniser was tested in a variety of testing conditions giving an overall performance of approximately 88%. Classification was undertaken using a Support Vector Machine (SVM) classifier. The classification is carried out in two stages: rim's shape classification followed by the classification of interior of the sign. The classifier was trained and tested using binary images in addition to five different types of moments which are Geometric moments, Zernike moments, Legendre moments, Orthogonal Fourier-Mellin Moments, and Binary Haar features. The performance of the SVM was tested using different features, kernels, SVM types, SVM parameters, and moment's orders. The average classification rate achieved is about 97%. Binary images show the best testing results followed by Legendre moments. Linear kernel gives the best testing results followed by RBF. C-SVM shows very good performance, but v-SVM gives better results in some case.
