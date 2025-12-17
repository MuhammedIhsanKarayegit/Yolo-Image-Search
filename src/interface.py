import streamlit as st
import sys
from pathlib import Path
import time

# Add project root to  the system path
sys.path.append(str(Path(__file__).parent))

def init_session_state():
    session_defaults = {
        "image_dir": "value"
    }

    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

st.set_page_config(page_title = "YOLOv11  Search App", layout = "wide")
st.title("Computer Vision Powered Search Application")

#Main options 
option = st.radio("Choose an Option:",
                  ("Process new images","Load existing metadata"),
                  horizontal = True)

if option == "Process new images":
    with st.expander("Process new images", expanded = True):
        col1, col2 = st.columns(2)
        with col1:
            image_dir = st.text_input("Image directory path:", placeholder = "path/to/images")
        with col2:
            model_path = st.text_input("Model weights path:", "yolo11m.pt")

        if st.button("Start Inference"):
            if image_dir:
                try:
                    with st.spinner("Running object detection..."):
                        time.sleep(3)
                        st.success(f"Processed images.")
                except Exception as e:
                    st.error(f"Error during inference: {str(e)}")
            else:
                st.warning(f"Please enter an image directory path")
else:
    with st.expander("Load Existing Metadata", expanded = True):
        metadata_path = st.text_input("Metada fiel path:", placeholder = "path/to/metadata.json")

        if st.button("Load Metadata"):
            if metadata_path:
                try:
                    with st.spinner("Loading Metadata..."):
                        time.sleep(3)
                        st.success(f"Successfully loaded metadata.")
                except Exception as e:
                    st.error(f"Error loading metadata: {str(e)}")
            else:
                st.warning(f"Please enter metadata file path")

