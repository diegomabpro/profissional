def format_currency(value):
    """
    Formata um valor como moeda.
    """
    return f"R$ {value:,.2f}"

def validate_ticker(ticker):
    """
    Valida se um ticker está no formato correto.
    """
    return isinstance(ticker, str) and len(ticker) >= 3