# stock-analyzer

## Graham Number

The Graham Number is a metric used to determine the fundamental value of a stock and is a useful tool to quickly guage whether a stock may be undervalued. The value is calculated by multiplying the price/earnings (PE) ratio by the price/book value (PBV) of a stock. 

A low PE suggests that the earnings are high, and a low PBV indicates that there is low risk in investing. Therefore, a company that is low risk and high reward will tend to have a lower PE * PBV value. Benjamin Graham sets the threshold for this value for an undervalued company to be at 22.5

## stock-analyzer

Combing through hundreds of stocks and financials to find undervalued stocks can be tedious, so the purpose of this project was to create a script that can automatically retrieved current stock information, calculate the PE * PBV value, and return all of the stock that are below the 22.5 threshold to quickly find potentially undervalued stocks. While all of these stocks may not necessarily be good picks and might be valued low for a reason, it at least gives a good starting point to find stocks that are selling well below their intrinsic price.

### Retrieving Stock Data

To get information about stock PE and PBV values, the IEX Developer API (https://iextrading.com/developer/) is used to pull the most current information about which stocks are listed on the market and their corresponding statistics.
