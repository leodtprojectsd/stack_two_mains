import pandas as pd 

def get_data_age(path_to_raw_data_age):  
    df = pd.read_csv(path_to_raw_data_age)
    return df

def get_data_height(path_to_raw_data_height): 
    df = pd.read_csv(path_to_raw_data_height)
    return df

# get_data_age().to_csv("raw_age_data.csv", index=False)
# get_data_height().to_csv("raw_height_data.csv", index=False)