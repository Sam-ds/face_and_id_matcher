import cv2
import face_recognition


def scan_face(face_cascades):

    global video, check, frame, faces, x, y, w, h, key
    while True:
        video = cv2.VideoCapture(0)
        check, frame = video.read()
        faces = face_cascades.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
        for x, y, w, h in faces:
            shopper_faces = frame[y:(y + 30) + (h + 30), x:(x - 30) + (w + 30)]
            cv2.imwrite('face.jpeg', shopper_faces)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow('Face Detector', frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break


def Scan_id():
    global video, check, frame, faces, x, y, w, h, key
    while True:
        video = cv2.VideoCapture(0)
        check, frame = video.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5);
        for x, y, w, h in faces:
            shopper_face_in_id = frame[y:(y + 30) + (h + 30), x:(x - 30) + (w + 30)]
            cv2.imwrite('identity_card.jpeg', shopper_face_in_id)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3);

        cv2.imshow('Identity scanner', frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break


def match_face_and_id():
    # read 1st image and store encodings
    shopper_face = face_recognition.load_image_file("face.jpeg")
    id_proof = face_recognition.load_image_file("identity_card.jpeg")
    shopper_face_encoding = face_recognition.face_encodings(shopper_face)[0]
    id_proof_encoding = face_recognition.face_encodings(id_proof)[0]
    results = face_recognition.compare_faces([shopper_face_encoding], id_proof_encoding)
    if results[0]:
        print('proof matched with the shopper')


if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    scan_face(face_cascade)
    Scan_id()
    match_face_and_id()

