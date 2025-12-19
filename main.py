import pandas as pd

def load_data(file_path:str):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['ticker', 'date'])
    return df

def daily_to_monthly(df:pd.DataFrame):
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    monthly = df.groupby(['ticker', 'year', 'month']).agg({
        'open': 'first',
        'close': 'last',     
        'high': 'max',
        'low': 'min'
    })
    monthly=monthly.reset_index()
    return monthly

def calculate_ema_sma(month_df:pd.DataFrame):
    closes = month_df['close'].tolist()
    sma_10 = []
    sma_20 = []
    ema_10 = []
    ema_20 = []
    multiplier_10 = 2/(10 + 1)
    multiplier_20 = 2/(20 + 1)

    for i in range(len(closes)):
        if i+1 >= 10:
            sma_10.append(sum(closes[i-9:i+1])/10)
        else:
            sma_10.append(None)

        if i + 1 >= 20:
            sma_20.append(sum(closes[i-19:i+1]) / 20)
        else:
            sma_20.append(None)

    for i in range(len(closes)):
        if i == 9:
            ema_10.append(sum(closes[:10])/10)
        elif i > 9:
            ema_val = (closes[i] - ema_10[-1]) * multiplier_10 + ema_10[-1]
            ema_10.append(ema_val)
        else:
            ema_10.append(None)

        if i == 19:
            ema_20.append(sum(closes[:20])/20)
        elif i > 19:
            ema_val = (closes[i] - ema_20[-1]) * multiplier_20 + ema_20[-1]
            ema_20.append(ema_val)
        else:
            ema_20.append(None)

    month_df['SMA_10'] = sma_10
    month_df['SMA_20'] = sma_20
    month_df['EMA_10'] = ema_10
    month_df['EMA_20'] = ema_20
    return month_df

def create_files(df:pd.DataFrame):
    tickers = df['ticker'].unique()
    for ticker in tickers:
        ticker_df = df[df['ticker'] == ticker]
        month_df = daily_to_monthly(ticker_df)
        month_df = calculate_ema_sma(month_df)
        month_df = month_df.reset_index()

        file_name = f"result_{ticker}.csv"
        month_df.to_csv(file_name, index=False)
        print(f"{file_name} created successfully.")

if __name__ == "__main__":
    input_file = "./dataset.csv"
    df = load_data(input_file)
    create_files(df)
