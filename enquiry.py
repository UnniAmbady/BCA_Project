"""
File: enquiry.py
AI Champions Bootcamp 2024
BCA Project
Agent-Based Analyzer for Technical and Regulatory Requirements Checks

Authors: Unni & Woon Wei (BCA)
Date Created: 2024-10-01
Last Updated: 2024-11-03
Version: 1.2

Functions:
- enquire(): User input is augmented with a context setting to BCA Requlatory and passed to GPT. 
            Reponses are returned to user without checking.

Notes:
- Assumption: This app is for testing purposes only, So response content checking is not very important at this stage of POC.
- Example: User input : Velocity of Wind; the respose will be ......In Singapore, building designs must account for wind loads 
            as specified in the Singapore Standard SS EN 1991-1-4: Eurocode 1—Actions on Structures.
            This ability is achived through paraphrasing the user input with context setting.
"""


import streamlit as st
from openai import OpenAI

def enquire(client):
    # Create an OpenAI client.
    # Define the context
    context = "Building and Construction Authority (BCA), Singapore Building Regulations, and BCA Submission Requirements."

    st.write("Here, companies can make any general enquiry about BCA submission requirements.")
    st.write("Type a keyword related to buildings...")
    st.write("Examples: ZEB, piling, Green Mark, ventilation, etc.")

    # Create the clickable link
    #st.markdown(
    #    "[BCA Submission Requirements](https://www1.bca.gov.sg/regulatory-info/building-control/corenet-x)",
    #    unsafe_allow_html=True)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": context + prompt}) #UNNI 1Nov
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model= "gpt-4o-mini",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
#end of function definision
