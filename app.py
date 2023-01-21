import streamlit as st 
import cv2
import numpy as np
import keras



class demo:
    def __init__(self, model_path : str = 'assets/maize-detector.h5') -> None:
        st.title("Gerageza Ikoranabuhanga ryacu!")
        self.model = keras.models.load_model(model_path)
    
        img = st.file_uploader("Uploading ifoto y' igihingwa cyawe aha!", type=['png', 'jpg', 'jpeg'])
        if img is not None:
            img_ = self.process_img(img)
            self.predict_img(img_)

        img = st.camera_input("Capture ifoto y' igihingwa cyawe aha!")
        if img is not None:
            img_ = self.process_img(img)
            self.predict_img(img_)

    def process_img(self, img):
        file_bytes = np.asarray(bytearray(img.read()), dtype=np.uint8) / 255
        opencv_image = cv2.imdecode(file_bytes, 1)
        resized_img = cv2.resize(opencv_image, (224, 224))
        st.image(opencv_image, channels="BGR", caption="Ifoto y' igihingwa cyawe", use_column_width=True)
        return resized_img

    def predict_img(self, img):
        print(self.model.predict(img))
        

def contact():
    st.sidebar.title("Contact")
    st.sidebar.info("Email: mugenzik@gmail.com")
    st.sidebar.info("Phone: +250780587387")


#the navbar function
def contact_navbar():
    st.sidebar.title("Contact")
    st.sidebar.info("Email: mugenzik@gmail.com")
    st.sidebar.info("Phone: +250780587387")
    st.sidebar.map()


#the main function
def main():


    #the navbar
    contact_navbar()

    #home section
    st.title("Ahabanza")
    st.write("Reba ubuzima bw' ibihingwa byawe!")
    st.image('assets/maize.jpg')

    #the demo section
    demo()
    
    
    



if __name__ == "__main__":
    st.set_page_config(page_title="Eza Neza!")
    main()
