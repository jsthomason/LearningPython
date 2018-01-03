#!/usr/bin/python3
#
# Python Assignment #1
#

import sys, os

# Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]
# Sort the list based on the top level domain (edu, com, org, in) using custom sorting


unsorted_urls = ["www.annauniv.edu", "www.foodnetwork.tv", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

def sortURLs(unsorted_urls):
    return sorted(unsorted_urls, key=lambda se: se.split('.')[-1])


print("\nPython Assignment #1\n")

print("UnSorted: {0}".format(str(unsorted_urls)))
print("Sorted:   {0}".format(str(sortURLs(unsorted_urls))))

sys.exit(0)

