import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn import preprocessing
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D


def pca_processing(fname, n_comp=3):
    '''
    process file and get data to put into PCA for clustering
    specify fname string
    specify n_comp for amount of principle components
    returns pca object, name of players, data of the pca corresponding to names
    :input: fname, str
            n_comp, int
    :return: pca, data_pca, player_name
    
    '''
    df = pd.read_csv(fname)
    kept_cols = [
        col for col in df.columns if col.endswith("freq")
    ]
    kept_cols.append("PLAYER_NAME")
    kept_cols.reverse()
    df = df[kept_cols]
    player_name = df["PLAYER_NAME"]
    
    data_org = df.iloc[:, 1:]
    pca = PCA(n_components=n_comp)
    pca.fit(data_org)
    data_pca = data_org @ pca.components_.T
    assert len(data_pca) == len(player_name)

    return data_pca, player_name, pca


def k_means(fname, dim=3, cluster=8):
    """
    return recontruction of clusters, 
            shape = [#cluster, original_dimention]
    """
    data, names, pca = pca_processing(fname, dim)
    X = np.array(data)
    k_means = KMeans(n_clusters=cluster).fit(X)
    labels = k_means.labels_
    fig = plt.figure(1, figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    ax.scatter(X[:, 1], X[:, 0], X[:, 2], c=labels.astype(np.float), edgecolor='k')
    fig.show()
    print("Cluster shape: ", k_means.cluster_centers_.shape)
    clusters_projected = pca.inverse_transform(k_means.cluster_centers_)
    print("Recontruction shape: ", clusters_projected.shape)
    return clusters_projected


k_means("data/data_cleaned/pca_data/2015_pca_table.csv") #This will reproduce the k means clustering as in the notebook