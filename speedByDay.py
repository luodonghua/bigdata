import sys

from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: speedByDay <file>")
        exit(-1)

    sc = SparkContext()
    # sc.setLogLevel("ERROR")

    sortedAvg = sc.textFile(sys.argv[1]) \
                .filter(lambda line: line[0:9] <> "StationID") \
                .map(lambda line: (line.split(",")[3],(float(line.split(",")[4]),1))) \
                .reduceByKey(lambda a,b: (a[0]+b[0],a[1]+b[1])) \
                .mapValues(lambda v: v[0]/v[1]) \
                .sortByKey()

    output = sortedAvg.collect()
    for (day, speed) in output:
        print(day+': '+str(speed))

    sortedAvg.saveAsTextFile("/user/donghua/speedByDay")
sc.stop()
