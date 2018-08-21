import re
import urllib.request
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, num_retries=2):
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Error: ', e.reason)
        # not always code exists
        try:
            print(e.code)
        except Exception as error:
            print(error.args)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries - 1)

    return html

print(download('http://httpstat.us/500'))