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
from scatter_input import scatter_plot_in

flist=['./poss_ppp_dir/poss2015.csv','./poss_ppp_dir/poss2016.csv','./poss_ppp_dir/poss2017.csv','./poss_ppp_dir/poss2018.csv','./poss_ppp_dir/poss2019.csv']
def create_slider_scatter(fname_list, title_graph, yaxis_label, x_axis_label):
	"""
	get xy should take in the list of filenames for each year and output the x values, i.e. total possessions for the year vs total PPP.
	PPP should be weighted according to the number of possessions right, like a players season PPP, is PPP_i * Poss_i, where i is the playtype
	"""
	fig = go.Figure()
	colorscale_curr=[[0.0, "rgb(165,0,38)"],[0.1111111111111111, "rgb(215,48,39)"],[0.2222222222222222, "rgb(244,109,67)"],[0.3333333333333333, "rgb(253,174,97)"],[0.4444444444444444, "rgb(254,224,144)"],[0.5555555555555556, "rgb(224,243,248)"],[0.6666666666666666, "rgb(171,217,233)"],[0.7777777777777778, "rgb(116,173,209)"],[0.8888888888888888, "rgb(69,117,180)"],[1.0, "rgb(49,54,149)"]]
	colorscale_curr.reverse()

	#just gonna use global variable list of path strings; too lazy to input strings from outside funciton lmao 
	for i in range(len(flist)):
		x_1, y_1, names = scatter_plot_in(flist[i])
		#x_1, y_1, names = [10, 8, 7], [0.9, 0.5, 0.3],["Harden","Lebum","Poopface"]

		fig.add_trace(
		go.Scatter(x=x_1, y= y_1, text = names, hoverinfo = 'text', mode='markers', marker=dict(color=y_1 , colorscale=colorscale_curr, size=12, line=dict(width=2, color ='DarkSlateGrey')), visible=False, name="Points Per Possession vs Possessions " + str(i)
		))
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

	sliders = [dict(
	    active=5,
	    currentvalue={"prefix": "Year: "},
	    pad={"t": 5},
	    steps=steps
	)]
	start_index = 2015
	fig.update_layout(
	    sliders=sliders,
	    #title = "9 Cluster classification of players based on Scoring Styles"
	    title={"text": title_graph},
	    xaxis_title=x_axis_label,
    	yaxis_title=yaxis_label,
	)

	#fig.show()
	plotly.offline.plot(fig, filename=title_graph+".html")
	return "Completed"
print(create_slider_scatter(['2015','2016','2019','2020'], 'TestSample', 'yaxis_label', 'x_axis_label'))
