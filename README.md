# Example for Stack Overflow 

The obejective of this repo is to tranform the single script ```main_everything_in_one_script.ipynb``` into functions and files in different folders.
Since the script performs multiple analysis (height, age), these should be in separate mains that can call on the same functions. 

The file ```main_separated_code.ipynb``` is my attempt at separating out the code.
It is a single file that imports the files from the dirctories: main_one_age, main_two_height, main_display_combined. 

**Objective 1**: 

 - I would prefer if the sections of main_separated_code.ipynb were instead hosted within the folders main_one_age, main_two_height, main_display_combined, within the files (main_two_height_00_and_01_and_02.py, main_one_age_00_and_01_and_02.py and main_display_combined). Howver I am unable to make these mains run while within these subfolders (not ROOT) . 


**Objective 2**: 
 - Run the single blocks of a main eg"import_and_clean_age_00.py" as main directly. 
eg: this should work 
 from display_data import display_data
```python
def display_data_main_one(age_mean):
    return display_data.common_function_display_data(age_mean)
     
if __name__ == '__main__': 
    display_data("path to age mean")
    
 OUT: 
 ModuleNotFoundError: No module named 'display_data'
 ```
 **Objective 3**
 - use a standard way of writing the file "path_for_data_etc.py" that contains all the paths to import/export data. 
 - write pyproject.toml/setup.py/ or any other file that is necessary so that the project can be considered complete. 
 
The final project should be something that runs, and that has all the files necessary for a good standard python project
