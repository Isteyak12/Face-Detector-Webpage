import cv2
import streamlit as st
from PIL import Image as PILImage
import numpy as np

def detect_faces(image):
    # Your face detection logic here...
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
        for i in range(5):  # Try up to 5 devices
            cap = cv2.VideoCapture(i, cv2.CAP_V4L)  # Try different API backends if available
            if cap.isOpened():
                available_camera = i
                break
            cap.release()

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
