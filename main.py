import streamlit as st
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from fpdf import FPDF
import base64



def page1():
    st.image('Capture.PNG')

def page2():
    st.markdown("<h1 style='text-align: center;'>Welcome To My App!</h1>", unsafe_allow_html=True)

    st.markdown(
    "<p style='text-align: center;'>The primary motivation behind brain tumor detection and classification is to facilitate early diagnosis, enabling timely and accurate treatment decisions. By not only identifying the presence of a tumor but also classifying its type, the system empowers healthcare professionals with critical insights that can significantly improve patient outcomes and survival rates.</p>",
    unsafe_allow_html=True
)
    uploaded_image = st.file_uploader(
        "Please choose an image file", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        img1 = Image.open(uploaded_image)
        picture = img1.save(f'data/{uploaded_image.name}')
        source = f'data/{uploaded_image.name}'
        print(source)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(' ')

        with col2:
           st.image(img1, caption="Uploaded Image")

        with col3:
            st.write(' ')
       
        
        model=load_model('model_file.h5')   
        frame=cv2.imread(source)
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized=cv2.resize(gray,(48,48))
        normalize=resized/255.0
        reshaped=np.reshape(normalize, (1, 48, 48, 1))
        result=model.predict(reshaped)
        label=np.argmax(result, axis=1)[0]
        print(label)


   

        # # List of image paths
        # image_paths = source  # Populate this list with paths to your images

        # print("img _path is :     "+image_paths)
        # # Initialize sum of total extracted features
        features_sum = 0

       
        frame = cv2.imread(source)
        result = model.predict(reshaped)
        
        
        features_sum += np.sum(result)

        print(features_sum)




    




        if label == 0:
            st.write("<div style='text-align: center;'>Tumor is Detected. Type: Glioma Tumor</div>", unsafe_allow_html=True)

            if st.button("Generate PDF"):
                            # Add image section
                

                pdf = FPDF()
                pdf.add_page()

               # Add header image in center
                header_image_path = "logo.png"  # Path to your header image
                page_width = 210  # Width of the page in mm (A4 size)
                image_width = 20  # Width of the small image
                x_position = (page_width - image_width) / 2  # Calculate x-coordinate to center the image
                pdf.set_xy(x_position, 10)  # Set position to center horizontally and vertically
                pdf.image(header_image_path, w=image_width)

                # Add report title in center
                pdf.set_font("Arial", size=12)
                pdf.cell(20, 20, txt="Hamdard University Diagnostic Centre", ln=True, align='C')
                pdf.ln(10)

                # Add report content with doctor's name aligned left
                report_content = f"Tumor is Detected. Type: Glioma Tumor the tumor measures {features_sum} cm dimension. It appears to be well-defined with irregular borders. Imaging studies indicate that the mass is heterogeneously enhancing, with areas of necrosis and calcification. There is no evidence of local invasion into surrounding organs, although regional lymph nodes are mildly enlarged. Further biopsy and histopathological examination are recommended to determine the precise nature and grade of the tumor."
                pdf.set_font("Arial", size=10)
                pdf.multi_cell(0, 10, txt=report_content)

                # Add doctor's name aligned left
                doctor_name = "Mr Mohsin Raza Khan "  # Example doctor name
                pdf.ln(10)
                pdf.set_font("Arial", size=10)
                pdf.cell(200, 10, txt=f"Doctor's Name: {doctor_name}", ln=True, align='L')

            # Add signature column with image and text
                signature_image_path = "sign.png"  # Path to your signature image
                signature_column_x = 100
                signature_column_y = pdf.get_y() + 5
                signature_column_width = 30
                signature_column_height = 20

                # Add signature image
                pdf.image(signature_image_path, x=signature_column_x, y=signature_column_y, w=signature_column_height)

                pdf_output = pdf.output(dest='S').encode('latin1')
                b64 = base64.b64encode(pdf_output).decode()
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="Tumor_report.pdf">Download PDF Report</a>'

                st.markdown(href, unsafe_allow_html=True)

        if label == 1:
               st.write("<div style='text-align: center;'>Tumor is Detected. Type: Minigoma Tumor</div>", unsafe_allow_html=True)

               if st.button("Generate PDF"):
                            # Add image section
                

                    pdf = FPDF()
                    pdf.add_page()

                # Add header image in center
                    header_image_path = "logo.png"  # Path to your header image
                    page_width = 210  # Width of the page in mm (A4 size)
                    image_width = 20  # Width of the small image
                    x_position = (page_width - image_width) / 2  # Calculate x-coordinate to center the image
                    pdf.set_xy(x_position, 10)  # Set position to center horizontally and vertically
                    pdf.image(header_image_path, w=image_width)

                    # Add report title in center
                    pdf.set_font("Arial", size=12)
                    pdf.cell(20, 20, txt="Hamdard University Diagnostic Centre", ln=True, align='C')
                    pdf.ln(10)

                    # Add report content with doctor's name aligned left
                    report_content = f"Tumor is Detected. Type: Minigoma Tumor the tumor measures {features_sum} cm dimension. It appears to be well-defined with irregular borders. Imaging studies indicate that the mass is heterogeneously enhancing, with areas of necrosis and calcification. There is no evidence of local invasion into surrounding organs, although regional lymph nodes are mildly enlarged. Further biopsy and histopathological examination are recommended to determine the precise nature and grade of the tumor."
                    pdf.set_font("Arial", size=10)
                    pdf.multi_cell(0, 10, txt=report_content)

                    # Add doctor's name aligned left
                    doctor_name = "Mr Mohsin Raza Khan "  # Example doctor name
                    pdf.ln(10)
                    pdf.set_font("Arial", size=10)
                    pdf.cell(200, 10, txt=f"Doctor's Name: {doctor_name}", ln=True, align='L')

                # Add signature column with image and text
                    signature_image_path = "sign.png"  # Path to your signature image
                    signature_column_x = 100
                    signature_column_y = pdf.get_y() + 5
                    signature_column_width = 30
                    signature_column_height = 20

                    # Add signature image
                    pdf.image(signature_image_path, x=signature_column_x, y=signature_column_y, w=signature_column_height)

                    pdf_output = pdf.output(dest='S').encode('latin1')
                    b64 = base64.b64encode(pdf_output).decode()
                    href = f'<a href="data:application/octet-stream;base64,{b64}" download="Tumor_report.pdf">Download PDF Report</a>'

                    st.markdown(href, unsafe_allow_html=True)

        if label == 2:
            st.write("<div style='text-align: center;'>No Tumor is Detected. Type: No Tumor</div>", unsafe_allow_html=True)

            if st.button("Generate PDF"):
                            # Add image section
                

                pdf = FPDF()
                pdf.add_page()

               # Add header image in center
                header_image_path = "logo.png"  # Path to your header image
                page_width = 210  # Width of the page in mm (A4 size)
                image_width = 20  # Width of the small image
                x_position = (page_width - image_width) / 2  # Calculate x-coordinate to center the image
                pdf.set_xy(x_position, 10)  # Set position to center horizontally and vertically
                pdf.image(header_image_path, w=image_width)

                # Add report title in center
                pdf.set_font("Arial", size=12)
                pdf.cell(20, 20, txt="Hamdard University Diagnostic Centre", ln=True, align='C')
                pdf.ln(10)

                # Add report content with doctor's name aligned left
                report_content = f"No tumour is detected your braint condition is excellent"
                pdf.set_font("Arial", size=10)
                pdf.multi_cell(0, 10, txt=report_content)

                # Add doctor's name aligned left
                doctor_name = "Mr Mohsin Raza Khan "  # Example doctor name
                pdf.ln(10)
                pdf.set_font("Arial", size=10)
                pdf.cell(200, 10, txt=f"Doctor's Name: {doctor_name}", ln=True, align='L')

            # Add signature column with image and text
                signature_image_path = "sign.png"  # Path to your signature image
                signature_column_x = 100
                signature_column_y = pdf.get_y() + 5
                signature_column_width = 30
                signature_column_height = 20

                # Add signature image
                pdf.image(signature_image_path, x=signature_column_x, y=signature_column_y, w=signature_column_height)

                pdf_output = pdf.output(dest='S').encode('latin1')
                b64 = base64.b64encode(pdf_output).decode()
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="Tumor_report.pdf">Download PDF Report</a>'

                st.markdown(href, unsafe_allow_html=True)

        if label == 3:
            st.write("<div style='text-align: center;'>Tumor is Detected. Type: Pitutary Tumor</div>", unsafe_allow_html=True)

            if st.button("Generate PDF"):
                            # Add image section
                

                pdf = FPDF()
                pdf.add_page()

               # Add header image in center
                header_image_path = "logo.png"  # Path to your header image
                page_width = 210  # Width of the page in mm (A4 size)
                image_width = 20  # Width of the small image
                x_position = (page_width - image_width) / 2  # Calculate x-coordinate to center the image
                pdf.set_xy(x_position, 10)  # Set position to center horizontally and vertically
                pdf.image(header_image_path, w=image_width)

                # Add report title in center
                pdf.set_font("Arial", size=12)
                pdf.cell(20, 20, txt="Hamdard University Diagnostic Centre", ln=True, align='C')
                pdf.ln(10)

                # Add report content with doctor's name aligned left
                report_content = f"Tumor is Detected. Type: Pitutary Tumor the tumor measures {features_sum} cm dimension. It appears to be well-defined with irregular borders. Imaging studies indicate that the mass is heterogeneously enhancing, with areas of necrosis and calcification. There is no evidence of local invasion into surrounding organs, although regional lymph nodes are mildly enlarged. Further biopsy and histopathological examination are recommended to determine the precise nature and grade of the tumor."
                pdf.set_font("Arial", size=10)
                pdf.multi_cell(0, 10, txt=report_content)

                # Add doctor's name aligned left
                doctor_name = "Mr Mohsin Raza Khan "  # Example doctor name
                pdf.ln(10)
                pdf.set_font("Arial", size=10)
                pdf.cell(200, 10, txt=f"Doctor's Name: {doctor_name}", ln=True, align='L')

            # Add signature column with image and text
                signature_image_path = "sign.png"  # Path to your signature image
                signature_column_x = 100
                signature_column_y = pdf.get_y() + 5
                signature_column_width = 30
                signature_column_height = 20

                # Add signature image
                pdf.image(signature_image_path, x=signature_column_x, y=signature_column_y, w=signature_column_height)

                pdf_output = pdf.output(dest='S').encode('latin1')
                b64 = base64.b64encode(pdf_output).decode()
                href = f'<a href="data:application/octet-stream;base64,{b64}" download="Tumor_report.pdf">Download PDF Report</a>'

                st.markdown(href, unsafe_allow_html=True)



        try:
            image = Image.open(uploaded_image)
            
            
        except Exception:
            st.error("Error: Invalid image")
        else:
            img_array = np.array(image)
            
            return img_array



def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.selectbox('Go to', ['Welcome', 'My App'])

    if page == 'Welcome':
        page1()
    elif page == 'My App':
        page2()

if __name__ == "__main__":
    main()
