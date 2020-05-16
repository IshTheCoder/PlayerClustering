import pandas as pd
from collections import defaultdict


years = ['2015','2016','2017','2018','2019']
playtype = ['Isolation', 'Transition','Pick & Roll Ball Handler', 'Pick & Roll Roll Man', 'Post Up','Spot Up', 'Handoff', 'Cut', 'Off Screen', 'Putbacks','Misc']
pt_abrv = ['iso','tr','prb','prr','pu','su','ho','cut','os','putback','misc']

def scatter_plot_in(fname):
    '''
    Function that outputs total poss, ppp, and name of each player through 3 lists
    fname is expected directory path
    fname must use data in ./poss_ppp_dir OR SHIT WONT WORK :(

    '''
    
    df = pd.read_csv(fname)

    df_calc = pd.DataFrame()
    for i in pt_abrv:
        df_poss = df[i+'_poss']
        df_ppp = df[i+'_ppp']
    
        df_points = df_ppp * df_poss
        df_calc[i+'_points'] = df_points

    ppp = df_calc.sum(axis=1) / df['total_poss']
    return df['total_poss'].tolist(), ppp.tolist(), df['PLAYER_NAME'].tolist() 