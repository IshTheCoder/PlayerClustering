import pandas as pd

def top_five_freq(top_five_pk, pca_table):
    '''
    Takes list of list of top five players per cluster, and outputs a list of dataframes
    corresponding to those players' playtype frequency stats.

    pca_table input must be in the format returned by get_table.py

    :param: top_five_pk, list(list(strings))
    :param: pca_table, pd.DataFrame

    :return: list(pd.DataFrame)
    '''
    
    assert isinstance(top_five_pk, list)
    assert isinstance(pca_table, pd.DataFrame)

    top_five_fr = []
    for k in top_five_pk:
        assert isinstance(k, list)
        df_l = []
        for p in k:
            df_l.append(pd.DataFrame(pca_table.loc[p][1::2]).transpose())
        top_five_fr.append(pd.concat(df_l))
    
    return top_five_fr

    #df_filt.drop(columns=['total_poss'])[km.labels_ == 0].describe().loc['mean']
    #pca_proj = pca.fit_transform(df_filt.drop(columns=['total_poss']))
