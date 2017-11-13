a=[]

def getFileLines(fileName):
     file= open(fileName, 'r')
     result= len(file.readlines())
     file.close()
     a.append(result)
     return result
     
import os

dirname ='../cleanData/output2013'
fnames= os.listdir(dirname)
flines = [fn+ '\t'+str(getFileLines(os.path.join(dirname,fn)))
          for fn in fnames]
print len(flines)
print '\n'.join(flines)
print a 
print "max"
print max(a)
print "min"
print min(a)
r=0.0
for i in a:
     r=r+i
ave=r/len(flines)
     
print "average"
print ave
