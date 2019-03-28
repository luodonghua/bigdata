import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local[2]','Handson Spark Chapter 4')
spark = SparkSession(sc).builder.getOrCreate()

sc.setLogLevel('debug')

import urllib.request
url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)

raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')

csv = raw_data.map(lambda x: x.split(','))
normal_data = csv.filter(lambda x: x[41]=='normal.')
duration = normal_data.map(lambda x: int(x[0]))
total_duration = duration.reduce(lambda a,b: a+b)
print("total duration: {}, average duration: {}".format(total_duration, total_duration/normal_data.count()))

# db is a tube of (total, count) in this context
duration_count = duration.aggregate(
 (0,0),
 lambda db, new_value: (db[0]+new_value, db[1]+1),
 lambda db1, db2: (db1[0]+db2[0], db1[1]+db2[1])
)

print("average duration: {}".format(duration_count[0]/duration_count[1]))

# below is same as kv = csv.keyBy(lambda x: x[41])
kv = csv.map(lambda x: (x[41],x))
print(kv.take(1))

kv_duration = csv.map(lambda x: (x[41],float(x[0]))).reduceByKey(lambda x,y: x+y)
kv_duration.collect()

kv.countByKey()

sc.stop()

