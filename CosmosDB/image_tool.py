import json
from json import JSONEncoder

import numpy
import numpy as np
from PIL import Image

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def read_single_disk(image_path):
    """ read a single image.
        Parameters:
        ---------------
        image_path    image_path

        Returns:
        ----------
        image       image array, (32, 32, 3) to be stored
    """
    return Image.open(image_path)

def store_single_disk(image, image_path):
    """ Stores a single image as a .png file on disk.
        Parameters:
        ---------------
        image       image array, (32, 32, 3) to be stored
        image_path    image_path
    """
    Image.fromarray(image.astype(np.uint8)).save(image_path)

def image_decoder(image):
    decodedArrays = json.loads(image)
    return numpy.asarray(decodedArrays)


def image_encoder(image):
    return json.dumps(np.array(image), cls=NumpyArrayEncoder)