# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This subpackage contains classes and functions for defining and converting
between different physical units.

This code is adapted from the `pynbody
<http://code.google.com/p/pynbody/>`_ units module written by Andrew
Pontzen, who has granted the Astropy project permission to use the
code under a BSD license.
"""

from .core import *
from .si import *
from .astrophys import *
from .cgs import *
from .imperial import *
from .equivalencies import *
from .physical import *

# After importing the unit definitions above, set the unit namespace
# to this top-level module so that new units are added here.
UnitBase._set_namespace(globals())
