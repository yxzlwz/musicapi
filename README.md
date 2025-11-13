# MusicAPI

**Update: NetEase Music is unavailable.**

This is a Pypi package which can get music's source url from [music.qq.com](https://music.qq.com/) or [music.163.com](https://music.163.com/) with name or id.

The project is released on [pypi.org](), you can view it at [https://pypi.org/project/musicapi/](https://pypi.org/project/musicapi/).

## Install

Just install it with pip as usual.

```bash
pip3 install musicapi
```

## Usage

Import this package:

```python
import musicapi
import musicapi.qq
import musicapi.wyy
```

The followings are the example for QQ Music, if you're a user at NetEase Cloud Music, use `wyy` instead of `qq`.

### Get Music By ID

```python
import musicapi

print(musicapi.qq.get_by_id("0029B8mN2eOjhw"))
```

if the function successfully get the url, the function will return it in string; if it's not able to get(like it requires VIP), then the function will return None.

**How can I get the ID?**

First, get the music page's url from the website.

For QQ Music, it should be like `https://y.qq.com/n/ryqq/songDetail/<str:id>` (e.g. In `https://y.qq.com/n/ryqq/songDetail/0029B8mN2eOjhw`, the ID is `0029B8mN2eOjhw`).

For NetEase Cloud Music, it should be like `https://music.163.com/#/song?id=<str:id>` (e.g. In `https://music.163.com/#/song?id=1368754688`, the ID is `1368754688`)

### Get Music By Name

```
import musicapi

print(musicapi.qq.get_by_name("爱人错过"))
```

In this function, the programme will try to get top 10 music items from the search result of the website, and try to find the first one whose url is able to get, and then return the url in string. If all top 10 music items are unavailable, it will return None.

The search result depend on algorithms at the official website, so it is able to search with the name of the singer or the album in theory. But we strongly recommend you just use the music's name to search, for we don't know which kind of arrangement will be returned if you search with other informations.

## Contact

See [yxzlwz](https://github.com/yxzlwz)
