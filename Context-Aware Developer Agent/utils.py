import re

def prune_python_code(code: str) -> str:
    """Yorumları ve gereksiz boşlukları silerek bilgi yoğunluğunu artırır."""
    # Tek satırlı yorumları sil
    code = re.sub(r'#.*', '', code)
    # Fazla boş satırları teke indir
    code = re.sub(r'\n\s*\n', '\n', code)
    return code.strip()

def count_tokens(text: str) -> int:
    """1 token ≈ 4 karakter mantığıyla kabaca hesaplama yapar."""
    return len(text) // 4

def calculate_savings(original_tokens: int, pruned_tokens: int):
    """Maliyet tasarrufunu hesaplar."""
    price_per_1k = 0.005 # GPT-4o birim fiyatı
    orig_cost = (original_tokens / 1000) * price_per_1k
    opt_cost = (pruned_tokens / 1000) * price_per_1k
    savings = orig_cost - opt_cost
    return round(orig_cost, 4), round(opt_cost, 4), round(savings, 4)