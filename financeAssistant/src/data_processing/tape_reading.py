import pandas as pd

class TapeReading:
    def __init__(self, order_book, trade_data):
        """
        Inicializa o módulo de Tape Reading.
        :param order_book: DataFrame com o livro de ordens (bid/ask).
        :param trade_data: DataFrame com o histórico de negociações.
        """
        self.order_book = order_book
        self.trade_data = trade_data

    def analyze_order_flow(self):
        """
        Analisa o fluxo de ordens (compra vs. venda) no livro de ofertas.
        """
        bid_volume = self.order_book['bid_volume'].sum()
        ask_volume = self.order_book['ask_volume'].sum()

        if bid_volume > ask_volume:
            return "Mais pressão de compra (Buy Pressure)"
        elif ask_volume > bid_volume:
            return "Mais pressão de venda (Sell Pressure)"
        else:
            return "Equilíbrio entre compra e venda (Balanced)"

    def analyze_trade_flow(self, lookback=10):
        """
        Analisa o fluxo de negociações (trades) para identificar tendências.
        :param lookback: Número de negociações recentes a serem consideradas.
        """
        recent_trades = self.trade_data.tail(lookback)
        buy_trades = recent_trades[recent_trades['side'] == 'buy']
        sell_trades = recent_trades[recent_trades['side'] == 'sell']

        buy_volume = buy_trades['volume'].sum()
        sell_volume = sell_trades['volume'].sum()

        if buy_volume > sell_volume:
            return "Mais volume de compra (Buy Volume Dominance)"
        elif sell_volume > buy_volume:
            return "Mais volume de venda (Sell Volume Dominance)"
        else:
            return "Volume equilibrado (Balanced Volume)"

    def detect_large_orders(self, threshold=1000):
        """
        Detecta ordens grandes no livro de ofertas.
        :param threshold: Volume mínimo para considerar uma ordem como "grande".
        """
        large_bids = self.order_book[self.order_book['bid_volume'] >= threshold]
        large_asks = self.order_book[self.order_book['ask_volume'] >= threshold]

        return {
            "large_bids": large_bids,
            "large_asks": large_asks
        }

    def detect_block_trades(self, threshold=5000):
        """
        Detecta negociações grandes (block trades) no histórico de trades.
        :param threshold: Volume mínimo para considerar uma negociação como "block trade".
        """
        block_trades = self.trade_data[self.trade_data['volume'] >= threshold]
        return block_trades

    def get_market_sentiment(self):
        """
        Combina análise de fluxo de ordens e negociações para determinar o sentimento do mercado.
        """
        order_flow = self.analyze_order_flow()
        trade_flow = self.analyze_trade_flow()

        if "Buy" in order_flow and "Buy" in trade_flow:
            return "Sentimento de Alta (Bullish)"
        elif "Sell" in order_flow and "Sell" in trade_flow:
            return "Sentimento de Baixa (Bearish)"
        else:
            return "Sentimento Neutro (Neutral)"

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de dados do livro de ordens (order book)
    order_book = pd.DataFrame({
        'bid_price': [100, 99, 98],
        'bid_volume': [500, 300, 200],
        'ask_price': [101, 102, 103],
        'ask_volume': [400, 600, 700]
    })

    # Exemplo de dados de negociações (trades)
    trade_data = pd.DataFrame({
        'price': [100, 101, 100, 99, 101],
        'volume': [200, 150, 300, 100, 500],
        'side': ['buy', 'sell', 'buy', 'sell', 'buy']  # 'buy' ou 'sell'
    })

    # Inicializa o Tape Reading
    tape_reader = TapeReading(order_book, trade_data)

    # Análises
    order_flow = tape_reader.analyze_order_flow()
    trade_flow = tape_reader.analyze_trade_flow()
    large_orders = tape_reader.detect_large_orders()
    block_trades = tape_reader.detect_block_trades()
    market_sentiment = tape_reader.get_market_sentiment()

    # Resultados
    print(f"Fluxo de Ordens: {order_flow}")
    print(f"Fluxo de Negociações: {trade_flow}")
    print(f"Ordens Grandes: {large_orders}")
    print(f"Block Trades: {block_trades}")
    print(f"Sentimento do Mercado: {market_sentiment}")