import pandas as pd

def sum_encoder_fit_transform(df: pd.DataFrame, cat_variables:list, target_name:str) -> pd.DataFrame:
    '''Function for applyig su-encoding techique to some subset of data'''
    for var in cat_variables:
        df_agged = df.groupby(var)[target_name].mean().reset_index()
        mapping = dict(zip(df_agged[var].to_list(), df_agged[target_name].to_list()))
        df[var] = df[var].apply(lambda x: mapping[x])
    
    return df
