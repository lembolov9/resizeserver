from django.db import models

# Create your models here.

class ResizeTask(models.Model):
    resize_id = models.CharField(max_length=255, blank=True)
    original_img = models.ImageField(upload_to="originals/", blank=False)
    width = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    resized_img = models.ImageField(upload_to="resized/", blank=True)
