import streamlit as st
from chatbot.conversation import get_chatbot

st.set_page_config(page_title="Cricket Chatbot", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Information Chatbot")
st.write("Hello! I can answer anything about cricket — players, matches, teams, records, and rules.")

# Initialize chatbot in session state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = get_chatbot()
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Ask me anything about cricket..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from chatbot
    response = st.session_state.chatbot.predict(input=prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
