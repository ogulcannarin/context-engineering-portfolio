import streamlit as st
import os
from dotenv import load_dotenv
from ingestor import ProjectIngestor
from brain import ContextBrain
from utils import calculate_savings

# .env dosyasındaki OPENAI_API_KEY değişkenini sisteme yükler
load_dotenv()

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Context-Aware Developer Agent", layout="wide", page_icon="🤖")

# Başlık ve Açıklama
st.title("🚀 Context-Aware Developer Agent")
st.markdown("GitHub repolarını ve yerel kodları **Context Engineering** teknikleriyle analiz eden asistan.")

# .env dosyasından anahtarı çek
env_api_key = os.getenv("OPENAI_API_KEY")

# Yan Panel (Sidebar) - Ayarlar ve Analiz
with st.sidebar:
    st.header("🔑 API Ayarları")
    api_key = st.text_input(
        "OpenAI API Key:", 
        value=env_api_key if env_api_key else "", 
        type="password"
    )
    
    st.divider()
    
    st.header("📂 Proje Kaynağı")
    # Kullanıcıya yerel klasör mü yoksa GitHub mı olduğunu soruyoruz
    source_type = st.radio("Kaynak Türü:", ["Yerel Klasör", "GitHub Reposu"])
    
    if source_type == "Yerel Klasör":
        project_path = st.text_input("Klasör Yolu:", value=".")
        repo_url = None
    else:
        repo_url = st.text_input("GitHub Repo URL:", placeholder="https://github.com/user/repo")
        project_path = "temp_repo" # GitHub projeleri için geçici klasör

    if st.button("Analizi Başlat"):
        ingestor = ProjectIngestor(project_path)
        
        try:
            if source_type == "GitHub Reposu" and repo_url:
                with st.spinner("🚀 Repo GitHub'dan indiriliyor (Klonlanıyor)..."):
                    ingestor.download_github_repo(repo_url)
            
            with st.spinner("🔍 Kodlar analiz ediliyor ve budanıyor (Pruning)..."):
                ingestor.scan_project()
                ingestor.save_context()
            st.success("✅ Analiz Tamamlandı! Bağlam haritası hazır.")
        except Exception as e:
            st.error(f"❌ Bir hata oluştu: {e}")

# Ana Ekran Kontrolü
if os.path.exists("project_context.json"):
    brain = ContextBrain(api_key=api_key)
    
    # --- METRİK PANELİ ---
    st.subheader("📊 Bağlam Verimlilik Metrikleri")
    
    orig_t = sum(f['original_tokens'] for f in brain.project_data)
    opt_t = sum(f['optimized_tokens'] for f in brain.project_data)
    orig_cost, opt_cost, savings = calculate_savings(orig_t, opt_t)

    col1, col2, col3 = st.columns(3)
    col1.metric("Ham Maliyet (Tahmini)", f"${orig_cost}")
    col2.metric("Optimize Maliyet", f"${opt_cost}")
    
    savings_percent = round((savings / orig_cost) * 100, 1) if orig_cost > 0 else 0
    col3.metric("Net Tasarruf", f"${savings}", delta=f"%{savings_percent} Verimlilik")

    st.divider()

    # --- SOHBET ARAYÜZÜ ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Kod hakkında bir soru sorun (örn: 'Bu projenin mimarisi nasıl?')"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Bağlam taranıyor..."):
                response = brain.ask(prompt)
                st.markdown(response)
            
            with st.expander("🔍 Seçilen Dinamik Bağlam (Optimize Edilmiş Kod)"):
                relevant_code = brain.get_relevant_code(prompt)
                if relevant_code:
                    st.code(relevant_code, language="python")
                else:
                    st.info("Genel proje haritası kullanıldı.")
        
        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.info("👋 Başlamak için lütfen sol menüden bir proje kaynağı seçip 'Analizi Başlat' butonuna tıklayın.")