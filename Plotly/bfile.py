#!/usr/bin/python3
''' bfile.py -- binary file test class '''
import struct
import time

class BFile(object):
    ''' BFile class representing a binary file object '''

    error = None

    def __init__(self, bfname, sfmt):
        ''' 
        constructor
        params
            bfname - binary file name to read / write
            sfmt   - structure format; see help(struct) for fmt details
        '''
        self.fname = bfname
        self.sfmt = sfmt
    
    def readit(self):
        ''' 
        readit - read binary file
        return 
            data read from file the length of data format (self.sfmt)
            or Exception from 'open' error
        '''
        data = []
        slen = struct.calcsize(self.sfmt)
        sdat = None
        bf = None
        try:
            with open(self.fname, 'rb') as bf:
                while bf:
                    sdat = bf.read(slen)
                    if not sdat: break
                    data.append(struct.unpack(self.sfmt, sdat))
        except IOError as e:
            data.append(e)
        finally:
            if bf:
                bf.close()
        return data
    
    def writeit(self, *args, append=False):
        '''
        writeit - attempt to write '*args' to binary file
        params
            *args  - arguments to write; must match 'self.sfmt'
            append - defaults to False(new file; truncate); True will append data to file
        return
            True on positive write
            False on write failure
        '''
        OPEN_OPT = 'wb'
        EC = False
        if append:
            OPEN_OPT = 'ab'
        bargs = self.__packit__(*args)
        if bargs:
            try:
                with open(self.fname, OPEN_OPT) as bf:
                    bf.write(bargs)
                EC = True
            except IOError:
                EC = False
            finally:
                bf.close()
        return EC

    def __packit__(self, *args):
        ''' 
        packit 
        params
            *args - data to be packed into the file matching self.sfmt format 
        return 
            data - packed in byte format for saving to binary file
            or   - None on structure format and *arg mismatch error
        '''
        try:
            return struct.pack(self.sfmt, *args)
        except struct.error:
            return None



#########################################################################################
## Test Code
def main(**args):
    '''
    Test Code and Examples

    Structure Format String:
        The optional first format char indicates byte order, size and alignment:
      @: native order, size & alignment (default)
      =: native order, std. size & alignment
      <: little-endian, std. size & alignment
      >: big-endian, std. size & alignment
      !: same as >
    
    The remaining chars indicate types of args and must match exactly;
    these can be preceded by a decimal repeat count:
      x: pad byte (no data); c:char; b:signed byte; B:unsigned byte;
      ?: _Bool (requires C99; if not available, char is used instead)
      h:short; H:unsigned short; i:int; I:unsigned int;
      l:long; L:unsigned long; f:float; d:double.
    Special cases (preceding decimal count indicates length):
      s:string (array of char); p: pascal string (with count byte).
    Special cases (only available in native format):
      n:ssize_t; N:size_t;
      P:an integer type that is wide enough to hold a pointer.
    Special case (not in native mode unless 'long long' in platform C):
      q:long long; Q:unsigned long long
    Whitespace between formats is ignored.

    ### EXAMPLE ###

    # Construct the bfile object
    bin_file = BFile("test_file.dat","dIII") (see string format above)

    # Write some data to the file according to string format "dIII"
    bin_file.writeit(time.time(), 20, 30, 40)
    bin_file.writeit(time.time(), 30, 40, 50, append=True)
    bin_file.writeit(time.time(), 40, 50, 60, append=True)

    # Print the contents of the file as a List of Tuples
    print(bin_file.readit())

    # Setup some vars for List / Tuple parsing
    icmp_time = 0.0
    icmp_min = 0
    icmp_avg = 0
    icmp_max = 0

    # Iterate over the returned List
    for record in bin_file.readit():

        # Extract the Tuple into prepared vars
        icmp_time, icmp_min, icmp_avg, icmp_max = tuple(record)

        # Format and print as required
        print("{} min/avg/max {}/{}/{} ms".format(\\
            time.strftime("%d.%b.%Y %H:%M:%S", time.localtime(icmp_time)),\\
            icmp_min, icmp_avg, icmp_max))

    '''
    bin_file = BFile("test_file.dat","dIII")

    bin_file.writeit(time.time(), 20, 30, 40)
    bin_file.writeit(time.time(), 30, 40, 50, append=True)
    bin_file.writeit(time.time(), 40, 50, 60, append=True)

    print(bin_file.readit())

    icmp_time = 0.0
    icmp_min = 0
    icmp_avg = 0
    icmp_max = 0
    for record in bin_file.readit():
        icmp_time, icmp_min, icmp_avg, icmp_max = tuple(record)
        print("{} min/avg/max {}/{}/{} ms".format(\
            time.strftime("%d.%b.%Y %H:%M:%S", time.localtime(icmp_time)),\
            icmp_min, icmp_avg, icmp_max))


if __name__ == "__main__":
    main()
