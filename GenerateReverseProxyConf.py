port = '''
8040 
9864 
9000  
8041  
8042  
9866  
9995  
9867  
9868  
9997  
9870  
19888 
10033 
8083  
8020  
8086  
8022  
8888  
11000 
8088  
8091  
8030  
8031  
8032  
8033  
10020
'''

sourceip = '192.168.31.21'
targethost='node2.dbaglobe.com'
portlist = port.split('\n')

for i in range(len(portlist)):
    if(portlist[i].strip()!=''):
        print('Listen '+sourceip+':'+portlist[i].strip())
        print('\tProxyPreserveHost On')
        print('\tProxyPass / http://'+targethost+':'+portlist[i].strip()+'/')
        print('\tProxyPassReverse / http://'+targethost+':'+portlist[i].strip()+'/')
        print('')