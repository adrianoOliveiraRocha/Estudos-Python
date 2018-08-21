# -*- coding: utf-8 -*-
import urllib.request
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

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here

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

def get_links(html):
    abs_link = urljoin(start_url, link)
    # check if have already seen this link
    if abs_link not in seen:
        seen.add(abs_link)
        crawler_queue.append(abs_link)

crawl_sitemap('http://example.webscraping.com/sitemap.xml')


