import os

import threadpool
from datetime import time

from html_dloader import HtmlDLoader
from html_outputer import HtmlOutputer
from html_parser import HtmlParser
from url_manager import UrlManager


class GrabMain(object):
    def __init__(self, url):
        self.root_url = url
        self.urlManager = UrlManager()
        self.dLoader = HtmlDLoader()
        self.contParser = HtmlParser()
        self.contOutputer = HtmlOutputer()
        pass

    def grabText(self):
        if self.root_url is None:
            return
        self.urlManager.add_new_next_url(self.root_url)
        self.contParser.parser_set(None, None, None, None, None)
        while self.urlManager.get_new_next_count():
            try:
                new_url = self.urlManager.get_new_next_url()
                html_cont = self.dLoader.download(new_url)
                urls, nexts = self.contParser.parser_text_urls(html_cont)
                self.urlManager.add_new_next_urls(nexts)
                self.urlManager.add_new_urls(urls)
            except:
                print "url is error."

        pool = threadpool.ThreadPool(10)
        requests = threadpool.makeRequests(self.thread_grabText, self.urlManager.new_urls)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    def thread_grabText(self, url):
        try:
            print "curr url is %s." % url
            html_cont = self.dLoader.download(url)
            title, cont = self.contParser.parser_text_cont(html_cont)
            self.contOutputer.output_cont(title, cont)
        except:
            print "url is %s, error." % url


    def grabImgs(self):
        if self.root_url is None:
            return None
        self.urlManager.add_new_next_url(self.root_url)
        self.contParser.parser_set(None, None, None, None, None)
        while self.urlManager.get_new_next_count():
            try:
                new_url = self.urlManager.get_new_next_url()
                html_cont = self.dLoader.download(new_url)
                urls, nexts = self.contParser.parser_text_urls(html_cont)
                self.urlManager.add_new_next_urls(nexts)
                self.urlManager.add_new_urls(urls)
            except:
                print "url is error."

        pool = threadpool.ThreadPool(10)
        requests = threadpool.makeRequests(self.thread_grabImg, self.urlManager.new_urls)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    def thread_grabImg(self, url):
        try:
            print "curr url is %s." % url
            html_cont = self.dLoader.download(url)
            title, links = self.contParser.parser_img_cont(html_cont)
            if links is None or len(links) == 0:
                print "url is %s, not src." % url
                return None

            if title is None:
                title = time.time()
            try:
                if not os.path.isdir(title):
                    os.mkdir(title)
            except:
                title = time.time()
                if not os.path.isdir(title):
                    os.mkdir(title)

            params = []
            index = 0
            for link in links:
                params.append(([title, link, index], None))
                index += 1

            pool = threadpool.ThreadPool(12)
            requests = threadpool.makeRequests(self.contOutputer.output_img, params)
            [pool.putRequest(req) for req in requests]
            pool.wait()
        except:
            print "url is %s, error." % url

if __name__ == "__main__":
    obj = GrabMain("")
    obj.grabImgs()
    pass