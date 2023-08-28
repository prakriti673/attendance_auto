import face_recognition 
import cv2
import numpy as np
import csv
import os 
import glob
from datetime import datetime

video_capture = cv2.VideoCapture(0)

draco_image= face_recognition.load_image_file("faces/dracomalfoy.jpg")
draco_encoding=face_recognition.face_encoding(draco_image)[0]

harry_image= face_recognition.load_image_file("faces/harrypotter.jpg")
harry_encoding=face_recognition.face_encoding(harry_image)[0]

hermoine_image= face_recognition.load_image_file("faces/hermoine.jpg")
hermoine_encoding=face_recognition.face_encoding(hermoine_image)[0]

ron_image= face_recognition.load_image_file("faces/ronweasley.jpg")
ron_encoding=face_recognition.face_encoding(ron_image)[0]

known_faces_names = [
    'Draco Malfoy',
    'Harry Potter'
    'Hermoine Granger',
    'Ron Weasley'
]

student=known_faces_names.copy()

faces_location=[]
faces_encoding=[]
faces_names=[]
s=True

now=datetime.now
current_date=new_strftime("%Y-%m-%d")
f=open(current.date+'.csv','w+',newLine = '')
lnwriter= csv.writer(f)

while True:
    _.frame = video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=small_frame[:,:,::-1]
    if s:
        face_locations=face_recognition.face_location(rgb_small_frame)
        faces_encoding=face_recognition.face_encoding(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = rp.argmin(face_distance)
            if(matches[best_match_index]):
                name=known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in student:
                    student.remove(name)
                    print(student)
                    current_time=now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])
    cv2.imshow("Attendance System",frame)
    if cv2.writeKey() & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()