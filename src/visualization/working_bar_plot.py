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
from bar_plot_in import bar_plot_in

def bar_p(title_graph='Points per Possession (PPP) Average per Playstyle', x_axis_label = 'Playstyle', yaxis_label = 'PPP'):
    '''
    function that graphs the bar plot
    use bar_plot_in function.
    can specify labels of graph.
    
    '''
    names, y_1 = bar_plot_in()
    fig = go.Figure(data=[go.Bar(x=names, y = y_1, width=0.4,marker={
        'color': y_1,
        'colorscale': 'Viridis'
    })])
    fig.update_layout(
            title={"text": title_graph},
            xaxis_title=x_axis_label,
            yaxis_title=yaxis_label,
        )
    fig.update_xaxes(title_font=dict(size=30))
    fig.update_yaxes(title_font=dict(size=30))
    fig.show()
    plotly.offline.plot(fig, filename=title_graph+".html")


 