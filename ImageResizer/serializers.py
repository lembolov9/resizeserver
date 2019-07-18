from rest_framework import serializers

from ImageResizer.models import ResizeTask


class ResizeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResizeTask
        fields = ('pk','original_img', 'width', 'height')