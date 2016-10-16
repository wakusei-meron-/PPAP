#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import domain
from itertools import chain

BASE_URL = 'https://www.googleapis.com/customsearch/v1'#?key=AIzaSyA1n6G5_ZDAXyEQpkRO-MpPwGWSYDvYVoU&cx=017028400548203066578:uuq01vmwwue'
API_KEY = 'AIzaSyA1n6G5_ZDAXyEQpkRO-MpPwGWSYDvYVoU'
ENGINE_ID = '017028400548203066578:uuq01vmwwue'
INTEGRATED_ID = 3

def flatten2(L):
  if isinstance(L, list):
    return reduce(lambda a,b: a + flatten(b), L, [])
  else:
    return [L]

def find(keyword):
  """ 画像一覧の取得
  @prams keyword: 検索すキーワード
  @returns Imageの配列
  """
  url = '{}?key={}&cx={}&q={}'.format(BASE_URL, API_KEY, ENGINE_ID, keyword)
  req = urllib2.Request(url)
  res = urllib2.urlopen(req).read()
  dictObj = json.loads(res)
  items = dictObj['items']
  pagemaps = [item['pagemap'] for item in items]
  cse_images = [ pagemap['cse_image'] for pagemap in pagemaps if (pagemap.has_key('cse_image'))]
  cse_images_flatten = list(chain.from_iterable(cse_images))
  return [domain.Image(INTEGRATED_ID, i['src'], -1, -1, 'unknown')for i in cse_images_flatten]

# デバッグ用
if __name__ == '__main__':
  find('hoge')
