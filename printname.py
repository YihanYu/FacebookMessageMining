import csv
import os
a=[]
output=open('namesincomments.csv', 'w')
output.write('name\n')
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
                     
              
                     output.write(user+'\n')
freoutput=open('namesincommentsfre.csv', 'w')   
freoutput.write('name,frequency\n')             
print len(a)
b=set(a)
print len(b)
fre=""
for i in b:
     fre=str(a.count(i))
     freoutput.write(i+','+fre+'\n')
     

       
         
