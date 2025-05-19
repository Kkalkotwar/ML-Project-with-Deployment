## New End-to-End Machine Learning Project with Deployment

# End-to-End-Machine-Learning-Project-with-Deployment
This is the Repository which contains End-to-End Machine Learning Project Workflow with Deployment.

## WorkFlow

1. Update config.yaml    ------> Inside the Config folder (Not in src folder, it is out of src folder).
2. Update schema.yaml    ------> It's just a file where you mention the columns you have in you data with respect to 
                                 the data types.
3. Update params.yaml    ------> We will be writing all the parameters we wil be using in our project.
                                 Let's say values like "α" , "β" , "γ" which might be used in our process code. 
4. Update the entity     ------> Updating the config_entity.py file in src folder
5. Update the configuration manager in src config -----> Inside the src.config folder ["Configuration.py" file]
6. Update the components ------> Components like "Data Ingestion", "Data Validation", "Data Transformation"...etc. 
7. Update the pipeline   ------> Update and adding the pipeline. Basically integrating all the components with
                                 pipeline {Training pipeline separate and prediction pipeline separate}.
8. Update the main.py    ------> This will be the main.py file update.
9. Update the app.py     ------> Inside app.py we will be writing the UI related functionality, and integrate this
                                 main.py with app.py {User will run the app.py and it will run all the code.}






# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Kkalkotwar/End-to-End-Machine-Learning-Project-with-Deployment.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n ml_project python=3.8 -y
or 
python -m venv {environment_name}
```

```bash
conda activate mlproj
or
activate the venv by coping the relative path of activate file {.venv\Scripts\activate}
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```