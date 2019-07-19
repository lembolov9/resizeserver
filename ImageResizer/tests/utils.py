import tempfile
from PIL import Image
from random import randint as ri

def generate_random_image():
    img = Image.new("RGB", (ri(1,150), (ri(1,150))), (ri(1,255), ri(1,255), ri(1,255)))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
    img.save(tmp_file)
    return tmp_file


def generate_good_requests():
    requests = list()

    for i in range(3):
        requests.append(
            {
                "img" : generate_random_image(),
                "data": {
                "width": ri(1, 9999),
                "height": ri(1, 9999),
                }
            })

    return requests

def generate_bad_requests():
    requests = list()


    requests.append(
        {
            "img" : generate_random_image(),
            "data": {
                "width": ri(10000, 20000),
                "height": ri(10000, 20000)
            }
        }
    )
    requests.append(
        {
            "data": {
                "width": ri(1, 9999),
                "height": ri(1, 9999),
            }
        }
    )
    return requests