#! /usr/bin/env python3

import urllib.request as u2
from lxml import html
import os, json
a = str(os.environ['APIFY_TOKEN'])
print( os.environ['APIFY_TOKEN'] )
print(a)
request = u2.Request('https://example.com/')

src = u2.urlopen(request).read()

html_load = html.fromstring( src.decode() )

print( html_load.xpath('//h1/text()')[0] )


