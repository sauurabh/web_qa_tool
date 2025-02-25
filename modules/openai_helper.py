from openai import OpenAI
from config import API_KEY

client = OpenAI(api_key=API_KEY)

def generate_answer_with_openai(query, relevant_chunks):
    context = "\n".join(relevant_chunks)

    prompt = f"""
    You are an AI assistant that answers questions based on the provided context.
    
    - If the context contains relevant information, generate a well-structured answer.
    - If the query asks for a summary and context exists, summarize the key points clearly from context.
    - If the context does not contain enough relevant information, respond with:
      "I'm sorry, but I couldn't find relevant information based on the provided content."

    Context:
    {context}

    Question: {query}
    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that provides answers based on context."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.2
    )
    
    return response.choices[0].message.content.strip()



