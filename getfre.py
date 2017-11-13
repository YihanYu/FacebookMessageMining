import csv
import os
a=[]
b=[]
for file in os.listdir("H:\outputfrom"):
     filename = os.path.basename(file)
     readfile ="H:\outputfrom"+"\\"+ filename
     
     with open(readfile) as csvfile:
          reader= csv.DictReader(csvfile)
          for line in reader:
                 if line["from"]!="":
                     name=line["from"]
                     d=eval(name)
                     user=d["name"]
                     a.append(user)
                     
                     
for file in os.listdir("H:\outputgun"):
     filename = os.path.basename(file)
     readfile ="H:\outputgun"+"\\"+ filename
     
     with open(readfile) as csvfile:
          reader= csv.DictReader(csvfile)
          for line in reader:
                 if line["from"]!="":
                     name=line["from"]
                     d=eval(name)
                     user=d["name"]
                     b.append(user)                     
              
freoutput=open('commentsfre.csv', 'w')   
freoutput.write('name,frequency\n')             
print len(a)
c=set(b)
print len(c)
fre=""
for i in c:
     fre=str(a.count(i))
     freoutput.write(i+','+fre+'\n')