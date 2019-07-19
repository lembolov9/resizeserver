from django.urls import path

from ImageResizer.views import TaskRegistryView

urlpatterns = [
    path('', TaskRegistryView.as_view(), name='photos')
]