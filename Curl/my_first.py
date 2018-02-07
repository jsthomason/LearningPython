#!/usr/bin/python3
"""
| my_first.py
| learning to use the curl lib
| I would like to automate MAC address lookups via the pycurl module
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import pycurl as pc
from io import BytesIO
from html.parser import HTMLParser
import sys
import re

class MyHTMLParser(HTMLParser):
    true_tag = False
    p = re.compile("www.google.com/search")

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for k, v in attrs:
                if self.p.search(v):
                    self.true_tag = True

    def handle_data(self, data):
        if self.true_tag: 
            print("Manufacture:", data)
            self.true_tag = False

def resolve(mac_addr):
    """
    resolve(mac_addr)
    Resolve the OID portion of the MAC address to the Vendor
    http://coffer.com/mac_find/?string=A4:18:75:DB:61:C0
    """
macs = ["A4:18:75:DB:61:C0","00:08:30:95:A1:C0"]
for mac in macs:
    url = "http://www.coffer.com/mac_find/?string=" + mac
    
    curl = pc.Curl()
    buff = BytesIO()
    pars = MyHTMLParser()
    
    curl.setopt(pc.URL, url)
    curl.setopt(pc.WRITEDATA, buff)
    
    curl.perform()
    curl.close()
    
    html = buff.getvalue()
    pars.feed(html.decode('UTF-8'))

sys.exit(0)

