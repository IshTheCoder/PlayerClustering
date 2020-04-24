# NBA Player Data Analysis
Analyze player's performance including 11 playtypes to determine new catogories of team roles.

## Intro 

Traditional 5 types of team role in NBA does not apply accurately anymore beacuse of players score in different ways recently. We evaluate new grouping method by different playtypes -- how players handle the ball.

## Enviroment
To replicate the enviroment the project needs, run the code below
```
pip install -r requirements.txt
```
Typical packages included in this project are:
```
pandas          0.24.0
numpy           1.14.2
matplotlib      2.2.2
scipy           0.19.1
scikit-learn    0.19.2
requests        2.20.1
...
```

## File Structure
* data:
  * data_raw: Contains the csv we got from the json file for all players from 2015-2019 based on their different playtypes.
  * data_cleaned: Contains the data after cleanning, only with the columns we need for 11 playtypes for all players from 2015-2019.
    * pca_data: Contains the data for PCA.
    * poss_ppp_data: Contains the data for bar graph.
* src:
  * scraping: Contains the functions for scraping and storing the data from stats.nba.com/players/.
  * analysis: Process the data we got, including PCA and k-means.
  * visualization: Plot and visualize the results.
  
## How to run the code
* Fetch data:
```
 -> run pull_data.py: Pull Json file from stats.nba.com.
 -> run json_to_DF.py and get_data.py: Transfer Json file to csv format.
```
* Process data:
```
 -> run get_table.py and get_pca_aggr_data.py: Clean data and aquire yearly aggregated data.
 -> run kmeans.py: Perform PCA algorithm on cleaned data and use k-means method to get clustered data.
 -> run kmeans_top5.py: Extract information of 5 typical players from each cluster.
```
* Visualize data:
```
 -> run graph_drawer.py: Obtain playtype frequency based on yearly average.
 -> run figure_most_efficient_playtype.py: Obtain side by side bar plot of 5-year scoring efficiency per playtype.
 -> run grapher.py: Gain 2D plots of scoring efficiency.
 -> run draw_scatter: Visualize 3D playtypes clustered data.
 -> run pie_chart.py: Playtypes distribution for typicals players.
```
  
Note: Some figures are in the format of .html which can't be showed inline on Jupyternotebook. So we attached the link here.

[3D PCA categorizing Slider](https://plot.ly/~swishan/16)
![](https://github.com/tonyzhangmy/group3-NBA-player-analysis/blob/master/data/data_cleaned/plots/3D.png)
<br>
<br>
[2D Scatter plot Slider](https://plot.ly/~swishan/18)
![](https://github.com/tonyzhangmy/group3-NBA-player-analysis/blob/master/data/data_cleaned/plots/2D.png)
<br>
<br>
[Playtypes frequency](https://plot.ly/~swishan/20)
![](https://github.com/tonyzhangmy/group3-NBA-player-analysis/blob/master/data/data_cleaned/plots/Playtypes%20Frequency%20Shares.png)
<br>
<br>
