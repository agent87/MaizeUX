import streamlit as st 
import numpy as np
from tensorflow import keras

#Hide Tf Error
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



class demo:
    def __init__(self, model_path : str = 'maize-detector.h5') -> None:
        st.title("Gerageza Ikoranabuhanga ryacu!")
        self.model = keras.models.load_model(model_path)

        capture_tab, upload_tab = st.tabs(['Capture', 'Upload'])

        with capture_tab:
            self.demo_capture_ui()
        
        with upload_tab:
            self.demo_upload_ui()

    def demo_upload_ui(self):
        img = st.file_uploader("Uploading ifoto y' igihingwa cyawe aha!", type=['png', 'jpg', 'jpeg'])
        if img is not None:
            img_id = self.save_img(img)
            img = self.process_img(img_id)
            prediction = self.predict_img(img)
    
    def demo_capture_ui(self):
        img = st.camera_input("Fata ifoto y' igihingwa cyawe aha!")
        if img is not None:
            img_id = self.save_img(img)
            img = self.process_img(img_id)
            prediction = self.predict_img(img)


    def save_img(self, image_file):
        id =  len(os.listdir("temp/"))
        with open(f"temp/img-{id}.jpg", "wb") as f:
            f.write(image_file.getbuffer())
        return id

    def process_img(self, img_id):
        #Load flower jpeg image from local and set target size to 224 x 224
        img = keras.utils.load_img(f'temp/img-{img_id}.jpg', target_size=(224,224))

        #display image using streamlit
        st.image(img, caption='Igihingwa cyawe', use_column_width=True)

        #convert image to array
        input_img = keras.preprocessing.image.img_to_array(img)
        input_img = np.expand_dims(input_img, axis=0)

        return input_img


    def predict_img(self, img):
        pred = self.model.predict(img)
        print(pred)
        print(np.argmax(pred))
        pred = np.argmax(pred, axis=1)
        if pred == 0:
            st.warning("Your Maize Sample is infected with Corn Blight! Please take action immediately!")
        elif pred == 1:
            st.warning("Your Maize Sample is Infected with Common rust! Please take action immediately!")
        elif pred == 2:
            st.warning("Your Maize Sample is Infected with Gray Leaf Spot! Please take action immediately!")
        elif pred == 3:
            st.success("Your Maize Sample is Healthy! ")
        return pred
        

def contact():
    st.sidebar.title("Contact")
    st.sidebar.info("Email: mugenzik@gmail.com")
    st.sidebar.info("Phone: +250780587387")


#the navbar function
def contact_navbar():
    st.sidebar.title("Contact")
    st.sidebar.info("Email: mugenzik@gmail.com")
    st.sidebar.success("Phone: +250780587387")
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
