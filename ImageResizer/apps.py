from django.apps import AppConfig


class ImageresizerConfig(AppConfig):
    name = 'ImageResizer'

    def ready(self):
        import ImageResizer.receivers
