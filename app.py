import streamlit as st

st.title("👕 Clothing Shop Chatbot")

user_input = st.text_input("Ask something:")

if user_input:
    if "shirt" in user_input.lower():
        st.write("We have shirts. Price: 500 BDT")
    elif "pant" in user_input.lower():
        st.write("We have pants. Price: 800 BDT")
    elif "order" in user_input.lower():
        st.write("Order confirmed! We will contact you.")
    else:
        st.write("Please ask about products or order.")
