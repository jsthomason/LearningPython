#!/usr/bin/python3
"""
my_first.py -- my first expect script using python
"""
import sys
import pexpect as exp
un = 'jthomason'

try:
    host = exp.spawn("ssh -p10022 " + un + "@pingpost.solstas.com")
    idx = host.expect(['BobsBurgers', un + '@PingPost'], timeout=15)
    print(host.before)
    print("expect:   {0}".format(str(idx)))
    if idx == 0:
        print("What? BobsBurgers!")
    elif idx == 1:
        print("Got CLI...Listing Dir...")
        #print("sendline: {0}".format(str(host.sendline('ls -la /home/jthomason/'))))
        host.sendline('ls -la /home/'+un+'/')
        idx = host.expect([un+'@PingPost'])
        print(host.before)
        if idx == 0:
            print("Exiting...")
            host.sendline('exit')
        else:
            raise exp.EOF
    else:
        print("Didn't Match Crap!")


except exp.EOF:
    print("Expect EOF")

except exp.TIMEOUT:
    print("Expect TIMEOUT")



host.close()

sys.exit(0)
