import streamlit as st
from openai import OpenAI

def enquire(client):
    # Create an OpenAI client.
    # Define the context
    context = "BCA Building Regulation and BCA Submission Requirements"

    st.write( "Here the Companies can make any Generic Enquiry about the BCA Submission requirement. ")

    st.write(
    "Click the link below to get the full information on BCA Submission requirements.\n"
    "Clicking on the link will redirect you to the BCA website, and this app will be closed.")

    # Create the clickable link
    st.markdown(
        "[BCA Submission Requirements](https://www1.bca.gov.sg/regulatory-info/building-control/corenet-x)",
        unsafe_allow_html=True)

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
