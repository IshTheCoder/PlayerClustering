import json
import os
from get_table import get_pca_table
import pathlib

def get_aggr_data(datadir, outdir="aggr_data"):
    '''
    Get aggregated csv file to perform PCA on, and save them in outdir.

    :param: datadir, str (csv files from json_to_DF)
    :param: outdir, str (directory to store json files)

    '''
    assert datadir
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    years = ["2015", "2016", "2017", "2018", "2019"]

    for y in years:
        df = get_pca_table(
            InputDir=datadir, 
            SeasonYear=y
        )
        df.fillna(0, inplace=True)
        output_file = os.path.join(
            outdir, y + "_pca_table.csv"
        )
        df.drop(
            columns=["total_poss"], inplace=True
        )
        df.to_csv(output_file)
    return None

get_aggr_data(pathlib.Path().absolute()) #This will generate the folder with 5 csv files