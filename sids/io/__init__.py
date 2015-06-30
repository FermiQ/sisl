"""
IO imports
"""
from __future__ import print_function, division
from os.path import splitext as _ospsplitext

from .sile import *

# Import the different Sile objects
# enabling the actual print-out
from .fdf import *
from .xyz import *
from .siesta import *

# This is a file chooser which from the file-ending tries to 
# determine which kind of file we are dealing with.

_objs = {}

def add_Sile(ending,obj):
    """
    Public for attaching lookup tables for allowing
    users to attach files for the IOSile function call
    """
    global _objs
    _objs[ending] = obj

add_Sile('xyz',XYZSile)
add_Sile('XYZ',XYZSile)
add_Sile('fdf',FDFSile)
add_Sile('FDF',FDFSile)
add_Sile('nc',SIESTASile)
add_Sile('NC',SIESTASile)

# When new 
def get_Sile(file,*args,**kwargs):
    """ 
    Guess the file handle for the input file and return
    and object with the file handle.
    """
    try:
        end = _ospsplitext(file)[1]
        if end.startswith('.'): end = end[1:]
        return _objs[end](file,*args,**kwargs)
    except Exception as e:
        raise NotImplementedError("File requested could not be found, possibly the file has "+
                                  "not been implemented.")


if __name__ == "__main__":
    
    assert isinstance(get_Sile('test.xyz'),XYZSile),"Returning incorrect object"
    assert isinstance(get_Sile('test.XYZ'),XYZSile),"Returning incorrect object"
    try:
        io = get_Sile('test.xz')
        assert False,"Returning something which should not return"
    except: pass
    assert isinstance(get_Sile('test.fdf'),FDFSile),"Returning incorrect object"
    assert isinstance(get_Sile('test.FDF'),FDFSile),"Returning incorrect object"
    assert isinstance(get_Sile('test.nc'),SIESTASile),"Returning incorrect object"
    assert isinstance(get_Sile('test.NC'),SIESTASile),"Returning incorrect object"
