import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client['task_bot_db']
tasks_collection = db['tasks']

def add_task_to_db(task):
    tasks_collection.insert_one({"task": task})

def update_task_in_db(task_number, new_task):
    tasks = list(tasks_collection.find())
    if 0 < task_number <= len(tasks):
        task_id = tasks[task_number - 1]['_id']
        tasks_collection.update_one({"_id": task_id}, {"$set": {"task": new_task}})

def delete_tasks_from_db(task_numbers):
    tasks = list(tasks_collection.find())
    for task_number in task_numbers:
        if 0 < task_number <= len(tasks):
            task_id = tasks[task_number - 1]['_id']
            tasks_collection.delete_one({"_id": task_id})

def get_tasks_from_db():
    tasks = list(tasks_collection.find())
    return [(index + 1, task['task']) for index, task in enumerate(tasks)]
