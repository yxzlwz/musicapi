import json

from fake_useragent import UserAgent
from requests import *

ua = UserAgent()

id_cache = {}
name_cache = {}


def get_by_id(id):
    # if id_cache.get(id):
    #     return id_cache[id]
    r = post(
        "http://u.y.qq.com/cgi-bin/musicu.fcg?_=1587960702731",
        headers={
            "User-Agent": ua.random,
            "Content-Type": "text/plain;charset=UTF-8",
            "Connection": "close",
        },
        data=
        '{"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"4220211900","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":0,"platform":"23","h5to":"speed"}},"comm":{"g_tk":5381,"uin":0,"format":"json","platform":"h5"}}'
        % id,
    )
    purl = r.json()["req_0"]["data"]["midurlinfo"][0]["purl"]
    if purl:
        id_cache[id] = f"http://ws.stream.qqmusic.qq.com/{purl}"
        return id_cache[id]
    return None


def get_by_name(name):
    # if name_cache.get(name):
    #     return name_cache[name]
    r = get(
        f"https://c.y.qq.com/soso/fcgi-bin/client_search_cp?w={name}&n=10&p=1&aggr=1&lossless=0&cr=1&t=0"
    )
    for i in json.loads(r.text[9:-1])["data"]["song"]["list"]:
        url = get_by_id(i["songmid"])
        if url:
            name_cache[name] = url
            return url
    return None
