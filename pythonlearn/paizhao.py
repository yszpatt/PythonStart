# coding:utf-8
import requests
url = "http://photobuy.jd.com/ai/cv/snapshop"
params = {"imgUrl": (
    None, "http://img10.360buyimg.com/img/jfs/t24556/298/2279438650/19256/c8673529/5b7a85eeN91a8546c.jpg"), "token": (None, "abcdefgh")}
res = requests.post(url, files=params)
print(res.text)
