from os import listdir
from os.path import isfile, join
from detection import *


def highlight_people(source):
    if source.split('.')[-1] == 'jpg':
        photo_highlight(source)
    if source.split('.')[-1] == 'mp4':
        video_highlight(source)


dir_path = r'./test-resources'
photos = [f'{dir_path}' + f'/photos/{f}' for f in listdir(dir_path + '/photos')
          if isfile(join(dir_path + '/photos', f))]
videos = [f'{dir_path}' + f'/videos/{f}' for f in listdir(dir_path + '/videos')
          if isfile(join(dir_path + '/videos', f))]

for photo in photos:
    highlight_people((photo))

for video in videos:
    highlight_people((video))
