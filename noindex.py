import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('direct-guide.ditamap')
addnoindex = []
delnoindex = []
#for topicgroup in e.findall('.//topicgroup'):

findall_result = e.findall('//topicref')
#findall_result.extend(e.findall('./topicgroup/..topicref'))
#findall_result.extend(e.findall('./topicref/..topicref'))
#print (findall_result)


for topicref in findall_result:
	otherprops = topicref.get('otherprops','notfound')
	if otherprops == 'noindex':
		addnoindex.append(topicref.get('href'))
	if otherprops == 'notfound':
		delnoindex.append(topicref.get('href'))
	print (otherprops)

print ('Add NOINDEX:')
print (addnoindex)
for element in addnoindex:
	xmlfile = xml.etree.ElementTree.parse(element)
	rootelement = xmlfile.getroot()
	rootelement.set('otherprops','noindex')
	for concept in rootelement.findall('.//concept'):
		concept.set('otherprops','noindex')
	xmlfile.write(element)

print ('Del NOINDEX:')
print (delnoindex)
for delelement in delnoindex:
	print(delelement)
	xmlfile2 = xml.etree.ElementTree.parse(delelement)
	rootelement = xmlfile2.getroot()
	rootelement.attrib.pop('otherprops', None)
	for concept in rootelement.findall('.//concept'):
		concept.attrib.pop('otherprops', None)
	xmlfile2.write(delelement)

print('Finished!')