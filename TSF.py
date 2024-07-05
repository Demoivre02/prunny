import pandas as pd
import numpy as np


dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
ts = pd.Series(np.random.randn(len(dates)), index=dates)

def simple_stationarity_check(timeseries):
    rolling_mean = timeseries.rolling(window=7).mean()
    rolling_std = timeseries.rolling(window=7).std()
    
    print('Results of simple stationarity check:')
    print(f'Original series mean: {timeseries.mean():.4f}, std: {timeseries.std():.4f}')
    print(f'Rolling mean range: {rolling_mean.min():.4f} to {rolling_mean.max():.4f}')
    print(f'Rolling std range: {rolling_std.min():.4f} to {rolling_std.max():.4f}')
    
    if (rolling_mean.max() - rolling_mean.min()) < 0.1 * timeseries.std():
        print("The time series might be stationary")
    else:
        print("The time series might be non-stationary")


def apply_differencing(timeseries):
    return timeseries.diff().dropna()

print("Original Time Series:")
simple_stationarity_check(ts)

print("\nAfter Differencing:")
differenced_ts = apply_differencing(ts)
simple_stationarity_check(differenced_ts)
