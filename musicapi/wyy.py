import json
import random
import time

from fake_useragent import UserAgent
from requests import *

ua = UserAgent()

# 加密相关

import base64
import codecs

from Crypto.Cipher import AES

MODULUS = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
NONCE = b'0CoJUm6Qyw8W8jud'
PUBKEY = b'010001'


def random_str(length):
    return ''.join(
        random.choice('abcdefghijklmnopqrstuvwxyz1234567890')
        for i in range(length))


nnid = random_str(32)
headers = {
    'Origin': 'http://music.163.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://music.163.com',
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4",
    "User-Agent": ua.random,
    "Cookie":
    f"JSESSIONID-WYYY={random_str(176)}:{int(time.time()*1000)}; _iuqxldmzr_=32; _ntes_nnid={nnid},{int(time.time()*1000)}; _ntes_nuid={nnid};",
    "Connection": "keep-alive",
}


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + (chr(pad) * pad).encode()
    encryptor = AES.new(secKey, 2, b'0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(codecs.encode(text, 'hex_codec'), 16)**int(pubKey, 16) % int(
        modulus, 16)
    return format(rs, 'x').zfill(256)


# 接口


def get_by_id(id):
    text = json.dumps({"ids": [id], "br": 999000, "csrf_token": ''})
    secKey = random_str(16).encode()
    encText = aesEncrypt(aesEncrypt(text.encode(), NONCE), secKey)
    encSecKey = rsaEncrypt(secKey, PUBKEY, MODULUS)

    r = post("http://music.163.com/weapi/song/enhance/player/url",
             headers=headers,
             data={
                 "params": encText,
                 "encSecKey": encSecKey
             })

    return r.json()["data"][0]["url"]


def get_by_name(name):
    text = '{"s":"%s","type":"1","limit":1,"offset":0}' % name
    secKey = random_str(16).encode()
    encText = aesEncrypt(aesEncrypt(text.encode(), NONCE), secKey)
    encSecKey = rsaEncrypt(secKey, PUBKEY, MODULUS)
    r = post("http://music.163.com/weapi/cloudsearch/get/web?csrf_token=",
             headers=headers,
             data={
                 "params": encText,
                 "encSecKey": encSecKey
             })
    for i in r.json()["result"]["songs"]:
        url = get_by_id(i["id"])
        if url:
            return url
    return None
