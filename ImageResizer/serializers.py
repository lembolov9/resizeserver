from rest_framework import serializers

from ImageResizer.models import ResizeTask


class ResizeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResizeTask
        fields = ('pk','original_img', 'width', 'height')

    def validate_width(self, value):
        if not (0 < value < 10000):
            raise serializers.ValidationError("Width should be between 0 and 10000")  # raise ValidationError
        return value

    def validate_height(self, value):
        if not (0 < value < 10000):
            raise serializers.ValidationError("Height should be between 0 and 10000")  # raise ValidationError
        return value