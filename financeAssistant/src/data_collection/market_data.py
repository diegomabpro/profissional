import yfinance as yf
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

def get_yahoo_data(ticker, period="1mo"):
    """
    Coleta dados do Yahoo Finance.
    """
    asset = yf.Ticker(ticker)
    data = asset.history(period=period)
    return data

def get_alpha_vantage_data(api_key, ticker):
    """
    Coleta dados da Alpha Vantage (para informações adicionais).
    """
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, _ = ts.get_quote_endpoint(symbol=ticker)
    return data

def get_futures_data():
    """
    Coleta dados de contratos futuros (mini índice, mini dólar, ouro).
    """
    futures = {
        "WIN$": "Mini Índice",
        "WDO$": "Mini Dólar",
        "GC=F": "Ouro"
    }
    data = {}
    for ticker, name in futures.items():
        data[name] = get_yahoo_data(ticker)
    return data

def get_ibovespa_assets():
    """
    Retorna a lista de ativos que compõem o Ibovespa.
    """
    # Exemplo de ativos do Ibovespa (lista completa pode ser obtida via API ou manualmente)
    ibovespa_assets = {
        "PETR4.SA": "Petrobras",
        "VALE3.SA": "Vale",
        "ITUB4.SA": "Itaú Unibanco",
        "BBDC4.SA": "Bradesco",
        "BBAS3.SA": "Banco do Brasil",
        "B3SA3.SA": "B3",
        "ABEV3.SA": "Ambev",
        "WEGE3.SA": "Weg",
        "JBSS3.SA": "JBS",
        "RENT3.SA": "Localiza"
    }
    return ibovespa_assets