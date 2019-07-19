import logging

from resizeserver.celery import app
from ImageResizer.models import ResizeTask


logger = logging.getLogger(__name__)

@app.task()
def resize_image(pk):
    instance = ResizeTask.objects.get(id=pk)
    instance.resize()
    logger.info(f'Task with id = {instance.pk} is completed')

