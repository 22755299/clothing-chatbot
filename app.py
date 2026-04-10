import streamlit as st

products = {
    "tshirt": {
        "name": "Cool T-Shirt",
        "price": 500,
        "description": "100% cotton"
    }
}

def chatbot(user_input):
    user_input = user_input.lower()

    if "tshirt" in user_input:
        p = products["tshirt"]
        return f"{p['name']} | {p['price']}৳"

    elif "order" in user_input:
        return "Order 👉 https://wa.me/8801XXXXXXXXX"

    else:
        return "Sorry 😅"

st.title("🛍️ Clothing Shop Bot")

user = st.text_input("Ask something:")

if user:
    response = chatbot(user)
    st.write(response)
