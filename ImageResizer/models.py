from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models

# Create your models here.

class ResizeTask(models.Model):
    resize_id = models.CharField(max_length=255, blank=True)
    original_img = models.ImageField(upload_to="originals/", blank=False)
    width = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    resized_img = models.ImageField(upload_to="resized/", blank=True)
    completed = models.BooleanField(default=False)

    def resize(self):
        filename = self.original_img.name.split('/')[-1]
        img_io = BytesIO()
        img = Image.open(self.original_img).resize((self.width, self.height), Image.ANTIALIAS)
        img.save(img_io, format=filename.split('.')[-1], quality=100)

        self.resized_img.save(filename, content=ContentFile(img_io.getvalue()))
        self.completed = True
        self.save()
