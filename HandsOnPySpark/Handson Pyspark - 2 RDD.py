# Loading data on to Spark RDD

import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local[2]','HandsOn Pyspark Chapter 2')
spark = SparkSession(sc).builder.getOrCreate()

sc.setLogLevel('ERROR')



# http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
# curl -o kddcup.data_10_percent.gz http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
# file saved to: /Users/donghua/kddcup.data_10_percent 
# Below example uses Python library to download directly

import urllib.request

url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)


raw_data = sc.textFile("file:///tmp/kddcup.data_10_percent.gz")

raw_data.take(2)


# Example of creating RDD through parallelization
a = range(100)

print(list(a))


list_rdd = sc.parallelize(list(a))

list_rdd.take(2)

list_rdd.count()

list_rdd.reduce(lambda a,b: a+b)

contains_normal = raw_data.filter(lambda line: "normal." in line )
contains_normal.count()

split_file = raw_data.map(lambda line: line.split(','))

for i in split_file.take(2):
    print(i)


sc.stop()