
import os
from rembg import remove
from PIL import Image
import cv2
import streamlit as st

# Function to upscale an image using OpenCV (placeholder for Real-ESRGAN integration)
def upscale_image(image):
    scale_percent = 200  # Upscale by 200%
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    upscaled = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
    return upscaled

# Function to apply a grayscale filter
def apply_grayscale_filter(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

# Function to remove the background using rembg
def remove_background(image_path):
    with open(image_path, "rb") as input_file:
        output = remove(input_file.read())
    return Image.open(output)

# Streamlit app
def create_photo_editor_app():
    st.title("AI Photo Editor")
    st.write("Enhance your photos with AI-powered tools: Upscaling, Filters, and Background Editing.")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        image_path = f"temp_image.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        image = cv2.imread(image_path)

        st.write("### Choose an Action")
        action = st.selectbox("Select an action", ["Upscale Image", "Apply Grayscale Filter", "Remove Background"])

        if st.button("Process"):
            if action == "Upscale Image":
                upscaled_image = upscale_image(image)
                upscaled_pil = Image.fromarray(cv2.cvtColor(upscaled_image, cv2.COLOR_BGR2RGB))
                st.image(upscaled_pil, caption="Upscaled Image", use_column_width=True)

            elif action == "Apply Grayscale Filter":
                gray_image = apply_grayscale_filter(image)
                gray_pil = Image.fromarray(gray_image)
                st.image(gray_pil, caption="Grayscale Image", use_column_width=True)

            elif action == "Remove Background":
                bg_removed_image = remove_background(image_path)
                st.image(bg_removed_image, caption="Background Removed Image", use_column_width=True)

if __name__ == "__main__":
    create_photo_editor_app()
