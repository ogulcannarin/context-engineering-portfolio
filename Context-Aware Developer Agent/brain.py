import json
from openai import OpenAI  # OpenAI kütüphanesini kurman gerekir: pip install openai

class ContextBrain:
    def __init__(self, context_file="project_context.json", api_key=None):
        try:
            with open(context_file, 'r') as f:
                self.project_data = json.load(f)
        except:
            self.project_data = []
        
        # API Bağlantısı
        self.client = OpenAI(api_key=api_key) if api_key else None

    def get_relevant_code(self, query):
        """Dinamik Bağlam: Soruyla ilgili kodları seçer."""
        relevant_parts = []
        for file in self.project_data:
            if any(word.lower() in file['file_path'].lower() for word in query.split()):
                relevant_parts.append(f"--- DOSYA: {file['file_path']} ---\n{file['content']}")
        return "\n\n".join(relevant_parts)

    def ask(self, user_query):
        if not self.client:
            return "Lütfen geçerli bir API anahtarı girin."

        related_code = self.get_relevant_code(user_query)
        
        # David Kimai: 'Information Density' yüksek bir system prompt
        system_prompt = (
            "Sen uzman bir yazılım geliştiricisin. Sana sağlanan kod parçaları "
            "yorum satırlarından arındırılmış ve optimize edilmiştir. "
            "Sadece verilen bağlama dayanarak teknik ve kısa cevaplar ver."
        )
        
        user_prompt = f"BAĞLAM (KODLAR):\n{related_code}\n\nSORU: {user_query}"

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini", # Hem ucuz hem hızlı, portfolyo için ideal
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Hata oluştu: {str(e)}"