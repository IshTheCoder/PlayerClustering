from pull_nba import pull_nba #use sys to import directly later
from json_to_DF import json_to_DF
import pandas as pd
import os
import numpy as np

s = ['iso','tr','prb','prr','pu','su','ho','cut','os','putback','misc']

def get_all_files(SeasonYear='2018', PlayerOrTeam = 'P'):
    '''
    Get all files for diff playtypes depending on year. You can specify player or team data.
    '''

    for PlayType in s:
        pull_nba(PlayType, SeasonYear, PlayerOrTeam)

def get_pca_table(InputDir, SeasonYear='2018', PlayerOrTeam = 'P'):
    '''
    Get table for pca
    '''
    new_df = pd.DataFrame()
    poss = pd.Series(dtype = np.dtype('float'))

    for PlayType in s:
        filename = 'leaguedash_' + PlayType + '_' + SeasonYear + '_' + PlayerOrTeam + '.json'
        filename = os.path.join(InputDir, filename)
        df = json_to_DF(filename)

        col_freq_name = PlayType + '_' + 'freq'
        col_ppp_name = PlayType + '_' + 'ppp'
        col_poss_name= PlayType+'_'+'poss'

        df_1 = pd.DataFrame()
        df_1['PLAYER_NAME'] = df['PLAYER_NAME']
        df_1[col_freq_name] = df['POSS_PCT']
        df_1[col_ppp_name]=df['PPP']
        df_1[col_poss_name]=df['POSS']*df['GP']

        if (new_df.empty):
            new_df = df_1
        else:
            new_df = pd.merge(new_df, df_1, how='outer', on='PLAYER_NAME')

        df = df.set_index('PLAYER_NAME')
        df = df['POSS']*df['GP']
        poss = poss.add(df, fill_value=0)

    new_df = new_df[~new_df.duplicated(subset=['PLAYER_NAME'])]
    poss = poss[~poss.index.duplicated()]

    new_df = pd.merge(poss.rename('total_poss'),new_df, on='PLAYER_NAME')
    new_df = new_df.set_index('PLAYER_NAME')
    return new_df

