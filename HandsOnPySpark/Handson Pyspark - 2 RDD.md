

```python
# Loading data on to Spark RDD

import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local[2]','HandsOn Pyspark Chapter 2')
spark = SparkSession(sc).builder.getOrCreate()

sc.setLogLevel('debug')
```


```python
# http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
# curl -o kddcup.data_10_percent.gz http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
# file saved to: /Users/donghua/kddcup.data_10_percent 
# Below example uses Python library to download directly

import urllib.request

url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)
```


```python
raw_data = sc.textFile("file:///tmp/kddcup.data_10_percent.gz")
```


```python
raw_data.take(2)
```




    ['0,tcp,http,SF,181,5450,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0.00,0.00,0.00,0.00,1.00,0.00,0.00,9,9,1.00,0.00,0.11,0.00,0.00,0.00,0.00,0.00,normal.',
     '0,tcp,http,SF,239,486,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,8,8,0.00,0.00,0.00,0.00,1.00,0.00,0.00,19,19,1.00,0.00,0.05,0.00,0.00,0.00,0.00,0.00,normal.']




```python
raw_data
```




    file:///tmp/kddcup.data_10_percent.gz MapPartitionsRDD[5] at textFile at NativeMethodAccessorImpl.java:0




```python
a = range(100)
```


```python
a
```




    range(0, 100)




```python
print(list(a))
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]



```python
list_rdd = sc.parallelize(list(a))
```


```python
list_rdd
```




    ParallelCollectionRDD[7] at parallelize at PythonRDD.scala:195




```python
list_rdd.take(2)
```




    [0, 1]




```python
list_rdd.count()
```




    100




```python
len(a)
```




    100




```python
list_rdd.reduce(lambda a,b: a+b)
```




    4950




```python
contains_normal = raw_data.filter(lambda line: "normal." in line )
contains_normal.count()
```




    97278




```python
split_file = raw_data.map(lambda line: line.split(','))
```


```python
for i in split_file.take(2):
    print(i)
```

    ['0', 'tcp', 'http', 'SF', '181', '5450', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0.00', '0.00', '0.00', '0.00', '1.00', '0.00', '0.00', '9', '9', '1.00', '0.00', '0.11', '0.00', '0.00', '0.00', '0.00', '0.00', 'normal.']
    ['0', 'tcp', 'http', 'SF', '239', '486', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0.00', '0.00', '0.00', '0.00', '1.00', '0.00', '0.00', '19', '19', '1.00', '0.00', '0.05', '0.00', '0.00', '0.00', '0.00', '0.00', 'normal.']

