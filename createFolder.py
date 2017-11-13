import csv
name=""
def mkdir(path):
     import os
     path=path.strip()
     path=path.rstrip("\\")
     os.makedirs(path)


with open('H:\output.csv') as csvfile:
     reader= csv.DictReader(csvfile)
     for row in reader:
         name=row['time']
         name=name[0:10]
         name=name+"_"+row['objectid']
         mkpath="H:\star"+"\\"+ name
         mkdir(mkpath)