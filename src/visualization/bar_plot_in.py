import pandas as pd
from statistics import mean
from collections import defaultdict
from line_plot_in import line_plot_in

years = ['2015','2016','2017','2018','2019']
playtype = ['Isolation', 'Transition','Pick & Roll Ball Handler', 'Pick & Roll Roll Man', 'Post Up','Spot Up', 'Handoff', 'Cut', 'Off Screen', 'Putbacks','Misc']
pt_abrv = ['iso','tr','prb','prr','pu','su','ho','cut','os','putback','misc']

def bar_plot_in():
    '''
    function that gives appropriate input for the bar plot
    bar plot expects possession by ppp data per playtype

    '''

    ppp_mean = defaultdict(list)
    for y in years:
        fname = 'poss' + y + '.csv'
        df = pd.read_csv('./poss_ppp_dir/' + fname)

        for i in pt_abrv:
            df_poss = df[i+'_poss']
            df_ppp = df[i+'_ppp']
            valid = df_ppp.ne(0)
            df_points = (df_ppp.loc[valid] * df_poss[valid]).sum()
            ppp_w  = df_points / (df_poss[valid].sum())
            ppp_mean[i].append(ppp_w)
    
    mean_aggr = []
    for i in pt_abrv:
        mean_aggr.append(round(mean(ppp_mean[i]),2))

    return playtype, mean_aggr
            
            
            
