**Abstract**

Community detection is a vital task in network analysis, involving the identification of groups of nodes within a network that exhibit distinct behavior compared to other groups. In attributed graphs, where nodes possess feature attributes, this task becomes more complex as it requires integrating both structural and attribute information. This paper proposes the Attribute-Embedded Graph Autoencoder (AEGAE) method for community detection in attributed graphs. AEGAE consists of two primary modules: the first employs Laplacian regularization to capture topological information and filter out high-frequency noise, yielding regularized signals that better reflect network structure. The second module applies a Graph Autoencoder that uses these regularized signals to generate refined node embeddings that capture essential graph features. Spectral clustering is then applied to similarity matrices derived from these embeddings to uncover communities. AEGAE’s effectiveness is validated through experiments on four benchmark datasets, where it consistently outperforms existing methods based on metrics such as Adjusted Rand Index (ARI), Accuracy (AAC), and Normalized Mutual Information (NMI). By addressing the challenges associated with node attribute noise, AEGAE establishes a new benchmark in community detection, highlighting its potential contributions to network analysis. 

**Environment Info**
Python 3.7.4
PyTorch 1.4.0
CUDA 10.2

**Then, run the command:**

pip install -r requirements.txt

**RUN**

python train.py --dataset cora --gnnlayers 4 --upth_st 0.015 --lowth_st 0.1 --upth_ed 0.001 --lowth_ed 0.5

**The source code and datasets for this study are openly available at **https://doi.org/10.5281/zenodo.14038245****
