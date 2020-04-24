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


def create_slider_scatter(fname_list title_graph, yaxis_label, x_axis_label):
	"""
	Required format of get_y output, names is the list of all 11 playtypes
	y_1 is a list of listse i.e. a list of 11 5 element lists, each inner list
	is the line of frequency change over the years. If you can ideally please try to normalize the 
	data for each year, for total freq of playtypes per year to sum to 100
	names is a list of the names of playtypes.
	"""
	y_1, names = get_y(fname_list[i])

	for i in range(y_1):
		x_1= [2015, 2016, 2017, 2018, 2019]

		count+=1
		fig.add_trace(
		go.Scatter(datasets_[i])
		)

	start_index = 2015
	fig.update_layout(
	    sliders=sliders,
	    #title = "9 Cluster classification of players based on Scoring Styles"
	    title={"text": title_graph},
	    xaxis_title=x_axis_label,
    	yaxis_title=yaxis_title,
    	showlegend=True
	)

	#fig.show()
	plotly.offline.plot(fig, filename=title_graph+".html")
	return "Completed"