''' Module to hold global settings reused throughout qualysapi. '''

__author__ = "Colin Bell <colin.bell@uwaterloo.ca>"
__copyright__ = "Copyright 2011-2013, University of Waterloo"
__license__ = "BSD-new"

global defaults
global default_filename

import os

# print(("os_name:", os.name))
if os.name == 'nt':
    default_filename = "config.ini"
else:
    default_filename = ".qcrc"

# print(("default_filename:", default_filename))
defaults = {'hostname': 'qualysapi.qualys.com',
            'max_retries': '3'}
