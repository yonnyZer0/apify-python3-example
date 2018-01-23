#! /usr/bin/env python3

import urllib.request as u2
from lxml import html
import os, json

print( os.environ )

print( os.environ.get('APIFY_TOKEN','').encode() )

request = u2.Request('https://example.com/')

src = u2.urlopen(request).read()

html_load = html.fromstring( src.decode() )

print( html_load.xpath('//h1/text()')[0] )


