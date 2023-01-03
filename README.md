# Multiple Mains Project Structure
This project structure is suitable when: 
 - You want to run distinct analysis, sometimes separately (multiple mains)
 - These mains may share functions
 - You want the distinct analysis in separate folders

 This structure is useful as it keeps the project neet and tidy.

 - In cmd (not python terminal), from ProjectDIR activate the venv: ```.venv\Scripts\activate```
 
 - You can run all the analysis toghether: ```python __main__.py```
 
 - You can run analyis one on its own: ```python -m main_one_age.__main__```

 - You can run analys two on its onw  ```python -m main_two_height.__main__```


## Venv
Since we have created a Venv
 - from cmd ```python -m venv .venv ```
You have to pip install all the packages. 

After you have done that, you can run 
```pip freeze -r requirements.txt```
and it will create a small version of requiremens for the project. 



