#!/usr/bin/python3
#
# Python Assignment #1
#

import sys, os

# Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]
# Sort the list based on the top level domain (edu, com, org, in) using custom sorting


unsorted_urls = ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

sorted_urls   = []


def sortURLs(urls):
    if isSorted(urls): return sorted_urls
    

def isSorted(urls):
    result = True

    if type(urls) == list:
        for url in urls:
            print(url.split('.')[-1])
            result = True

    return result

sortURLs(unsorted_urls)

sys.exit(0)


