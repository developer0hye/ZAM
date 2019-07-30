# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module

It is ispired from [CBAM](https://arxiv.org/pdf/1807.06521.pdf) and [BAM](https://arxiv.org/abs/1807.06514). 

## ZCBAM Module

### ZCA: Zero parameter Channel Attention

### ZSA: Zero parameter Spatial Attention


## Dataset

### CIFAR-100

This dataset is just like the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), except it has 100 classes containing 600 images each. There are 500 training images and 100 testing images per class. The 100 classes in the CIFAR-100 are grouped into 20 superclasses. Each image comes with a "fine" label (the class to which it belongs) and a "coarse" label (the superclass to which it belongs).


## Training Rules

Epochs: 200

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model             | Acc1.        | Acc2.        | Acc3.        | Acc4.        | Acc5.        | Best Acc.        | Avg Acc.        |
| ----------------- | ----------- | ----------- | ----------- | ----------- |----------- |----------- |----------- |
| resnet18 | 76.36%      | 75.94%      | 76.38%      | 76.03%      |76.03%      |76.38%      |76.19% |
| resnet18 + CBAM           |  76.20% | 76.55%      |       76.23%| 76.26%      |76.16%      |76.55%      |76.33% |
| resnet18 + ZCBAM           |  76.46% |       76.95%|       76.30%| 76.34%      |76.12%      |**76.95%**      |**76.52%**|

## References
