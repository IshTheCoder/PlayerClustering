import pandas as pd
import json

def json_to_DF(fname, FILTER_OUT = []):
    '''
    Takes NBA json file and returns dataframes of it for better computation
    NOTE: need to include .json extension in the string; opens from current directory
    NOTE:   FILTER_OUT expects a list of strings that filters out column data by specified header
            Header names to use can be found via: some_json_dict['resultSets'][0]['headers']
            headers = ['SEASON_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 
            'TEAM_ABBREVIATION', 'TEAM_NAME', 'PLAY_TYPE', 'TYPE_GROUPING', 
            'PERCENTILE', 'GP', 'POSS_PCT', 'PPP', 'FG_PCT', 'FT_POSS_PCT', 
            'TOV_POSS_PCT', 'SF_POSS_PCT', 'PLUSONE_POSS_PCT', 'SCORE_POSS_PCT', 
            'EFG_PCT', 'POSS', 'PTS', 'FGM', 'FGA', 'FGMX']
    :param: fname, str
    :param: FILTER_OUT, list
    :return: DataFrame
    '''

    with open(fname) as f:
        playt_json = json.load(f)

        '''
        Code to take nba json to dataframes is from below:
        https://towardsdatascience.com/using-python-pandas-and-plotly-to-generate-nba-shot-charts-e28f873a99cb
        '''

        data = playt_json['resultSets'][0]['rowSet']
        headers = playt_json['resultSets'][0]['headers']
        df = pd.DataFrame.from_records(data, columns=headers)
        df = df.drop(columns=FILTER_OUT)

        return df
