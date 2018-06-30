from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())

#select all li nodes.
print(html.xpath('//li'),'\n')

#select all direct 'a' children of all li nodes.
print(html.xpath('//li/a'),'\n')

#select all descendants 'a' nodes under the ul node.
print(html.xpath('//ul//a'),'\n')

#select all direct 'a' children of all ul nodes.
print(html.xpath('//ul/a'),'\n')

#select the 'a' node where 'href' is 'link4.html',then get its parent node,and then get its class attribute.
print(html.xpath('//a[@href="link4.html"]/../@class'))
#wih parent::
print(html.xpath('//a[@href="link4.html"]/parent::*/@class'))

#select the li node with 'class' as 'item-1'
print(html.xpath('//li[@class="item-1"]'))
print(html.xpath('//li[@class="item-1"]//text()'))

#get the node's attribute
print(html.xpath('//li/a/@href'))