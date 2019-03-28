
import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext('local[2]','Pyspark Handson - Chapter 3')
spark = SparkSession(sc).builder.getOrCreate()

sc.setLogLevel('debug')

import urllib.request
url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
localfile = '/tmp/kddcup.data_10_percent.gz'
f = urllib.request.urlretrieve(url,localfile)

from time import time
from IPython.core.magics.execution import _format_time as format_delta

start_time = time()

raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))


# withReplacement – can elements be sampled multiple times (replaced when sampled out)
# fraction – probability that each element is chosen; fraction must be [0, 1]
# seed – seed for the random number generator

sampled = raw_data.sample(False,0.1,42)
contains_normal_sample = sampled.map(lambda x: x.split(",")).    filter(lambda x: "normal" in x)

contains_normal = raw_data.map(lambda x: x.split(',')).    filter(lambda x: "normal" in x)

start_time = time()

contains_normal.count()

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))


start_time = time()

contains_normal_sample.count()

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))


start_time = time()

contains_normal.cache()

contains_normal.count()

stop_time = time()
print('time: {}'.format(format_delta(stop_time-start_time)))

raw_data.count()

data_in_memory = raw_data.takeSample(False, 10000, 42)
type(data_in_memory)

contains_normal_py =[line.split(',') for line in data_in_memory if "normal" in line]


len(contains_normal_py)
print(data_in_memory[0])
print(contains_normal_py[0])


normal_sample = sampled.filter(lambda line: "normal" in line)

print (sampled.count(), normal_sample.count())

non_normal_sample = sampled.subtract(normal_sample)

non_normal_sample.count()

feature_1 = sampled.map(lambda line: line.split(',')).  map(lambda features: features[1]).distinct()
feature_1.collect()

feature_2 = sampled.map(lambda line: line.split(',')).  map(lambda features: features[2]).distinct()
print(feature_2.collect())

