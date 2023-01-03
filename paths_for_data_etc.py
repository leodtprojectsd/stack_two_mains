# file with all python paths --> this should become the standard python way of doing this 
import os 
from pathlib import Path
import sys


from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent

RAW_DATA_DIR = ROOT_DIR / "data" / "raw_data"
age_raw_data_path = RAW_DATA_DIR / "raw_age_data.csv"
height_raw_data_path = RAW_DATA_DIR / "raw_height_data.csv"

CLEAN_DATA_DIR = ROOT_DIR / "data" / "cleaned_data"
age_clean_data_path = CLEAN_DATA_DIR / "clean_age_data.csv"
height_clean_data_path = CLEAN_DATA_DIR / "clean_height_data.csv"

