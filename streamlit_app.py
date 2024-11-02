import streamlit as st
from openai import OpenAI
from enquiry import enquire
from about import about

# Show title and description.
st.title("💬 BCA Project ..🎈")
st.write( "This is the solution for AI Champions Bootcamp 2024.")
st.write( "Agent-based Analyzer for Technical and Regulatory Requirements Checks")

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
#openai_api_key = st.text_input("OpenAI API Key", type="password")
openai_api_key = st.secrets["openai"]["secret_key"]
client = OpenAI(api_key=openai_api_key)

# Create radio buttons in a single row
options = st.radio("Navigate", ["About", "Enquire", "Require", "Agent", "Ack"], horizontal=True)

# Define functions for "About", "Require", and "Agent"
#def about():
#    st.write("**About BCA Project**")

def require():
    st.write("**Requirements Section**")
    st.write("This part allows BCA officers to drag and drop the latest revision in submission requirements.")
    st.write("The enquiry page will enhance its response based on the new set of information provided.")
def agent():
    st.write("**Agents** for Submissions Checking are AI enabled...")
    st.write("Companies can drag & drop their submissions here.")
    st.write("Integrated AI agents will perform the checking...")
    st.write("A report on compliance and deviations will be generated...")
    st.write("Use case for building windows is provided separately...")
    

def ack():
    st.write("""
            **Acknowledgment**
            
            We would like to express our deepest gratitude to Nick Tan from GovTech, who was the guiding force and guru behind the successful completion of our LLM Project. 
            Without his committed guidance and unwavering support, this journey would not have been possible.
            
            Nick Tan not only taught us the intricacies of data embedding but also inspired us to immerse ourselves fully in this field. 
            His expertise, patience, and encouragement kept us motivated and on the right path throughout this project. 
            His passion for knowledge and his dedication to sharing it have left an indelible mark on our learning experience.
            
            Thank you, Nick Tan, for your invaluable contributions and for being such an exceptional mentor. 
            This success is a testament to your dedication, and we are truly grateful to have had the privilege of learning under your guidance.
            """)

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

    
    
