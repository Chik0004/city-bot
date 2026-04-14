import streamlit as st
from router import generate_response

st.set_page_config(page_title="City Assistant", page_icon="🏙️")

st.title("🏙️ City Assistant")
#st.image("Logo.png", width=50)
#st.title("City Assistant")
"""col1, col2 = st.columns([1, 6])

with col1:
    st.image("logo.png", width=40)

with col2:
    st.markdown("## City Assistant")"""
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate bot response
    responses = generate_response(user_input)

    # Combine into single clean message
    bot_reply = "\n\n".join(responses)

    # Show bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
