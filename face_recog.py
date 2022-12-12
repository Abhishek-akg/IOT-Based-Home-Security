import face_recognition
import cv2
import numpy as np

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(3, GPIO.OUT, initial = GPIO.LOW)

video_capture = cv2.VideoCapture(0)
print(video_capture)

bishal_image = face_recognition.load_image_file("<image_path>/1b.jpg")
bishal_face_encoding = face_recognition.face_encodings(bishal_image)[0]

prayag_image = face_recognition.load_image_file("<image_path>/2p.jpg")
prayag_face_encoding = face_recognition.face_encodings(prayag_image)[0]

known_face_encodings = [
    bishal_face_encoding,
    prayag_face_encoding
]
known_face_names = [
    "Bishal Saha",
    "Prayag Raj Sharma"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()

    if process_this_frame:
        print(ret)
        print(frame)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            
            if name == "Unknown":
                GPIO.output(37, GPIO.LOW)
                GPIO.output(3, GPIO.HIGH)
            else:
                GPIO.output(3, GPIO.LOW)
                GPIO.output(37, GPIO.HIGH)

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
GPIO.output(37, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
cv2.destroyAllWindows()
