from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama


BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
KNOWLEDGE_FILE = BASE_DIR / "knowledge.txt"


app = FastAPI(title="AI Bootcamp RAG Exercise")


# ---------------------------------------------------------
# LOAD THE KNOWLEDGE BASE
# ---------------------------------------------------------

with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as file:
    knowledge_lines = [
        line.strip()
        for line in file.readlines()
        if line.strip()
    ]


documents = [
    Document(page_content=line)
    for line in knowledge_lines
]


# ---------------------------------------------------------
# LLM + PROMPT
# ---------------------------------------------------------

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


prompt = ChatPromptTemplate.from_template(
    """
You are an assistant for the AI Development Bootcamp.

Answer the question using only the context below.

If the answer is not in the context, say:
"I don't have enough information in the knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""
)


# ---------------------------------------------------------
# REQUEST MODEL
# ---------------------------------------------------------

class QuestionRequest(BaseModel):
    question: str


# ---------------------------------------------------------
# RAG FUNCTION
# ---------------------------------------------------------

def create_retriever():

    # TODO 1:
    # Create Ollama embeddings using:
    
        
    # model="nomic-embed-text"

    embeddings = None


    # TODO 2:
    # Create a FAISS vector store

    vector_store = None


    if vector_store is None:
        return None

    return vector_store.as_retriever(
        search_kwargs={"k": 3}
    )


# ---------------------------------------------------------
# API
# ---------------------------------------------------------

@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/ask")
def ask_question(data: QuestionRequest):

    if not data.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )


    retriever = create_retriever()

    if retriever is None:
        raise HTTPException(
            status_code=500,
            detail="Complete TODO 1 and TODO 2 in app.py"
        )


    # TODO 3:
    # 1. Retrieve relevant documents for data.question
    # 2. Combine their page_content into "context"
    # 3. Format the prompt
    # 4. Send it to the LLM
    # 5. Store the final text in "answer"

    context = ""
    answer = "TODO"


    return {
        "question": data.question,
        "answer": answer,
        "context": context
    }


# ---------------------------------------------------------
# FRONTEND
# ---------------------------------------------------------

# Keep this mount LAST so /api routes work first.
app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR, html=True),
    name="frontend"
)


# ---------------------------------------------------------
# RUN
# ---------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    print()
    print("AI RAG Interview App")
    print("Open: http://127.0.0.1:8000")
    print()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
