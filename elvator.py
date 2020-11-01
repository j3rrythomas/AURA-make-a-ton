import selenium
from selenium.webdriver import Chrome
import time
import cv2
import numpy as np
import dlib


def getl():

    driver=Chrome(executable_path="C:\webdriver\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://plantigrade-scope.000webhostapp.com/")
    #link=driver.find_elements_by_class_name("alanBtn-root alan-a1f67070ae885c19049f4dc1c47d03712e956eca572e1d8b807a3e2338fdd0dc")
    #link.click()



def no_of_face():
    cap = cv2.VideoCapture(0)


    # Detect the coordinates
    detector = dlib.get_frontal_face_detector()

    flag=1
    # Capture frames continuously
    while True:

        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # RGB to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        # Iterator to count faces
        i = 0
        for face in faces:

            # Get the coordinates of faces
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

            # Increment iterator for each face in faces
            i = i+1

            # Display the box and faces
            cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print("No of faces", i)
            print("hi")
            if(i<=2):
                time.sleep(1)
                getl()
                cv2.destroyAllWindows()
                return
            else:
                cv2.putText(frame,"THERE ARE MORE THAN 2 PEOPLE HERE",(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
                time.sleep(2)

                break

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # This command let's us quit with the "q" button on a keyboard.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()





