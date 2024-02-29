import os
from binance.client import Client
import time

def check_perpetual_vs_spot(api_key, api_secret, symbol='BTCUSDT'):
    # Initialize Binance client
    client = Client(api_key, api_secret)

    # Get perpetual and spot prices
    ticker = client.get_symbol_ticker(symbol=symbol)
    perpetual_price = float(client.futures_mark_price(symbol=symbol)['markPrice'])
    spot_price = float(ticker['price'])

    # Check if perpetual price is lower than spot price
    if perpetual_price > spot_price:
        return True
    else:
        return False

def execute_trade(api_key, api_secret, symbol='BTCUSDT'):
    # Initialize Binance client
    client = Client(api_key, api_secret)

    # Your trade execution logic here
    # Example: place an order to buy perpetual or sell spot
    # Replace this example with your actual trading logic
    try:
        # Example: place a test order
        order = client.create_test_order(
            symbol=symbol,
            side=Client.SIDE_BUY,
            type=Client.ORDER_TYPE_MARKET,
            quantity=0.001  # Example quantity
        )
        print("Trade executed successfully.")
        return True
    except Exception as e:
        print(f"Trade execution failed: {e}")
        return False

def main():
    # Load API key and secret from environment variables
    api_key = os.environ.get('BINANCE_API_KEY')
    api_secret = os.environ.get('BINANCE_API_SECRET')

    # Attempt trade execution up to 3 times
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        print(f"Attempt {attempts} to execute trade.")
        if check_perpetual_vs_spot(api_key, api_secret):
            if execute_trade(api_key, api_secret):
                break
            else:
                print("Retrying trade...")
                time.sleep(2)  # Wait before retrying
        else:
            print("Perpetual price of BTC is higher than spot price.")
            break
    else:
        print("Max attempts reached. Trade execution failed.")

if __name__ == "__main__":
    main()
