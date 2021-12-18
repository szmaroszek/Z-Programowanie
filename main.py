import cv2
import pytesseract

from os import listdir
from os.path import isfile, join

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.3/bin/tesseract'


def read_from_image(img_path):
    img_cv = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)

dir_path = r'./photos'
photos = [f'{dir_path}/{f}' for f in listdir(dir_path) if isfile(join(dir_path, f))]

photos_read =[]
for photo in photos:
    photos_read.append(read_from_image(photo))

[print(f'--- photo: {i+1} ---\n' + photo) for i, photo in enumerate(photos_read)]
