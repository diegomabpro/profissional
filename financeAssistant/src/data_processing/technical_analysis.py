import pandas as pd
import talib

def identify_trend(data, lookback=20):
    """
    Identifica a tendência do mercado.
    """
    highs = data['High'].rolling(window=lookback).max()
    lows = data['Low'].rolling(window=lookback).min()

    if highs.iloc[-1] > highs.iloc[-2] and lows.iloc[-1] > lows.iloc[-2]:
        return "Uptrend"
    elif highs.iloc[-1] < highs.iloc[-2] and lows.iloc[-1] < lows.iloc[-2]:
        return "Downtrend"
    else:
        return "Range"

def calculate_rsi(data, period=14):
    """
    Calcula o RSI (Relative Strength Index).
    """
    return talib.RSI(data['Close'], timeperiod=period)

def calculate_macd(data, fastperiod=12, slowperiod=26, signalperiod=9):
    """
    Calcula o MACD (Moving Average Convergence Divergence).
    """
    macd, macdsignal, macdhist = talib.MACD(
        data['Close'], fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod
    )
    return macd, macdsignal, macdhist

def calculate_moving_average(data, period=20):
    """
    Calcula a média móvel simples (SMA).
    """
    return talib.SMA(data['Close'], timeperiod=period)

def calculate_bollinger_bands(data, period=20, nbdevup=2, nbdevdn=2):
    """
    Calcula as Bandas de Bollinger.
    """
    upper, middle, lower = talib.BBANDS(
        data['Close'], timeperiod=period, nbdevup=nbdevup, nbdevdn=nbdevdn
    )
    return upper, middle, lower