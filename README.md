# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module



## Network


## ZCBAM

### ZCA: Zero parameter Channel Attention

### ZSA: Zero parameter Spatial Attention

## Dataset

### CIFAR-100

This dataset is just like the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), except it has 100 classes containing 600 images each. There are 500 training images and 100 testing images per class. The 100 classes in the CIFAR-100 are grouped into 20 superclasses. Each image comes with a "fine" label (the class to which it belongs) and a "coarse" label (the superclass to which it belongs).


## Training Rules

Epochs: 100

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model             | Acc0.        | Acc1.        | Acc2.        |
| ----------------- | ----------- | ----------- | ----------- |
| resnet18 (fine-tuned for cifar100(3x32x32)| 76.36%      | 75.94%      | 76.38%      |
| resnet18 + CBAM           |  76.20% | 76.55%      |       %|
| resnet18 + ZCBAM           |  76.46% |       %|       %|
