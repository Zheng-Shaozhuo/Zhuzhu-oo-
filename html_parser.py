import re

from bs4 import BeautifulSoup


class HtmlParser:
    def __init__(self):
        self.parser_target_url = None
        self.parser_htitle = None
        self.parser_hcont = None
        self.parser_page_next = None
        self.parser_target_sub_url = None

    def parser_set(self, target_url, title, cont, page_next, target_sub_url = None):
        self.parser_target_url = target_url
        self.parser_htitle = title
        self.parser_hcont = cont
        self.parser_page_next = page_next
        self.parser_target_sub_url = target_sub_url

    def parser_text_urls(self, html_cont):
        if html_cont is None or 0 == len(html_cont):
            return None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self.parser_get_text_urls(soup, self.parser_target_url)
        page_next = self.parser_get_text_urls(soup, self.parser_page_next)
        return new_urls, page_next

    def parser_text_cont(self, html_cont):
        if html_cont is None or 0 == len(html_cont):
            return None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        title = self.parser_get_cont(soup, self.parser_htitle, 0)
        cont = self.parser_get_cont(soup,self.parser_hcont, 1)
        return title, cont

    def parser_img_cont(self, html_cont):
        if html_cont is None or 0 == len(html_cont):
            return None
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        title = self.parser_get_cont(soup, self.parser_htitle, 0)
        src_urls = self.parser_get_src_urls(soup, self.parser_target_sub_url)
        return title, src_urls

    def parser_get_text_urls(self, soup, parser_url):
        urls = set()
        links = soup.findAll('a', href=re.compile(r"%s" % parser_url))
        for link in links:
            urls.add("%s" % link['href'])
        return urls

    def parser_get_src_urls(self, soup, parser_url):
        urls = set()
        links = soup.find_all('img', src=re.compile(r"%s" % parser_url))
        for link in links:
            urls.add(link['src'])
        return urls

    # flag 0=title, 1=content
    def parser_get_cont(self, soup, parser_cont, flag = 0):
        if 0 == flag:
            title_node = soup.find('title', parser_cont)
            return title_node.get_text()
        elif 1 == flag:
            cont_node = soup.find('div', class_=r"%s" % parser_cont)
            return cont_node.get_text()
        else:
            pass
