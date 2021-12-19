import numpy as np
import cv2
from os import listdir
from os.path import isfile, join


def highlight_people(source):
    if source.split('.')[-1] == 'jpg':
        photo_highlight(source)
    if source.split('.')[-1] == 'mp4':
        video_highlight(source)

def photo_highlight(photo):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cv2.startWindowThread()

    out = cv2.imwrite('output.jpg', (640,480))

    detection(photo, out, hog)
        
    cv2.waitKey(10000) & 0xFF == ord('q')
    cv2.destroyAllWindows()

def video_highlight(video):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    cv2.startWindowThread()

    cap = cv2.VideoCapture(video)
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15., (640,480))

    while(True):
        detection(cap, out, hog)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    
    cv2.destroyAllWindows()

def detection(cap, out, detect_mode):
    try:
        _, frame = cap.read()
    except:
        frame = cv2.imread(cap)

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    boxes, _ = detect_mode.detectMultiScale(gray, winStride=(4, 4), padding=(4, 4))
    
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    try:
        out.write(frame.astype('uint8'))
    except:
        out = cv2.imwrite('output.jpg', frame)

    cv2.putText(frame, str(len(boxes)), (600, 450), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('frame',frame)


dir_path = r'./test-resources'
photos = [f'{dir_path}' + f'/photos/{f}' for f in listdir(dir_path + '/photos') if isfile(join(dir_path + '/photos', f))]
videos = [f'{dir_path}' + f'/videos/{f}' for f in listdir(dir_path + '/videos') if isfile(join(dir_path + '/videos', f))]

for photo in photos:
    highlight_people((photo))

for video in videos:
    highlight_people((video))
