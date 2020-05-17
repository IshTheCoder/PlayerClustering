from pull_nba import pull_nba
from json_to_DF import json_to_DF
import time
import os
def get_data(outdir="data/all_jsons/"):
    '''
    This function is to get all year data from one click.
    
    Note: Need to run 'pull_nba.py' and 'json_to_DF.py' first
    '''
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    playtype = ['iso', 'tr', 'prb', 'prr', 'pu', 'su', 'ho', 'cut', 'os', 'putback', 'misc']
    year = ['2019', '2018', '2017', '2016', '2015']
    teamorplayer = ['P', 'T']
    
    for i in playtype:
        for j in year:
            for k in teamorplayer:
                pull_nba(i, j, k,outdir)
                nba_data = json_to_DF(outdir+'leaguedash_{}_{}_{}.json'.format(i, j, k))
                print('Export Playtype = {}, Year = {}, Player or Team = {} successed'.format(i, j, k))
                time.sleep(20)
    return 'Finished'
get_data()