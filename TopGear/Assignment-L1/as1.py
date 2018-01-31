#!/usr/bin/python3
"""Python Assignment #1
Given a list,
url = [ www.annauniv.edu,
        www.google.com,
        www.ndtv.com,
        www.website.org,
        www.bis.org.in,
        www.rbi.org.in]
Sort the list based on the top level domain (edu, com, org, in) using custom sorting
"""
import sys

URLS = ["www.annauniv.edu",\
        "www.foodnetwork.tv",\
        "www.google.com",\
        "www.ndtv.com",\
        "www.website.org",\
        "www.bis.org.in",\
        "www.rbi.org.in"]

def sort_urls(urls):
    """
    Sort a list of URLs by Top Level Domain(TLD)
    Params:
        urls - list of urls
    Returns:
        list - sorted list of URLs
    """
    return sorted(urls, key=lambda se: se.split('.')[-1])

print("\nPython Assignment #1\n")
print("UnSorted: {0}".format(str(URLS)))
print("Sorted:   {0}".format(str(sort_urls(URLS))))

sys.exit(0)
