#!/usr/bin/env python

import http.client
import json

# Adjust these number to suit your needs
buy_silver_ratio_min = 66
buy_gold_ratio_max = 40

payload = ''
headers = {
  'x-access-token': 'goldapi-dwpk2uki92tuzg-io',
  'Content-Type': 'application/json'
}
conn = http.client.HTTPSConnection("www.goldapi.io")

# Get current silver price.
conn.request("GET", "/api/XAG/USD", payload, headers)
res = conn.getresponse()
data = json.loads(res.read().decode("utf-8"))
silver_price = data['price']

# Get current gold price.
conn.request("GET", "/api/XAU/USD", payload, headers)
res = conn.getresponse()
data = json.loads(res.read().decode("utf-8"))
gold_price = data['price']

gold_silver_ratio = round(gold_price/silver_price, 2)

print(f"Today's gold to silver ratio is: {gold_silver_ratio}")
if gold_silver_ratio >= buy_silver_ratio_min:
    print("Buy Silver!")
elif buy_gold_ratio_max <= gold_silver_ratio > buy_silver_ratio_min:
    print("Hang tight.  Don't buy either.")
elif gold_silver_ratio < buy_gold_ratio_max:
    print("Buy Gold!")
