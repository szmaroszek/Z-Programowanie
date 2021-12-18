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

img_1_path = photos[0]
img_1_cv = cv2.imread(img_1_path)
img_rgb = cv2.cvtColor(img_1_cv, cv2.COLOR_BGR2GRAY)

filtered_img_1 = []
filtered_img_1.append(cv2.threshold(cv2.GaussianBlur(img_rgb, (5, 5), 0), 0, 255,
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
filtered_img_1.append(cv2.threshold(cv2.bilateralFilter(img_rgb, 5, 75, 75), 0, 255,
                                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
filtered_img_1.append(cv2.threshold(cv2.medianBlur(img_rgb, 3), 0, 255,
                                    cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1])
filtered_img_1.append(cv2.adaptiveThreshold(cv2.GaussianBlur(img_rgb, (5, 5), 0), 255,
                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2))
filtered_img_1.append(cv2.adaptiveThreshold(cv2.bilateralFilter(img_rgb, 9, 75, 75), 255,
                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2))
filtered_img_1.append(cv2.adaptiveThreshold(cv2.medianBlur(img_rgb, 3), 255,
                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2))

filtered_photos_read = []
for photo in filtered_img_1:
    filtered_photos_read.append(pytesseract.image_to_string(photo))

[print(f'--- photo: {i+1} ---\n' + photo) for i, photo in enumerate(photos_read)]
[print(f'--- Filtered photo, filter: {i+1} ---\n' + photo) for i, photo in enumerate(photos_read)]