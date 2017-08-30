# TODO: add docstring
# TODO: add assumptions
import requests
from lxml import html

# URL Constants
BASE_URL = "https://www.investing.com/commodities/"
TAIL_URL = "-historical-data"

NSMAP = {'html': "http://www.w3.org/1999/xhtml"}

# path = '//html:div[@id="replacetext"]/html:table/html:tbody//html:tr/html:td/html:a//text()'
# packages = html.xpath(path, namespaces=NSMAP)
