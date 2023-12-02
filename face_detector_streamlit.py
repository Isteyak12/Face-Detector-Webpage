import cv2
import streamlit as st
import numpy as np

def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image

def main():
    st.title("Face Detection with Streamlit")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            st.error("Failed to access the camera.")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result_img = detect_faces(frame)
        st.image(result_img, caption='Live Video Face Detection', channels="BGR", use_column_width=True)

if __name__ == '__main__':
    main()
