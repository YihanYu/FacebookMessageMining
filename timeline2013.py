import csv
import os
import itertools
fields = ["objectid", "time"]

readfile ="H:\input.csv"
writefile ="H:\output.csv"
with open(readfile) as infile, open(writefile, "wb") as outfile:
    
     r = csv.DictReader(infile)
     w = csv.DictWriter(outfile, fields, extrasaction="ignore")
     
     w.writeheader()
      
     for row in itertools.islice(r,198, 418):
         if row:
             w.writerow(row)
     