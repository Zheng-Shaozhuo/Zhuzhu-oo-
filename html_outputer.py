import os
from datetime import time

from html_dloader import HtmlDLoader


class HtmlOutputer:
    def __init__(self):
        self.dLoader = HtmlDLoader()
        pass

    def output_cont(self, title, cont):
        if title is None:
            title = time.time()
        fout = open('%s.txt' % title, 'w')
        fout.write("%s" % cont.encode('utf-8'))

        pass

    def output_img(self, title, url, index = None):
        filename = os.path.join(title, str(index) + '.jpg')
        try:
            with open(filename, 'wb') as f:
                f.write(self.dLoader.download(url))
        except:
            print "srcurl is %s, error" % url



