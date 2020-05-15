import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import matplotlib; matplotlib.use("TkAgg")



def pca_processing(fname, n_comp=3):
    '''
    Function to decrease the dimension of the players based on their POSS_PCT
    :param fname: the path of the pca_table file
    :param n_comp: the number of main components we want to use
    :return: data after pca with dimension n*n_comp; player names
    '''
    df = pd.read_csv(fname)
    kept_cols = [
        col for col in df.columns if col.endswith("freq")
    ]
    kept_cols.append("PLAYER_NAME")
    kept_cols.reverse()
    df = df[kept_cols]

    player_name = df["PLAYER_NAME"]
    data_org = df.iloc[:, 2:]
    pca = PCA(n_components=n_comp)
    pca.fit(data_org)
    data_pca = data_org @ pca.components_.T
    assert len(data_pca) == len(player_name)

    return data_pca, player_name


def k_means(fname, dim=3, cluster_num=5, show_img=False):
    '''
    Function to cluster the data into cluster_num groups and visualize them in a 3D space
    :param fname: the path of the pca_table file
    :param dim: the number of dimensions we want to use
    :param cluster_num: the number of clusters we want to cluster them
    :param show_img: show k-means image or not
    :return: NONE
    '''
    assert isinstance(fname, str)
    data, names = pca_processing(fname, dim)
    X = np.array(data)
    k_means = KMeans(n_clusters=cluster_num).fit(X)
    labels = k_means.labels_
    fig = plt.figure(1, figsize=(4, 3))
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
    ax.scatter(X[:, 1], X[:, 0], X[:, 2], c=labels.astype(np.float), edgecolor='k')
    if show_img is True:
        fig.show()
    distance = k_means.transform(X)
    return names, labels, distance


def calculate_top5(distance, names):
    '''
    Function to find the top5 players who are the most closest to the k-means's cluster center
    :param distance: Distance of each player to the clusters
    :param names: names of each player
    :return: top5 names of each clusters
    '''
    dim = len(distance[0])
    result = np.zeros((dim, 5))
    top5_name = []
    for i in range(dim):
        temp = []
        curr = np.array(distance[:, i])
        min_5 = curr.argsort()[:5]
        result[i, :] = min_5
        for index in min_5:
            temp.append(names[index])
        top5_name.append(temp)
    return top5_name


def top5_img(distance, names, year):
    '''
    :param distance: distance of player to kmeans center
    :param names: player names
    :param year: year
    :return: dictionary of player names and their play type
    '''
    assert 2015 <= year <= 2019
    top5names = calculate_top5(distance, names)
    path = "aggr_data/" + str(year) + "_pca_table.csv"
    df = pd.read_csv(path)
    data_per_player = np.zeros((1, 11))
    for i in range(len(top5names)):
        for j in range(len(top5names[i])):
            new_df = df[df['PLAYER_NAME'] == top5names[i][j]]
            data = new_df[
                ["iso_freq", "tr_freq", "prb_freq", "prr_freq", "pu_freq", "su_freq", "ho_freq", "cut_freq", "os_freq",
                 "putback_freq", "misc_freq"]]
            data = data.values.tolist()
            data = np.array(data)[0]
            data_per_player = np.vstack((data_per_player, data))
    data_per_player = data_per_player[1:,:]
    data_per_player = data_per_player / data_per_player.sum(axis=1, keepdims=True)
    # print(data_per_player.shape)
    result = {}
    for i in range(8):
        for j in range(5):
            result[top5names[i][j]] = data_per_player[i * 5 + j, :]
    return result

def survey(results):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
        The category labels.
    """
    category_names = ["Iso",
                      "Tra",
                      "PRB",
                      "PRR",
                      "Pos",
                      "Spo",
                      "Han",
                      "Cut",
                      "Off",
                      "OffR",
                      "Misc"]

    labels = list(results.keys())
    new_labels = []
    start = " "
    for i in range(len(labels)):
        new_labels.append(labels[i])
        if i % 5 == 4:
            new_labels.append(start)
            start += " "
    labels = new_labels
    data = np.array(list(results.values()))
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i])
        if i % 5 == 4:
            new_data.append(np.zeros(shape=data[0].shape))
    data = np.array(new_data)

    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(11,20))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.tick_params(axis='both', which='major', labelsize=8)
        ax.barh(labels, widths, left=starts, height=0.8,
                label=colname, color=color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


names, labels, distance = k_means('aggr_data/2017_pca_table.csv', 3, 8)
results = top5_img(distance, names, 2017)
survey(results)
plt.show()


def draw_elbow_line(fname, dim=3):
    k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = []
    for i in k:
        data, names = pca_processing(fname, dim)
        X = np.array(data)
        k_means = KMeans(n_clusters=i).fit(X)
        distance = k_means.transform(X)
        result.append(np.sum(np.min(distance, axis=1)))
    # return k, result
    plt.plot(k, result)
    plt.show()
#
# draw_elbow_line('aggr_data/2016_pca_table.csv', 3)
# # plt.plot(k, result)
# # plt.show()



# names, labels, distance = k_means('aggr_data/2019_pca_table.csv', 3, 8) #UNCOMMENT THIS PART TO SEE THE MAGIC!
# print(calculate_top5(distance, names))

# k_means('aggr_data/2015_pca_table.csv', 3, 5)