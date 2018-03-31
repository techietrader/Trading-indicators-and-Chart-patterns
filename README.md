I have written Python codes for an indicator and a couple of Advance Chart patterns.
1.	Indicators: -SuperTrend, ATR
2.	Chart Patterns: - Heiken Ashi, Renko

<b>A Supertrend</b> is a trend following indicator similar to moving averages. It is plotted on price and the current trend can simply be determined by its placement vis-a-vis price. It is a very simple indicator and constructed with the help of just two parameters- period and multiplier.
It can be used in conjunction with any other indicator, something like a Crossover with a moving average or as a standalone with any chart pattern.
You can find some cool videos on it on Youtube- https://www.youtube.com/results?search_query=supertrend


<b>Heiken-Ashi Candlesticks</b> are an offshoot from Japanese candlesticks. Heiken-Ashi Candlesticks use the open-close data from the prior period and the open-high-low-close data from the current period to create a combo candlestick. The resulting candlestick filters out some noise in an effort to better capture the trend.  More can be found out on :- http://stockcharts.com/school/doku.php?id=chart_school:chart_analysis:heikin_ashi

This is how Heiken-Ashi calculated:- 
1. The Heiken-Ashi Close is simply an average of the open, high, low and close for the current period. 

<b>HA-Close = (Open(0) + High(0) + Low(0) + Close(0)) / 4</b>

2. The Heiken-Ashi Open is the average of the prior Heiken-Ashi candlestick open plus the close of the prior Heiken-Ashi candlestick. 

<b>HA-Open = (HA-Open(-1) + HA-Close(-1)) / 2</b> 

3. The Heiken-Ashi High is the maximum of three data points: the current period's high, the current Heiken-Ashi candlestick open or the current Heiken-Ashi candlestick close. 

<b>HA-High = Maximum of the High(0), HA-Open(0) or HA-Close(0) </b>

4. The Heiken-Ashi low is the minimum of three data points: the current period's low, the current Heiken-Ashi candlestick open or the current Heiken-Ashi candlestick close.

<b>HA-Low = Minimum of the Low(0), HA-Open(0) or HA-Close(0) </b>


<b> Renko Bars</b> on the other hand are not like traditional OHLC candles but are more like a user defined size which can possibly be anything. Once price surpasses the top or bottom of previous bar, new renko bar is placed. Renkos are mostly time and noise independent and they don’t have shadows like candlesticks. Renko bars are mostly used in finding support and resistances.  More on them: -
https://www.investopedia.com/terms/r/renkochart.asp


Where to go next:
1.	Fork it and tweak it according to your own use
2.	Try backtesting trading strategies 


<b>Disclaimer:- Use at your own risk</b>
