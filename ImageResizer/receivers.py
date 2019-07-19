from django.db.models.signals import post_save
from django.dispatch import receiver

from ImageResizer.models import ResizeTask
from ImageResizer.tasks import resize_image


@receiver(post_save, sender = ResizeTask)
def start_resize_signal_receiver(sender, instance, created, *args, **kwargs):
    if created:
        instance.resize_id = resize_image.apply_async(args=[instance.pk])
        instance.save()
