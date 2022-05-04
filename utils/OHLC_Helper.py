from pandas import DataFrame


def getAlphaOHLC(data:DataFrame) -> DataFrame:
    data['open'] = data['1. open']
    data['high'] = data['2. high']
    data['low'] = data['3. low']
    data['close'] = data['4. close']
    data['volume'] = data['5. volume']
    data.drop(['1. open', '2. high', '3. low', '4. close', '5. volume'], axis=1, inplace=True)
    data.sort_index(inplace=True)
    return data