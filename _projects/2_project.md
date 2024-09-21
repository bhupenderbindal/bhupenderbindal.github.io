---
layout: page
title: "Studienarbeit: MVCNN"
description: Multiview classification of chloroplast cells
img: assets/img/mvcnn.png
importance: 1
category: work
---

Abstract:

Biological membranes are vital for cellular functioning in both plants and animals. Understanding the 3D structures of these membranes is essential to comprehend their functionality. Due to their nanoscale size, these structures are studied using transmission electron microscopy, which provides 2D micrographs of 3D structures. These micrographs are challenging to analyse due to their similar appearance. The aim of this study was
to classify 2D micrograph projections using convolutional neural networks (CNNs) and compare two classification strategies: one using a single image of the micrograph and the other employing images from diﬀerent sections of the same micrograph. The CNNs were trained on projections generated through SPIRE software. The results demonstrated that CNNs utilising a multi-view approach, considering multiple views of the micrograph, outperformed those using a single-view strategy. However, more rigorous testing on a wide variety of real TEM specimens is necessary to determine the eﬃcacy of models trained on software-generated projections to real TEM micrographs.


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/mvcnn.png" title="example image" class="img-fluid rounded z-depth-1" width="600" height="400"%}
    </div>
</div>
<div class="caption">
    a) Latefusion (fc) strategy; b) Score fusion (sum) strategy; adapted from <a href='https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0245230'>paper</a>.
</div>

Code and documentation: [GitHub repo](https://github.com/bhupenderbindal/sa_mvcnn).

<!-- adding presentation -->
<!-- <object data="/assets/pdf/Multi view classification of chloroplast cells_10.09.pdf" width="1000" height="1000" type='application/pdf'></object> -->
