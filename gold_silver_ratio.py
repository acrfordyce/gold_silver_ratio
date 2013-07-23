#!/usr/bin/env python

import urllib
import re
import string

commodities_url = "http://money.cnn.com/data/commodities/"
commodities_content = urllib.urlopen(commodities_url).read()

m = re.compile(r'<strong>Gold.*?\n.*?\n.*?\n.*?\n.*?last_-1">(.*?)<')
n = re.compile(r'<strong>Silver.*?\n.*?\n.*?\n.*?\n.*?last_-1">(.*?)<')

commodities_prices = []

gold_price = m.finditer(commodities_content)
silver_price = n.finditer(commodities_content)

for match in gold_price:
    commodities_prices.append(match.group(1))
    
for match in silver_price:
    commodities_prices.append(match.group(1))

for i in range(len(commodities_prices)):
    commodities_prices[i] = string.replace(commodities_prices[i], ',', '')
        
gold_price = float(commodities_prices[0])
silver_price = float(commodities_prices[1])

gold_silver_ratio = gold_price/silver_price

print "Today's gold to silver ratio is: ", gold_silver_ratio
