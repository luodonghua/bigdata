

```python
import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

spark=SparkSession(SparkContext()).builder.master('local[2]').appName('Handson PySpark Chapter 5').getOrCreate()
```


```python
sc = spark.sparkContext
sc.setLogLevel('debug')
```


```python
sc.getConf().getAll()
```




    [('spark.sql.warehouse.dir', '/user/hive/warehouse'),
     ('spark.rdd.compress', 'True'),
     ('spark.app.id', 'local-1553755489097'),
     ('spark.driver.port', '51208'),
     ('spark.serializer.objectStreamReset', '100'),
     ('spark.executor.id', 'driver'),
     ('spark.submit.deployMode', 'client'),
     ('spark.app.name', 'Handson PySpark Chapter 5'),
     ('spark.driver.host', '192.168.31.177'),
     ('spark.ui.showConsoleProgress', 'true'),
     ('spark.master', 'local[2]')]




```python
import urllib.request
url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)

raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')
csv = raw_data.map(lambda x: x.split(','))
duration = raw_data.map(lambda x: [int(x[0])])
```


```python
from pyspark.mllib.stat import Statistics
summary = Statistics.colStats(duration)
```


```python
summary.mean()[0]
```




    0.06611054995637812




```python
summary.count()
```




    494021




```python
metrics = csv.map(lambda x: [x[0],x[4],x[5]])
metrics.take(2)
```




    [['0', '181', '5450'], ['0', '239', '486']]




```python
Statistics.corr(metrics, method="spearman")
```




    array([[ 1.        ,  0.01419628,  0.29918926],
           [ 0.01419628,  1.        , -0.16793059],
           [ 0.29918926, -0.16793059,  1.        ]])




```python
Statistics.corr(metrics, method="pearson")
```




    array([[ 1.00000000e+00,  4.25823027e-03,  5.43953448e-03],
           [ 4.25823027e-03,  1.00000000e+00, -1.59677215e-06],
           [ 5.43953448e-03, -1.59677215e-06,  1.00000000e+00]])




```python
from pyspark.mllib.linalg import Vectors
```


```python
visitors_freq = Vectors.dense(0.13, 0.61, 0.8, 0.5, 0.3)
print(Statistics.chiSqTest(visitors_freq))
```

    Chi squared test summary:
    method: pearson
    degrees of freedom = 4 
    statistic = 0.5852136752136753 
    pValue = 0.9646925263439344 
    No presumption against null hypothesis: observed follows the same distribution as expected..



```python
visitors_freq = Vectors.dense(0.13, 0.61, 0.8, 0.5, 8)
print(Statistics.chiSqTest(visitors_freq))
```

    Chi squared test summary:
    method: pearson
    degrees of freedom = 4 
    statistic = 22.469462151394424 
    pValue = 1.6158934330234853E-4 
    Very strong presumption against null hypothesis: observed follows the same distribution as expected..



```python
print(Statistics.chiSqTest(duration.collect()))
```

    Chi squared test summary:
    method: pearson
    degrees of freedom = 494020 
    statistic = 2041502.1434188513 
    pValue = 0.0 
    Very strong presumption against null hypothesis: observed follows the same distribution as expected..



```python
spark.stop()
```
