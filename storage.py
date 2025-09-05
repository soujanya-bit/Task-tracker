import json
import os

FILE_NAME="tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME,"r") as f:
        return json.load(f)
    

def save_tasks(tasks):
    with open(FILE_NAME,"w") as f:
        json.dump(tasks,f,indent=4)