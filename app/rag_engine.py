import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from openai import OpenAI
from sentence_transformers import SentenceTransformer, util

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(file)->str:
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def chunk_text(text:str, chunk_size: int=500)->list:
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def embed_chunks(chunks: list)->list:
    return embedding_model.encode(chunks, convert_to_tensor=True)

def retrieve_relevant_chunk(chunks:list, embeddings, query:str) ->str:
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    scores=util.cos_sim(query_embedding, embeddings)[0]
    best_idx = scores.argmax().item()
    return chunks[best_idx]

def generate_answer(context: str, question: str)->str:
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

async def process_query(file, question: str) -> str:
    text = extract_text_from_pdf(file)
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    context = retrieve_relevant_chunk(chunks, embeddings, question)
    answer = generate_answer(context, question)
    return answer
