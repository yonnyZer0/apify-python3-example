#! /usr/bin/env python3

import urllib.request as u2
from lxml import html
import os

print( str( os.environ ).replace(', ','\n') )

print( open(os.environ['APIFY_DEFAULT_KEY_VALUE_STORE_ID'],'r').read() )
