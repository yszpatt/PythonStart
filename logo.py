# encoding:utf-8
import base64
import urllib
import urllib2

'''
logo商标识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"

# 二进制方式打开图片文件
f = open('[本地文件]', 'rb')
img = base64.b64encode(f.read())

params = {"custom_lib": True, "image": img}
params = urllib.urlencode(params)

access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print(content)
