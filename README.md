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
| base line + CBAM         | 86.55%     |
| base line + zero parameter channel(Avg & Max Pooling)       | -%     |
| base line + zero parameter spatial(Avg & Max Pooling)       | -%      |
| base line + ZCBAM(Avg Pooling)         | -%      |
| base line + ZCBAM(Max Pooling)       | -%      |
| base line + ZCBAM(Avg & Max Pooling)         | 86.63%|

