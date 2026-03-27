# DSRCNet: Tiny Object Detection in Remote Sensing Images via Dense Semantic Supervision and Spatial Calibration

[![Status](https://img.shields.io/badge/Paper-Under_Review-orange.svg)]()
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Pytorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?e&logo=PyTorch&logoColor=white)]()

> **Note**:The manuscript is currently under review.

---

## 💡 Introduction

Tiny objects in remote sensing images contain very few pixels and often exhibit extreme aspect ratios, leading to severe feature loss and imprecise localization in existing detection models 

We propose the **Dense Semantic Region-supervised Reconstruction and Spatial Calibration Network (DSRCNet)** to address these challenges through a unified closed-loop framework. DSRCNet significantly reduces model parameters while achieving an optimal balance between accuracy and inference speed.

### Core Components:
* **DSRS (Dense Semantic Region Supervision):** Establishes the semantic foundation by generating auxiliary heatmaps in shallow layers, guiding early network attention for weak targets.
* **MKCPB (Multi-Kernel Context Perception Block):** Replaces the traditional downsampling modules by synchronously performing spatial compression and multi-scale context interaction, preserving fine-grained textures.
* **DSFCM (Depth-adaptive Strip Feature Calibration Module):** Completes the alignment process by recalibrating feature activations toward geometric centers using strip convolutions and coordinate pooling.

---

## 🚀 Main Results

Extensive experiments on **VisDrone**, **AI-TOD**, and **DIOR** datasets show that DSRCNet achieves an exceptional trade-off between accuracy and speed.

### Performance on VisDrone Validation Dataset
Tested on a single NVIDIA GeForce RTX 3090 GPU.

| Model | Params (M) | FLOPs (G) | mAP_50 (%) | mAP_50-95 (%) | FPS |
| :--- | :---: | :---: | :---: | :---: | :---: |
| DSRCNet-N | **1.2** | **11.7** | 38.6 | 23.3 | **146** |
| DSRCNet-S | 4.1 | 35.3 | 45.8 | 27.4 | 133 |
| DSRCNet-M | 11.9 | 94.3 | 51.1 | 31.8 | 108 |
| DSRCNet-L | 26.2 | 199.7 | **52.1** | **32.5** | 63 |

>DSRCNet-S requires only 4.1M parameters, achieving a 63.4% reduction relative to the 11.2M YOLOv8-S baseline, while the mAP_50 on VisDrone increases from 39.6% to 45.8%.

## 🖼️ Visualizations

Our proposed DSRCNet provides more accurate focus on the geometric centers of tiny objects and effectively suppresses background noise compared to baseline models.

<div align="center">
  <img src="vis.pdf" width="1000" alt="Qualitative comparison on VisDrone dataset">
  <p align="left"><b>Figure: Qualitative comparison of feature heatmaps and detection results on the VisDrone dataset.</b><br>
  Columns from left to right: (a) Ground Truth, (b) Baseline heatmaps, (c) DSRCNet heatmaps, (d) Baseline detection results, and (e) DSRCNet detection results. The DSRCNet heatmaps clearly demonstrate a more accurate focus on the geometric centers of objects.</p>
</div>
