import streamlit as st
from openai import OpenAI
from enquiry import enquire

# Show title and description.
st.title("💬 BCA Project ..🎈")
st.write( "This is a Agentic Help Tool for Submissins to BCA..")

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
#openai_api_key = st.text_input("OpenAI API Key", type="password")
openai_api_key = st.secrets["openai"]["secret_key"]
client = OpenAI(api_key=openai_api_key)



if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    enquire(client)
    
