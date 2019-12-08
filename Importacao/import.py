# important: SN2013dy data is not avaiable
# change in SN names with dash - to '-', otherwise the wget will not work on it 
import json             

json_data=open('Export.json')
data=json.load(json_data)
f=open('namesSN','w')
g=open('nSN','w')

for i in range(0,len(data)):
    line=data[i]['Name']

    f.write('wget https://sne.space/sne/'+str(line.split()[0])+'.json'+'\n')
    g.write(str(line.split()[0])+'\n')

f.close()
g.close()
