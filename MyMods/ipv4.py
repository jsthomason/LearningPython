"""
ipv4.py
IPv4 Utilities Module

c2m(cidr)              -- cidr to mask
m2c(sm)                -- mask to cidr
num_hosts(cidr)        -- Number of hosts for passed cidr (minus network and broadcast)
network(addr,cidr)     -- Network for given address and cidr
bcast(addr,cidr)       -- Broadcast for given address and cidr
first_addr(addr,cider) -- First address within address range
last_addr(addr,cidr)   -- Last address within address range

Supporting functions
__vc__                 -- Valid CIDR?
__vm__                 -- Valid Mask?
__vmo__                -- Valid Mask Octet?
__va__                 -- Valid Address?
__vao__                -- Valid Address Octet?


"""
#
# c2m(cidr)
# cidr to mask
def c2m(cidr):
  """
  convert a cidr integer(between 0 - 32) to a subnet mask(xxx.xxx.xxx.xxx)
  """
  x    = 0
  y    = 8
  sm   = ''
  bits = ''

  if __vc__(cidr):
    
    diff = 32 - cidr

    while cidr > 0:
      bits += '1'
      cidr -= 1

    while diff > 0:
      bits += '0'
      diff -= 1

    while y <= 32:
      sm += str(int(bits[x:y], 2))
      if y < 32: sm += '.'
      x = y
      y += 8

  else:
    sm = "Invalid CIDR " + str(cidr)

  return sm

#
# m2c(sm)
# mask to cidr
def m2c(sm):
  """
  convert a subnet mask string(x.x.x.x) to a cider integer(between 0 - 32)
  """
  cidr = 0
  if __vm__(sm):
    octets = sm.split('.')
    for octet in octets:
      octet = int(octet)
      while octet: cidr += (octet & 1); octet >>= 1

  else:
    cidr = -1

  return cidr


#
# num_hosts(cidr)
# Number of hosts for passed cidr (minus network and broadcast)
def num_hosts(cidr):
  hosts = -1
  try:
    if not __vc__(cidr):
      raise TypeError("Not a Valid CIDR Value: " + str(cidr))

    else:
      bits = 32 - cidr
      if bits == 0: hosts = (2**bits)
      else: hosts = (2**bits) - 2
  except TypeError as te:
    hosts = te
  
  return hosts


#
# network(addr,cidr)
# Network for given address and cidr
def network(addr,cidr):
  dot      = 1
  net_addr = ""
  if __va__(addr) and __vc__(cidr):
    ad_octs = addr.split('.')
    sm_octs = (c2m(cidr)).split('.')
    for ad_oct,sm_oct in zip(ad_octs,sm_octs):
      net_addr += (str(int(ad_oct)&int(sm_oct)))
      if dot < 4: net_addr += "."; dot += 1
  else:
    net_addr = None

  return net_addr

#
# bcast(addr,cidr)
# Broadcast for given address and cidr
def bcast(addr,cidr):
  dot      = 1
  net_addr = ""
  if __va__(addr) and __vc__(cidr):
    addr = network(addr,cidr)
    ad_octs = addr.split('.')
    sm_octs = (c2m(cidr)).split('.')
    for ad_oct,sm_oct in zip(ad_octs,sm_octs):
      ad_oct = int(ad_oct)
      sm_oct = int(sm_oct)
      if sm_oct == 255:
        net_addr += str(ad_oct)
      elif sm_oct == 0:
        net_addr += '255'
      else:
        net_addr += (str(ad_oct^(sm_oct^255)))
      if dot < 4: net_addr += "."; dot += 1
  else:
    net_addr = None

  return net_addr

#
# first_addr(addr,cidr)
# First address within address range
def first_addr(addr,cidr):
  net_addr = ""
  if __va__(addr) and __vc__(cidr):
    ad_octs = (network(addr,cidr)).split('.')
    if int(ad_octs[3]) < 254:
      net_addr = ad_octs[0] + '.' + ad_octs[1] + '.' + ad_octs[2] + '.' + str(int(ad_octs[3])+1)
    else:
      net_addr = ad_octs[0] + '.' + ad_octs[1] + '.' + ad_octs[2] + '.' + ad_octs[3]
  else:
    net_addr = None

  return net_addr

#
# last_addr(addr,cidr)
# Last address within address range
def last_addr(addr,cidr):
  net_addr = ""
  if __va__(addr) and __vc__(cidr):
    ad_octs = (bcast(addr,cidr)).split('.')
    if int(ad_octs[3]) > 1:
      net_addr = ad_octs[0] + '.' + ad_octs[1] + '.' + ad_octs[2] + '.' + str(int(ad_octs[3])-1)
    else:
      net_addr = ad_octs[0] + '.' + ad_octs[1] + '.' + ad_octs[2] + '.' + ad_octs[3]
    #sm_octs = (c2m(cidr)).split('.')
    #for ad_oct,sm_oct in zip(ad_octs,sm_octs):
    #  pass
  else:
    net_addr = None

  return net_addr


#
#+++++++++++++++++++++++++++++Supporting Functions+++++++++++++++++++++++++++++
#
#
# __vm__(sm)
# Is the passed subnet mask valid?
def __vm__(sm):
  valid = True
  if type(sm) == str:
    try:
      octets = sm.split(".")
      if len(octets) == 4:
        # Str to Int...
        idx = 0
        while idx < len(octets):
          octets[idx] = int(octets[idx])
          idx += 1

        # Got valid octets???
        for octet in octets:
          if not __vmo__(octet):
#            print("Failed __vmo__()")
            valid = False
            break

        # 4th octet can not = 254
        if valid:
          if octets[3] == 254:
            valid = False

        # Octets in proper order???
        if valid:
          idx = 1
          while idx < len(octets):
            if octets[idx] > octets[idx-1]: 
#              print("Failed Proper Order @ idx", idx)
              valid = False
              break
            idx += 1

      else:
#        print("Failed sm has too many octets")
        valid = False

    except ValueError:
#      print("Failed converting str to int")
      valid = False

  else:
    valid = False

  return valid

#
# __vmo__(octet)
# Is passed subnet mask octet valid?
def __vmo__(octet):

  valid = False
  bits  = 255
  if type(octet) == int:
    while bits:
      if octet == bits or octet == 0:
        valid = True
        break
      bits = (bits << 1) - 256

  return valid

#
# __vc__(cidr)
# Is the passed cidr valid?
def __vc__(cidr):
  valid = False
  if type(cidr) == int and cidr >= 0 and cidr <= 32 and cidr != 31: valid = True
  return valid


#
# __va__
# -- Valid Address?
def __va__(addr):
  valid = True
  try:
    octets = addr.split('.')
    if len(octets) == 4:
      for octet in octets:
        octet = int(octet)
        if __vao__(octet): continue
        else: raise TypeError
    else: raise TypeError
  except TypeError:
    valid = False
  return valid


#
# __vao__
# -- Valid Address Octet?
def __vao__(octet):
  valid = False
  if type(octet) == int and octet >= 0 and octet <= 255: valid = True
  return valid





