## hdfs


access_logs_raw = sc.textFile("/data/access.log")
access_logs_raw.take(3)
df = access_logs_raw.filter(lambda x:len(x)>1). \
    map(lambda x:(x[:14].strip(),x[16:21].strip(),x[22:].split(' ')[0],x[22:].split(' ')[1],\
                    x[22:].split(' ')[3],x[22:].split(' ')[4],x[22:].split(' ')[5], \
                    x[22:].split(' ')[6],x[22:].split(' ')[7],x[22:].split(' ')[7])).toDF()
df.show(3)
df.printSchema()
# df.write.mode('overwrite').parquet('/data/access_parquet_default')
# df.write.mode('overwrite').orc('/data/access_orc_default')
df.write.mode('overwrite').parquet('/data/access_parquet_none',compression='none')
df.write.mode('overwrite').parquet('/data/access_parquet_uncompressed',compression='uncompressed')
df.write.mode('overwrite').parquet('/data/access_parquet_snappy',compression='snappy')
df.write.mode('overwrite').parquet('/data/access_parquet_gzip',compression='gzip')
df.write.mode('overwrite').orc('/data/access_orc_none',compression='none')
df.write.mode('overwrite').orc('/data/access_orc_snappy',compression='snappy')
df.write.mode('overwrite').orc('/data/access_orc_zlib',compression='zlib')
df.write.mode('overwrite').orc('/data/access_orc_lzo',compression='lzo')

# df.write.mode('overwrite').parquet('file:///Users/donghua/Downloads/access_parquet_lzo',compression='lzo')
# df.write.mode('overwrite').parquet('file:///Users/donghua/Downloads/access_parquet_brotli',compression='brotli')
# df.write.mode('overwrite').parquet('file:///Users/donghua/Downloads/access_parquet_lz4',compression='lz4')
# df.write.mode('overwrite').parquet('file:///Users/donghua/Downloads/access_parquet_zstd',compression='zstd')


df = spark.read.option('inferSchema','true').csv("/data/http.log",sep='\t')
df.printSchema()
df.show(5)
df.write.mode('overwrite').parquet('/data/http_parquet_default')
df.write.mode('overwrite').parquet('/data/http_parquet_none',compression='none')
df.write.mode('overwrite').parquet('/data/http_parquet_uncompressed',compression='uncompressed')
df.write.mode('overwrite').parquet('/data/http_parquet_snappy',compression='snappy')
df.write.mode('overwrite').parquet('/data/http_parquet_gzip',compression='gzip')
df.write.mode('overwrite').orc('/data/http_orc_default')
df.write.mode('overwrite').orc('/data/http_orc_none',compression='none')
df.write.mode('overwrite').orc('/data/http_orc_snappy',compression='snappy')
df.write.mode('overwrite').orc('/data/http_orc_zlib',compression='zlib')
df.write.mode('overwrite').orc('/data/http_orc_lzo',compression='lzo')
