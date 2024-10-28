import torch
import torch.nn as nn
import torch.nn.functional as F

from layers import *

import torch
import torch.nn as nn
import torch.nn.functional as F

from layers import *

class LinTrans(nn.Module):
    def __init__(self, layers, dims):
        super(LinTrans, self).__init__()
        self.layers = nn.ModuleList()
        
        
        for i in range(layers):
            self.layers.append(nn.Linear(dims[i], dims[i+1]))
            

        self.dcs = SampleDecoder(act=lambda x: x)

    def scale(self, z):
        
        zmax = z.max(dim=1, keepdim=True)[0]
        zmin = z.min(dim=1, keepdim=True)[0]
        z_std = (z - zmin) / (zmax - zmin)
        z_scaled = z_std
    
        return z_scaled

    def forward(self, x):
        out = x
        for layer in self.layers:
            out = layer(out)
        out = self.scale(out)
        out = F.normalize(out)
        return out

class FeedForwardNN(nn.Module):
    def __init__(self, ft_in, nb_classes, hidden_sizes=[128, 64]):
        super(FeedForwardNN, self).__init__()
        self.layers = nn.ModuleList()
        prev_size = ft_in
        for size in hidden_sizes:
            self.layers.append(ChebConv(prev_size, size))
            prev_size = size
        self.output_layer = ChebConv(prev_size, nb_classes)

    def forward(self, seq):
        x = seq
        for layer in self.layers:
            x = F.relu(layer(x))
        ret = self.output_layer(x)
        return ret


