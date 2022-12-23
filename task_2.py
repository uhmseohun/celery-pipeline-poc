from app import app
from model import Data


@app.task
def task_2(data: Data):
    print("Task 2")
    print(f"Data from Task 1: {data}")
