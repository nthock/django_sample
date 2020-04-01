from celery.decorators import task
# from polls.functions import adding_task
# adding_task(1, 2)
# adding_task.delay(1, 2)

@task(name="adding_task")
def adding_task(x, y):
    return x + y