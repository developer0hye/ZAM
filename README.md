# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module



## Network


## ZBAM

### ZCA: Zero Parameter Channel Attention

### ZSA: Zero Parameter Spatial Attention

## Training Rules

Epochs: 100

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model             | Acc.        |
| ----------------- | ----------- |
| base line              | 86.62%      |
| base line + CBAM **1st**         | **86.93%**     |
| base line + zero parameter channel(Avg Pooling)       | 86.24%     |
| base line + zero parameter channel(Max Pooling)       | 86.45%     |
| base line + zero parameter spatial(Avg Pooling)       | 86.68%      |
| base line + zero parameter spatial(Max Pooling) **2nd**      | **86.84%**      |
| base line + ZCBAM(Avg Pooling)         | 86.75%      |
| base line + ZCBAM(Max Pooling)       | 86.5%      |
| base line + ZCBAM(Avg & Max Pooling)         | 86.63%|

