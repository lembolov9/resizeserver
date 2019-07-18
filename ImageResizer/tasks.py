from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile

from ImageResizer.models import ResizeTask
from resizeserver.celery import app


@app.task(track_started = True)
def resize_image(pk):
    instance = ResizeTask.objects.get(pk=pk)
    filename = instance.original_img.name.split('/')[-1]

    img_io = BytesIO()
    img = Image.open(instance.original_img).resize((instance.width, instance.height), Image.ANTIALIAS)
    img.save(img_io, format=filename.split('.')[-1], quality=100)

    instance.resized_img.save(filename, content=ContentFile(img_io.getvalue()))