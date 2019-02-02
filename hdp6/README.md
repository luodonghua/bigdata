Steps and repo files for HDP lab installation

1. Install preprequsites packages
```bash
yum install -y yum-utils
yum install -y zip unzip
```
2. Install MySQL Repo
```bash
rpm -ihv https://github.com/luodonghua/bigdata/blob/master/hdp6/mysql80-community-release-el7-2.noarch.rpm?raw=true
yum repolist all | grep mysql|grep enabled
yum-config-manager --disable mysql80-community
yum-config-manager --enable mysql57-community
yum repolist all | grep mysql|grep enabled
yum install -y mysql-community-server
systemctl start mysqld
grep 'temporary password' /var/log/mysqld.log
mysql -u root -p
```

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'N0t_ThisPassWd';

create database ambari DEFAULT CHARACTER SET utf8;
create user 'ambari'@'%' IDENTIFIED BY 'N0t_ThisPassWd';
grant all on *.* TO 'ambari'@'%';

create database druid DEFAULT CHARACTER SET utf8;
create user 'druid'@'%' IDENTIFIED BY 'N0t_ThisPassWd';
grant all on druid.* TO 'druid'@'%';

create database hive DEFAULT CHARACTER SET utf8;
create user 'hive'@'%' IDENTIFIED BY 'N0t_ThisPassWd';
grant all on hive.* TO 'hive'@'%';

create database oozie DEFAULT CHARACTER SET utf8;
create user 'oozie'@'%' IDENTIFIED BY 'N0t_ThisPassWd';
grant all on oozie.* TO 'oozie'@'%';

create database ranger DEFAULT CHARACTER SET utf8;
create user 'rangeradmin'@'%' IDENTIFIED BY 'N0t_ThisPassWd';
grant all on *.* TO 'rangeradmin'@'%' WITH GRANT OPTION;

create user 'rangeradmin'@'localhost' IDENTIFIED BY 'N0t_ThisPassWd';
grant all on *.* TO 'rangeradmin'@'localhost' WITH GRANT OPTION;

create database rangerkms DEFAULT CHARACTER SET utf8;
create user 'rangerkms'@'%' IDENTIFIED BY 'N0t_ThisPassWd';
grant all on *.* TO 'rangerkms'@'%';
```


3. Install Java and JDBC
```bash
yum install jdk-8u201-linux-x64.rpm
mkdir /usr/share/java
wget -O /usr/share/java/mysql-connector-java.jar https://github.com/luodonghua/bigdata/blob/master/hdp6/mysql-connector-java-5.1.47.jar?raw=true
```
