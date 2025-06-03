# MSCL-SwinUNet

This repo is the implementation of ["Multi-Scheme Cross-Level Attention Embedded U-shape Transformer for MRI Semantic Segmentation"]. we refer to  [MMSegmentation](https://github.com/open-mmlab/mmsegmentation) and [MMGeneration](https://github.com/open-mmlab/mmgeneration) and Supervised MRI Semantic Segmentation task. Many thanks to SenseTime and their two excellent repos.

<table>
    <tr>
    <td><img src="PaperFigs\Fig1.png" width = "100%" alt="MSCL-SwinUNet"/></td>
    <td><img src="PaperFigs\Fig5.png" width = "100%" alt="ACDC"/></td>
     <td><img src="PaperFigs\Fig6.png" width = "100%" alt="MM-WHS"/></td>
    </tr>
</table>

<table>
  <tr>
    <td rowspan="2">
      <img src="PaperFigs/Fig1.png" width="400px" alt="MSCL-SwinUNet"/>
    </td>
    <td>
      <img src="PaperFigs/Fig5.png" width="300px" alt="ACDC Dataset"/>
    </td>
  </tr>
  <tr>
    <td>
      <img src="PaperFigs/Fig6.png" width="300px" alt="MM-WHS Dataset"/>
    </td>
  </tr>
</table>




## Dataset

To evaluate the performance and generalization ability of the proposed MSCL-SwinUNet, we conducted experiments on three benchmark datasets across different imaging modalities.The **ACDC (Automatic Cardiac Diagnosis Challenge)** dataset is an MRI-based cardiac imaging dataset comprising **150 examinations** from different patients. It provides **pixel-level annotations** for **three anatomical structures**, namely the **left ventricle (LV)**, **right ventricle (RV)**, and **myocardium (MYO)**.The **MM-WHS (Multi-Modality Whole Heart Segmentation)** dataset includes **two imaging modalities**, consisting of **52 CT scans** and **46 MR scans**.To further assess cross-modality generalization, we employed the **Synapse multi-organ segmentation dataset**, which contains **3,779 CT images** spanning **30 anatomical categories**.


## SwinUNet

### Install

1. requirements:
    
    python >= 3.7
        
    pytorch >= 1.4
        
    cuda >= 10.0
    
2. prerequisites: Please refer to  [MMSegmentation PREREQUISITES](https://mmsegmentation.readthedocs.io/en/latest/get_started.html); Please don't forget to install mmsegmentation with

     ```
     cd MMOTU_DS2Net
     
     pip install -e .
     
     chmod 777 ./tools/dist_train.sh
     
     chmod 777 ./tools/dist_test.sh
     ```

### Training

**mit_b5.pth** : [google drive](https://drive.google.com/drive/folders/1cmKZgU8Ktg-v-jiwldEc6IghxVSNcFqk?usp=sharing) (Before training Segformer or DS<sup>2</sup>Net_T, loading ImageNet-pretrained mit_b5.pth is very useful. We provide this pretrained backbone here. The pretrained backbone has already been transformed to fit for our repo.)

#### Task: Single-modality semantic segmentation

<table>
    <tr>
    <td><img src="PaperFigs\SSeg.jpg" width = "100%" alt="Single-Modality semantic segmentation"/></td>
    </tr>
</table>
  
     cd MSCL-SwinUNet
     
     ./tools/dist_train.sh ./experiments/MSCL_SwinUNet_160k_WHS/config/MSCL_SwinUNet_160k_WHS.py 2 2


### Testing

#### Task: Single-modality semantic segmentation
  
     cd MSCL-SwinUNet
     
     ./tools/dist_test.sh ./experiments/MSCL_SwinUNet_160k_WHS/config/MSCL_SwinUNet_160k_WHS.py ./experiments/MSCL_SwinUNet_160k__WHS/results/WHS_iter_3200_81.11.pth 2 --eval mDice


## Description of MSCL-SwinUNet

If you have any question, please discuss with me by sending email to wq@cap.edu.cn.


# References
Many thanks to their excellent works
* [MMSegmentation](https://github.com/open-mmlab/mmsegmentation)
* [MMGeneration](https://github.com/open-mmlab/mmgeneration)
