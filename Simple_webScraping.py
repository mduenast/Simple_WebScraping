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

        def get_web(self):
            """
            Obre una conexio per a demanar un recurs identificat amb la url, en aquest cas un html, que retorna i despres tanca la conexio.
            :return html
            """
            file = urllib2.urlopen(self.url)
            html = file.read()
            file.close()
            return html

        def main(self):
            web = self.get_web()
            

if __name__ == "__main__":
    simple_webscraping = Simple_WebScraping("https://www.packtpub.com/packt/offers/free-learning")
    simple_webscraping.main()