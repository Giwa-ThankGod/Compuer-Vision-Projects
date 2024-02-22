import os
from pathlib import Path
from PIL import Image
import numpy as np

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# im = np.array(Image.open('img01.jpg'))
# print(im.shape, im.dtype)

arr = np.array([1,2,3])
print(arr)