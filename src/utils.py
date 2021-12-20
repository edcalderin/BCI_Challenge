import pandas as pd
import numpy as np

def dataframe_missing_values(df):
    df_missing_values = pd.DataFrame(df.isna().sum()/df.shape[0], columns=['%'])
    df_missing_values.sort_values('%', ascending=True, inplace=True)
    return df_missing_values

def get_columns_with_nan_values(df, threshold=.5):
    df_nan = dataframe_missing_values(df)    
    return df_nan[df_nan['%']>threshold].index

def less_frequent_categories(serie, n):
    counts = serie.value_counts()
    counts = counts[counts<n].index.tolist()
    return counts

def get_high_correlated_features(df, dtype):
    corrs = df.select_dtypes(dtype).corr()
    df_corrs = pd.DataFrame(np.triu(corrs, k=1), columns=corrs.index)
    df_corrs = (df_corrs >= abs(.8)).sum()
    corr_features = df_corrs.loc[lambda x: x==1].index.tolist()
    return corr_features