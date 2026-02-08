import os
from dotenv import find_dotenv, load_dotenv

env_path = find_dotenv()
load_dotenv(env_path)

api_key = os.getenv("API_KEY")


def query(user_querry):
    

    from google import genai

    my_ai = genai.Client(api_key=api_key)

    response = my_ai.models.generate_content(
        model="gemini-3-flash-preview", contents=user_querry
    )

    return response.text


import streamlit as st

st.title("Omnix AI")
st.text("Welcome to Omnix AI! Ask me anything and I'll do my best to assist you.")
try:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for i in st.session_state.messages:
        with st.chat_message(i["role"]):
            st.markdown(i["msg"])


    user_input = st.chat_input("Enter your question:")

    if user_input:
        st.session_state.messages.append({"role": "user", "msg": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("Omnix"):
            with st.spinner("Generating response..."):
                result = query(user_input)
                st.markdown(result)
        st.session_state.messages.append({"role": "Omnix", "msg": result})

except Exception as e:
    st.error(f"An error occurred: {e}")

