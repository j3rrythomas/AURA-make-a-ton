import os
import face_recognition as fr
import dlib

for dirpath, dnames, fnames in os.walk("./Images"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
                try:
                	face = fr.load_image_file("Images/" + f)
                    encoding = fr.face_encodings(face[0])
                except IndexError as e:
                    print(e)




                encoded[f.split(".")[0]] = encoding
        print(encoded)
