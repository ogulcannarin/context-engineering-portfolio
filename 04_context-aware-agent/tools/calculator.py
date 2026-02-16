def calculate(expression: str):
    """Evaluates a mathematical expression safely."""
    try:
        # Güvenli eval için sadece matematiksel operatörlere izin ver
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            return "Hata: Sadece matematiksel işlemler (+, -, *, /, parantez) kullanılabilir."
        
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Hesaplama hatası: {str(e)}"