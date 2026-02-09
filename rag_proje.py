import os
from dotenv import load_dotenv # Yeni eklediğimiz kütüphane

# 1. Önce .env dosyasını yükle
load_dotenv() 

# 2. Artık anahtarı güvenli şekilde alabilirsin
api_key = os.getenv("OPENAI_API_KEY")

# Kontrol (Opsiyonel): Eğer anahtar yoksa hata versin
if not api_key:
    raise ValueError("API Key bulunamadı! Lütfen .env dosyasını kontrol et.")

# LangChain otomatik olarak 'OPENAI_API_KEY' ortam değişkenini arar, 
# ama biz yine de emin olmak için tanımlayalım.
os.environ["OPENAI_API_KEY"] = api_key

# Gerekli kütüphaneler
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

# --- ADIM 1: VERİ HAZIRLIĞI (Yapay Zekanın Bilmediği Bilgi) ---
# Normalde bu bir PDF veya TXT dosyası olabilir. Biz burada string olarak tanımlıyoruz.
raw_text = """
Mars'taki Zog Kolonisi, 2042 yılında Elon Musk'ın gizli kardeşi 'Zelon Musk' tarafından kuruldu.
Zog Kolonisi'nde para kullanılmaz, bunun yerine 'Kırmızı Taş' adı verilen kristaller takas edilir.
Koloninin en ünlü yemeği 'Tozlu Solucan Çorbası'dır.
Kolonide uyumak yasaktır, insanlar günde 20 dakika meditasyon yaparak dinlenirler.
Eğer biri uyurken yakalanırsa, ceza olarak Dünya'ya geri gönderilir.
"""

print(f"1. Ham metin uzunluğu: {len(raw_text)} karakter")

# --- ADIM 2: CHUNKING (Parçalama) ---
# Metni küçük parçalara bölüyoruz ki vektör veritabanı yutabilsin.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,    # Her parça en fazla 100 karakter olsun
    chunk_overlap=20   # Her parça bir öncekiyle 20 karakter örtüşsün (Bağlam kopmasın)
)

# Metni dökümanlara dönüştür
docs = text_splitter.create_documents([raw_text])

print(f"2. Chunking yapıldı. Toplam parça sayısı: {len(docs)}")
print(f"   Örnek Parça: '{docs[0].page_content}'")

# --- ADIM 3: EMBEDDING & VECTOR DB (Vektörleştirme ve Kayıt) ---
# Metinleri sayılara (vektörlere) çevirip ChromaDB'ye (Geçici Hafıza) kaydediyoruz.
embeddings = OpenAIEmbeddings() # Bu model metni vektöre çevirir

# Veritabanını oluştur ve verileri göm
db = Chroma.from_documents(
    documents=docs, 
    embedding=embeddings
)
print("3. Veriler vektörleştirildi ve ChromaDB'ye kaydedildi.")

# --- ADIM 4: SEMANTIC SEARCH (Anlamsal Arama) ---
query = "Kolonide insanlar nasıl dinlenir?" # Kullanıcı sorusu
print(f"\n--- Kullanıcı Sorusu: {query} ---")

# Soruyu vektöre çevir ve en yakın 2 parçayı getir
retrieved_docs = db.similarity_search(query, k=2)

print("\n4. Semantic Search Sonuçları (Bulunan Parçalar):")
for i, doc in enumerate(retrieved_docs):
    print(f"   Sonuç {i+1}: {doc.page_content}")

# --- ADIM 5 & 6: PROMPT + AUGMENTED GENERATION ---
# LLM'e (GPT-3.5/4) bulduğumuz parçaları ve soruyu birleştirip gönderiyoruz.

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Basit bir Prompt şablonu oluşturalım
context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])

prompt = f"""
Sen bir asistansın. Aşağıdaki bağlam bilgisini kullanarak soruyu cevapla.
Eğer bilgi bağlamda yoksa "Bilmiyorum" de.

BAĞLAM BİLGİSİ:
{context_text}

SORU:
{query}
"""

print("\n5. LLM'e Gönderilen Final Prompt Hazırlandı.")
print("6. Cevap Üretiliyor (Generation)...")

response = llm.invoke(prompt)

print(f"\n--- FİNAL CEVAP ---\n{response.content}")