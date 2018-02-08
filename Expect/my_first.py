#!/usr/bin/python3
"""
my_first.py -- my first expect script using python
"""
import sys
import pexpect as exp
un = 'john.x.thomason'
pw = 'Quest123'
en = 'sho33mem'
dev = 'gso-sc01.qdx.com'

try:
    host = exp.spawn('ssh -o "StrictHostKeyChecking no" -o "KexAlgorithms=+diffie-hellman-group1-sha1" ' + un + '@' + dev)
    print(str(host))
    idx = host.expect(['Password'], timeout=30)
    #print("expect:   {0}".format(str(idx)))
    if idx == 0:
        host.sendline(pw)
        print("Sent my pw")
        host.expect(['.*>'])
        print("Enabling...")
        host.sendline('en')
        print("Sent 'en'")
        host.expect(['Password'], timeout=30)
        print("Password: ")
        host.sendline(en)
        print("Sent en pw")
        host.expect(['.*#'], timeout=30)
        print("Exec prompt '#'")
        host.sendline('term len 0')
        print("Sent 'term len 0'")
        host.expect(['.*#'], timeout=30)
        print("Exec prompt '#'")
        host.sendline('sho run br')
        print("Sent 'sho run br'")
        host.expect(['.*#'], timeout=60)
        print(host.before)
        print("Exec prompt '#'")
        host.sendline('exit')
        print("Sent 'exit'")
    else:
        print("Didn't Match Crap!")


except exp.EOF:
    print("Expect EOF")

except exp.TIMEOUT:
    print("Expect TIMEOUT")



host.close()

sys.exit(0)
