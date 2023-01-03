from import_data.import_data import get_data_height
from clean_data.clean_data import clean_height
import paths_for_data_etc

def import_clean_height():
        
    df_height = get_data_height(paths_for_data_etc.height_raw_data_path)    
    df_height_clean = clean_height(df_height)  
    return df_height_clean

if __name__ == '__main__': 
    import_clean_height()