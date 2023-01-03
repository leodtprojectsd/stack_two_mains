import pandas as pd
 # functions for cleaning data #-> These functions into src/clean_data/clean_data.py
def clean_age (df): 
    df['age'] = pd.to_numeric(df['age'])
    return df 

def clean_height (df): 
    df['height'] = df['height'].replace("replace_this_with_190", 200)
    return df 