#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
import domain

BASE_URL = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search?mkt=en-us'
AUTH_KEY = 'Ocp-Apim-Subscription-Key'
API_KEY = '207378cc6de84a5799367835c4889df2'
INTEGRATED_ID = 1


def find(keyword, offset, count, mkt):
    """ 画像一覧の取得
    @params keyword: 検索キーワード
    @params offset: オフセット
    @params count: 取得件数
    @params mkt: 国の指定などのマーケット(ex. ja-JP)
    @returns Imageの配列
    """
    url = '{}&q={}&offset={}&count={}&mkt={}'.format(BASE_URL, keyword, offset, count, mkt)
    req = urllib2.Request(url)
    req.add_header(AUTH_KEY, API_KEY)
    res = urllib2.urlopen(req).read()
    dictObj = json.loads(res)
    imgs = [domain.Image(INTEGRATED_ID, v['contentUrl'], v['width'], v[
                         'height'], v['contentSize'])for v in dictObj['value']]
    return imgs

# デバッグ用
if __name__ == '__main__':
    find('hoge')
