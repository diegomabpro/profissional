from data_processing.technical_analysis import (
    identify_trend, calculate_rsi, calculate_macd, calculate_moving_average
)

def trend_following_strategy(data):
    """
    Estratégia de seguir a tendência (trend following).
    """
    trend = identify_trend(data)
    if trend == "Uptrend":
        return "Buy"
    elif trend == "Downtrend":
        return "Sell"
    else:
        return "Hold"

def mean_reversion_strategy(data, rsi_threshold=30):
    """
    Estratégia de reversão à média (mean reversion).
    """
    rsi = calculate_rsi(data).iloc[-1]
    if rsi < rsi_threshold:
        return "Buy"
    elif rsi > (100 - rsi_threshold):
        return "Sell"
    else:
        return "Hold"

def macd_crossover_strategy(data):
    """
    Estratégia de crossover do MACD.
    """
    macd, macdsignal, _ = calculate_macd(data)
    if macd.iloc[-1] > macdsignal.iloc[-1] and macd.iloc[-2] <= macdsignal.iloc[-2]:
        return "Buy"
    elif macd.iloc[-1] < macdsignal.iloc[-1] and macd.iloc[-2] >= macdsignal.iloc[-2]:
        return "Sell"
    else:
        return "Hold"