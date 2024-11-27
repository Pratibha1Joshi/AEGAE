# AEGAE: Attribute-Embedded Graph Autoencoder

This repository provides the implementation of the AEGAE method for community detection in attributed graphs. AEGAE integrates Laplacian regularization and a graph autoencoder to generate robust node embeddings for identifying communities in complex networks.

## Key Features
- Laplacian regularization to filter high-frequency noise in graph signals.
- Graph Autoencoder to refine node embeddings.
- Pairwise cosine similarity computation for clustering.
- Spectral clustering for community detection.
- Support for visualizing communities using t-SNE.


**Abstract**

The community detection is a crucial task in network analysis. It identifies  groups of nodes within a network that exhibits distinct behavior compared to other groups. The structural and attributed features posE challenges in attributed graph for the community identification. In this work, the Attribute-Embedded Graph Autoencoder (AEGAE) method for community detection is proposed. The AEGAE method for community detection comprises two key functions. Initially, the network is represented as an adjacency matrix. The Laplacian matrix of the graph is computed that captures  the graph topological information. Further, the eigen decomposition of Laplacain matrix is performed to obtain Laplacian regularized matrix. This process reduces the noise from the graph and the Rayleigh quotient is used to measure the regularity of the graph. The Graph Autoencoder is applied on the regularized signal matrix to generate node embeddings that captures the essential structural features of the graph. The pairwise cosine similarity matrix with reduced dimensionality is obtained from the embeddings. Moreover, the node pairs are randomly selected to train the GAE model. To obtain optimal embedding the cross-entropy loss is computed iteratively. Further, to obtain optimal solution the GAE is trained with varying threshold values. The similarity matrix is recomputed based on the optimal embedding. The Spectral clustering method is applied on the optimal similarity matrix to reveal the hidden communities in the attributed graph. The performance of the AEGAE is evaluated on four real world datasets. The proposed method outperforms with respect to existing methods in terms of evaluation parameters like Adjusted Rand Index (ARI), Accuracy (ACC), and Normalized Mutual Information (NMI).  

![image](https://github.com/user-attachments/assets/36f2c6ec-1b1a-4204-8c7b-2f11db6ed111)



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
These datasets are publicaly available and you can also download it form the data folder. Change the directory accordingly.

cd AEGAE
pip install -r requirements.txt

Training the Model

Run the main script with the desired dataset:

**Training**

python train.py --dataset cora --gnnlayers 4 --upth_st 0.015 --lowth_st 0.1 --upth_ed 0.001 --lowth_ed 0.5

**visulaization of the result**

python clustering_metric.py 

**The source code and datasets for this study are openly available at **https://doi.org/10.5281/zenodo.14038245****
