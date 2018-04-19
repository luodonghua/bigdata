import json
jsonObj = json.load(open('Working with Text Data.ipynb'))
for i  in [cells['source'] for cells in jsonObj['cells']]:
    print (i[0]) if len(i)>0 else '' 
