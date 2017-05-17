import urllib2

import pycurl as pycurl
from cStringIO import StringIO

import certifi


class HtmlDLoader:
    def __init__(self):
        pass

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url, timeout=20)
        if 200 != response.getcode():
            return None
        return response.read()

    def download_CURL(self, url):
        buf = StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.CONNECTTIMEOUT, 60)
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()

        cont = None
        if 200 == c.getinfo(pycurl.RESPONSE_CODE):
            cont = buf.getvalue()
        else:
            cont = None
        c.close()
        return cont
