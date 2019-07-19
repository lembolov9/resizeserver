import random

import factory
from factory.fuzzy import FuzzyText

from ImageResizer.models import ResizeTask


class ResizeTaskFactory(factory.DjangoModelFactory):
    class Meta:
        model = ResizeTask

    original_img = factory.django.ImageField(color='blue')
    resized_img = FuzzyText()
    width = random.randint(5, 200)
    height = random.randint(5, 200)