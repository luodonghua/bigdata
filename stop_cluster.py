#!/usr/bin/python2.7

# Get a handle to the API client
from cm_api.api_client import ApiResource

cm_host = "cdh-vm.dbaglobe.com"
api = ApiResource(cm_host, username="admin", password="admin")

# Get a list of all clusters
cdh5 = None
for c in api.get_all_clusters():
  print str(c)+'\n'
  if c.version == 'CDH5':
    cdh5 = c

if cdh5 <> None:
  for s in cdh5.get_all_services():
    if s.type == 'HDFS':
      hdfs = s
    if s.type == 'YARN':
      yarn = s
    if s.type == 'SPARK_ON_YARN':
      spark = s
    if s.type == 'HIVE':
      hive = s
    if s.type == 'ZOOKEEPER':
      zk = s
    if s.type == 'IMPALA':
      impala = s
    if s.type == 'OOZIE':
      oozie = s
    if s.type == 'HUE':
      hue = s

# Stop Hue
cmd = hue.stop().wait()
print 'Name: {}  Before: {} Result: {}'.format(hue.name.ljust(15),hue.serviceState.ljust(13),cmd.success)

# Stop Oozie
# cmd = oozie.stop().wait()
# print 'Name: {}  Before: {} Result: {}'.format(oozie.name.ljust(15),oozie.serviceState.ljust(13),cmd.success)

# Stop Impala
cmd = impala.stop().wait()
print 'Name: {}  Before: {} Result: {}'.format(impala.name.ljust(15),impala.serviceState.ljust(13),cmd.success)

# Stop Hive
cmd = hive.stop().wait()
print 'Name: {}  Before: {} Result: {}'.format(hive.name.ljust(15),hive.serviceState.ljust(13),cmd.success)

# Stop Spark on Yarn
cmd = spark.stop().wait()
print 'Name: {}  Before: {} Result: {}'.format(spark.name.ljust(15),spark.serviceState.ljust(13),cmd.success)



# Stop Yarn
cmd = yarn.stop().wait()
print 'Name: {}  Before: {} Result: {}'.format(yarn.name.ljust(15),yarn.serviceState.ljust(13),cmd.success)

# Stop ZooKeeper
cmd = zk.stop().wait()
print 'Name: {}  Before: {} Result: {}'.format(zk.name.ljust(15),zk.serviceState.ljust(13),cmd.success)

# Stop HDFS
cmd = hdfs.stop().wait()
print 'Name: {}  Before: {} Result: {}'.format(hdfs.name.ljust(15),hdfs.serviceState.ljust(13),cmd.success)

