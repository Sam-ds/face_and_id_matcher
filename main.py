import cv2
import sys
import face_recognition

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    video = cv2.VideoCapture(0)
    check, frame = video.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in faces:
        shopper_faces = frame[y:(y + 30) + (h + 30), x:(x - 30) + (w + 30)]
        cv2.imwrite('face.jpeg', shopper_faces)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('Face Detector', frame);
    key = cv2.waitKey(1);

    if key == ord('q'):
        break;

while True:
    video = cv2.VideoCapture(0);
    check, frame = video.read();
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5);
    for x, y, w, h in faces:
        shopper_face_in_id = frame[y:(y + 30) + (h + 30), x:(x - 30) + (w + 30)]
        cv2.imwrite('identity_card.jpeg', shopper_face_in_id)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3);

    cv2.imshow('Identity scanner', frame);
    key = cv2.waitKey(1);

    if key == ord('q'):
        break;
# read 1st image and store encodings
known_image = face_recognition.load_image_file("face.jpeg")
unknown_image = face_recognition.load_image_file("identity_card.jpeg")
biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
if results[0]:
    print('proof matched with the shopper')

video.release();
cv2.destroyAllWindows();

sys.exit(0)
