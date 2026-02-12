# 🧠 Context Management RAG Demo

Bu proje, **Context Engineering** kavramlarını uygulamalı olarak göstermek için geliştirilmiş mini bir RAG (Retrieval-Augmented Generation) demosudur.

Amaç, klasik RAG sistemlerinin ötesine geçerek:

- Multi-Query Retrieval
- HyDE (Hypothetical Document Embeddings)
- Akıllı context işleme

gibi teknikleri pratikte uygulamaktır.

---

# 🚀 Özellikler

## ✅ Multi-Query Retrieval
Kullanıcı sorusu LLM tarafından farklı varyasyonlara çevrilir ve her biri için arama yapılır.

👉 Amaç: Retrieval kalitesini artırmak  
👉 Sonuç: Daha doğru doküman eşleşmesi

---

## ✅ HyDE (Hypothetical Document Embeddings)
LLM, soruya hayali bir cevap üretir.  
Bu cevap embedding’e dönüştürülüp arama yapılır.

👉 Amaç: Anlamsal benzerliği artırmak  
👉 Sonuç: Daha doğru bilgiye ulaşma

---

## ✅ Vector Database (ChromaDB)
Dokümanlar embedding’e dönüştürülerek vektör veritabanında saklanır.

👉 Semantic search yapılır  
👉 Keyword matching’e bağlı kalmaz

---

## ✅ Context Processing
Chunking + embedding pipeline ile context optimize edilir.

---

# 🛠️ Kullanılan Teknolojiler

- Python
- LangChain
- OpenAI Embeddings
- ChatOpenAI
- ChromaDB
- dotenv

