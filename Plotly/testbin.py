#!/usr/bin/python3

import time
from bfile import BFile

bf = BFile("testbin.dat", "dfff")

#print(bf.readit())

icmp_time = 0.0
icmp_min = 0.0
icmp_avg = 0.0
icmp_max = 0.0
for record in bf.readit():
    icmp_time, icmp_min, icmp_avg, icmp_max = tuple(record)
    print("{0} min/avg/max {1:.1f}/{2:.1f}/{3:.1f} ms".format(\
        time.strftime("%d.%b.%Y %H:%M:%S", time.localtime(icmp_time)),\
        icmp_min, icmp_avg, icmp_max))
