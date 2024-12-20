"""
File: stremlit_app.py
AI Champions Bootcamp 2024
BCA Project
Agent-Based Analyzer for Technical and Regulatory Requirements Checks

Authors: Unni & Woon Wei (BCA)
Date Created: 2024-10-01
Last Updated: 2024-11-03
Version: 1.2

Functions:
- __main(): This is the main function from where the various pages are slected using a Radio-button Selector.
            The client variable is created here once at the start and it is passed to other modules as a parameter.

Notes:
- Assumption: This Page is created from Streamlit Example and modified to our needs
            The OpenAI Scret Key is hiddedn in the Scret Vault of Streamlit.
            Therefore, any user geting the link can straight away use the App
            Payment to OpenAI for usage is done by Unni.
            
- Example: The Title and Project Name stays in the display all the while using this APP
            The lower part display is updated based on the Radio Button Selection
            ["About", "Enquire", "Require", "Agent", "Ack"]
            
"""


import streamlit as st
from openai import OpenAI
from enquiry import enquire
from Update_Requirements import UpdateRequirements
#from about import about

# Show title and description.
st.title(" 🎈**BCA Project**")
# Use HTML and CSS to adjust spacing between emojis
st.markdown(
    """
    <h1 style="letter-spacing: -0.2em;">🧱🧱🧱🧱🧱🧱🧱🧱</h1>
    """,
    unsafe_allow_html=True
)
st.write( "AI Champions Bootcamp 2024..")
st.write( "**Agent-based Analyzer for Technical and Regulatory Requirements Checks**")

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
    #st.write("**About BCA Project**")
    show_popup1 = st.checkbox("GPT Model Used")
    model= "gpt-4o-mini"
    if show_popup1:
        st.code(f" GPT API Model used is =\n{model}", language="text")
    st.markdown('[**About the Project**](https://sway.cloud.microsoft/vQFtLnQTDaYLqiAM?ref=Link)')

def require(): #Now Not in Use as new module is added
    st.write("**Requirements Section**")
    st.markdown('[BCA Submission Requirements](https://www1.bca.gov.sg/regulatory-info/building-control/building-plan-submission)')
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
    UpdateRequirements(client)
    #require()
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

    
    
