from alghorithms.calculations import alghorithm_age

def process_age(df_age_clean): 
    df_age_processed = alghorithm_age(df_age_clean) 
    return df_age_processed

if __name__ == '__main__': 
    process_age("path_to_df_age_clean")
