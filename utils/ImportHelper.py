def importAll():
    # import statements
    from typing import Tuple, Union, List, Any

    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    # import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import plotly.io as pio
    from numpy import ndarray
    from pandas import DataFrame, Series

    from utils.OHLC_Helper import getAlphaOHLC

    sns.set_theme(color_codes=True)
    import statsmodels.api as sm
    from sklearn.linear_model import LinearRegression
    import yfinance as yf
    from alpha_vantage.techindicators import TechIndicators
    from alpha_vantage.timeseries import TimeSeries
    import talib
    sns.set_theme(color_codes=True)
    API_KEY = 'EC1W3AWVDZ3LA1T8'
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    sns.set(rc={'figure.figsize': (30, 9)})