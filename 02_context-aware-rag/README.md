Context-Aware RAG PDF Assistant

A context-aware Retrieval-Augmented Generation (RAG) system that intelligently processes retrieved context before sending it to an LLM, improving answer relevance and reducing hallucinations.

This project demonstrates practical context engineering techniques such as filtering, ranking, token optimization, and summarization.

🎯 Project Goal

Most RAG systems simply retrieve chunks and send them to the LLM.

This project focuses on:

Optimizing context before generation

to improve accuracy, efficiency, and reliability.
Features

✅ PDF document ingestion
✅ Smart chunking with overlap
✅ Embedding-based semantic search
✅ Vector database retrieval (ChromaDB)
✅ Context filtering
✅ Relevance ranking
✅ Token budgeting
✅ Context summarization
✅ Hallucination reduction prompt strategy

PDF → Chunking → Embeddings → Vector DB
                              ↓
User Query → Retrieval
                              ↓
Filtering → Ranking → Token Control → Summarization
                              ↓
LLM → Final Answer

Why This Project Matters

Many RAG demos stop at retrieval.

This project goes further by implementing context processing pipelines, which are critical in production-grade RAG systems.

It shows understanding of:

Context engineering

LLM limitations

Token efficiency

Hallucination mitigation

Retrieval optimization

🛠️ Tech Stack

Python

LangChain

OpenAI API

ChromaDB

PyPDF

dotenv

⚙️ Installation
1️⃣ Clone the repo
git clone https://github.com/yourusername/context-aware-rag.git
cd context-aware-rag

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set API key

Create .env file:

OPENAI_API_KEY=your_api_key_here

4️⃣ Add PDF

Place your PDF in:

data/sample.pdf

5️⃣ Run
python app.py

💡 Example Use Cases

Research paper Q&A

Study assistant

Document analysis

Contract review

Knowledge base assistant

📈 Future Improvements

Source citation

Cross-encoder reranking

Multi-query retrieval

Web UI (Streamlit/Gradio)

Persistent vector storage

Memory-aware conversations

🧑‍💻 Author

Oğulcan Narin
Software Engineering Student 

