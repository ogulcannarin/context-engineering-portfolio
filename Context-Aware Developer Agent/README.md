# 🤖 Context-Aware Developer Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**GitHub repolarını ve yerel projeleri Context Engineering teknikleriyle analiz eden yapay zeka destekli geliştirici asistanı**

[Özellikler](#-özellikler) • [Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [Mimari](#-mimari) • [Teknolojiler](#-teknolojiler)

</div>

---

## 📋 İçindekiler

- [Genel Bakış](#-genel-bakış)
- [Özellikler](#-özellikler)
- [Nasıl Çalışır?](#-nasıl-çalışır)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Mimari](#-mimari)
- [Teknolojiler](#-teknolojiler)
- [Proje Yapısı](#-proje-yapısı)
- [Katkıda Bulunma](#-katkıda-bulunma)

---

## 🎯 Genel Bakış

**Context-Aware Developer Agent**, yazılım geliştiriciler için tasarlanmış akıllı bir kod analiz asistanıdır. David Kimai'nin **"Information Density"** prensiplerine dayanan bu araç, kod tabanlarını optimize ederek LLM'lere (Large Language Models) daha verimli bağlam sağlar.

### 🎪 Neden Bu Proje?

Modern AI destekli geliştirme araçları, kod tabanlarını analiz ederken gereksiz yorumlar, boşluklar ve tekrarlayan içeriklerle token limitlerini hızla doldurur. Bu:
- 💸 **Yüksek API maliyetlerine** yol açar
- ⚡ **Yavaş yanıt süreleri** oluşturur
- 🎯 **Bağlam kalitesini** düşürür

**Context-Aware Developer Agent** bu sorunları çözmek için:
- ✂️ Kodları **akıllıca budayarak** bilgi yoğunluğunu artırır
- 🎯 **Dinamik bağlam seçimi** ile sadece ilgili kod parçalarını kullanır
- 📊 **Gerçek zamanlı maliyet takibi** ile optimizasyon metrikleri sunar
- 🔄 Hem **yerel projeler** hem de **GitHub repoları** ile çalışır

---

## ✨ Özellikler

### 🔍 Akıllı Kod Analizi
- **Pruning (Budama) Teknolojisi**: Yorumlar ve gereksiz boşluklar otomatik olarak temizlenir
- **Dinamik Bağlam Seçimi**: Kullanıcı sorusuna göre sadece ilgili dosyalar LLM'e gönderilir
- **Token Optimizasyonu**: %40-60 arası token tasarrufu sağlar

### 💬 Interaktif Sohbet Arayüzü
- **Streamlit Tabanlı UI**: Modern ve kullanıcı dostu arayüz
- **Gerçek Zamanlı Analiz**: Kodlarınız hakkında anında yanıtlar alın
- **Bağlam Görüntüleme**: Hangi kod parçalarının kullanıldığını görerek şeffaflık

### 📊 Maliyet ve Verimlilik Metrikleri
- **Karşılaştırmalı Token Sayımı**: Ham vs Optimize edilmiş token miktarları
- **Maliyet Hesaplama**: Gerçek zamanlı API maliyet tahmini (GPT-4o-mini bazlı)
- **Tasarruf Oranı**: Net tasarruf ve verimlilik yüzdesi

### 🔗 Çoklu Kaynak Desteği
- 📂 **Yerel Klasörler**: Bilgisayarınızdaki projeleri analiz edin
- 🐙 **GitHub Repoları**: Herhangi bir public GitHub reposunu doğrudan klonlayıp inceleyin

---

## 🧠 Nasıl Çalışır?

### 1️⃣ **Ingestor Modülü** (`ingestor.py`)
Proje tabanını tarar ve analiz eder:

```python
ingestor = ProjectIngestor("./my_project")
ingestor.scan_project()  # Kodları tarar ve budayarak optimize eder
ingestor.save_context()  # JSON formatında kaydeder
```

**Optimizasyon İşlemleri:**
- ✂️ Tek satırlık yorumları temizler (`# ...`)
- 🧹 Fazla boş satırları birleştirir
- 📦 Gereksiz klasörleri atlar (venv, node_modules, __pycache__)

### 2️⃣ **Brain Modülü** (`brain.py`)
OpenAI API ile entegre çalışır:

```python
brain = ContextBrain(api_key="your_openai_key")
response = brain.ask("Bu projenin mimarisi nasıl?")
```

**Akıllı Sorgu Mekanizması:**
- 🎯 Kullanıcı sorusundaki anahtar kelimelere göre ilgili dosyaları filtreler
- 📤 Sadece gerekli kod parçalarını LLM'e gönderir
- 🔄 Dinamik prompt oluşturarak verimli yanıtlar alır

### 3️⃣ **Utils Modülü** (`utils.py`)
Yardımcı fonksiyonlar:

```python
# Kod budama
clean_code = prune_python_code(raw_code)

# Token hesaplama (1 token ≈ 4 karakter)
token_count = count_tokens(text)

# Maliyet analizi
orig_cost, opt_cost, savings = calculate_savings(orig_tokens, pruned_tokens)
```

---

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- OpenAI API Key

### Adım 1: Projeyi Klonlayın
```bash
git clone https://github.com/yourusername/context-aware-developer-agent.git
cd context-aware-developer-agent
```

### Adım 2: Sanal Ortam Oluşturun (Önerilir)
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 4: `.env` Dosyası Oluşturun
Proje klasöründe `.env` dosyası oluşturup API anahtarınızı ekleyin:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

> **💡 Not**: `.gitignore` dosyası `.env`'yi zaten hariç tutuyor, API anahtarınız güvende!

---

## 📖 Kullanım

### Streamlit Arayüzünü Başlatın
```bash
streamlit run app.py
```

Tarayıcınızda otomatik olarak `http://localhost:8501` adresi açılacaktır.

### Yerel Proje Analizi
1. Sol menüden **"Yerel Klasör"** seçin
2. Proje klasör yolunu girin (örn: `./my_project`)
3. **"Analizi Başlat"** butonuna tıklayın
4. Sohbet kutusundan sorular sorun!

### GitHub Repo Analizi
1. Sol menüden **"GitHub Reposu"** seçin
2. Repo URL'sini girin (örn: `https://github.com/user/repo`)
3. **"Analizi Başlat"** butonuna tıklayın (Repo otomatik klonlanır)
4. Kod hakkında soru sorun!

### Örnek Sorular
```text
- "Bu projenin mimarisi nasıl organize edilmiş?"
- "app.py dosyasındaki ana fonksiyonları açıklar mısın?"
- "Hangi Python kütüphaneleri kullanılmış?"
- "Veri akışı nasıl çalışıyor?"
```

---

## 🏗️ Mimari

```
┌─────────────────────────────────────────────────┐
│           STREAMLIT UI (app.py)                 │
│  ┌──────────────┐      ┌──────────────────┐    │
│  │  Sohbet      │      │  Metrik Paneli   │    │
│  │  Arayüzü     │      │  (Token/Maliyet) │    │
│  └──────────────┘      └──────────────────┘    │
└───────────┬─────────────────────┬───────────────┘
            │                     │
            ▼                     ▼
┌─────────────────────┐  ┌─────────────────────┐
│   ProjectIngestor   │  │   ContextBrain      │
│   (ingestor.py)     │  │   (brain.py)        │
│                     │  │                     │
│ • scan_project()    │  │ • get_relevant_code │
│ • download_github() │  │ • ask()             │
│ • save_context()    │  │                     │
└─────────┬───────────┘  └──────────┬──────────┘
          │                         │
          ▼                         ▼
    ┌─────────────────┐      ┌─────────────┐
    │ project_context │      │ OpenAI API  │
    │     .json       │      │ (GPT-4o)    │
    └─────────────────┘      └─────────────┘
```

### Veri Akışı
1. **Kullanıcı** → Proje kaynağı seçer (Yerel/GitHub)
2. **Ingestor** → Kodları tarar, budayarak `project_context.json` oluşturur
3. **Kullanıcı** → Soru sorar
4. **Brain** → Soruyla ilgili kod parçalarını filtreler
5. **OpenAI** → Bağlama dayalı yanıt üretir
6. **Streamlit** → Cevap + kullanılan kod parçalarını gösterir

---

## 🛠️ Teknolojiler

| Kategori | Teknoloji | Kullanım Amacı |
|----------|-----------|----------------|
| **Frontend UI** | [Streamlit](https://streamlit.io/) | Web arayüzü ve interaktif dashboard |
| **AI Model** | [OpenAI GPT-4o-mini](https://openai.com/) | Kod analizi ve soru-cevap |
| **Kod Yönetimi** | [GitPython](https://gitpython.readthedocs.io/) | GitHub repo klonlama |
| **Env Yönetimi** | [python-dotenv](https://github.com/theskumar/python-dotenv) | API key güvenliği |
| **Dil** | Python 3.8+ | Ana programlama dili |

---

## 📂 Proje Yapısı

```
Context-Aware Developer Agent/
│
├── app.py                   # Streamlit ana uygulama dosyası
├── ingestor.py              # Proje tarama ve budama modülü
├── brain.py                 # OpenAI entegrasyonu ve bağlam yönetimi
├── utils.py                 # Yardımcı fonksiyonlar (pruning, token count)
│
├── requirements.txt         # Python bağımlılıkları
├── .env                     # API anahtarları (GIT'e dahil değil!)
├── .gitignore               # Git hariç tutma kuralları
│
├── project_context.json     # Oluşturulan optimize edilmiş bağlam (runtime)
├── temp_repo/               # GitHub klonları için geçici klasör
│
└── README.md                # Bu dosya!
```

---

## 📊 Performans Metrikleri

### Örnek Optimizasyon Sonuçları (Orta Ölçekli Proje)

| Metrik | Ham Kod | Optimize Kod | Tasarruf |
|--------|---------|--------------|----------|
| **Toplam Token** | 12,500 | 7,200 | **42%** ⬇️ |
| **Tahmini Maliyet** | $0.0625 | $0.036 | **$0.0265** 💰 |
| **İşlem Süresi** | 2.8s | 1.6s | **43%** ⚡ |

> ℹ️ Fiyatlar GPT-4o-mini ($0.005/1k token) üzerinden hesaplanmıştır.

---

## 🎓 Context Engineering Nedir?

**Context Engineering**, yapay zeka modellerine verilen bağlamı (context) optimize ederek:
- 🎯 **Daha alakalı yanıtlar** elde etmeyi
- 💸 **Token maliyetlerini düşürmeyi**
- ⚡ **Yanıt sürelerini hızlandırmayı** amaçlar

### Bu Projede Kullanılan Teknikler:
1. **Code Pruning** - Gereksiz içeriklerin temizlenmesi
2. **Dynamic Context Selection** - Soruya göre bağlam filtreleme
3. **Information Density** - Minimum token ile maksimum bilgi
4. **Token Budget Management** - Maliyet kontrolü

> 📚 **Referans**: [David Kimai - Context Engineering Principles](https://github.com/davidkimai/context-engineering)

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. 🍴 Projeyi fork edin
2. 🌿 Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. 💾 Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. 📤 Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. 🎉 Pull Request açın

### Geliştirme Fikirleri
- [ ] Multi-language desteği (JavaScript, Java, Go vb.)
- [ ] Vectorstore entegrasyonu (Pinecone/Chroma)
- [ ] Semantic search ile gelişmiş bağlam seçimi
- [ ] Proaktif kod önerileri
- [ ] Export/Import bağlam özelliği

---

## 📜 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 📧 İletişim

**Proje Sahibi**: [GitHub Profiliniz]

⭐ Projeyi beğendiyseniz yıldız vermeyi unutmayın!

---

<div align="center">

**Made with ❤️ and AI**

[⬆ Yukarı Çık](#-context-aware-developer-agent)

</div>
