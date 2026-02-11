# 🧠 Bağlam-Farkında RAG PDF Asistanı

> Geri çağırma sonrası akıllı bağlam işleme ile gelişmiş RAG sistemi

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-green.svg)](https://langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-orange.svg)](https://openai.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-purple.svg)](https://www.trychroma.com/)

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Neden Bu Proje?](#-neden-bu-proje)
- [Özellikler](#-özellikler)
- [Mimari](#-mimari)
- [Kurulum](#️-kurulum)
- [Kullanım](#-kullanım)
- [Bağlam İşleme Teknikleri](#-bağlam-i̇şleme-teknikleri)
- [Teknoloji Yığını](#️-teknoloji-yığını)
- [Kullanım Senaryoları](#-kullanım-senaryoları)
- [Gelecek Geliştirmeler](#-gelecek-geliştirmeler)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [İletişim](#-i̇letişim)

## 🎯 Proje Hakkında

**Bağlam-Farkında RAG PDF Asistanı**, geleneksel RAG (Retrieval-Augmented Generation) sistemlerinin ötesine geçen, akıllı bağlam mühendisliği teknikleri kullanan bir uygulamadır. Çoğu RAG sistemi sadece belge parçalarını geri çağırıp doğrudan LLM'e gönderirken, bu proje **bağlamı optimize ederek** daha doğru, verimli ve güvenilir yanıtlar üretir.

### 🌟 Ana Hedef

LLM'e gönderilmeden önce geri çağırılan bağlamı optimize etmek:
- ✅ **Doğruluğu artırmak**
- ✅ **Halüsinasyonları azaltmak**
- ✅ **Token verimliliği sağlamak**
- ✅ **İlgililik skorunu yükseltmek**

## 🔍 Neden Bu Proje?

Çoğu RAG demo projesi **geri çağırma** aşamasında durur. Bu proje, **üretim seviyesi RAG sistemlerinde kritik öneme sahip** olan bağlam işleme pipeline'larını uygular.

### 💡 Gösterilen Yetenekler

| Beceri | Açıklama |
|--------|----------|
| 🧩 **Bağlam Mühendisliği** | Filtreleme, sıralama, özetleme teknikleri |
| 🎯 **LLM Optimizasyonu** | Token yönetimi ve halüsinasyon önleme |
| 🔗 **RAG Pipeline** | End-to-end retrieval ve generation süreci |
| 📊 **Vektör Veritabanı** | Semantik arama ve embedding yönetimi |
| 🛡️ **Kalite Kontrolü** | İlgililik skorlama ve bağlam filtreleme |

## ✨ Özellikler

### 📥 Belge İşleme
- ✅ PDF doküman yükleme ve ayrıştırma
- ✅ Akıllı chunk'lama (örtüşme ile)
- ✅ Metin ön işleme ve temizleme

### 🔍 Geri Çağırma ve Arama
- ✅ Embedding tabanlı semantik arama
- ✅ ChromaDB vektör veritabanı entegrasyonu
- ✅ Benzerlik skoru hesaplama

### 🎛️ Bağlam İşleme (Temel Fark!)
- ✅ **Bağlam Filtreleme**: İlgisiz chunk'ları eleme
- ✅ **İlgililik Sıralaması**: En önemli bağlamı önceliklendirme
- ✅ **Token Bütçeleme**: Model limitlerini aşmama
- ✅ **Bağlam Özetleme**: Uzun metinleri kondense etme
- ✅ **Halüsinasyon Önleme**: Prompt mühendisliği stratejileri

### 🤖 Üretim
- ✅ OpenAI API entegrasyonu
- ✅ Optimize edilmiş prompt şablonları
- ✅ Kaynak referanslama

## 🏗️ Mimari

```
┌─────────────────────────────────────────────────────────────────┐
│                         RAG PIPELINE                             │
└─────────────────────────────────────────────────────────────────┘

📄 PDF Doküman
     ↓
📝 Chunk'lama (Overlap ile)
     ↓
🧮 Embedding Oluşturma (OpenAI)
     ↓
💾 Vektör Veritabanı (ChromaDB)
     ↓
❓ Kullanıcı Sorusu → 🔍 Semantik Arama
     ↓
📊 Retrieval (Top-k Chunk)
     ↓
┌────────────────────────────────────┐
│    BAĞLAM İŞLEME (Core Value)      │
├────────────────────────────────────┤
│  1️⃣ Filtreleme (Skor < 0.7)       │
│  2️⃣ Sıralama (İlgililik)          │
│  3️⃣ Token Kontrolü (Max 2000)      │
│  4️⃣ Özetleme (Gerekirse)          │
└────────────────────────────────────┘
     ↓
🤖 LLM (OpenAI GPT)
     ↓
💬 Optimize Edilmiş Yanıt
```

## ⚙️ Kurulum

### Gereksinimler

- Python 3.8+
- OpenAI API anahtarı
- pip paket yöneticisi

### Adım 1: Repoyu Klonlayın

```bash
git clone https://github.com/kullaniciadi/context-aware-rag.git
cd context-aware-rag
```

### Adım 2: Sanal Ortam Oluşturun (Önerilir)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### Adım 4: Ortam Değişkenlerini Ayarlayın

Proje kök dizininde `.env` dosyası oluşturun:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Adım 5: PDF Dokümanınızı Ekleyin

PDF dosyanızı şu konuma yerleştirin:

```
data/sample.pdf
```

## 🚀 Kullanım

### Temel Kullanım

```bash
python app.py
```

### Örnek Kod

```python
from rag_assistant import RAGAssistant

# RAG asistanını başlat
assistant = RAGAssistant(pdf_path="data/sample.pdf")

# Dokümanı işle
assistant.process_document()

# Soru sor
response = assistant.query("Bu dokümanda ana fikirler nelerdir?")
print(response)
```

### İleri Seviye Kullanım

```python
# Özel parametrelerle
assistant = RAGAssistant(
    pdf_path="data/sample.pdf",
    chunk_size=500,
    chunk_overlap=50,
    top_k=5,
    relevance_threshold=0.7,
    max_tokens=2000
)

# Birden fazla soru
questions = [
    "Dokümanın ana konusu nedir?",
    "Hangi metodolojiler kullanılmış?",
    "Sonuçlar ne gösteriyor?"
]

for question in questions:
    answer = assistant.query(question)
    print(f"S: {question}")
    print(f"C: {answer}\n")
```

## 🔧 Bağlam İşleme Teknikleri

Bu proje aşağıdaki bağlam optimizasyon tekniklerini uygular:

### 1️⃣ Bağlam Filtreleme

```python
def filter_context(chunks, threshold=0.7):
    """İlgililik skoru düşük chunk'ları filtrele"""
    return [chunk for chunk in chunks if chunk.score >= threshold]
```

**Neden Önemli:** İlgisiz bağlam LLM'i yanıltabilir ve token israfına yol açar.

### 2️⃣ İlgililik Sıralaması

```python
def rank_chunks(chunks):
    """Chunk'ları ilgililik skoruna göre sırala"""
    return sorted(chunks, key=lambda x: x.score, reverse=True)
```

**Neden Önemli:** En önemli bilgiyi LLM'e önce sunmak yanıt kalitesini artırır.

### 3️⃣ Token Bütçeleme

```python
def apply_token_budget(chunks, max_tokens=2000):
    """Toplam token sayısını sınırla"""
    total_tokens = 0
    selected_chunks = []
    
    for chunk in chunks:
        chunk_tokens = count_tokens(chunk.content)
        if total_tokens + chunk_tokens <= max_tokens:
            selected_chunks.append(chunk)
            total_tokens += chunk_tokens
        else:
            break
    
    return selected_chunks
```

**Neden Önemli:** Model limitlerini aşmamak ve maliyeti kontrol etmek kritiktir.

### 4️⃣ Bağlam Özetleme

```python
def summarize_context(chunks):
    """Uzun chunk'ları özetle"""
    summarized = []
    for chunk in chunks:
        if len(chunk.content) > 1000:
            summary = summarize(chunk.content)
            summarized.append(summary)
        else:
            summarized.append(chunk.content)
    return summarized
```

**Neden Önemli:** Token verimliliği sağlarken bilgi kaybını minimize eder.

### 5️⃣ Halüsinasyon Önleme

Prompt stratejisi:

```python
PROMPT_TEMPLATE = """
Aşağıdaki bağlama dayanarak soruyu yanıtla.
SADECE verilen bağlamdaki bilgileri kullan.
Eğer bağlamda cevap yoksa, "Bu bilgi dokümanda bulunmuyor" de.

Bağlam:
{context}

Soru: {question}

Yanıt:
"""
```

## 🛠️ Teknoloji Yığını

| Teknoloji | Kullanım Amacı |
|-----------|----------------|
| **Python** | Ana programlama dili |
| **LangChain** | RAG pipeline framework |
| **OpenAI API** | LLM ve embeddings |
| **ChromaDB** | Vektör veritabanı |
| **PyPDF2** | PDF ayrıştırma |
| **python-dotenv** | Ortam değişkeni yönetimi |
| **tiktoken** | Token sayma |

## 💼 Kullanım Senaryoları

### 🎓 Akademik
- Araştırma makalesi analizi
- Ders çalışma asistanı
- Literatür taraması

### 💼 İş Dünyası
- Sözleşme inceleme
- Doküman analizi
- Bilgi tabanı asistanı

### 🏥 Sağlık
- Tıbbi doküman özeti
- Hasta dosyası analizi
- Klinik kılavuz asistanı

### ⚖️ Hukuk
- Yasal doküman araştırma
- Emsal karar analizi
- Sözleşme karşılaştırma

## 📈 Gelecek Geliştirmeler

### Öncelikli
- [ ] **Kaynak Alıntılama**: Yanıtlarda sayfa numarası referansı
- [ ] **Cross-Encoder Reranking**: İleri seviye sıralama
- [ ] **Multi-Query Retrieval**: Sorgunu genişletme

### Orta Vadeli
- [ ] **Web Arayüzü**: Streamlit/Gradio UI
- [ ] **Kalıcı Depolama**: Disk tabanlı vektör DB
- [ ] **Batch İşleme**: Çoklu doküman desteği

### Uzun Vadeli
- [ ] **Hafıza Yönetimi**: Konuşma geçmişi
- [ ] **Çoklu Format**: DOCX, TXT, HTML desteği
- [ ] **API Endpoint**: REST API servisi
- [ ] **Fine-tuning**: Domain-specific model

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'inizi push edin (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 🙏 Teşekkürler

Bu proje, [Context-Engineering](https://github.com/davidkimai/Context-Engineering) reposundan ilham alınarak geliştirilmiştir.

## 📬 İletişim

**Oğulcan Narin**  
Yazılım Mühendisliği Öğrencisi


- Email: ogulcannarin268@gmail.com

---

<div align="center">

**⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with ❤️ by Oğulcan Narin

</div>
