# 🤖 Context-Aware Agent

<div align="center">

**Modern Context Engineering Prensiplerine Dayalı Akıllı AI Agent Sistemi**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-green.svg)](https://openai.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-orange.svg)](https://www.trychroma.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20API-teal.svg)](https://fastapi.tiangolo.com/)

[English](#) · **Türkçe** · [Documentation](#)

</div>

---

## 📋 İçindekiler

- [Hakkında](#-hakkında)
- [Temel Özellikler](#-temel-özellikler)
- [Mimari](#-mimari)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)
- [Context Engineering Nedir?](#-context-engineering-nedir)
- [Teknik Detaylar](#-teknik-detaylar)
- [Örnekler](#-örnekler)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 🎯 Hakkında

**Context-Aware Agent**, modern yapay zeka sistemlerinin temel taşlarından biri olan **Context Engineering** prensiplerini uygulayan gelişmiş bir AI agent sistemidir. Bu proje, Andrej Karpathy'nin ünlü sözünden ilham alır:

> *"Context engineering is the delicate art and science of filling the context window with just the right information for the next step."*  
> — Andrej Karpathy

### 🎓 Proje Hedefi

Bu proje, üç temel Context Engineering konseptini pratik bir uygulamada birleştirerek gösterir:

1. **Retrieval Augmented Generation (RAG)** - Bilgi getirme ve zenginleştirme
2. **Memory Systems** - Akıllı hafıza yönetimi
3. **Tool Integrated Reasoning** - Araç entegrasyonu ve akıl yürütme

---

## ✨ Temel Özellikler

### 🧠 **1. Gelişmiş Hafıza Sistemi (Memory System)**

- **Semantic Search**: OpenAI embeddings kullanarak anlam bazlı arama
- **Vector Database**: ChromaDB ile yüksek performanslı vektör depolama
- **Conversation History**: Geçmiş konuşmaları hatırlama ve bağlam kurma
- **Long-term Memory**: Kalıcı bilgi saklama

```python
# Örnek: Agent adınızı hatırlar
You: Benim adım Oğulcan
Agent: Merhaba Oğulcan! Size nasıl yardımcı olabilirim?

You: Adım neydi?
Agent: Adınız Oğulcan.
```

### 📚 **2. RAG (Retrieval Augmented Generation)**

- **Dynamic Context**: Her sorguya özel ilgili bilgileri getirme
- **Embedding-based Retrieval**: Semantic similarity ile akıllı arama
- **Context Window Optimization**: En ilgili bilgiyle context'i zenginleştirme

```python
# Memory'den ilgili bilgileri çekip context oluşturur
def retrieve_context(query: str):
    memories = search_memory(query)
    return "\n".join(memories) if memories else ""
```

### 🛠️ **3. Tool Integration (Araç Entegrasyonu)**

Agent, dış araçları kullanarak yeteneklerini genişletir:

- **⏰ Time Tool**: Güncel saat ve tarih bilgisi
- **🔢 Calculator**: Matematiksel hesaplamalar
- **🔮 Extensible**: Kolayca yeni araçlar eklenebilir

```python
# Tool kullanım örneği
You: 125 * 48 kaç eder?
Agent: Tool result: 6000
```

---

## 🏗️ Mimari

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         USER INPUT                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      AGENT CORE                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  1. RAG Pipeline                                      │  │
│  │     └─► retrieve_context(query)                      │  │
│  │         └─► ChromaDB Semantic Search                 │  │
│  └───────────────────────────────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  2. LLM Processing (GPT-4.1-mini)                    │  │
│  │     ├─► System Prompt + Context                      │  │
│  │     ├─► Tool Decision Making                         │  │
│  │     └─► Response Generation                          │  │
│  └───────────────────────────────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  3. Tool Execution (Optional)                        │  │
│  │     ├─► Time Tool                                    │  │
│  │     ├─► Calculator                                   │  │
│  │     └─► Custom Tools...                              │  │
│  └───────────────────────────────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  4. Memory Update                                    │  │
│  │     └─► add_memory(conversation)                     │  │
│  │         └─► ChromaDB Storage                         │  │
│  └───────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      RESPONSE OUTPUT                        │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

```
User Query
    │
    ├─► [RAG] → Search Memory → Relevant Context
    │                              │
    ├─► [LLM] ← Context + Query ──┘
    │       │
    │       ├─► Need Tool? → Yes → [TOOL] → Execute → Result
    │       └─► Need Tool? → No  → Direct Response
    │                                        │
    └─► [MEMORY] ← Save Conversation ───────┘
                                            │
                                            ▼
                                      Final Response
```

---

## 🚀 Kurulum

### Gereksinimler

- Python 3.10 veya üzeri
- OpenAI API Key
- Git

### 1. Repository'yi Klonlayın

```bash
git clone https://github.com/yourusername/context-aware-agent.git
cd context-aware-agent
```

### 2. Virtual Environment Oluşturun (Önerilir)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

`.env` dosyası oluşturun:

```env
OPENAI_API_KEY=your_api_key_here
```

**Güvenlik Önemli:** `.env` dosyanızı asla GitHub'a yüklemeyin!

---

## 💻 Kullanım

### 🖥️ CLI Modu (Command Line Interface)

```bash
python main.py
```

**Örnek Etkileşim:**

```
Agent hazır! Çıkmak için 'exit' yaz.

You: Merhaba
Agent: Merhaba! Size nasıl yardımcı olabilirim?

You: Benim adım Ali
Agent: Merhaba Ali! Tanıştığımıza memnun oldum. Size nasıl yardımcı olabilirim?

You: 250 * 16 kaç eder?
Agent: Tool result: 4000

You: Saat kaç?
Agent: Tool result: 14:42:30

You: Adım neydi?
Agent: Adınız Ali.

You: exit
```

### 🌐 API Modu (FastAPI)

Agent'ı bir web servisi olarak çalıştırabilirsiniz:

**Not**: Bu özellik için `main.py` dosyasını FastAPI versiyonuna geri döndürmeniz gerekir.

```bash
uvicorn main:app --reload
```

API'ye erişim:

```bash
curl "http://127.0.0.1:8000/chat?q=Merhaba"
```

Swagger UI: http://127.0.0.1:8000/docs

---

## 📁 Proje Yapısı

```
context-aware-agent/
│
├── 📄 agent.py              # Ana agent mantığı ve orchestration
├── 📄 main.py               # CLI interface
├── 📄 memory.py             # ChromaDB hafıza yönetimi
├── 📄 rag.py                # RAG pipeline implementation
├── 📄 tools.py              # Tool registry ve yönetimi
├── 📄 requirements.txt      # Proje bağımlılıkları
├── 📄 .env                  # Environment variables (GİZLİ)
├── 📄 README.md             # Bu dosya
│
└── 📁 tools/                # Tool implementations
    ├── __init__.py
    ├── calculator.py        # Matematiksel hesaplama aracı
    └── time_tool.py         # Zaman/tarih aracı
```

### Dosya Açıklamaları

#### `agent.py` - Agent Core

Agent'ın beyni. Tüm işlemleri koordine eder:
- RAG pipeline'ı çalıştırır
- LLM ile iletişim kurar
- Tool execution'ı yönetir
- Memory update yapar

#### `memory.py` - Memory System

ChromaDB kullanarak:
- Konuşma geçmişini vektör formatında saklar
- Semantic search ile ilgili memoryleri getirir
- OpenAI embeddings ile vektörizasyon yapar

#### `rag.py` - RAG Pipeline

Retrieval Augmented Generation için:
- Memory'den query'ye uygun context çeker
- Context'i formatlar ve döndürür

#### `tools.py` - Tool Registry

Tüm araçları merkezi bir yerde toplar:
- Tool registration
- Tool discovery
- Modüler tool ekleme

---

## 🎓 Context Engineering Nedir?

**Context Engineering**, Large Language Model'lerin (LLM) performansını optimize etmek için context window'a doğru bilgiyi doğru zamanda ekleme sanatıdır.

### Üç Temel Pillar

#### 1️⃣ **Retrieval Augmented Generation (RAG)**

**Problem**: LLM'ler sadece eğitim verilerindeki bilgileri bilir.

**Çözüm**: Harici bilgi kaynaklarından dinamik olarak bilgi çekerek LLM'in context'ini zenginleştir.

```python
# RAG Akışı
User Query → Search Vector DB → Retrieve Top-K Results → 
→ Add to Context → Send to LLM → Enhanced Response
```

**Avantajlar**:
- ✅ Güncel bilgi erişimi
- ✅ Domain-specific knowledge
- ✅ Hallucination'ı azaltma
- ✅ Maliyet optimizasyonu (fine-tuning yerine)

#### 2️⃣ **Memory Systems**

**Problem**: LLM'ler stateless'tır, önceki konuşmaları hatırlayamaz.

**Çözüm**: Konuşma geçmişini vektör database'de sakla ve ilgili olanları geri getir.

```python
# Memory Akışı
Conversation → Create Embedding → Store in ChromaDB →
→ New Query → Semantic Search → Retrieve Relevant Memories →
→ Add to Context
```

**Tipleri**:
- **Short-term**: Aktif konuşma buffer'ı
- **Long-term**: Kalıcı bilgi saklama
- **Episodic**: Olay bazlı hatırlama
- **Semantic**: Anlam bazlı ilişkilendirme

#### 3️⃣ **Tool Integrated Reasoning**

**Problem**: LLM'ler hesaplama yapamaz, güncel bilgiye erişemez.

**Çözüm**: LLM'e external tools kullanma yeteneği ver.

```python
# Tool Integration Akışı
User Query → LLM Analyzes → Decides Tool Need →
→ Calls Tool → Gets Result → Incorporates in Response
```

**Tool Örnekleri**:
- 🔍 Web Search (Google, Bing)
- 🧮 Calculator
- 📊 Data Analysis (Python REPL)
- 🌤️ Weather API
- 📧 Email Sender
- 📁 File Operations

---

## 🔧 Teknik Detaylar

### Kullanılan Teknolojiler

| Teknoloji | Amaç | Versiyon |
|-----------|------|----------|
| **OpenAI API** | LLM ve Embeddings | GPT-4.1-mini |
| **ChromaDB** | Vector Database | Latest |
| **FastAPI** | Web Framework | Latest |
| **Python** | Ana Dil | 3.10+ |
| **Uvicorn** | ASGI Server | Latest |
| **python-dotenv** | Env Management | Latest |

### Embedding Model

- **Model**: `text-embedding-3-small`
- **Dimension**: 1536
- **Use Case**: Semantic search için optimize edilmiş

### LLM Configuration

```python
model = "gpt-4.1-mini"
temperature = 0.7  # Creativity vs Consistency balance
max_tokens = 500   # Response length limit
```

### Vector Search Parameters

```python
n_results = 3  # Top-K similar memories
distance_metric = "cosine"  # Similarity metric
```

---

## 📚 Örnekler

### Örnek 1: Basit Konuşma

```python
User: Merhaba, nasılsın?
Agent: Merhaba! Ben bir AI asistanıyım ve her zaman hazırım. 
       Size nasıl yardımcı olabilirim?
```

### Örnek 2: Memory Kullanımı

```python
User: Benim adım Mehmet
Agent: Merhaba Mehmet! Tanıştığımıza memnun oldum.

User: Python öğreniyorum
Agent: Harika! Python öğrenmek çok iyi bir seçim.

User: Adım neydi?
Agent: Adınız Mehmet.

User: Ne öğreniyordum?
Agent: Python öğreniyordunuz.
```

### Örnek 3: Tool Kullanımı - Calculator

```python
User: 1234 * 5678 kaç eder?
Agent: TOOL:calculator:1234*5678
       Tool result: 7006652
```

### Örnek 4: Tool Kullanımı - Time

```python
User: Saat kaç?
Agent: TOOL:time
       Tool result: 14:42:30

User: Bugünün tarihi nedir?
Agent: TOOL:datetime
       Tool result: 2026-02-16 14:42:30
```

### Örnek 5: Kompleks Senaryo

```python
User: Benim adım Ayşe ve matematik öğretmeniyim
Agent: Merhaba Ayşe! Matematik öğretmeni olmanız harika.

User: (150 + 75) / 5 kaç eder?
Agent: TOOL:calculator:(150+75)/5
       Tool result: 45.0

User: Adım neydi ve ne iş yapıyorum?
Agent: Adınız Ayşe ve matematik öğretmenisiniz.
```

---

## 🎨 Yeni Tool Ekleme

Sisteme kolayca yeni tool ekleyebilirsiniz:

### Adım 1: Tool Fonksiyonu Oluşturun

`tools/weather_tool.py`:
```python
import requests

def get_weather(city: str):
    """Get weather for a city"""
    # API call implementation
    return f"{city} için hava durumu: Güneşli, 22°C"
```

### Adım 2: Tool Registry'ye Ekleyin

`tools.py`:
```python
from tools.weather_tool import get_weather

TOOLS = {
    "time": get_time,
    "calculator": calculate,
    "weather": get_weather,  # ⬅️ Yeni tool
}
```

### Adım 3: System Prompt'u Güncelleyin

`agent.py`:
```python
SYSTEM_PROMPT = """
...
• weather → returns weather for a city
...
Examples:
TOOL:weather:Istanbul
"""
```

✅ **İşte bu kadar!** Yeni tool hazır.

---

## 🚧 Geliştirme Roadmap

### Yakın Gelecek (v1.1)

- [ ] Multiple memory types (short-term, long-term)
- [ ] Conversation summarization
- [ ] Memory pruning/cleanup
- [ ] Tool error handling improvements
- [ ] Logging system

### Orta Vade (v1.2)

- [ ] Web Search tool
- [ ] Wikipedia integration
- [ ] File upload/analysis
- [ ] Multi-language support
- [ ] Streamlit UI

### Uzun Vade (v2.0)

- [ ] Multi-agent collaboration
- [ ] Advanced RAG techniques (HyDE, Query Rewriting)
- [ ] Custom embedding models
- [ ] GraphRAG implementation
- [ ] Production deployment guide

---

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz!

### Nasıl Katkıda Bulunulur?

1. **Fork** edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. **Pull Request** açın

### Katkı Alanları

- 🐛 Bug fixes
- ✨ Yeni özellikler
- 📝 Dokümantasyon iyileştirmeleri
- 🧪 Test coverage artırma
- 🎨 UI/UX geliştirmeleri
- 🌍 Çeviriler

---

## 📖 Referanslar & Kaynaklar

### Context Engineering

- [David Kimai - Context Engineering Course](https://github.com/davidkimai/Context-Engineering)
- [Andrej Karpathy - Context Engineering](https://twitter.com/karpathy)
- [LangChain Documentation](https://python.langchain.com/)

### RAG

- [RAG Papers](https://arxiv.org/abs/2005.11401)
- [Advanced RAG Techniques](https://www.pinecone.io/learn/retrieval-augmented-generation/)

### Vector Databases

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Vector Database Comparison](https://www.pinecone.io/learn/vector-database/)

---

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👨‍💻 Geliştirici

**Oğulcan**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-profile)
- Email: your.email@example.com

---

## 🙏 Teşekkürler

- [OpenAI](https://openai.com/) - GPT-4 ve Embeddings API
- [ChromaDB](https://www.trychroma.com/) - Vector Database
- [David Kimai](https://github.com/davidkimai) - Context Engineering eğitimi
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Andrej Karpathy](https://twitter.com/karpathy) - Context Engineering konsepti

---

## 📞 İletişim & Destek

Sorularınız veya önerileriniz için:

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yourusername/context-aware-agent/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/context-aware-agent/discussions)
- 📧 **Email**: your.email@example.com

---

<div align="center">

**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with ❤️ and 🤖 by Context Engineers

</div>
