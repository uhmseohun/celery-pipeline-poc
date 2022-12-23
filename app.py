from celery import Celery
from kombu import Queue

app = Celery('main')


class CeleryConfig:
    broker_url = 'redis://localhost:6379'
    include = ['task_1', 'task_2']
    task_queues = (
        Queue("task_1_queue", routing_key="task_1.#"),
        Queue("task_2_queue", routing_key="task_2.#"),
    )

    #  configs for pydantic
    task_serializer = "pickle"
    result_serializer = "pickle"
    event_serializer = "json"
    accept_content = ["application/json", "application/x-python-serialize"]
    result_accept_content = ["application/json", "application/x-python-serialize"]


app.config_from_object(CeleryConfig)
