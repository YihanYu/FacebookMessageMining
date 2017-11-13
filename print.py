#loading comment file using pandas
from pandas import Series,DataFrame 
import pandas as p
train=p.read_csv("20150403.csv", delimiter=';')

x=Series(data=train['message'].values)
print x

