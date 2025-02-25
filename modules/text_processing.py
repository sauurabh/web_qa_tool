import re

def split_text_into_chunks(text, max_length=500):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def preprocess_text_for_rag(extracted_texts):
    preprocessed_data = {}
    for url, text in extracted_texts.items():
        chunks = split_text_into_chunks(text)
        preprocessed_data[url] = chunks
    return preprocessed_data
