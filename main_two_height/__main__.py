# this file should run the main_two_height from WITHIN the folder main_two_height
if __package__ is None:
    from pathlib import Path, sys
    sys.path.append(str(Path(__file__).resolve().parent.parent))

 # general imports 
import pandas  as pd 

# import path files
import paths_for_data_etc # this needs the __package__ part 

 #import subsections of main 
from . import import_and_clean_height_00
from . import process_height_01
from . import display_height_02 


def main(): 
    # 00 import and clean
    df_height_clean = import_and_clean_height_00.import_clean_height()
    # save to clean
    df_height_clean.to_csv(paths_for_data_etc.height_clean_data_path, index=False)

    #01 process 
     # reload data from clean
    df_height_clean  =  pd.read_csv(paths_for_data_etc.height_clean_data_path)
    height_sum = process_height_01.process_height(df_height_clean)
    #02 display 
    display_height_02.display_data_main_one(height_sum)



if __name__ == '__main__': 
    main()