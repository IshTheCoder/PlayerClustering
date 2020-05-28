#Visualization
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import matplotlib; matplotlib.use("TkAgg")
from sklearn import cluster
import plotly
import plotly.graph_objects as go
from sklearn.metrics import silhouette_samples, silhouette_score

#plotly.offline.init_notebook_mode()
#plotly.tools.set_credentials_file(username='swishan', api_key='nQfq97kmHYvg1HhlKSp5')



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
    # fig, ax = plt.subplots()
    # for i in range(int(data_pca.size/2)):
    #     player = data_pca[i]
    #     ax.scatter(player[0], player[1])
    # plt.show()

    return data_pca, player_name


def k_means(fname, dim=3, cluster_num=5):
    '''
    Function to cluster the data into cluster_num groups and visualize them in a 3D space
    :param fname: the path of the pca_table file
    :param dim: the number of dimensions we want to use
    :param cluster_num: the number of clusters we want to cluster them
    :return: NONE
    '''
    assert isinstance(fname, str)
    data, names = pca_processing(fname, dim)
    X = np.array(data)
    k_means = KMeans(n_clusters=cluster_num).fit(X)
    labels = k_means.labels_



    return names, X, labels

def get_silscores(fname, dim=3):
    best=0
    final_clus=0
    for cluster_num in range(5,9):
        data, names = pca_processing(fname, dim)
        X = np.array(data)
        k_means = KMeans(n_clusters=cluster_num).fit(X)
        labels = k_means.labels_
        silhouette_avg = silhouette_score(X, labels)
        if silhouette_avg >= best:
            best = silhouette_avg
            final_clus= cluster_num

    return best, final_clus

final_list=['2015','2016','2017','2018','2019']
for each in final_list:
    print(each)
    print(get_silscores('aggr_data/'+each+'_pca_table.csv', dim=3))

#######################


#data = [plotly.graph_objs.Scatter3d(x=X[:, 1], y=X[:, 0], z=X[:, 2], text = names, hoverinfo = 'text', mode='markers', marker=dict(color=labels))]
# fig = go.Figure()


final_list=['2015','2016','2017','2018','2019']
dims = [5, 6, 7, 8, 8]
count =0 

for each in final_list:

	names, X, labels = k_means('aggr_data/'+each+'_pca_table.csv', dim=3, cluster_num=dims[count])
	count+=1
	fig.add_trace(
	go.Scatter3d(x=X[:, 1], y=X[:, 0], z=X[:, 2], text = names, hoverinfo = 'text', mode='markers', marker=dict(color=labels), visible=False, name="Player Clusters for " + each)
	)

print(len(fig.data))
fig.data[0].visible = True

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="restyle",
        args=["visible", [False] * len(fig.data)],
        label='Year ' + str(i + 2015)

    )
    step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)


#plotly.offline.plot(data, filename='Clusters_9.html')

# sliders = [dict(
#     active=5,
#     currentvalue={"prefix": "Year: "},
#     pad={"t": 5},
#     steps=steps
# )]
# start_index = 2015
# fig.update_layout(
#     sliders=sliders,
#     #title = "9 Cluster classification of players based on Scoring Styles"
#     title={"text": "Scoring Clusters Per Year"}
# )

# #fig.show()
# plotly.offline.plot(fig, filename='Cluster_final.html')
# #k_means('aggr_data/2015_pca_table.csv', 3, 9)


