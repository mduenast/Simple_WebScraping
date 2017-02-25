#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup

'''
Recordatori de llibre gratuit
@author mdt3@alumnes.udl.cat
'''

class Simple_WebScraping(object):

        def __init__(self,url):
            """
            constructor de Simple_WebScraping amb la url com a argument
            :param url:
            """
            self.url = url



if __name__ == "__main__":
    simple_webscraping = Simple_WebScraping("https://www.packtpub.com/packt/offers/free-learning")
