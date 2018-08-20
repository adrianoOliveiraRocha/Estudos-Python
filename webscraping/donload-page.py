# -*- coding: utf-8 -*-
import urllib.request
from urllib.error import (URLError, HTTPError, 
                          ContentTooShortError)


def download(url):
    print('Downloading url: ', url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
    return html
        
    
html = download('http://www.yahoo.com')
print(html)
