import os
from dotenv import load_dotenv

# Güvenlik Kontrolü
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("⚠️ API Key bulunamadı! .env dosyasını kontrol et.")

# ---- GÜNCEL IMPORTLAR ----
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --- 1. VERİ SETİ ---
raw_text = """
Buzul Kalesi Güvenlik Raporu:
Tesisin ana güç kaynağı 'Zero-Point Energy' (ZPE) modülüdür.
ZPE modülü aşırı ısınırsa, sistem otomatik olarak 'Kızıl Kış' (Red Winter) protokolünü başlatır.
Kızıl Kış protokolü, tüm kapıları kilitler ve oksijen seviyesini %15'e düşürür.
Bu protokolü sadece 'Yönetici Omega' yetki koduyla iptal edebilirsiniz.
İptal şifresi her gün değişir, bugünün şifresi: 'Aurora-77'.
"""

print("⚙️ Veritabanı hazırlanıyor...")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30
)

docs = text_splitter.create_documents([raw_text])

embeddings = OpenAIEmbeddings()
vector_db = Chroma.from_documents(docs, embeddings)

# LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# --- 2. MULTI QUERY ---
print("\n--- TEKNİK 1: MULTI-QUERY ---")

multi_query_prompt = PromptTemplate.from_template("""
Sen bir yapay zeka asistanısın.

Görevin kullanıcı sorusunu vektör araması için 3 farklı şekilde yeniden yazmak.

Sadece 3 soru üret.
Açıklama yapma.

Soru: {question}
""")

generate_queries_chain = (
    multi_query_prompt
    | llm
    | StrOutputParser()
    | (lambda x: x.split("\n"))
)

user_question = "Sistem ısınırsa ne olur?"
print(f"👤 Kullanıcı Sorusu: {user_question}")

generated_queries = generate_queries_chain.invoke(
    {"question": user_question}
)

print("\n🤖 Alternatif Sorular:")
for i, q in enumerate(generated_queries):
    print(f"{i+1}. {q}")

retrieved_docs = vector_db.similarity_search(
    generated_queries[0],
    k=1
)

print("\n🔎 Bulunan Metin:")
print(retrieved_docs[0].page_content)

# --- 3. HYDE ---
print("\n--- TEKNİK 2: HyDE ---")

hyde_prompt = PromptTemplate.from_template("""
Soruyu cevaplayan kısa hayali bir paragraf yaz.

Soru: {question}
""")

hyde_chain = hyde_prompt | llm | StrOutputParser()

bad_question = "İptal şifresi ne?"
print(f"\n👤 Kullanıcı Sorusu: {bad_question}")

hypothetical_answer = hyde_chain.invoke(
    {"question": bad_question}
)

print("\n👻 Hayali Cevap:")
print(hypothetical_answer)

hyde_docs = vector_db.similarity_search(
    hypothetical_answer,
    k=1
)

print("\n✅ Gerçek Metin:")
print(hyde_docs[0].page_content)
