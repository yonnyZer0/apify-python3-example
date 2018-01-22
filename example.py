#! /usr/bin/env python3

import urllib.request as u2
from lxml import html
import os

request = u2.Request('https://api.apify.com/v2/key-value-stores/' + os.environ['APIFY_DEFAULT_KEY_VALUE_STORE_ID'], headers={ 'Content-Type': 'application/json' })


print( request.urlopen().read() )


