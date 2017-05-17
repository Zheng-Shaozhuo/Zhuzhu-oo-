class UrlManager:
    def __init__(self):
        self.old_urls = set()
        self.new_urls = set()
        self.old_next_urls = set()
        self.new_next_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_count(self):
        return len(self.new_urls)

    def get_old_count(self):
        return len(self.old_urls)

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_next_url(self, url):
        if url is None:
            return
        if url not in self.new_next_urls and url not in self.old_next_urls:
            self.new_next_urls.add(url)

    def add_new_next_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_next_url(url)

    def get_new_next_count(self):
        return len(self.new_next_urls)

    def get_old_next_count(self):
        return len(self.old_next_urls)

    def get_new_next_url(self):
        new_url = self.new_next_urls.pop()
        self.old_next_urls.add(new_url)
        return new_url