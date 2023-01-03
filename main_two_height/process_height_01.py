from alghorithms.calculations import alghorithm_height

def process_height(df_height_clean): 
    df_height_processed = alghorithm_height(df_height_clean) 
    return df_height_processed

if __name__ == '__main__': 
    process_height("path_to_df_height_clean")
