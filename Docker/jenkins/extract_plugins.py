import requests
import xml.etree.ElementTree as ET

r = requests.get('http://0.0.0.0:8080/pluginManager/api/xml?depth=1', auth=('admin', 'password'))

tree = ET.fromstring(r.content)
plugins = (child for child in tree)
plugins_short = ((p.find('shortName').text, p.find('version').text) for p in plugins)

with open('plugins.txt', 'w') as out:
    for name, version in plugins_short:
        out.write('{0}:{1}\n'.format(name, version))
