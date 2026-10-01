"""Streamlit chat app for the HR Policy Assistant.

Run with: streamlit run app.py
"""

import streamlit as st

from hr_assistant.logger import get_logger
from hr_assistant.pipeline import ask, build_hr_assistant

logger = get_logger(__name__)

st.set_page_config(
    page_title="CognivexaAI HR Policy Assistant",
    page_icon="🤖"
)

st.title("🤖 CognivexaAI HR Policy Assistant")
st.caption(
    "Ask questions about the CognivexaAI Solutions Pvt. Ltd. HR Policy."
)

@st.cache_resource(show_spinner="Setting up the assistant...")
def get_agent():
    return build_hr_assistant()


agent = get_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept a new question
question = st.chat_input("Ask a question about HR policy...")

if question:
    logger.info("New HR policy question received")

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching the HR policy..."):
            try:
                answer = ask(agent, question)
            except Exception:
                logger.exception("Failed to answer HR policy question")
                answer = (
                    "Sorry, I could not process your question right now. "
                    "Please try again."
                )

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
