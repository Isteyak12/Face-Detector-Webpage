import cv2
import streamlit as st
from PIL import Image as PILImage
import numpy as np

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return image

def main():
    st.title("Face Detection with Streamlit")

    st.sidebar.header("Select Detection Method")
    detection_method = st.sidebar.radio("Choose Detection Method", ("Image", "Live Video"))

    if detection_method == "Image":
        st.sidebar.subheader("Upload Image")
        uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = PILImage.open(uploaded_file)
            st.image(np.array(image), caption='Uploaded Image', use_column_width=True)
            if st.button('Detect Faces (Image)'):
                result_img = detect_faces(np.array(image))
                st.image(result_img, caption='Result', use_column_width=True)

    elif detection_method == "Live Video":
        st.sidebar.subheader("Live Video Face Detection")
        available_camera = None
        for i in range(4):
            video_stream = cv2.VideoCapture(i)
            if video_stream.isOpened():
                available_camera = i
                break
            video_stream.release()

        if available_camera is not None:
            st.sidebar.text(f"Camera index {available_camera} is available")
            video_stream = cv2.VideoCapture(available_camera)
            stframe = st.empty()

            while True:
                ret, frame = video_stream.read()
                if not ret:
                    st.error("Failed to access the camera.")
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result_img = detect_faces(frame)
                stframe.image(result_img, caption='Live Video Face Detection', channels="RGB", use_column_width=True)
        else:
            st.error("No available camera found.")

if __name__ == '__main__':
    main()
