#### File created:
```bash
gzip access.log
split -b 15m access.log.gz access.log.gz-

gzip http.log
split -b 15m http.log.gz http.log.gz-
```



#### How to uncompress the data
```bash
cat access.log.gz-a* |gunzip > access.log
cat http.log.gz-a* |gunzip > http.log
```

