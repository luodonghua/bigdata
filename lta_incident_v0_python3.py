#!/Users/donghua/anaconda3/bin/python

import json
import http.client 
from datetime import datetime, timedelta
import time

if __name__=="__main__":
    #Authentication parameters
    headers = { 'AccountKey' : 'i/<your Key Here>==', 'accept' : 'application/json'}  #this is by default
    #API parameters
    uri = 'datamall2.mytransport.sg'
    path = '/ltaodataservice/TrafficIncidents?'
  
    past_messages = []
  
    while True:
        event_request_time = datetime.now()
        conn = http.client.HTTPConnection(uri)
        conn.request("GET", path, '', headers)
        response = conn.getresponse()
        if response.status == 200:
            body = response.read()
            #Parse JSON to print
            jsonObj = json.loads(body)
            #print (json.dumps(jsonObj, sort_keys=True, indent=4))
            for msg in jsonObj['value']:
                if msg['Type'] != 'Roadwork':
                    message = msg['Message']
                    # skip the message if message already in past_messages list
                    old_message_flag = 0
                    for q in past_messages:
                        if message == q[0]:
                            old_message_flag = 1
                            continue
                    if old_message_flag == 1:
                        continue
                    past_messages.append((message, event_request_time))
                    print ('API Time: {}, Message: {}'.format(event_request_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:19],message))
        # Clean up past_message older than 1 day
        for q in past_messages:
            if q[1] < datetime.now() - timedelta(days=1):
                past_messages.remove(q)
        # Sleep for 60 for next round
        time.sleep(60)    
