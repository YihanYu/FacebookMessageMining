
from pandas import Series,DataFrame 
import pandas as p
train=p.read_csv("ori2.csv", delimiter=';')
x={'objectid':train['objectid'].values, 'message':train['message'].values, 'type':train['type'].values}
df= DataFrame(x)

df=df[df['type']=='photo']
print df
df.to_csv('St_output.csv')

