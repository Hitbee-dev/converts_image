from PIL import Image
import os

file_list = os.listdir('images/')
print(file_list)

for image in file_list:
    imgname = image.split(".")
    img = Image.open(f'images/{imgname[0]}.{imgname[1]}').convert('RGB')
    img.save(f'converts_images/{imgname[0]}.png', 'png')/