import json
import plotly
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PIL
import imageio
from imageio import imread
from scipy.stats import entropy
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly 
import wpcc
plotly.tools.set_credentials_file(username='swishan', api_key='nQfq97kmHYvg1HhlKSp5')




inferno = [[0.0, 'rgb(0, 0, 3)'],
 [0.1, 'rgb(22, 11, 57)'],
 [0.2, 'rgb(65, 9, 103)'],
 [0.3, 'rgb(106, 23, 110)'],
 [0.4, 'rgb(147, 37, 103)'],
 [0.5, 'rgb(187, 55, 84)'],
 [0.6, 'rgb(220, 80, 57)'],
 [0.7, 'rgb(243, 119, 25)'],
 [0.8, 'rgb(251, 164, 10)'],
 [0.9, 'rgb(245, 215, 69)'],
 [1.0, 'rgb(248, 250, 100)']]
def plot_scatter(x_data, y_data, size_marker, color_marker):


	data = [
	    go.Scatter(
	        x =list_SVI,
	        y = TS_1,
	        text = name_list,
	        hoverinfo = 'text',
	        mode='markers',
	        marker=dict(
	        	size=PTS,
	        	cmax=0.0,
	        	cmin=0.1,
	        	color=TS_reg,
	        	colorbar=dict(
	        	title="TS regular"
	        	),
	       	colorscale=inferno


	        	)

			),
	    
	]


	layout = go.Layout(

		plot_bgcolor='rgba(0,0,0)',
		paper_bgcolor='rgba(0,0,0)',



		title='Playoff Shot versatility ',
		font=dict(
	        family="sans serif",
	        color="LightSeaGreen"
	    ),

	    xaxis=dict( 
	    	showticklabels=False,
	    	title= "Playoff Shot versatility",
	        range=[0.0, 1.0],
	    ),
	    yaxis=dict(showgrid=True,
	    	gridcolor='SeaGreen',
	        range=[0.0, 1.0],
	        title='Playoff TS change vs Shot versatility index',

	    )

	)

	fig = go.Figure(data=data, layout=layout)

	plotly.offline.plot(fig, filename='TS_Change_Vers_2.html')
	return 0


#py.iplot(fig,sharing='public',filename='shot_vers_reg')


