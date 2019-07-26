# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module



## Network


## ZBAM

### ZCA: Zero Parameter Channel Attention

### ZSA: Zero Parameter Spatial Attention

## Dataset

### CIFAR-10
The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. 

There are 50000 training images and 10000 test images.

![CIFAR - 10](https://user-images.githubusercontent.com/35001605/61969431-77aae100-b015-11e9-901e-e20740b523b9.PNG)


## Training Rules

Epochs: 100

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model             | Acc.        |
| ----------------- | ----------- |
| base line              | 86.62%      |
| base line + CBAM -- **1st**          | **86.93%**     |
| base line + zero parameter channel(Avg Pooling)       | 86.24%     |
| base line + zero parameter channel(Max Pooling)       | 86.45%     |
| base line + zero parameter channel(Avg & Max Pooling)       | 86.07%  |
| base line + zero parameter spatial(Avg Pooling)       | 86.68%      |
| base line + zero parameter spatial(Max Pooling)       | 86.84%      |
 base line + zero parameter spatial(Avg & Max Pooling)       | 86.53%     |
| base line + zero parameter channel/spatial(Avg Pooling)         | 86.75% |
| base line + zero parameter channel/spatial(Max Pooling)       | 86.5%|
| base line + zero parameter channel/spatial(Avg & Max Pooling)         |86.63%|
