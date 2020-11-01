import face_recognition as fr
import os
import cv2
#import face_recognition
import numpy as np
from time import sleep


def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./Images"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("Images/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

#Program Excection starts here
def f():
    cam = cv2.VideoCapture(0)

    known_faces = get_encoded_faces()
    face = list(known_faces.values())
    names = list(known_faces.keys())

    process_frame = True

    face_locations = []
    face_encodings = []

    while True:
        ret,frame = cam.read()

        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)

        rgb_small_frame = small_frame[:,:,::-1] #convertion from bgr to rgb

        if process_frame:
            face_locations = fr.face_locations(rgb_small_frame)
            face_encodings = fr.face_encodings(rgb_small_frame,face_locations)
            face_names = []

            for face_encoding in face_encodings:
                matches = fr.compare_faces(face,face_encoding)
                name ="Unknown"

                face_distances = fr.face_distance(face,face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = names[best_match_index]

                face_names.append(name)

        process_frame = not process_frame

        for(y1,x2,y2,x1),name in zip(face_locations,face_names):
            x1 *=4
            x2 *=4
            y1 *=4
            y2 *=4

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

            cv2.rectangle(frame,(x1,y2-30),(x2,y2),(0,255,0),cv2.FILLED)

            font = cv2.FONT_HERSHEY_DUPLEX

            cv2.putText(frame,name,(x1+6,y2-6),font,1.0,(255,255,255),1)

        cv2.imshow('Video',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()



