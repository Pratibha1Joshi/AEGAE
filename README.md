**Abstract**

Community detection is a vital task in network analysis, involving the identification of groups of nodes within a network that exhibit distinct behavior compared to other groups. In attributed graphs, where nodes possess feature attributes, this task becomes more complex as it requires integrating both structural and attribute information. This paper proposes the Attribute-Embedded Graph Autoencoder (AEGAE) method for community detection in attributed graphs. AEGAE consists of two primary modules: the first employs Laplacian regularization to capture topological information and filter out high-frequency noise, yielding regularized signals that better reflect network structure. The second module applies a Graph Autoencoder that uses these regularized signals to generate refined node embeddings that capture essential graph features. Spectral clustering is then applied to similarity matrices derived from these embeddings to uncover communities. AEGAE’s effectiveness is validated through experiments on four benchmark datasets, where it consistently outperforms existing methods based on metrics such as Adjusted Rand Index (ARI), Accuracy (AAC), and Normalized Mutual Information (NMI). By addressing the challenges associated with node attribute noise, AEGAE establishes a new benchmark in community detection, highlighting its potential contributions to network analysis. 

**Environment Info**

pytorch (tested on 1.2.1)
Required libraries: NetworkX, PyTorch, Numpy, Scipy (see requirements.txt for a complete list)

**Then, run the command:**

pip install -r requirements.txt
