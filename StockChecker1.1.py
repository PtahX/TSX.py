# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:47:21 2016

@author: PtahX
This Script is meant to allow for checking a stock against a group of set values and give them a grading of pass or fail
"""

import time
import urllib.request
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import math
from math import *
import os

clear = lambda: os.system('cls')

StockRank = 0  # start number for later ranking of stocks
def get_marketCap(self):
    ''' 0 Scrape Yahoo for the current Market Cap'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag0 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[0]
    mCap = str(tag0.nextSibling.text)
    return mCap


def get_priceEarn(self):
    '''2 Price to Earnings Yahoo Scrape'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag2 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[2]
    priceEarn = float(tag2.nextSibling.text)
    return priceEarn


def get_priceEarnGrowth(self):
    '''4 Price to Earnings Growth'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag4 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[4]
    peg = float(tag4.nextSibling.text)
    return peg


def get_priceSales(self):
    '''5 Price to Sales Scrape'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag5 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[5]
    priceSales = str(tag5.nextSibling.text)
    return priceSales


def get_priceBook(self):
    '''6 Price to Book Scrape from Yahoo '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag6 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[6]
    pbr = float(tag6.nextSibling.text)
    return pbr


def get_enterpriseValue(self):
    ''' 8 Scrape Yahoo for the current Enterprise Value / EBITDA'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag8 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[8]
    enterpriseValue = str(tag8.nextSibling.text)
    return enterpriseValue


def get_stockName(self):
    '''9 Scrape Full Stock name associated with ticker'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag9 = soup.findAll('h2')[3]
    stockName = str(tag9.text)
    return stockName.title()


def get_netProfit(self):
    '''12	Operating Margin (ttm):8.01% (AKA Net Profit Margin)'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag12 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[12]
    netProfit = str(tag12.nextSibling.text)
    return netProfit


def get_roe(self):
    '''14 Scrape Yahoo for the Current Return on Equity'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag14 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[14]
    roe = str(tag14.nextSibling.text)
    return roe


def get_quarterRevGrowth(self):
    '''index 17 Scrape Yahoo for Quarterly Revenue Growth '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag17 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[17]
    quarterRevGrowth = str(tag17.nextSibling.text)
    return quarterRevGrowth


def get_currentPrice(self):
    '''20 Current Price of Stock'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag20 = soup.findAll('span')[20]  # gets current stock price
    currentPrice = float(tag20.text)
    return currentPrice


def get_earningsPerShare(self):
    '''21 Earnings Per Share Calc '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag21 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[21]
    eps = float(tag21.nextSibling.text)
    return eps


def get_debtEquity(self):
    '''26 Debt to Equity Ratio Scrape '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag26 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[26]
    dToE = float(tag26.nextSibling.text)
    return dToE


def get_currentRatio(self):
    '''27 Current Ratio Yahoo Scrape '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag27 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[27]
    currentRatio = float(tag27.nextSibling.text)
    return currentRatio


def get_bookPerShare(self):
    '''28 Book Value Per Share Calc '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag28 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[28]
    bps = float(tag28.nextSibling.text)
    return bps


def get_leveredFCF(self):
    '''30 levered free cash flow '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag30 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[30]
    leveredFCF = str(tag30.nextSibling.text)
    return leveredFCF


def get_sharesOut(self):
    ''' 40 Shares Outstanding ... ideally (FCF) / (# of shares) / (stock price) = Free Cash Yield goes here '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag40 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[40]
    sharesOut = str(tag40.nextSibling.text)
    return sharesOut


def get_insider(self):
    '''42	% Held by Insiders '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag42 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[42]
    insiders = str(tag42.nextSibling.text)
    return insiders


def get_institutions(self):
    ''' 43	Scrape for % Held by Institutions '''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag43 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[43]
    institutions = str(tag43.nextSibling.text)
    return institutions


def get_dividend(self):
    '''50 Scrape Yahoo for the Current Dividend'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag50 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[50]
    dividend = float(tag50.nextSibling.text)
    return dividend


def get_divYield(self):
    '''51 Scrape Yahoo For the Dividend Yield'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag51 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[51]
    divYield = str(tag51.nextSibling.text)
    return divYield


def get_fiveYearDiv(self):
    '''52 Scrape yahoo for the 5 year Dividend Yield'''
    optionsUrl = "https://ca.finance.yahoo.com/q/ks?s=" + stock
    optionsPage = urlopen(optionsUrl)
    soup = BeautifulSoup(optionsPage, "lxml")  # lxml defined for other sytems in case not running lxml by default
    tag52 = soup.findAll('td', {'class': 'yfnc_tablehead1'})[52]
    fiveYearDiv = str(tag52.nextSibling.text)
    return fiveYearDiv


''' Calculations ***********************************************************'''


def calc_grahamNum(self):
    ''' Graham Number Calculator '''
    grahamNum = round(float(math.sqrt(22.5 * eps * bps)), 2)
    return grahamNum


def calc_sellPrice(self):
    '''Calculate the Suggested price to sell this stock at'''
    grahamSell = float(math.sqrt(22.5 * eps * bps))
    sellPrice = round((float(grahamSell * 1.5)), 2)
    return sellPrice


def calc_fairValue(self):
    grahamSell = float(math.sqrt(22.5 * eps * bps))
    fairValue = round((float(grahamSell * 1.25)), 2)
    return fairValue



def calc_ncav(Self):
    #Net Current Asset Value As Described by Ben Graham - You want 2/3 or 66%
    #of this number as a but Price
    try:
        ncavFairValue= float((currentAssets - totalLiabilities) / sharesOutstanding)
        ncavBuy= float(ncavFairValue * 0.66)
        return ncavBuy
    except:
        print("unable to Calculate the NCAV for this stock")
        print("")
        pass


def main(Self):
    ''' full Stock Name '''
    stockName = get_stockName(stock)
    print('You are doing a check on: ' + str(stockName))
    line()

    '''Current Price'''
    currentPrice = get_currentPrice(stock)
    print(('The Current Stock Price is:$') + ('\t') + str(currentPrice))
    print()

    ''' earnings per share'''
    eps = get_earningsPerShare(stock)
    # Printout under Graham Number below for Console formatting


    ''' book value '''
    bps = get_bookPerShare(stock)
    # Printout under Graham Number below for Console formatting



    '''Graham Number & Fair Value & Sell Price'''
    try:
        grahamNum = calc_grahamNum(stock)
        fairValue = calc_fairValue(stock)
        sellPrice = calc_sellPrice(stock)
        print(('Graham Number is: $') + ('\t') + str(grahamNum))
        print(('The Fair Value of the Stock is: $') + ('\t') + str(fairValue))
        print(('The Price I\'d recommend selling at is: $') + ('\t') + str(sellPrice))

        if currentPrice <= grahamNum:
            print('PASS - This stock appears to be at an excellent buy price at the moment')

        elif fairValue > currentPrice > grahamNum:
            print(
                'CAUTION - The stock is still trading below the the Fair Value price BUT is still a bit expensive to buy at the moment')

        else:
            print('FAIL - This stock is currently not trading at a discount')
        print()

    except:
        print("The Graham Number can not be calculated")
        print("")
        pass

    ''' Earnings Per Share '''
    # defined Earlier
    print(('The Earnings Per Share is') + '\t' + str(eps))
    if eps > 0:
        print('PASS - This Stock Has a Positive Earnings ')
    else:
        print('FAIL - This Stock is currently Failing the Earnings Per Share Requirement')
    print()

    ''' Book Value Per Share'''
    print(('Book Value Per Share is') + '\t' + str(bps))
    print()

    '''Price To Book '''
    pbr = get_priceBook(stock)

    if float(pbr) < 1.5:
        print('PASS - Price to Book is excellent and appears to be selling at a discount!')

    elif 1.5 < float(pbr) < 2.5:
        print('Moderate - Price to Book is alright but getting a bit expensive')

    else:
        print(
            'FAIL - Price to Book is HIGH indicating this is an expensive stock indicate a company with serious underlying problems.')
    print()

    try:
        ''' Price to Earnings '''
        pe = float(get_priceEarn(stock))
        print('Price to Earnings Ratio :' + '\t' + str(pe))
        if 0 < pe < 15:
            print('PASS - Price to earnings is below 15')
        else:
            print('FAILED - Price to Earnings check')
        print()

    except:
        pass

    ''' Price to Earnings Growth'''
    peg = get_priceEarnGrowth(stock)
    print('Price to Earnings Growth Ratio :' + '\t' + str(peg))
    if peg < 1:
        print('PASS - PEG ratio lower than 1 means a stock is below its fair value')
    else:
        print('FAIL - PEG ratio greater than 1 means the stock is relatively expensive')
    print()

    ''' Current Ratio '''
    currentRatio = float(get_currentRatio(stock))
    print(('Current Ratio') + "\t" + str(stock) + "\t" + str(currentRatio))

    if 1.5 < currentRatio < 2.4:
        print('PASS - Current ratio is in a good Range')

    elif currentRatio > 2.4:
        print('CAUTION - The Current Ratio is too high - this may mean the company has some problems')

    else:
        print('FAIL - The Current Ratio is out of an acceptable range')
    print()

    ''' Market Cap'''
    marketCap = get_marketCap(stock)
    mCapStrip = float(marketCap.rstrip("MB"))  # strips the M or B off the back to allow use in calculations

    print(('The Current Market Cap is:') + str(marketCap))
    if mCapStrip > 500:
        print('PASS -  This company is large enough to expect a long future')

    elif 300 < mCapStrip < 500:
        print('CAUTION - This company is a bit small though on the Canadian Market it should still be acceptable')

    else:
        print(
            'FAIL - The Market Cap is out of an acceptable range - if there is a "B" for billion after the Current Market Cap ignore this Fail!')
    print()

    try:
        '''  Debt to Equity'''
        debtEquity = get_debtEquity(stock)
        print(('Debt to Equity Ratio') + "\t" + str(stock) + "\t" + ('is: ') + str(debtEquity))

        if float(debtEquity) < 120:
            print((
                  'PASS - The Debt to Equity Ratio is under 120 which is good Lower numbers are generally preferred because high debt loads can turn into big problems in a downturn.'))
        else:
            print((
                  'FAIL - Debt to equiy ratio is high, this can sometimes be acceptable. Taking on more debt during expansionary times gives a boost to profits. Heavy established industries like utilities and industrials generally have higher debt-equity ratios than rapidly growing companies that may carry little or no debt at all') + (
                  '\t'))
        print()

    except:
        print("The Debt To Equity can not be calculated")
        print("")

    ''' Price to Sales '''
    priceSales = float(get_priceSales(stock))
    print(('Price to Sales Ratio') + "\t" + str(stock) + "\t" + ('is: ') + str(priceSales))

    if float(priceSales) < 1:
        print((
              'PASS - The Price to Sales Ratio ( A very important one) is Excellent however bear in mind the beauty of a low P/S ratio can be spoiled by a constant lack of profitability and large levels of debt.') + (
              '\n'))
    else:
        print((
              'FAIL - The Price to Sales Ratio is HIGH (A very important ratio) - Like other ratios, you should compare the P/S of a stock of those with competitors and with historical sales multiples. Sales are also more difficult to manipulate than earnings, giving a more reliable gauge of value. ') + (
              '\n'))
    print()

    ''' Enterprise Value'''
    enterpriseValue = get_enterpriseValue(stock)
    print(('Enterprise Value / EBITDA for ') + "\t" + str(stock) + "\t" + ('is: ') + str(enterpriseValue))

    if float(enterpriseValue) < 7.5:
        print('PASS')
    else:
        print('FAIL')
    print()






def line():
    print('--------------------------------------------------------------------------')

clear()
''' aquire the users Stock Ticker'''
#Get Users Ticker or Quit
stock = input("Please add ticker here (type 'quit' to stop): ")


if stock == 'quit':
    active = False

else:
    stock = stock.upper()
    print('You are running Steve\'s Stock Analyzer on the stock ticker:' + str(stock))
    active = True

    while active:
        main(stock)
        active = False







# ************************************************************************** TO ADD LATER ***************************************************************************


# also would like the average PE over 10 years
# EPS difference from previous year same quarter (eg 1st quarter 2013 vs 1st quarter 2014)



# Growth Factors
# IS EPS Growing at least 20% per year
# if EPS increases quarter after quater this is called earnings momentum


# print()
# print('##########################################')
# print()
# print()



'''

0	Market Cap (intraday)5:992.79M
1	Enterprise Value (2015-01-26)3:1.06B
2	Trailing P/E (ttm, intraday):9.88
3	Forward P/E (fye 2015-12-31)1:9.04
4	PEG Ratio (5 yr expected)1:1.25
5	Price/Sales (ttm):0.94
6	Price/Book (mrq):2.39
7	Enterprise Value/Revenue (ttm)3:1.01
8	Enterprise Value/EBITDA (ttm)6:9.28
9	Fiscal Year Ends:Dec 31
10	Most Recent Quarter (mrq):2014-09-30
11	Profit Margin (ttm):10.07%
12	Operating Margin (ttm):8.01%
13	Return on Assets (ttm):7.88%
14	Return on Equity (ttm):28.29%
15	Revenue (ttm):1.05B
16	Revenue Per Share (ttm):2.67
17	Qtrly Revenue Growth (yoy):9.50%
18	Gross Profit (ttm):N/A
19	EBITDA (ttm)6:113.70M
20	Net Income Avl to Common (ttm):105.40M
21	Diluted EPS (ttm):0.26
22	Qtrly Earnings Growth (yoy):-84.30%
23	Total Cash (mrq):15.40M
24	Total Cash Per Share (mrq):0.04
25	Total Debt (mrq):78.00M
26	Total Debt/Equity (mrq):18.97
27	Current Ratio (mrq):2.48
28	Book Value Per Share (mrq):1.05
29	Operating Cash Flow (ttm):91.70M
30	Levered Free Cash Flow (ttm):32.30M
31	Beta:N/A
32	52-Week Change3:15.00%
33	S&P500 52-Week Change3:15.17%
34	52-Week High (2015-01-02)3:2.80
35	52-Week Low (2014-10-14)3:1.91
36	50-Day Moving Average3:2.49
37	200-Day Moving Average3:2.38
38	Avg Vol (3 month)3:1,538,400
39	Avg Vol (10 day)3:2,402,110
40	Shares Outstanding5:392.41M
41	Float:391.86M
42	% Held by Insiders1:N/A
43	% Held by Institutions1:N/A
44	Shares Short 3:N/A
45	Short Ratio 3:N/A
46	Short % of Float 3:N/A
47	Shares Short (prior month)3:N/A
48	Forward Annual Dividend Rate4:N/A
49	Forward Annual Dividend Yield4:N/A
50	Trailing Annual Dividend Yield3:0.06
51	Trailing Annual Dividend Yield3:2.40%
52	5 Year Average Dividend Yield4:N/A
53	Payout Ratio4:N/A
54	Dividend Date3:2014-12-19
55	Ex-Dividend Date4:N/A
56	Last Split Factor (new per old)2:N/A
57	Last Split Date3:N/A

'''
