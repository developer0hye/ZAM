# ZCBAM
ZCBAM: Zero parameter Convolutional Block Attention Module



## Network


## ZBAM

### ZCA: Zero Parameter Channel Attention

### ZSA: Zero Parameter Spatial Attention

## Training Rules

Epochs: 30

Batch Size: 128

Learning Rate: 0.1

## Experimental Results

| Model             | Acc.        |
| ----------------- | ----------- |
| base line              | 72.98%      |
| base line + CBAM         | 75.0%      |
| base line + zero parameter channel(Avg & Max Pooling)       | x%      |
| base line + zero parameter spatial(Avg & Max Pooling)       | x%      |
| base line + ZCBAM(Avg Pooling)         | 73.53%      |
| base line + ZCBAM(Max Pooling)       | x%      |
| base line + ZCBAM(Avg & Max Pooling)         | 74.59%      |

