import os
import json
import shutil # Klasör silme işlemleri için
from git import Repo # GitHub reposunu klonlamak için
from utils import prune_python_code, count_tokens

class ProjectIngestor:
    def __init__(self, project_path):
        self.project_path = project_path
        self.context_data = []

    def download_github_repo(self, repo_url):
        """
        GitHub reposunu geçici bir klasöre klonlar.
        """
        temp_dir = "temp_repo"
        
        # Eğer klasör zaten varsa, temiz bir başlangıç için önce sileriz
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
        
        # Repoyu klonla
        Repo.clone_from(repo_url, temp_dir)
        
        # Tarama yapılacak yolu geçici klasör olarak ayarla
        self.project_path = temp_dir
        return temp_dir

    def scan_project(self):
        """
        Projeyi tarar, kodları budar (Pruning) ve bağlam verisini hazırlar.
        """
        self.context_data = [] # Her analizde listeyi sıfırla
        
        for root, dirs, files in os.walk(self.project_path):
            # Gereksiz ve çok yer kaplayan klasörleri atla
            if any(x in root for x in ['venv', '.git', '__pycache__', 'node_modules']):
                continue
                
            for file in files:
                if file.endswith(".py"): # Sadece Python dosyalarına odaklan
                    full_path = os.path.join(root, file)
                    
                    try:
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            
                            # David Kimai: Information Density artırımı için budama işlemi
                            clean_content = prune_python_code(content)
                            
                            # Bağlam verisini oluştur
                            self.context_data.append({
                                "file_path": os.path.relpath(full_path, self.project_path),
                                "content": clean_content,
                                "original_tokens": count_tokens(content),
                                "optimized_tokens": count_tokens(clean_content)
                            })
                    except Exception as e:
                        print(f"Hata: {file} okunamadı. {e}")
                        
        return self.context_data

    def save_context(self, output_file="project_context.json"):
        """
        Hazırlanan bağlamı JSON olarak kaydeder.
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.context_data, f, indent=4)