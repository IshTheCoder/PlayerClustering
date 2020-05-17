import json
import os
import pandas as pd
from get_table import get_pca_table

def get_aggr_data(datadir, outdir="data/data_cleaned/pca_data",possdir='data/data_cleaned/poss_ppp_data'):
    '''
    Get aggregated csv file to perform PCA on, and save them in outdir.

    :param: datadir, str (csv files from json_to_DF)
    :param: outdir, str (directory to store json files)

    '''
    assert datadir
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    
    if not os.path.exists(possdir):
        os.mkdir(possdir)

    years = ["2015", "2016", "2017", "2018", "2019"]

    for y in years:
        df = get_pca_table(
            InputDir=datadir, 
            SeasonYear=y
        )
        df.fillna(0, inplace=True)
        #generate the poss2015.csv
        allColumns=df.columns.values.tolist()
        poss_columns=[col for col in allColumns if ('_ppp' in col) or ('_poss' in col)]
        df1=df[poss_columns]
        output_poss_file=os.path.join(possdir,'poss'+y+'.csv')
        output_file = os.path.join(
            outdir, y + "_pca_table.csv"
        )
        drop_columns=[col for col in allColumns if '_poss' in col]
        df.drop(
            columns=drop_columns, inplace=True
        )
        df.to_csv(output_file)
        df1.to_csv(output_poss_file)
    return None
get_aggr_data('data/all_jsons')