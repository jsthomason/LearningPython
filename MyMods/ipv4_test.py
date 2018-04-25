#!/usr/bin/python3
from ipv4 import *
#
# Test Code...
#
# Testing c2m function
print("Testing c2m() function...")
for i in range(-1,34):
  print("CIDR {0:>2} SM {1}".format(i,c2m(i)))

print("CIDR  A SM",c2m('A'))
print("CIDR 12.5 SM",c2m(12.5))
print("CIDR Bob SM",c2m("Bob"))


#
# Testing m2c function
octets = {'o1':255, 'o2':255, 'o3':255, 'o4':255}

def __octet__(o):
  return ((o<<1)-256)

print("\nTesting m2c() function...")

for k in octets:
  while octets[k] >= 0:
    sm = "{0}.{1}.{2}.{3}".format(octets['o1'],octets['o2'],octets['o3'],octets['o4'])
    octets[k] = __octet__(octets[k])
    #print(sm)
    print("SM {0} CIDR {1}".format(sm, m2c(sm)))
  octets[k] = 0

sm = "john.and.beth.thomason"
print("SM {0} CIDR {1}".format(sm, m2c(sm)))

sm = "255.255.255.255.255"
print("SM {0} CIDR {1}".format(sm, m2c(sm)))

sm = 32 
print("SM {0} CIDR {1}".format(sm, m2c(sm)))

sm = "375.292.0.47"
print("SM {0} CIDR {1}".format(sm, m2c(sm)))

sm = "0.255.0.92"
print("SM {0} CIDR {1}".format(sm, m2c(sm)))

sm = "0.255.0.0"
print("SM {0} CIDR {1}".format(sm, m2c(sm)))



#
# Test Code...
#
# Testing num_hosts
print("\nTesting num_hosts(cidr) function")
print("CIDR {0} has {1} Hosts".format(-1, num_hosts(-1)))
for cidr in range(0,33):
  print("CIDR {0:2} has {1:10} Hosts".format(cidr, num_hosts(cidr)))
print("CIDR {0} has {1} Hosts".format(33, num_hosts(33)))
print("CIDR {0} has {1} Hosts".format('A', num_hosts('A')))
print("CIDR {0} has {1} Hosts".format('255.255.0.0', num_hosts('255.255.0.0')))
print("CIDR {0} has {1} Hosts".format(12.5, num_hosts(12.5)))


#
# Test Code
#
# Testing network(addr,cidr)
print("\nTesting network(addr,cidr) function")
#a = "10.22.134.54"
a = "255.255.255.255"
c = 0
while c <= 32:
  print("The Network for {0}/{1} is {2}".format(a,c,network(a,c)))
  c += 1

c = -1
print("The Network for {0}/{1} is {2}".format(a,c,network(a,c)))

c = 33
print("The Network for {0}/{1} is {2}".format(a,c,network(a,c)))

a = "10.10.10.256"
c = 24
print("The Network for {0}/{1} is {2}".format(a,c,network(a,c)))

a = "10.10.10.-1"
c = 12
print("The Network for {0}/{1} is {2}".format(a,c,network(a,c)))


#
# Test Code
#
# Testing bcast(addr,cidr)
print("\nTesting bcast(addr,cidr) function")
#a = "10.22.134.54"
a = "0.0.0.0"
c = 0
while c <= 32:
  print("The Network for {0}/{1} is {2}".format(a,c,bcast(a,c)))
  c += 1

a = "10.10.10.-1"
c = 12
print("The Broadcast for {0}/{1} is {2}".format(a,c,bcast(a,c)))
a = "10.10.10.10"
c = 24
print("The Broadcast for {0}/{1} is {2}".format(a,c,bcast(a,c)))
a = "10.10.10.256"
c = 24
print("The Broadcast for {0}/{1} is {2}".format(a,c,bcast(a,c)))




#
# Test Code
#
# Testing first_addr(addr,cidr)
print("\nTesting first_addr(addr,cidr) function")
a = "255.255.255.255"
c = 0
while c <= 32:
  print("First Address for {0}/{1} is {2}".format(a,c,first_addr(a,c)))
  c += 1

a = "10.10.10.-1"
c = 12
print("First Address for {0}/{1} is {2}".format(a,c,first_addr(a,c)))
a = "10.10.10.10"
c = 24
print("First Address for {0}/{1} is {2}".format(a,c,first_addr(a,c)))
a = "10.10.10.256"
c = 24
print("First Address for {0}/{1} is {2}".format(a,c,first_addr(a,c)))




#
# Test Code
#
# Testing last_addr(addr,cidr)
print("\nTesting last_addr(addr,cidr) function")
a = "0.0.0.0"
c = 0
while c <= 32:
  print("Last Address for {0}/{1} is {2}".format(a,c,last_addr(a,c)))
  c += 1

a = "10.10.10.-1"
c = 12
print("Last Address for {0}/{1} is {2}".format(a,c,last_addr(a,c)))
a = "10.10.10.256"
c = 24
print("Last Address for {0}/{1} is {2}".format(a,c,last_addr(a,c)))



