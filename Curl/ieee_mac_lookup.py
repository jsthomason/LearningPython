#!/usr/bin/python3
"""
ieee_mac_lookup.py
Use the IEEE MAC registration listings to lookup MAC to Vendor resolution.
"""
import pycurl as pc
import getopt as go
import sys
import csv
import re

files   = {"oui":"oui.csv","oui28":"mam.csv","oui36":"oui36.csv"}
url     = "http://standards-oui.ieee.org/"
cached  = False
mal     = None
mam     = None
mas     = None

def get_fresh_files():
    """
    Get a fresh copy of the IEEE MAC .csv files
    http://standards-oui.ieee.org/oui/oui.csv
    http://standards-oui.ieee.org/oui36/oui36.csv
    http://standards-oui.ieee.org/oui28/mam.csv

    """
    global files, url
    ec    = 0

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
    Strip the MAC address separators
    params: mac - pass mac in any form...
    aa:bb:cc:dd:ee:ff
    aa-bb-cc-dd-ee-ff
    aabb.ccdd.eeff
    aabbccddeeff

    params: mac - Raw MAC Addr
    returns: mac - with separators removed
    """
    return re.sub('[-|.|:]', '', mac)

def mal_mac(mac):
    """
    Parse the MAC address in a usable lookup form...
    DB Search requires this format...
    aabbcc    MA-L

    params: mac - Raw MAC Addr
    returns: mac - in MA-L format
    """
    return mac[0:6]


def mam_mac(mac):
    """
    Parse the MAC address in a usable lookup form...
    
    DB Search requires this format...
    aabbccd   MA-M

    params: mac - Raw MAC Addr
    returns: mac - in MA-M format
    """
    return mac[0:7]


def mas_mac(mac):
    """
    Parse the MAC address in a usable lookup form...
    
    DB Search requires this format...
    aabbccdde  MA-S

    params: mac - Raw MAC Addr
    returns: mac - in MA-S format
    """
    return mac[0:9]

def format_error(arg):
    """MAC address format error message"""
    print("\"{0}\" is not a valid MAC address.\n".format(arg))

def usage():
    """Display Script Usage & Exit"""
    print()
    print("Usage: {0} [-h|--help] [-u|--update] [-i|--ifile <input_file>] [-f|--filter <word>] [<MAC_Address> <MAC_Address>]".format(sys.argv[0]))
    print("       -h|--help               -- Display this usage")
    print("       -u|--update             -- Update the MAC Address Database")
    print("       -i|--ifile <input_file> -- Name of input file containing MAC addresses one per line")
    print("       -f|--filter <word>      -- Word to filter results; typically a company name and used in conjunction with '-i' option to filter the results of numerous entries")
    print("       MAC_Address -- System(s) MAC Address(es); One or more MAC addresses")
    print()
    sys.exit(2)


def open_csv(name):
    """
    open_csv(name)
    Open csv(MAC DB) for searching
    
    params:  name     - file name to open
    returns: csv_dict - dictionary of MAC OID(key); Vendor(value)
    """
    csv_dict = dict()
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

def parse_ifile(ifile):
    """
    Parse the input file, and build a list of MAC addresses

    params: ifile - Input file name
    returns: macs - List of MAC addresses
    """
    macs = []
    try:
        fin = open(ifile)
        for l in fin:
            macs.append(l.strip())
        fin.close()
    except Exception as e:
        print("\nException opening file: {0}\n{1}\n".format(ifile, str(e)))
        sys.exit(3)

    return macs

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ main() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(argv):
    """
    Main Method

    params: argv - a list of options and arguments
    returns: exit code 0  
    """
    ifile   = None 
    ifilter = None
    
    # Got Args???
    if len(argv) == 0:
        usage() 

    # Try parsing the command line...
    try:
        opts, args = go.getopt(argv,"hui:",["ifile=","update"])
    except go.GetoptError:
        usage()

    # Parse the CLI Options
    for opt, opt_arg in opts:
        # Help - Display Usage
        if opt == '-h':
            usage()
        # Update the MAC DB
        elif opt in ("-u", "--update"):
            get_fresh_files()
        # Input File
        elif opt in ("-i:", "--ifile="):
            ifile = opt_arg[0:255] 
        # Filter Results
        elif opt in ("-f:", "--filter="):
            ifilter = opt_arg[0:255]

    # Got Input File?
    if ifile:
        args = parse_ifile(ifile)

    # Loop through MAC address(es)
    for arg in args:
        if len(arg) >= 12 and len(arg) <= 17:
            cache_db()
            mac = strip_sep(arg)
            if len(mac) == 12:
                # key in dict 
                print(arg)
                if mas_mac(mac).upper() in mas:
                    for m in mas[mas_mac(mac).upper()]:
                        print(" {0}".format(m))

                elif mam_mac(mac).upper() in mam:
                    for m in mam[mam_mac(mac).upper()]:
                        print(" {0}".format(m))

                elif mal_mac(mac).upper() in mal:
                    for m in mal[mal_mac(mac).upper()]:
                        print(" {0}".format(m))

                else:
                    print(" {0}".format("UnKnown..."))
                print()

            else:
                format_error(arg)
        else:
            format_error(arg)

    # Thumbs Up!
    sys.exit(0)

# Let's get going...
if __name__ == "__main__":
   main(sys.argv[1:])
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


