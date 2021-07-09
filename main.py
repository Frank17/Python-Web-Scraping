class URLM:
    '''URL Manager'''
    def __init__(self):
        self.new_urls = set()    # A set of to-be-scraped URL
        self.old_urls = set()    # A set fo scraped URL

    def add_url(self, URL):
        if URL is None or len(URL) == 0 or \
        URL in self.new_urls | self.old_urls:  
            return                           
        self.new_urls.add(URL)

    def add_urls(self, URLs):
        if URLs is None or len(URLs) == 0:
            return
        self.new_urls |= set(URLs)

    def get_url(self):
        if self.has_url():
            URL = self.new_urls.pop()
            self.old_urls.add(URL)
            return URL
        return
        
    def has_url(self):
        return len(self.new_urls) > 0