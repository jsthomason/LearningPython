#!/usr/bin/python3
"""
ieee_mac_lookup.py
Use the IEEE MAC registration listings to lookup MAC to Vendor resolution.
"""
import pycurl as pc
import sys
import csv
import re

files    = {"oui":"oui.csv","oui28":"mam.csv","oui36":"oui36.csv"}
csv_dict = dict()
cached   = False
mal      = None
mam      = None
mas      = None

def get_fresh_files():
    """
    get_fresh_copy()
    Get a fresh copy of the IEEE MAC .csv files
    http://standards-oui.ieee.org/oui/oui.csv
    http://standards-oui.ieee.org/oui36/oui36.csv
    http://standards-oui.ieee.org/oui28/mam.csv

    """
    global files
    ec    = 0
    url   = "http://standards-oui.ieee.org/"

    for din, fin in files.items():
        print("\n" + url + din + "/" + fin)
        try:
            with open(fin, 'wb') as fout:
                curl = pc.Curl()
                curl.setopt(curl.VERBOSE, True)
                curl.setopt(curl.URL, url + din + "/" + fin)
                curl.setopt(curl.WRITEDATA, fout)
                print("Downloading New {0}\n".format(fin))
                curl.perform()
                curl.close()
        except Exception as e:
            print("Could Not Open File: " + fin + "\n" + str(e))
            ec = 128

    return ec

def strip_sep(mac):
    """
    strip_sep(mac)
    Strip the MAC address separators
    params mac - pass mac in any form...
    aa:bb:cc:dd:ee:ff
    aa-bb-cc-dd-ee-ff
    aabb.ccdd.eeff
    aabbccddeeff

    returns mac - with separators removed
    """
    return re.sub('[-|.|:]', '', mac)

def mal_mac(mac):
    """
    mal_mac(mac)
    Parse the MAC address in a usable lookup form...
    
    DB Search requires this format...
    aabbcc    MA-L

    returns mac - in MA-L format
    """
    return mac[0:6]


def mam_mac(mac):
    """
    mam_mac(mac)
    Parse the MAC address in a usable lookup form...
    
    DB Search requires this format...
    aabbccd   MA-M

    returns mac - in MA-M format
    """
    return mac[0:7]


def mas_mac(mac):
    """
    mas_mac(mac)
    Parse the MAC address in a usable lookup form...
    
    DB Search requires this format...
    aabbccdde  MA-S

    returns mac - in MA-S format
    """
    return mac[0:9]

def format_error(arg):
    """MAC address format error message"""
    print("\"{0}\" is not a valid MAC address.\n".format(arg))

def open_csv(name):
    """
    open_csv(name)
    Open csv(MAC DB) for searching
    
    params: name - file name to open
    """
    global csv_dict
    try:
        with open(name, newline='') as csvfile:
            readCSV = csv.reader(csvfile)
            for row in readCSV:
                csv_dict[row[1]] = row[2:]
        csvfile.close()

    except Exception as e:
        print("Could not open file " + name + "\n" + str(e))

    return csv_dict

def cache_db():
    """Cache CSV MAC Databases in Memory"""
    global cached, mal, mam, mas, files
    if not cached:
        for k,v in files.items():
            if   k == "oui":
                mal = open_csv(v)
            elif k == "oui28":
                mam = open_csv(v)
            elif k == "oui36":
                mas = open_csv(v)
        cached = True

    return cached

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ main() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Testing file open...
#print(open_csv("mam.csv"))


print("\n")

if len(sys.argv) == 1:
    print("Usage: {0} [update] <MAC_Address> [<MAC_Address>]".format(sys.argv[0]))
    print("       update      -- Update the MAC Address Database")
    print("       MAC_Address -- System(s) MAC Address(es); One or more MAC addresses")
    print("\n")

else:
    for arg in sys.argv[1:]:
        if arg == "update":
            get_fresh_files()
    
        elif len(arg) >= 12 and len(arg) <= 17:
            #print("DB Cached? " + str(cached))
            cache_db()
            arg = strip_sep(arg)
            if len(arg) == 12:
                # key in dict 
                if mas_mac(arg).upper() in mas:
                    print("{0}\n{1}\n".format(arg, mas[mas_mac(arg).upper()]))
                    continue
                if mam_mac(arg).upper() in mam:
                    print("{0}\n{1}\n".format(arg, mam[mam_mac(arg).upper()]))
                    continue
                if mal_mac(arg).upper() in mal:
                    print("{0}\n{1}\n".format(arg, mal[mal_mac(arg).upper()]))

            else:
                format_error(arg)
        else:
            format_error(arg)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

sys.exit(0)

