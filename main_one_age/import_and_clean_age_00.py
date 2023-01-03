# these relative imports are not working. 
from import_data.import_data import get_data_age
from clean_data.clean_data import clean_age
import paths_for_data_etc

def import_clean_age():
        
    df_age = get_data_age(paths_for_data_etc.age_raw_data_path)    # -> this step into file main_age/00_import_and_clean_age.py
    df_age_clean = clean_age(df_age)  # -> this step into file main_age/00_import_and_clean_age.py
    return df_age_clean

if __name__ == '__main__': 
    import_clean_age()