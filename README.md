# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module

It is ispired from [CBAM](https://arxiv.org/pdf/1807.06521.pdf) and [BAM](https://arxiv.org/abs/1807.06514). 

My work is motivated by the following one question.

Is it possible to improve performance of CNNs using attention module that has no additional parameters(weight and bias)?

## ZCBAM Module

### ZCA: Zero parameter Channel Attention

### ZSA: Zero parameter Spatial Attention

### Residual Units

![Residual Units](https://user-images.githubusercontent.com/35001605/62101421-5cb7c580-b2d0-11e9-919b-62efbbdc4cd6.png)

## Dataset: CIFAR- 100

This dataset is just like the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html), except it has 100 classes containing 600 images each. There are 500 training images and 100 testing images per class. The 100 classes in the CIFAR-100 are grouped into 20 superclasses. Each image comes with a "fine" label (the class to which it belongs) and a "coarse" label (the superclass to which it belongs).

## Training Rules

Epochs: 200

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model| Param.| Acc1.| Acc2.| Acc3.| Acc4.| Acc5.| Best Acc.| Avg Acc.|
| ----------------- | ----------- | ----------- | ----------- | ----------- | ----------- |----------- |----------- |----------- |
| resnet18 | 11.22M      | 76.36%      | 75.94%      | 76.38%      | 76.03%      |76.37%      |76.38%      |76.24% |
| resnet18 + CBAM |11.39M     |  76.20% | 76.55%      |       76.23%| 76.26%      |76.16%      |76.55%      |76.33% |
| resnet18 + ZCBAM |  **11.22M**     | 76.46% |       76.95%|       76.30%| 76.34%      |76.12%      |**76.95%**      |**76.52%**|

## Reference

- Paper: [CBAM: Convolutional Block Attention Module](https://arxiv.org/pdf/1807.06521)
- Paper: [BAM: Bottleneck Attention Module](https://arxiv.org/abs/1807.06514)
- Repository: [Jongchan/attention-module](https://github.com/Jongchan/attention-module)
- Repository: [luuuyi/CBAM.PyTorch](https://github.com/luuuyi/CBAM.PyTorch)
- Repository: [kobiso/CBAM-tensorflow](https://github.com/kobiso/CBAM-tensorflow)
- Repository: [weiaicunzai/pytorch-cifar100](https://github.com/weiaicunzai/pytorch-cifar100)

