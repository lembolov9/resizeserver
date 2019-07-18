from django.db.models.signals import post_save
from django.dispatch import receiver

from ImageResizer.models import ResizeTask
from ImageResizer.tasks import resize_image


@receiver(post_save, sender=ResizeTask)
def create_resize_task(sender, instance, created, **kwargs):
    if created:
        task_id = resize_image.apply_async(args = [instance.pk]).id
        instance.resize_id = task_id
        instance.save()