# Web Content Q&A Tool (RAG-based)

## Overview
This is a **Web-based Q&A Tool** that allows users to ask questions based on extracted content from URLs. The tool leverages:
- **BeautifulSoup** for web scraping
- **FAISS** for semantic search and retrieval
- **Sentence Transformers** for text embeddings
- **OpenAI GPT-3.5 Turbo** for generating answers
- **Streamlit** for the user-friendly web interface

## Features
✅ Extracts textual content from multiple URLs
✅ Splits text into chunks for efficient retrieval
✅ Creates an FAISS index for fast similarity search
✅ Retrieves relevant content based on user queries
✅ Uses OpenAI's GPT-3.5 Turbo to generate answers
✅ Displays relevant content chunks for transparency
✅ User-friendly UI with Streamlit

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/your-username/web-qa-tool.git
cd web-qa-tool
pip install -r requirements.txt
```

## Environment Variables
Create a `.env` file and add your **OpenAI API Key**:
```
OPENAI_API_KEY=your_openai_api_key
```

## Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

### Steps to Use:
1. Enter URLs (one per line) in the input field.
2. Click **Process URLs** to extract and index content.
3. Ask questions in the chat interface.
4. View generated answers along with relevant content chunks.

## Project Structure
```
web_qa_tool/
│── main.py                # Streamlit UI (entry point)
│── config.py              # Configuration (e.g., API keys)
│── requirements.txt       # Dependencies
│
├── modules/               # Folder for modularized functionalities
│   │── text_extraction.py # Functions to extract text from URLs
│   │── text_processing.py # Text splitting and preprocessing functions
│   │── faiss_indexing.py  # FAISS index creation and retrieval
│   │── openai_helper.py   # OpenAI API interaction
```

## API & Libraries Used
- **BeautifulSoup** for extracting web content
- **Sentence Transformers (`all-MiniLM-L6-v2`)** for embeddings
- **FAISS** for fast similarity search
- **OpenAI GPT-3.5 Turbo** for answer generation
- **Streamlit** for UI

## Future Enhancements
🔹 Currently processing a single page from a URL, but we can extend it to process an entire website
🔹 Improved chunking strategy for better context retrieval
🔹 Option to upload documents (PDF, DOCX) for Q&A

