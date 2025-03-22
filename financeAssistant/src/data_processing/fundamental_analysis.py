def calculate_pe_ratio(price, earnings):
    """
    Calcula o índice P/L (Preço/Lucro).
    """
    return price / earnings

def calculate_p_vpa(price, book_value):
    """
    Calcula o índice P/VPA (Preço/Valor Patrimonial por Ação).
    """
    return price / book_value

def calculate_dividend_yield(dividends, price):
    """
    Calcula o Dividend Yield (DY).
    """
    return (dividends / price) * 100

def calculate_roe(net_income, equity):
    """
    Calcula o Retorno sobre o Patrimônio Líquido (ROE).
    """
    return (net_income / equity) * 100