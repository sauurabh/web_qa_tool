import streamlit as st
from modules.text_extraction import extract_text_from_urls
from modules.text_processing import preprocess_text_for_rag
from modules.faiss_indexing import create_faiss_index, retrieve_relevant_chunks
from modules.openai_helper import generate_answer_with_openai

# Streamlit UI
st.title("Web Content Q&A Tool (RAG Application)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

urls = st.text_area("Enter URLs (one per line)", height=100)
urls = [url.strip() for url in urls.split("\n") if url.strip()]

if st.button("Process URLs"):
    if urls:
        with st.spinner("Extracting and processing content..."):
            extracted_texts = extract_text_from_urls(urls)
            if extracted_texts:
                preprocessed_data = preprocess_text_for_rag(extracted_texts)
                all_chunks = [chunk for chunks in preprocessed_data.values() for chunk in chunks]
                
                index, chunks = create_faiss_index(all_chunks)
                
                st.session_state.preprocessed_data = preprocessed_data
                st.session_state.faiss_index = index
                st.session_state.chunks = chunks
                st.success("URLs processed and indexed successfully!")
            else:
                st.error("No text could be extracted from the provided URLs.")
    else:
        st.error("Please enter at least one valid URL.")

if 'preprocessed_data' in st.session_state:
    st.subheader("Chat")

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    query = st.chat_input("Ask a question based on the content...")

    if query:
        st.session_state.chat_history.append({"role": "user", "content": query})

        with st.spinner("Searching for relevant information..."):
            relevant_chunks = retrieve_relevant_chunks(st.session_state.faiss_index, st.session_state.chunks, query, top_k=3)
            answer = generate_answer_with_openai(query, relevant_chunks)
            
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

            with st.chat_message("user"):
                st.write(query)
            with st.chat_message("assistant"):
                st.write(answer)

            with st.expander("Relevant Chunks"):
                for i, chunk in enumerate(relevant_chunks):
                    st.write(f"**Chunk {i+1}:** {chunk[:200]}...")
