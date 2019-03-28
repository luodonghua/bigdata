import findspark
findspark.init('/Users/donghua/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkContext
sc = SparkContext('local[2]', 'Handson PySpark Chapter 6')

from pyspark.sql import Row, SQLContext, SparkSession
# SQLContext replaced by SparkSession since 2.0, SQLContext can be created through
# sql_context = SQLConect(sc)
spark = SparkSession(sc).builder.getOrCreate()

raw_data = sc.textFile('file:///tmp/kddcup.data_10_percent.gz')
csv = raw_data.map(lambda x: x.split(','))

print(csv.take(1))

rows = csv.map(lambda p: Row(duration=int(p[0]), protocol=p[1],service=p[2]))

rows.take(1)

df=spark.createDataFrame(rows)

df.printSchema()

df.show(5)

df.registerTempTable('rdd')

spark.sql("""SELECT duration from rdd WHERE protocol='tcp' and duration > 2000""")

df.select("duration").filter("protocol='tcp'").filter("duration>2000").show(5)

