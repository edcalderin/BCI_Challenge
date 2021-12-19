import pandas as pd

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

def preprocess_month(df):
    '''
    Function to split data, create new series and dropping original feature
    '''
    year, month= [], []
    df_copy = df.copy()
    
    for item in df_copy['mes']:
        year.append(str(item)[:4])
        month.append(str(item)[4:])
    
    df_copy['year'] = year
    df_copy['month'] = month
    
    # Converting data type
    df_copy['year'] = df_copy.year.astype('int16')
    df_copy['month'] = df_copy.month.astype('int16')
    
    # Dropping original feature
    df_copy.drop('mes', axis=1, inplace=True)
    
    return df_copy