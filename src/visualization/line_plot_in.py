
from collections import defaultdict
import pandas as pd
import os

years = ['2015','2016','2017','2018','2019']
playtype = ['Isolation', 'Transition','Pick & Roll Ball Handler', 'Pick & Roll Roll Man', 'Post Up','Spot Up', 'Handoff', 'Cut', 'Off Screen', 'Putbacks','Misc']
pt_abrv = ['iso','tr','prb','prr','pu','su','ho','cut','os','putback','misc']

def line_plot_in():
    '''
    Input for line plot.
    returns a list of 11 lists, where each inner list corresponds to a playtype, and contains 5 values 
    corresponding to the average frequency for years 2015-2019.
    also returns a corresponding list of playtype strings for labeling

    :return: list(PLAYTYPE_STRINGS), list(list(floats))
    '''


    df_l = defaultdict(list)

    for y in years:
        fname = 'poss' + y + '.csv'
        df = pd.read_csv('./poss_dir/' + fname)
        poss_tot = df['total_poss'].sum()

        for i in pt_abrv:
            poss_i = df[i+'_poss'].sum()
            df_l[i].append(round(100*(poss_i/poss_tot),2))
    
    y_1 = []
    for i in pt_abrv:
        y_1.append(df_l[i])



    return playtype, y_1
