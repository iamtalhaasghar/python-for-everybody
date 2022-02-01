import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
total = 0
for i in tree.findall('.//count'):
    total += int(i.text)
print(total)   
