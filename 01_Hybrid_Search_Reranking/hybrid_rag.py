import os
from dotenv import load_dotenv

# --- GÜVENLİK ---
# .env dosyasını yüklüyoruz
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("⚠️ API Key bulunamadı! Lütfen .env dosyasını kontrol et.")
os.environ["OPENAI_API_KEY"] = api_key

# --- KÜTÜPHANELER ---
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder

# --- 1. VERİ HAZIRLIĞI (Zorlu Senaryo) ---
# Vektörün tek başına zorlanacağı, içinde özel kodlar olan bir metin.
raw_text = """
Gizli Proje: 'Project Chimera'. Kod adı: X-99.
Bu proje, insan zihnini dijital ortama aktarmayı hedefler.
X-99 sunucuları sadece Antarktika'daki 'Buzul Kalesi'nde bulunur.
Sisteme giriş şifresi 'Mavi_Ufuk_2042'dir.
Eğer sistem aşırı ısınırsa, acil durum protokolü 'Protokol Omega' devreye girer.
Protokol Omega, tüm verileri siler ve tesisi kilitler.
Yetkili personel dışında kimse 'Bölge 51-B'ye giremez.
"""

print(f"📄 Metin uzunluğu: {len(raw_text)} karakter")

# Chunking (Parçalama)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
docs = text_splitter.create_documents([raw_text])
print(f"🧩 Toplam Parça Sayısı: {len(docs)}")

# --- 2. HİBRİT ARAMA MOTORLARINI KURMA ---

# A) Vektör Veritabanı (Anlamsal Arama)
print("⚙️  Vektör veritabanı kuruluyor...")
embeddings = OpenAIEmbeddings()
vector_db = Chroma.from_documents(docs, embeddings)

# B) BM25 (Kelime Bazlı Arama)
# BM25 metni kelime kelime ayırmamızı ister (Tokenization)
print("⚙️  BM25 motoru kuruluyor...")
tokenized_corpus = [doc.page_content.lower().split(" ") for doc in docs]
bm25 = BM25Okapi(tokenized_corpus)

# C) Reranker (Yeniden Sıralayıcı) - Cross Encoder
# Bu model soruyu ve cevabı YANYANA okuyup puan verir.
print("⏳ Reranker modeli indiriliyor (Bu ilk seferde biraz sürebilir)...")
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2') 
print("✅ Tüm sistemler hazır!\n")

# --- 3. ANA FONKSİYON: HYBRID SEARCH + RERANKING ---
def search_system(query):
    print(f"🔎 SORU: '{query}'")
    
    # ADIM 1: Geniş Arama (Recall) - Hem Vektör hem Kelime ile çok sayıda sonuç getir
    # Vektörden 3 tane al
    vector_results = vector_db.similarity_search(query, k=3)
    
    # BM25'ten 3 tane al
    tokenized_query = query.lower().split(" ")
    bm25_results = bm25.get_top_n(tokenized_query, docs, n=3)
    
    # Listeleri birleştir ve kopyaları temizle (Deduplication)
    combined_docs = []
    seen_contents = set()
    
    for doc in vector_results + bm25_results:
        if doc.page_content not in seen_contents:
            combined_docs.append(doc)
            seen_contents.add(doc.page_content)
            
    print(f"   🔹 İlk Havuz (Vektör + BM25): {len(combined_docs)} döküman bulundu.")

    # ADIM 2: Reranking (Precision) - Cross Encoder ile Puanlama
    # Modele şöyle soruyoruz: [Soru, Metin] ikilisi ne kadar alakalı?
    pairs = [[query, doc.page_content] for doc in combined_docs]
    scores = reranker.predict(pairs)
    
    # Skorları dökümanlarla eşleştirip sıralayalım (En yüksek puan en üste)
    ranked_results = sorted(zip(combined_docs, scores), key=lambda x: x[1], reverse=True)
    
    print("   🔹 Reranking Sonuçları:")
    for i, (doc, score) in enumerate(ranked_results):
        print(f"      {i+1}. Skor: {score:.4f} | Metin: {doc.page_content[:50]}...")
        
    # En iyi sonucu döndür
    return ranked_results[0][0]

# --- 4. TEST ZAMANI ---

# Test 1: Anlamsal Soru (Vektör bunu sever)
best_doc = search_system("İnsan zihnini bilgisayara aktarma projesi nerede?")

# Test 2: Kod Adı Sorusu (BM25 bunu sever, Vektör bazen kaçırır)
best_doc_2 = search_system("X-99 şifresi nedir?")

# --- 5. GENERATION (Cevap Üretme) ---
print("\n🤖 LLM Cevap Üretiyor...")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

final_prompt = f"""
Bağlam bilgisini kullanarak soruyu cevapla:
Bağlam: {best_doc_2.page_content}
Soru: X-99 şifresi nedir?
"""
response = llm.invoke(final_prompt)
print(f"🏁 SONUÇ: {response.content}")