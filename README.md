# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module



## Network


## ZCBAM

### ZCA: Zero parameter Channel Attention

### ZSA: Zero parameter Spatial Attention

## Dataset

### CIFAR-10

This dataset is just like the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), except it has 100 classes containing 600 images each. There are 500 training images and 100 testing images per class. The 100 classes in the CIFAR-100 are grouped into 20 superclasses. Each image comes with a "fine" label (the class to which it belongs) and a "coarse" label (the superclass to which it belongs).


## Training Rules

Epochs: 100

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model             | Acc.        |
| ----------------- | ----------- |
| base line              | 76.36%      |
| base line + CBAM           |  76.20% |
| base line + ZCBAM           |  76.46% |
| base line + zero parameter channel(Avg Pooling)       |     |
| base line + zero parameter channel(Max Pooling)       |    |
| base line + zero parameter channel(Avg & Max Pooling)       |   |
| base line + zero parameter spatial(Avg Pooling)       |       |
| base line + zero parameter spatial(Max Pooling)       |       |
 base line + zero parameter spatial(Avg & Max Pooling)       |      |
| base line + zero parameter channel/spatial(Avg Pooling)         |  |
| base line + zero parameter channel/spatial(Max Pooling)       | |
| base line + zero parameter channel/spatial(Avg & Max Pooling)         ||
