# AEGAE: Attribute-Embedded Graph Autoencoder

This repository provides the implementation of the AEGAE method for community detection in attributed graphs. AEGAE integrates Laplacian regularization and a graph autoencoder to generate robust node embeddings for identifying communities in complex networks.

## Key Features
- Laplacian regularization to filter high-frequency noise in graph signals.
- Graph Autoencoder to refine node embeddings.
- Pairwise cosine similarity computation for clustering.
- Spectral clustering for community detection.
- Support for visualizing communities using t-SNE.


**Abstract**

Community detection is a vital task in network analysis, involving the identification of groups of nodes within a network that exhibit distinct behavior compared to other groups. In attributed graphs, where nodes possess feature attributes, this task becomes more complex as it requires integrating both structural and attribute information. This paper proposes the Attribute-Embedded Graph Autoencoder (AEGAE) method for community detection in attributed graphs. AEGAE consists of two primary modules: the first employs Laplacian regularization to capture topological information and filter out high-frequency noise, yielding regularized signals that better reflect network structure. The second module applies a Graph Autoencoder that uses these regularized signals to generate refined node embeddings that capture essential graph features. Spectral clustering is then applied to similarity matrices derived from these embeddings to uncover communities. AEGAE’s effectiveness is validated through experiments on four benchmark datasets, where it consistently outperforms existing methods based on metrics such as Adjusted Rand Index (ARI), Accuracy (AAC), and Normalized Mutual Information (NMI). By addressing the challenges associated with node attribute noise, AEGAE establishes a new benchmark in community detection, highlighting its potential contributions to network analysis. 

![image](https://github.com/user-attachments/assets/7068e857-2911-4201-99a4-67e5c8b480a3)


## Dependencies
The code is implemented in Python. Below are the required libraries:
- Python 3.8 or later
- NumPy >= 1.21
- SciPy >= 1.7
- scikit-learn >= 1.0
- TensorFlow >= 2.9
- matplotlib >= 3.5
- pandas >= 1.3

Install dependencies using:
```bash
pip install -r requirements.txt

Datasets
This repository supports the following datasets:

Cora
Citeseer
Pubmed
wiki
These datasets are publicay available and you can also download it form the data folder. Change the directory accordingly.

cd AEGAE
pip install -r requirements.txt

Training the Model

Run the main script with the desired dataset:

**Training**

python train.py --dataset cora --gnnlayers 4 --upth_st 0.015 --lowth_st 0.1 --upth_ed 0.001 --lowth_ed 0.5

**visulaization of the result**

python clustering_metric.py 

**The source code and datasets for this study are openly available at **https://doi.org/10.5281/zenodo.14038245****
