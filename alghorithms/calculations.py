import pandas as pd 

 # functions for processing data #-> These functions into src/alghorithms/calculations.py
def alghorithm_age (df):
    return df['age'].mean()

def alghorithm_height (df):
    return df['height'].sum()

 # function that combines both processed data # 
def product_alg_age_and_height(mean_age, sum_height): 
    return mean_age * sum_height