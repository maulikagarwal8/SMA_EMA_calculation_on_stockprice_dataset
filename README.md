## **Problem Statement**

This is a 2-year historical dataset containing daily stock prices for 10 unique symbols (ticker) in a single CSV file. Goal is to develop a script that:
1. Converts the data from daily to monthly frequency.
2. Calculates SMA 10 , SMA 20 and EMA 10 & EMA 20. 
3. Creates individual files for each stock symbol.


## Formulae used for SMA And EMA calculation

*Simple Moving Average(SMA)*\
Formula: Sum of closing prices (over 'N' periods) / Number of periods (N).\
Example (5-day SMA): (Day 1 Close + Day 2 Close + Day 3 Close + Day 4 Close + Day 5 Close) / 5 

*Exponential Moving Average (EMA)*\
Calculate the Multiplier (Smoothing Constant):\
Multiplier = 2 / (Number of Periods + 1).\
(For a 20-day EMA, Multiplier = 2 / (20 + 1) = 0.0952).

Calculate the EMA:\
EMA = (Current Price - Previous Day's EMA) * Multiplier + Previous Day's EMA.\
(For the first EMA, you often use the SMA as the "Previous Day's EMA").