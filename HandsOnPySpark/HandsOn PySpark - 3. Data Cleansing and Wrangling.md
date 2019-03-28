

```python
import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local[2]','Pyspark Handson - Chapter 3')
spark = SparkSession(sc).builder.getOrCreate()
```


```python
sc.setLogLevel('debug')
```


```python
import urllib.request
url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)
```


```python
from time import time
from IPython.core.magics.execution import _format_time as format_delta

start_time = time()

raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))
```

    time: 88.8 ms



```python
# withReplacement – can elements be sampled multiple times (replaced when sampled out)
# fraction – probability that each element is chosen; fraction must be [0, 1]
# seed – seed for the random number generator

sampled = raw_data.sample(False,0.1,42)
contains_normal_sample = sampled.map(lambda x: x.split(",")).\
    filter(lambda x: "normal" in x)

contains_normal = raw_data.map(lambda x: x.split(',')).\
    filter(lambda x: "normal" in x)
```


```python
start_time = time()

contains_normal.count()

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))
```

    time: 3.71 s



```python
start_time = time()

contains_normal_sample.count()

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))
```

    time: 1.21 s



```python
start_time = time()

contains_normal.cache()

contains_normal.count()

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))
```

    time: 86.1 ms



```python
raw_data.count()
```




    494021




```python
data_in_memory = raw_data.takeSample(False, 10000, 42)
type(data_in_memory)
```




    list




```python
contains_normal_py =[line.split(',') for line in data_in_memory if "normal" in line]
```


```python
len(contains_normal_py)
```




    1998




```python
print(data_in_memory[0])
```

    0,icmp,ecr_i,SF,520,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,511,511,0.00,0.00,0.00,0.00,1.00,0.00,0.00,255,255,1.00,0.00,1.00,0.00,0.00,0.00,0.00,0.00,smurf.



```python
print(contains_normal_py[0])
```

    ['0', 'tcp', 'http', 'SF', '223', '9121', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '8', '0.00', '0.00', '0.00', '0.00', '1.00', '0.00', '0.25', '72', '255', '1.00', '0.00', '0.01', '0.04', '0.00', '0.00', '0.00', '0.00', 'normal.']



```python
normal_sample = sampled.filter(lambda line: "normal" in line)
```


```python
print (sampled.count(), normal_sample.count())
```

    49387 9733



```python
non_normal_sample = sampled.subtract(normal_sample)
```


```python
non_normal_sample.count()
```




    39654




```python
feature_1 = sampled.map(lambda line: line.split(',')).\
  map(lambda features: features[1]).distinct()
```


```python
feature_1.collect()
```




    ['tcp', 'icmp', 'udp']




```python
feature_2 = sampled.map(lambda line: line.split(',')).\
  map(lambda features: features[2]).distinct()
```


```python
print(feature_2.collect())
```

    ['http', 'smtp', 'auth', 'ecr_i', 'finger', 'ftp', 'domain_u', 'ntp_u', 'eco_i', 'private', 'ftp_data', 'telnet', 'pop_3', 'mtp', 'link', 'gopher', 'other', 'IRC', 'klogin', 'echo', 'time', 'remote_job', 'hostnames', 'uucp_path', 'nntp', 'http_443', 'efs', 'uucp', 'sql_net', 'daytime', 'rje', 'csnet_ns', 'sunrpc', 'bgp', 'vmnet', 'nnsp', 'whois', 'domain', 'printer', 'kshell', 'iso_tsap', 'name', 'supdup', 'pop_2', 'ldap', 'login', 'netbios_ns', 'imap4', 'Z39_50', 'discard', 'systat', 'exec', 'netstat', 'netbios_dgm', 'urh_i', 'urp_i', 'courier', 'ctf', 'shell', 'netbios_ssn', 'ssh', 'X11']

