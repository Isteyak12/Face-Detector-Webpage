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
    detection_method = st.sidebar.radio("Choose Detection Method", ("Image", "Pre-recorded Video"))

    if detection_method == "Image":
        # Your image upload logic...
        pass

    elif detection_method == "Pre-recorded Video":
        st.sidebar.subheader("Pre-recorded Video Face Detection")
        video_file = st.sidebar.file_uploader("Choose a video file...", type=["mp4"])  # Allow only MP4 videos

        if video_file is not None:
            video_bytes = video_file.read()
            cap = cv2.VideoCapture(video_bytes)

            stframe = st.empty()

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result_img = detect_faces(frame)
                stframe.image(result_img, caption='Pre-recorded Video Face Detection', channels="RGB", use_column_width=True)

if __name__ == '__main__':
    main()
