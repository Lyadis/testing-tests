import sys
from lxml import etree

QUERY = '{{{0}}}reporting/{{{0}}}plugin'
SNIPPET = '''<plugin>
		<groupId>org.codehaus.mojo</groupId>
		<artifactId>cobertura-maven-plugin</artifactId>
		<version>2.7</version>
	</plugin>'''

def main():
	path = sys.argv[1]
	doc = etree.parse(path)
	root = doc.getroot()
	name = lambda n: '{{{0}}}{1}'.format(root.nsmap[None], n)
	projectNode = root.find(name('project'))
	reportingNode = root.find(name('reporting'))
	if reportingNode:
		pluginsNode = reportingNode.find(name('plugins'))
		if pluginsNode:
			pluginsNode.insert(0, etree.fromstring(SNIPPET))
		else:
			reportingNode.insert(0, etree.fromstring('<plugins>{}</plugins>'.format(SNIPPET)))
	else:
		root.insert(0, etree.fromstring('<reporting><plugins>{}</plugins></reporting>'.format(SNIPPET)))
	doc.write(path)

if __name__ == '__main__':
	main()
