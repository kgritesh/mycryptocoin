# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division

import math
import requests


class UnocoinScraper(object):
    HEADERS = {
        'Referer': 'https://www.unocoin.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/60.0.3112.90 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    BUY_URL = 'https://www.unocoin.com/signup?buycurrencyrate=0'
    SELL_URL = 'https://www.unocoin.com/signup?sellcurrencyrate=0'

    def scrape(self):
        buy_price = self.get_buy_price()
        sell_price = self.get_sell_price()
        print(f'Buy Price: {buy_price}\nSell Price: {sell_price}')
        return buy_price, sell_price

    def get_buy_price(self):
        resp = requests.get(self.BUY_URL, headers=self.HEADERS)
        return self._parse_resp(resp.text)

    def get_sell_price(self):
        resp = requests.get(self.SELL_URL, headers=self.HEADERS)
        return self._parse_resp(resp.text)

    def _parse_resp(self, content):
        parts = content.split(',')
        btc_usd = float(parts[0])
        usd_inr = float(parts[1])
        fee_rate = float(parts[2]) / 100
        tax_rate = float(parts[3]) / 100
        actual_amount = btc_usd * usd_inr
        fee = math.ceil(fee_rate * actual_amount)
        tax = fee * tax_rate
        return actual_amount + fee + tax







        return btc_usd * usd_inr







