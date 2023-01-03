# this file should run the main_one_age, from WITHIN the folder main_one_age

if __package__ is None:
    from pathlib import Path, sys
    sys.path.append(str(Path(__file__).resolve().parent.parent))

# general imports 
import pandas as pd 

# import path files
import paths_for_data_etc

 #import subsections of main 
from . import import_and_clean_age_00
from . import process_age_01
from . import display_age_02 


def main (): 
    # 00 import and clean age 
    df_age_clean = import_and_clean_age_00.import_clean_age()
    # save in clean 
    df_age_clean.to_csv(paths_for_data_etc.age_clean_data_path, index=False)

    # 01 process age 
    # reload data from clean
    df_age_clean = pd.read_csv(paths_for_data_etc.age_clean_data_path)
    age_mean = process_age_01.process_age(df_age_clean)

    #02 display age 
    display_age_02.display_data_main_one(age_mean)


if __name__ == '__main__': 
    main()

