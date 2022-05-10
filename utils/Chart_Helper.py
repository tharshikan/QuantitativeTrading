from typing import List

import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame


class Ohlc_columns:
    open = 'open'
    high = 'high'
    low = 'low'
    close = 'close'
    volume = 'volume'
def buySellChart(ohlc_df, buy_signal, sell_signal,columns:List[str]=['close']) -> DataFrame:
    transactions = pd.concat([buy_signal, sell_signal], axis=0)
    fig, ax = plt.subplots(figsize=(30, 8))
    # plt.figure(figsize=(42,8))
    plt.plot(ohlc_df['close'])
    plt.plot(ohlc_df['upper'])
    plt.plot(ohlc_df['lower'])
    plt.plot(sell_signal.index, sell_signal['close'], 'ro')
    plt.plot(buy_signal.index, buy_signal['close'], 'go')

    last_buy_date = None
    last_buy_price = None
    profits = []

    for date, row in transactions.iterrows():
        if (row['isSell'] == 1 ):
            profit = row['close'] - last_buy_price
            ax.axvspan(last_buy_date, date, facecolor='g' if profit > 0 else 'r', alpha=0.3)
            profits.append(profit)
        else:
            last_buy_date = date
            last_buy_price = row['close']
    print(f'profits {profits}')
    return transactions

def shortCloseChart(ohlc_df, short_signal, close_signal, columns:List[str]=['close']) -> DataFrame:
    transactions = pd.concat([short_signal, close_signal], axis=0)
    fig, ax = plt.subplots(figsize=(30, 8))
    # plt.figure(figsize=(42,8))
    plt.plot(ohlc_df['close'])
    plt.plot(ohlc_df['upper'])
    plt.plot(ohlc_df['lower'])
    plt.plot(close_signal.index, close_signal['close'], 'ro')
    plt.plot(short_signal.index, short_signal['close'], 'go')

    last_buy_date = None
    last_buy_price = None
    profits = []

    for date, row in transactions.iterrows():
        if (row['isShort'] == 1 ):
            profit = row['close'] - last_buy_price
            ax.axvspan(last_buy_date, date, facecolor='g' if profit > 0 else 'r', alpha=0.3)
            profits.append(profit)
        else:
            last_buy_date = date
            last_buy_price = row['close']
    print(f'profits {profits}')
    return transactions


