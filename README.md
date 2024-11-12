# AEGAE: Attribute-Embedded Graph Autoencoder

This repository provides the implementation of the AEGAE method for community detection in attributed graphs. AEGAE integrates Laplacian regularization and a graph autoencoder to generate robust node embeddings for identifying communities in complex networks.

## Key Features
- Laplacian regularization to filter high-frequency noise in graph signals.
- Graph Autoencoder to refine node embeddings.
- Pairwise cosine similarity computation for clustering.
- Spectral clustering for community detection.
- Support for visualizing communities using t-SNE.


**Abstract**

The community detection is a vital task in network analysis. It identify the group of nodes with unique behaviors. The node in attributed graphs has additional features. The feature poses challenges in community detection because it requires structural and attribute information. In this work the Attribute-Embedded Graph Autoencoder (AEGAE) method for community detection is proposed. For the community detection the AEGAE method performed in two key functions. The first uses Laplacian regularization to capture network topology. It filters out high-frequency noise, producing signals that better represent the graph structure. In second Graph Autoencoder perorms the node embedding. The embedding captures essential features of the graph, spectral clustering is applied to similarity matrices of the features. The performance AEGAE is evaluated on four real world datasets. The proposed method outperforms existing methods in terms of evaluation parameters like Adjusted Rand Index (ARI), Accuracy (ACC), and Normalized Mutual Information (NMI). 

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
