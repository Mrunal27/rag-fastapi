# 🔍 RAG Pipeline API with FastAPI & Docker

This project wraps a Retrieval-Augmented Generation (RAG) pipeline in a FastAPI service. Upload a PDF, ask a question, and receive a context-aware answer powered by OpenAI.

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Mrunal27/rag-fastapi.git
cd rag-fastapi

2. Create .env file
touch .env

3. Add your OpenAI API key:
OPENAI_API_KEY = ""

3. Build and Run with Docker
docker build -t rag-api .
docker run -p 8000:8000 rag-api

4. Access Swagger UI
Visit http://localhost:8000/docs

5. Test the API
• 	Upload a PDF
• 	Ask a question
• 	Receive a context-aware answer

🧰 Tech Stack
• 	FastAPI · Docker · Python · OpenAI API · Sentence Transformers · PyPDF2


#RetrievalAugmentedGeneration #GenerativeAI #BackendEngineering #MLPlatform #OpenAI #Docker #PythonDev #CareerPivot #ReliableSystems #OpenToWork