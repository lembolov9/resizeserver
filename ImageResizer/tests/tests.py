# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from jsonschema import validate

from ImageResizer.tests.factories import ResizeTaskFactory
from ImageResizer.tests.utils import generate_good_requests
from ImageResizer.tests.utils import generate_bad_requests


class TaskRegistryViewTests(APITestCase):

    def test_create_task_pos_requests(self):
        for i in generate_good_requests():
            with open(i["img"].name, 'rb') as img:
                i["data"]['original_img'] = img
                response = self.client.post(path=reverse('photos'), data=i['data'])
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                validate(response.json(),
                         schema={
                             "type": "object",
                             "required": [
                                 "pk",
                                 "original_img",
                                 "width",
                                 "height"
                             ],
                             "items": {
                                 "pk": "number",
                                 "original_img": "string",
                                 "width": "number",
                                 "height": "number"
                             }
                         })

    def test_create_task_neg_requests(self):
        for i in generate_bad_requests():
            if i.get('img'):
                img = open(i["img"].name, 'rb')
                i["data"]['original_img'] = img
            response = self.client.post(path=reverse('photos'), data=i['data'])
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_task_status_completed(self):
        task = ResizeTaskFactory(completed = True)
        response = self.client.get(reverse('photos'), {"resize_id": task.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        validate(response.json(),
                 schema={
                     "type": "object",
                     "required": [
                         "status",
                         "img_path"
                     ],
                     "items": {
                         "status": "COMPLETED",
                         "img_path": "string",
                     }
                 })

    def test_check_task_status_pending(self):
        task = ResizeTaskFactory(completed=False)
        response = self.client.get(reverse('photos'), {"resize_id": task.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        validate(response.json(),
                 schema={
                     "type": "object",
                     "required": [
                         "status"
                     ],
                     "items": {
                         "status": "PENDING"
                     }
                 })




