import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

spark=SparkSession(SparkContext()).builder.master('local[2]').appName('Handson PySpark Chapter 5').getOrCreate()

sc = spark.sparkContext
sc.setLogLevel('debug')
sc.getConf().getAll()


import urllib.request
url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)

raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')
csv = raw_data.map(lambda x: x.split(','))
duration = raw_data.map(lambda x: [int(x[0])])

from pyspark.mllib.stat import Statistics
summary = Statistics.colStats(duration)
summary.mean()[0]
summary.count()

metrics = csv.map(lambda x: [x[0],x[4],x[5]])
metrics.take(2)

Statistics.corr(metrics, method="spearman")

Statistics.corr(metrics, method="pearson")

from pyspark.mllib.linalg import Vectors

visitors_freq = Vectors.dense(0.13, 0.61, 0.8, 0.5, 0.3)
print(Statistics.chiSqTest(visitors_freq))

visitors_freq = Vectors.dense(0.13, 0.61, 0.8, 0.5, 8)
print(Statistics.chiSqTest(visitors_freq))

print(Statistics.chiSqTest(duration.collect()))

spark.stop()

