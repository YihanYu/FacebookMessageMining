
import xml.dom.minidom

dom= xml.dom.minidom.parse('H:\stanford-corenlp-full-2015-04-20\output.xml')

root= dom.documentElement
itemlist= root.getElementsByTagName('sentence')

item= itemlist[2]
output=open('output.csv', 'w')
output.write('sentemceid,sentiment\n')
for item in itemlist:
      un=item.getAttribute("id")
      pd=item.getAttribute("sentimentValue")
      output.write(str(un)+ ','+str(pd)+ '\n')
      
output.close()