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

# Create radio buttons in a single row
options = st.radio("Navigate", ["About", "Enquire", "Require", "Agent", "Ack"], horizontal=True)

# Define functions for "About", "Require", and "Agent"
def about():
    st.write("About BCA Project")

def require():
    st.write("Requiremets Section")

def agent():
    st.write("Agentic will Analize your submission")

def ack():
    st.write("Acknoledgements Section")

# Check radio button selection
if options == "About":
    about()
elif options == "Require":
    require()
elif options == "Agent":
    agent()
elif options == "Enquire":
    enquire(client)
elif options == "Ack":
    ack()
else:
    st.write( "Waiting for you to test my APP")
   


if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")

    
    
