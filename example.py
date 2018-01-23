#! /usr/bin/env python3

import urllib.request as u2
from lxml import html
import os, json

print( os.environ )

request = u2.Request('https://example.com/')

src = u2.urlopen(request).read()

html_load = html.frombinary( src.decode() )

print( html_load.xpath('//h1/text()')[0] )


