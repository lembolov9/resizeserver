from celery.result import AsyncResult
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from ImageResizer.models import ResizeTask
from ImageResizer.serializers import ResizeTaskSerializer


class TaskRegistryView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            resize_task = ResizeTask.objects.get(pk = request.GET['resize_id'])
        except:
            raise NotFound(detail=f'The task with id = {request.GET["resize_id"]} does not exist')

        if resize_task.resized_img:
            return Response(
                {"status": "COMPLETED", "img_path": request.build_absolute_uri('/')[:-1] + resize_task.resized_img.url},
                status=status.HTTP_200_OK
            )
        else:
            result = AsyncResult(resize_task.resize_id).status

            if result == 'PENDING':
                return Response({"status": result}, status=status.HTTP_200_OK)

            elif result == "STARTED":
                return Response({"status": result}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        resize_task_serializer = ResizeTaskSerializer(data=request.data)

        if resize_task_serializer.is_valid():
            resize_task_serializer.save()
            return Response(resize_task_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(resize_task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)