import csv
import xml.dom.minidom
output=open('new1output.csv', 'w')
output.write('sentiment\n')
dom= xml.dom.minidom.parse('H:\stanford-corenlp-full-2015-04-20\output.xml')
sum=0.0
count=0

cc=dom.documentElement
cc=dom.getElementsByTagName('word')
a=[]
b=[]
for c in cc:
     if c.firstChild.data=="BBB":
          c1=c.parentNode
          if c1.getAttribute("id")=="1":
                 c2=c1.parentNode
                 c3=c2.parentNode
                 un=c3.getAttribute("id")
                 
                 a.append(un)
                
                 
root= dom.documentElement
itemlist= root.getElementsByTagName('sentence')

for item in itemlist:
      id=item.getAttribute("id")
      sv=item.getAttribute("sentimentValue")
      
      if id in a:
         sv=9  
     
      if sv!="":
         b.append(sv)

for i in b:
     j=int(i)
     if j!=9:
         sum=sum+j
         count+=1
     if j==9:
         if count!=0:
            ave=sum/count
            output.write(str(ave)+'\n')


         
      
