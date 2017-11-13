import csv
import os
import itertools
fields = ["message"]
for file in os.listdir("H:\input2013"):
  filename = os.path.basename(file)
  readfile ="H:\input2013"+"\\"+ filename
  writefile ="H:\output2013"+"\\"+filename
  with open(readfile) as infile, open(writefile, "wb") as outfile:
   
     r = csv.DictReader(infile, delimiter=';')
     w = csv.DictWriter(outfile, fields, extrasaction="ignore")
     w.writeheader()
     
     for row in itertools.islice(r,1, None):
         if row:
             w.writerow(row)
     
