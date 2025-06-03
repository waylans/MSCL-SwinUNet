# MSCL-SwinUNet

This repo is the implementation of ["Multi-Scheme Cross-Level Attention Embedded U-shape Transformer for MRI Semantic Segmentation"]. we refer to  [MMSegmentation](https://github.com/open-mmlab/mmsegmentation) and [MMGeneration](https://github.com/open-mmlab/mmgeneration) and mix them to implement unsupervised domain adaptation based segmentation (UDA SEG) task. Many thanks to SenseTime and their two excellent repos.

<table>
    <tr>
    <td><img src="PaperFigs\Fig1.png" width = "100%" alt="MMOTU"/></td>
    <td><img src="PaperFigs\Fig4.png" width = "100%" alt="DS2Net"/></td>
    </tr>
</table>

## Dataset

**Multi-Modality Ovarian Tumor Ultrasound (MMOTU) image dataset** consists of two sub-sets with two modalities, which are **OTU\_2d** and **OTU\_CEUS** respectively including **1469 2d ultrasound images** and **170 CEUS images**. On both of these two sub-sets, we provide pixel-wise semantic annotations and global-wise category annotations. **Many thanks to Department of Gynecology and Obstetrics, Beijing Shijitan Hospital, Capital Medical University and their excellent works on collecting and annotating the data.**



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
