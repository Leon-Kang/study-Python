class filter:
    def filter_emphasis(self, emphasis):
        print (r'\*(.+?)\*', emphasis)
    def filter_url(self, url):
        print (r'(http://[\.a-z0-9A-Z/]+)', url)
    def filter_mail(self, mail):
        print (r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', mail)