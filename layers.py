import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules.module import Module
from torch.nn.parameter import Parameter
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules.module import Module
from torch.nn.parameter import Parameter

class NonLinearEncoder(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(NonLinearEncoder, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

class CustomGraphConvolution(Module):
    def __init__(self, in_features, out_features, encoder, similarity_func, dropout=0.):
        super(CustomGraphConvolution, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.dropout = dropout
        self.encoder = encoder
        self.similarity_func = similarity_func
        self.reset_parameters()

    def reset_parameters(self):
        # Additional initialization for the encoder weights if needed
        self.encoder.apply(self._init_weights)

    def _init_weights(self, m):
        if isinstance(m, nn.Linear):
            torch.nn.init.xavier_uniform_(m.weight)

    def forward(self, input, adj):
        input = F.dropout(input, self.dropout, self.training)
        embeddings = self.encoder(input)
        support = torch.mm(embeddings, embeddings.t())
        output = self.similarity_func(support)
        return output

    def __repr__(self):
        return self.__class__.__name__ + ' (' \
               + str(self.in_features) + ' -> ' \
               + str(self.out_features) + ')'



# Now you can use this modified layer in your training loop
# ...
