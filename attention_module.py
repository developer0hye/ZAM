import torch
from torch import nn


##Original CBAM##

class ChannelAttention(nn.Module):
    def __init__(self, in_planes, ratio=16):
        super(ChannelAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)

        self.fc1   = nn.Conv2d(in_planes, in_planes // 16, 1, bias=False)
        self.relu1 = nn.ReLU()
        self.fc2   = nn.Conv2d(in_planes // 16, in_planes, 1, bias=False)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = self.fc2(self.relu1(self.fc1(self.avg_pool(x))))
        max_out = self.fc2(self.relu1(self.fc1(self.max_pool(x))))
        out = avg_out + max_out
        return self.sigmoid(out)

class SpatialAttention(nn.Module):
    def __init__(self, kernel_size=3):
        super(SpatialAttention, self).__init__()

        assert kernel_size in (3, 7), 'kernel size must be 3 or 7'
        padding = 3 if kernel_size == 7 else 1

        self.conv1 = nn.Conv2d(2, 1, kernel_size, padding=padding, bias=False)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        x = torch.cat([avg_out, max_out], dim=1)
        x = self.conv1(x)
        return self.sigmoid(x)

class CBAM(nn.Module):
    def __init__(self, in_planes):
        super(CBAM, self).__init__()

        self.ca = ChannelAttention(in_planes)
        self.sa = SpatialAttention()
        
    def forward(self, x):
        
        out = x * (self.ca(x))
        out = out * (self.sa(out))
        
        return out

## ZCBAM ##    
class ZeroChannelAttention(nn.Module):
    def __init__(self):
        super(ZeroChannelAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)
    
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        return self.sigmoid(self.avg_pool(x) + self.max_pool(x))

class ZeroSpatialAttention(nn.Module):
    def __init__(self):
        super(ZeroSpatialAttention, self).__init__()

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = torch.mean(x, dim=1, keepdim=True)
        max_out, _ = torch.max(x, dim=1, keepdim=True)
        return self.sigmoid(avg_out + max_out)
    
class ZCBAM(nn.Module):
    def __init__(self):
        super(ZCBAM, self).__init__()

        self.ca = ZeroChannelAttention()
        self.sa = ZeroSpatialAttention()
        
    def forward(self, x):
        
        out = x * self.ca(x)
        out = out * self.sa(out)
        
        return out