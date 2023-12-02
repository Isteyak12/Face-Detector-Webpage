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
        # Your image upload logic...
        pass

    elif detection_method == "Live Video":
        st.sidebar.subheader("Live Video Face Detection")

        video_stream = cv2.VideoCapture(0)  # Try without specifying the index
        stframe = st.empty()

        while True:
            ret, frame = video_stream.read()
            if not ret:
                st.error("Failed to access the camera.")
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result_img = detect_faces(frame)
            stframe.image(result_img, caption='Live Video Face Detection', channels="RGB", use_column_width=True)

if __name__ == '__main__':
    main()
