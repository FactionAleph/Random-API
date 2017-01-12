#to get the names module attributes
from __future__ import print_function
import sys, names
def attrs_and_types(mod_name):

    print('Attributes and their types for module {}:'.format(mod_name))
    print()
    for num, attr in enumerate(dir(eval(mod_name))):
        print("{idx}: {nam:30}  {typ}".format(
            idx=str(num + 1).rjust(4),
            
            nam=(mod_name + '.' + attr).ljust(30), 
            typ=type(eval(mod_name + '.' + attr))))

attrs_and_types(names.__name__)
