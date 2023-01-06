import streamlit as st 




def home():
    st.title("Ahabanza")

def demo():
    st.title("Gerageza Ikoranabuhanga ryacu!")
    img = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'])

def contact():
    st.sidebar.title("Contact")
    st.sidebar.info("Email: mugenzik@gmail.com")
    st.sidebar.info("Phone: +250780587387")


#the navbar function
def navbar():
    st.sidebar.title("Menu")
    global mode
    home_button = st.sidebar.button("Ahabanza", on_click=home)
    demo_button = st.sidebar.button("Gerageza Ikoranabuhanga ryacu!", on_click=demo)

    #contact banner
    contact()


#the main function
def main():
    navbar() #call the navbar function
    



if __name__ == "__main__":
    main()