import pandas as pd
from collections import defaultdict


years = ['2015','2016','2017','2018','2019']
playtype = ['Isolation', 'Transition','Pick & Roll Ball Handler', 'Pick & Roll Roll Man', 'Post Up','Spot Up', 'Handoff', 'Cut', 'Off Screen', 'Putbacks','Misc']
pt_abrv = ['iso','tr','prb','prr','pu','su','ho','cut','os','putback','misc']

def scatter_plot_in(fname):
    '''
    outdated function for input to scatter plot; use scatter_input.py
    '''
    
    df = pd.read_csv(fname)

    df_calc = pd.DataFrame()
    for i in pt_abrv:
        df_poss = df[i+'_poss']
        df_ppp = df[i+'_ppp']
    
        #df_points = df_ppp * df_poss
        #df_calc[i+'_points'] = df_points

    return df['total_poss'].tolist(), df_calc.sum(axis=1).tolist(), df['PLAYER_NAME'].tolist() 
        
            
            
            
