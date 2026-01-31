import streamlit as st
import time

# Set page title and icon
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")

st.balloons() # This creates an immediate balloon animation

st.title("💖 A Special Message for You")

# A "Click Me" button to reveal the message
if st.button("Click to Open Your Card"):
    with st.spinner("Opening..."):
        time.sleep(1) # Adds a little suspense
    
    st.header("Happy Birthday! 🎂")
    st.write("""
    Bangruu, you are the best! Eppudu ilane gola chestu happy happy ga vundu. 
    I promise i will be more patient with you this year.
    I love you so much, Harika Ammaaaa hahaha!
    """)
    
    # You can even add an image if you have a URL for one
    # st.image("https://example.com/your-photo.jpg")
    
    st.snow() # Another fun animation