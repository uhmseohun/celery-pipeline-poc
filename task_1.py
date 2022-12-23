from app import app
from model import Data
from task_2 import task_2


@app.task
def task_1():
    print('Task 1')

    data = Data(x=11)

    task_2.apply_async(
        args=[data],
        queue='task_2_queue',
    )
