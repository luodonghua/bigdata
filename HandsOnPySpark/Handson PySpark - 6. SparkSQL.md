

```python
import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
sc = SparkContext('local[2]', 'Handson PySpark Chapter 6')

from pyspark.sql import Row, SQLContext, SparkSession
# SQLContext replaced by SparkSession since 2.0, SQLContext can be created through
# sql_context = SQLConect(sc)
spark = SparkSession(sc).builder.getOrCreate()
```


```python
raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')
csv = raw_data.map(lambda x: x.split(','))
```


```python
print(csv.take(1))
```

    [['0', 'tcp', 'http', 'SF', '181', '5450', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0.00', '0.00', '0.00', '0.00', '1.00', '0.00', '0.00', '9', '9', '1.00', '0.00', '0.11', '0.00', '0.00', '0.00', '0.00', '0.00', 'normal.']]



```python
rows = csv.map(lambda p: Row(duration=int(p[0]), protocol=p[1],service=p[2]))
```


```python
rows.take(1)
```




    [Row(duration=0, protocol='tcp', service='http')]




```python
df=spark.createDataFrame(rows)
```


```python
df.printSchema()
```

    root
     |-- duration: long (nullable = true)
     |-- protocol: string (nullable = true)
     |-- service: string (nullable = true)
    



```python
df.show(5)
```

    +--------+--------+-------+
    |duration|protocol|service|
    +--------+--------+-------+
    |       0|     tcp|   http|
    |       0|     tcp|   http|
    |       0|     tcp|   http|
    |       0|     tcp|   http|
    |       0|     tcp|   http|
    +--------+--------+-------+
    only showing top 5 rows
    



```python
df.registerTempTable('rdd')
```


```python
spark.sql("""SELECT duration from rdd WHERE protocol='tcp' and duration > 2000""")
```


```python
df.select("duration").filter("protocol='tcp'").filter("duration>2000").show(5)
```

    +--------+
    |duration|
    +--------+
    |   12454|
    |   10774|
    |   13368|
    |   10350|
    |   10409|
    +--------+
    only showing top 5 rows
    

