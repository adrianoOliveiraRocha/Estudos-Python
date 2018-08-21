# -*- coding: utf-8 -*-
import re
import urllib.request
from urllib.parse import urljoin
from urllib.error import (URLError, HTTPError,
                          ContentTooShortError)
import re


def download(url, user_agent='wswp', num_retries=2,
             charset='utf-8'):
    print('Downloading url: ', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)
    return html


def link_crawler(start_url, link_regex):
    crawler_queue = [start_url]
    while crawler_queue:
        url = crawler_queue.pop()
        html = download(url)
        if html is not None:
            continue
        for link in get_links(html):
            if re.match(link_regex, link):
                crawler_queue.append(link)
