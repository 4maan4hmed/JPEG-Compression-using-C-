import streamlit as st
import os
from PIL import Image
import tempfile
from jpeg_wrapper import compress_jpeg

def main():
    # Check compressor availability
    script_dir = os.path.dirname(os.path.abspath(__file__))
    compressor_path = os.path.join(script_dir, "jpeg_compressor.exe")

    if not os.path.exists(compressor_path):
        st.error(f"JPEG compressor engine not found at: {compressor_path}")
        return

    
    st.title("JPEG Compression Tool")
    st.write("Upload an image and adjust compression quality")

    # File uploader
    uploaded_file = st.file_uploader("Choose a JPEG image", type=["jpg", "jpeg"])
    
    # Compression quality slider
    quality = st.slider(
        "Compression Quality", 
        min_value=0.002, 
        max_value=1.0, 
        value=0.5,
        help="1.0 = Best quality (low compression), 0.5 = Balanced, 0.1 = High compression, 0.002 = Extreme"
    )
    
    if uploaded_file is not None:
        # Show original image
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_input = os.path.join(temp_dir, "input.jpg")
            temp_output = os.path.join(temp_dir, "output.jpg")

            # Save uploaded file
            with open(temp_input, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Show size
            original_size = os.path.getsize(temp_input)
            st.write(f"Original file size: {original_size/1024:.2f} KB")

            if st.button("Compress Image"):
                with st.spinner("Compressing..."):
                    success, output = compress_jpeg(temp_input, temp_output, quality)
                    
                    if success and os.path.exists(temp_output):
                        compressed_size = os.path.getsize(temp_output)

                        # Show compressed image
                        compressed_image = Image.open(temp_output)
                        st.image(
                            compressed_image, 
                            caption=f"Compressed Image (Quality: {quality})", 
                            use_column_width=True
                        )

                        # Show size info
                        st.write(f"Compressed file size: {compressed_size/1024:.2f} KB")
                        st.write(f"Compression ratio: {original_size/compressed_size:.2f}:1")

                        # Show compressor stdout
                        st.text_area("Compression Details", output, height=100)

                        # Download option
                        with open(temp_output, "rb") as file:
                            st.download_button(
                                label="Download Compressed Image",
                                data=file,
                                file_name="compressed.jpg",
                                mime="image/jpeg"
                            )
                    else:
                        st.error(f"Compression failed: {output}")

if __name__ == "__main__":
    main()
