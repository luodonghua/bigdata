

```python
import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local[2]','Handson Spark Chapter 4')
spark = SparkSession(sc).builder.getOrCreate()

sc.setLogLevel('debug')
```


```python
import urllib.request
url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)
```


```python
raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')
```


```python
csv = raw_data.map(lambda x: x.split(','))
normal_data = csv.filter(lambda x: x[41]=='normal.')
duration = normal_data.map(lambda x: int(x[0]))
total_duration = duration.reduce(lambda a,b: a+b)
print("total duration: {}, average duration: {}".format(total_duration, total_duration/normal_data.count()))
```

    total duration: 21075991, average duration: 216.65732231336992



```python
# db is a tube of (total, count) in this context
duration_count = duration.aggregate(
 (0,0),
 lambda db, new_value: (db[0]+new_value, db[1]+1),
 lambda db1, db2: (db1[0]+db2[0], db1[1]+db2[1])
)

print("average duration: {}".format(duration_count[0]/duration_count[1]))
```

    average duration: 216.65732231336992



```python
# below is same as kv = csv.keyBy(lambda x: x[41])
kv = csv.map(lambda x: (x[41],x))
print(kv.take(1))
```

    [('normal.', ['0', 'tcp', 'http', 'SF', '181', '5450', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0.00', '0.00', '0.00', '0.00', '1.00', '0.00', '0.00', '9', '9', '1.00', '0.00', '0.11', '0.00', '0.00', '0.00', '0.00', '0.00', 'normal.'])]



```python
kv_duration = csv.map(lambda x: (x[41],float(x[0]))).reduceByKey(lambda x,y: x+y)
kv_duration.collect()
```




    [('normal.', 21075991.0),
     ('buffer_overflow.', 2751.0),
     ('loadmodule.', 326.0),
     ('perl.', 124.0),
     ('neptune.', 0.0),
     ('smurf.', 0.0),
     ('guess_passwd.', 144.0),
     ('pod.', 0.0),
     ('teardrop.', 0.0),
     ('portsweep.', 1991911.0),
     ('ipsweep.', 43.0),
     ('land.', 0.0),
     ('ftp_write.', 259.0),
     ('back.', 284.0),
     ('imap.', 72.0),
     ('satan.', 64.0),
     ('phf.', 18.0),
     ('nmap.', 0.0),
     ('multihop.', 1288.0),
     ('warezmaster.', 301.0),
     ('warezclient.', 627563.0),
     ('spy.', 636.0),
     ('rootkit.', 1008.0)]




```python
kv.countByKey()
```




    defaultdict(int,
                {'normal.': 97278,
                 'buffer_overflow.': 30,
                 'loadmodule.': 9,
                 'perl.': 3,
                 'neptune.': 107201,
                 'smurf.': 280790,
                 'guess_passwd.': 53,
                 'pod.': 264,
                 'teardrop.': 979,
                 'portsweep.': 1040,
                 'ipsweep.': 1247,
                 'land.': 21,
                 'ftp_write.': 8,
                 'back.': 2203,
                 'imap.': 12,
                 'satan.': 1589,
                 'phf.': 4,
                 'nmap.': 231,
                 'multihop.': 7,
                 'warezmaster.': 20,
                 'warezclient.': 1020,
                 'spy.': 2,
                 'rootkit.': 10})




```python
sc.stop()
```
