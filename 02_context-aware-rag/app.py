from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain_openai import OpenAIEmbeddings, ChatOpenAI

load_dotenv()

# -----------------------------
# PDF YÜKLEME
# -----------------------------
loader = PyPDFLoader("data/sample.pdf")
documents = loader.load()

# -----------------------------
# CHUNKING
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# -----------------------------
# EMBEDDING + DB
# -----------------------------
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings)

# -----------------------------
# MODEL
# -----------------------------
llm = ChatOpenAI(model="gpt-4o-mini")


# =============================
# CONTEXT PROCESSING
# =============================

# 1️⃣ FILTERING
def filter_docs(docs, min_length=80):
    return [d for d in docs if len(d.page_content) > min_length]


# 2️⃣ TOKEN LIMIT
def limit_tokens(docs, max_chars=2000):
    total = 0
    selected = []

    for d in docs:
        total += len(d.page_content)
        if total <= max_chars:
            selected.append(d)
        else:
            break

    return selected


# 3️⃣ SUMMARIZATION
def summarize_docs(docs, llm):
    summaries = []

    for d in docs:
        prompt = f"""
Aşağıdaki metni kısa ve öz şekilde özetle.
Önemli bilgileri koru.

Metin:
{d.page_content}
"""
        res = llm.invoke(prompt)
        summaries.append(res.content)

    return summaries


# =============================
# QA LOOP
# =============================
while True:
    question = input("\nSoru sor: ")

    # Retrieval + score
    results = db.similarity_search_with_score(question, k=5)

    # RANKING
    results = sorted(results, key=lambda x: x[1])
    docs_ranked = [r[0] for r in results]

    # FILTERING
    docs_filtered = filter_docs(docs_ranked)

    # TOKEN LIMIT
    final_docs = limit_tokens(docs_filtered)

    # SUMMARIZATION
    summaries = summarize_docs(final_docs, llm)

    context = "\n\n".join(summaries)

    prompt = f"""
Sadece aşağıdaki context'i kullanarak cevap ver.
Eğer cevap context'te yoksa "Bilmiyorum" de.

Context:
{context}

Soru:
{question}
"""

    response = llm.invoke(prompt)

    print("\nCevap:", response.content)
