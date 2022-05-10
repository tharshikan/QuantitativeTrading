from pandas import DataFrame


def getAlphaOHLC(data:DataFrame) -> DataFrame:
    data['Open'] = data['1. open']
    data['High'] = data['2. high']
    data['Low'] = data['3. low']
    data['Close'] = data['4. close']
    data['Volume'] = data['5. volume']
    data.drop(['1. open', '2. high', '3. low', '4. close', '5. volume'], axis=1, inplace=True)
    data.sort_index(inplace=True)
    return data