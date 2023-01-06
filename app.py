import streamlit as st 






def demo():
    st.title("Gerageza Ikoranabuhanga ryacu!")
    upload_col, capture_col = st.columns(2)
    
    img = st.file_uploader("Uploading ifoto y' igihingwa cyawe aha!", type=['png', 'jpg', 'jpeg'])
    if img is not None:
        st.image(img, caption="Ifoto y' igihingwa cyawe", use_column_width=True)

    img = st.camera_input("Capture ifoto y' igihingwa cyawe aha!")
    if img is not None:
        st.image(img, caption="Ifoto y' igihingwa cyawe", use_column_width=True)


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
    main()