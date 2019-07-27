# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module



## Network


## ZCBAM

### ZCA: Zero parameter Channel Attention

### ZSA: Zero parameter Spatial Attention

## Dataset

### CIFAR-10
The [CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) dataset consists of 60000 32x32 colour images in 100 classes, with 6000 images per class. 

There are 50000 training images and 10000 test images.

## Training Rules

Epochs: 100

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model             | Acc.        |
| ----------------- | ----------- |
| base line              | 76.36%      |
| base line + CBAM           |  76.20% |
| base line + zero parameter channel(Avg Pooling)       |     |
| base line + zero parameter channel(Max Pooling)       |    |
| base line + zero parameter channel(Avg & Max Pooling)       |   |
| base line + zero parameter spatial(Avg Pooling)       |       |
| base line + zero parameter spatial(Max Pooling)       |       |
 base line + zero parameter spatial(Avg & Max Pooling)       |      |
| base line + zero parameter channel/spatial(Avg Pooling)         |  |
| base line + zero parameter channel/spatial(Max Pooling)       | |
| base line + zero parameter channel/spatial(Avg & Max Pooling)         ||
