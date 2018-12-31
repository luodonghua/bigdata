
import tika
import json
import urllib3
import traceback
import os

http = urllib3.PoolManager()

tika.initVM()
from tika import parser
url = 'http://node02.dbaglobe.com:8983/solr/cms/update/json/docs?commit=true'

filelist = ['D:\\Temp\\Building Positive Relationships young children.pdf',
            'D:\\Temp\\Building Positive Relationships spouse n in laws.pdf']

for file in filelist:
    try:
        parsed = parser.from_file(file)
        #Add content to "combined" dict object
        combined={}
        combined['id']=os.path.basename(file) # use file name as Doc ID
        combined.update(parsed["metadata"])
        combined['content']=parsed["content"]
        combined_json = json.loads(json.dumps(combined))

        print(combined_json)

        # to clean up, execute solr command <delete><query>*:*</query></delete>
        # use immutable to avoid error "This ConfigSet is immutable.", use below to create the template before create the collection
        # http://node02:8983/solr/admin/configs?action=CREATE&name=myConfigSet&baseConfigSet=schemalessTemplate&configSetProp.immutable=false&wt=xml
        # to search: content:"Psychologist"

        response = http.request('POST',url,body=json.dumps(combined_json),headers={'Content-Type': 'application/json'})
        print (response.data)
    except:
        print(traceback.format_exc())
