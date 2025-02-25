import requests
from bs4 import BeautifulSoup
import streamlit as st

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ')
        cleaned_text = ' '.join(text.split())
        return cleaned_text
    except Exception as e:
        st.error(f"Error extracting text from {url}: {e}")
        return None

def extract_text_from_urls(urls):
    extracted_texts = {}
    for url in urls:
        text = extract_text_from_url(url)
        if text:
            extracted_texts[url] = text
    return extracted_texts
