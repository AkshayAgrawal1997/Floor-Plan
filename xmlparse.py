import xml.etree.ElementTree as ET
tree = ET.parse('sample.xml')
root = tree.getroot()
print root[1][3].text
print len(root[1])