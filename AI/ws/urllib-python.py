# -*- coding: utf-8 -*-
import urllib.request
# used to parse values into the url
import urllib.parse

#x = urllib.request.urlopen('https://www.google.com/')
#print(x.read())

'''
# this return a method no aloowed
url = 'https://www.google.com/search'
values = {'q' : 'python programming tutorials'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
req.add_header('User-agent', 'adrtests')
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''

'''
# this is foebidden
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    saveFile = open('data/noheaders.txt', 'w')
    saveFile.write(str(x.read()))
    saveFile.close()
except Exception as e:
    print(str(e))
'''

try:
    url = 'https://www.google.com/search?q=python'
    # this headres tell for google that we are humans
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) "
    "AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 "
    "Safari/537.17"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('data/withHeadres.txt', 'w')
    saveFile.write(str(respData))
except Exception as e:
    print(str(e))