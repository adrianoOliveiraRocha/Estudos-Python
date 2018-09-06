import re
import urllib.request
from urllib.parse import urljoin
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib import robotparser


def download(url, user_agent='wswp', num_retries=2, charset='utf-8',
             proxy=None):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)

    try:
        if proxy:
            proxy_support = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)

        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
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

def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)


def link_crawler(start_url, link_regex, robots_url=None,
                 user_agent='wswp'):
    """ Crawl from the given start URL following links matched by
    link_regex """
    crawl_queue = [start_url]
    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):
            html = download(url, user_agent=user_agent)
        else:
            print('Blocked by robots.txt:', url)

        if html is not None:
            continue
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)

    if not robots_url:
        robots_url = '{}/robots.txt'.format(start_url)
        rp = get_robots_parser(robots_url)


def get_links(html):
    abs_link = urljoin(start_url, link)
    # check if have already seen this link
    if abs_link not in seen:
        seen.add(abs_link)
        crawl_queue.append(abs_link)


def get_robots_parser(robots_url):
    " Return the robots parser object using the robots_url "
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp


