# 🧠 Context Engineering & Advanced RAG Architectures

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python) ![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge) ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange?style=for-the-badge) ![Reranking](https://img.shields.io/badge/Reranking-Cross--Encoder-red?style=for-the-badge)

Bu depo, **Large Language Models (LLM)** uygulamalarında karşılaşılan bağlam (context) yönetimi, halüsinasyon ve erişim (retrieval) problemlerini çözmek için geliştirdiğim ileri seviye RAG (Retrieval-Augmented Generation) mimarilerini içerir.

Buradaki amaç sadece bir chatbot yapmak değil; veriyi işleme, vektör uzayında arama yapma ve sonuçları yeniden sıralama (reranking) süreçlerini optimize eden bir **Context Engineering** yetkinliği kazanmaktır.

---

## 📂 Proje Modülleri ve Teknik Detaylar

### 1️⃣ Modül: Temel RAG Mimarisi (Mars Colony Assistant)
**Konum:** `/00_Basics_RAG_Intro`

Bu modülde, ham metin verisinin LLM tarafından anlaşılabilir hale getirilmesi ve sorgulanması için uçtan uca (end-to-end) bir boru hattı (pipeline) inşa edilmiştir.

#### 🛠️ Ne Yaptım?
* **Data Ingestion:** Ham metin verisi sisteme yüklendi.
* **Chunking (Parçalama):** `RecursiveCharacterTextSplitter` kullanılarak metin, bağlam kopukluğunu önlemek için **Overlap (Örtüşme)** stratejisi ile 100 karakterlik parçalara bölündü.
* **Embedding:** Metin parçaları `OpenAIEmbeddings` ile vektör uzayına (Vector Space) taşındı.
* **Vector Storage:** Veriler geçici hafıza olarak `ChromaDB` üzerinde endekslendi.
* **Retrieval & Generation:** Kullanıcı sorusu ile en alakalı parçalar getirilip GPT-3.5 modeline "Context" olarak sunuldu.

#### 🧠 Ne Öğrendim?
* **Context Window Yönetimi:** LLM'e tüm kitabı vermek yerine sadece ilgili sayfayı (chunk) vermenin maliyeti düşürdüğünü ve doğruluğu artırdığını öğrendim.
* **Chunk Overlap Önemi:** Cümlelerin tam ortadan bölünmemesi ve anlam bütünlüğünün korunması için `chunk_overlap` parametresinin kritik olduğunu deneyimledim.
* **Prompt Engineering:** Halüsinasyonu önlemek için modele *"Eğer bilgi bağlamda yoksa uydurma, bilmiyorum de"* talimatını vererek **Grounding (Temellendirme)** prensibini uyguladım.

---

### 2️⃣ Modül: Hybrid Search & Reranking (Project Chimera)
**Konum:** `/01_Hybrid_Search_Reranking`

Standart vektör aramalarının (Semantic Search) yetersiz kaldığı "Domain-Specific" terimler ve tam eşleşme gerektiren durumlar için geliştirilmiş hibrit bir arama motorudur.

#### 🛠️ Ne Yaptım?
* **Dual-Encoder vs. Cross-Encoder:** Arama hızını artırmak için önce Vektör Araması (Bi-Encoder), sonrasında hassasiyeti artırmak için Reranking (Cross-Encoder) mimarisini kurdum.
* **Hybrid Search Mekanizması:**
    1.  **Sparse Retrieval (BM25):** Anahtar kelime eşleşmesi (Keyword Matching) için `BM25Okapi` algoritmasını entegre ettim. Bu sayede "X-99", "Kod 404" gibi özel terimlerin kaçırılmasını engelledim.
    2.  **Dense Retrieval (ChromaDB):** Anlamsal benzerlikleri yakalamak için vektör veritabanını kullandım.
* **Reranking:** İki kanaldan gelen sonuç havuzunu birleştirip, `sentence-transformers/ms-marco-MiniLM-L-6-v2` Cross-Encoder modeli ile yeniden puanladım.

#### 🧠 Ne Öğrendim?
* **Recall vs. Precision Dengesi:** * *Recall (Kapsama):* Hibrit arama ile mümkün olduğunca çok potansiyel adayı (candidate generation) topladım.
    * *Precision (Hassasiyet):* Reranker kullanarak bu adaylar arasından en doğru olanı %98+ güven skoruyla filtreledim.
* **Semantic Gap:** Vektörlerin bazen zıt anlamlı kelimeleri (örneğin "mutlu" ve "mutsuz") birbirine yakın konumlandırdığını, ancak Keyword aramasının (BM25) bu açığı kapattığını analiz ettim.

---

## 🗺️ Context Engineering Yol Haritası

Bu portfolyo, aşağıdaki yetkinlikleri adım adım kazanmayı hedefler:

- [x] **1. Basic Pipeline:** Embedding, Vector DB, Retrieval.
- [x] **2. Chunking Strategies:** Recursive Character Splitting & Overlap.
- [x] **3. Hybrid Search:** Dense (Vector) + Sparse (BM25) entegrasyonu.
- [x] **4. Reranking:** Cross-Encoder ile sonuç iyileştirme.
- [ ] **5. Retrieval Evaluation:** Recall@k ve Precision@k metrikleri ile sistem başarısını ölçme.
- [ ] **6. Query Reformulation:** Multi-Query ve HyDE teknikleri ile kullanıcı sorgularını zenginleştirme.
- [ ] **7. Context Optimization:** "Lost in the Middle" problemini çözme ve token tasarrufu.
- [ ] **8. Hallucination Guardrails:** Yapay zeka çıktılarının doğruluğunu denetleyen güvenlik katmanları.
- [ ] **9. Cost & Latency Ops:** Embedding Cache ve üretim ortamı optimizasyonları.

---

## 🛠️ Kurulum

Projeyi yerel ortamınızda test etmek için:

```bash
# Depoyu klonlayın
git clone [https://github.com/KULLANICI_ADINIZ/context-engineering-portfolio.git](https://github.com/KULLANICI_ADINIZ/context-engineering-portfolio.git)

# Klasöre girin
cd context-engineering-portfolio

# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# .env dosyasını oluşturun ve API anahtarınızı ekleyin
# (Örnek: OPENAI_API_KEY=sk-...)