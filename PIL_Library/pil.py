import os
from pathlib import Path
from PIL import Image


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dropbox = BASE_DIR / 'CVision'

# imgbox = os.path.splitext('gray_img.jpg')[0] + '.jpg'

img = Image.open(r'img01.jpg')

print(img)

# CONVERT
# grayscale for value 'L'
gray_img = img.convert('L')

# Convert to Thumbnail
# img = img.thumbnail((128,128))

# CROPPING
box = (0,0,157,500)
region = img.crop(box)

# COPY AND PASTE REGION 
img_trans = region.convert('L')
# .transpose(Image.Transpose.ROTATE_180).convert('L')

# Paste the transposed image on the complete image
#(Method 1) 
img.paste(img_trans, box)

#(Method 2) Image.Image.paste(img,img_trans,box)

#RESIZE AND ROTATE
# img = img.resize((1080,1080))
# img = img.rotate(45)

#Try to delete any exiting file with same name
# if os.path.exists(BASE_DIR / 'CVision/gray_img.jpg'):
#     try:
#         os.remove(BASE_DIR / 'CVision/gray_img.jpg')
#     except OSError:
#         print("Could'nt delete file")


try:
    gray_img.save('gray_img.jpg')
except IOError:
    print("Cannot convert file!!")

img.show()