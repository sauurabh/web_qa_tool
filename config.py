import os
from dotenv import load_dotenv
import streamlit as st

# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")
API_KEY = st.secrets["OPENAI_API_KEY"]
