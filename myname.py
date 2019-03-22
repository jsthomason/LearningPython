#!/usr/bin/python3
import sys
'''
learning_python
<frame object at 0xfe3d18>
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'f_back', 'f_builtins', 'f_code', 'f_globals', 'f_lasti', 'f_lineno', 'f_locals', 'f_trace']
'''

def whoami():
    return sys._getframe(1).f_code.co_name

def learning_python():
    print(whoami())
    print(dir(sys._getframe().f_code))


    return


learning_python()

sys.exit(0)

