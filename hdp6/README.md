Steps and repo files for HDP lab installation

1. Install preprequsites packages
yum install -y yum-utils
yum install -y zip unzip

1. Install MySQL Repo
rpm -ihv https://github.com/luodonghua/bigdata/blob/master/hdp6/mysql80-community-release-el7-2.noarch.rpm?raw=true
yum repolist all | grep mysql|grep enabled
yum-config-manager --disable mysql80-community
yum-config-manager --enable mysql57-community
yum repolist all | grep mysql|grep enabled
yum install -y mysql-community-server
