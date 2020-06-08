# MongoDB Quick Guide

## Install

64 bits

```console
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/```

32 bits

Instalação em Ubuntu 18.04 32 bits

```console
https://gkbrown.org/2016/03/31/installing-mongodb-on-32-bit-ubuntu-15-10/```

It will crash with systemcl restart. Please, use:

```console
$ sudo kill -9 PID
$ sudo /etc/init.d/mongod start
```

After changing configuration file:

```console
/etc/mongodb.conf```


## Directories and files

Data

```console
/var/lib/mongodb```

Log

```console
/var/log/mongodb```

Configuration

```console
/etc/mongod.conf```


## Command line

MongoDB Client accessing localhost


```console
$ mongo

> show dbs
> use <dbname>
> show collections```

Show all items

```console
> db.<collection-name>.find({})```

Insert one item

```console
db.<collection-name>.insertOne({"name": "John", "age": 42})```

Delete all

```console
db.<collection-name>.deleteMany({})```

## DB Management

Creates backup local dir ./dump

```console
$ mongodump```

Restores backup from local dir ./dump

```console
$ mongorestore```

## Monitoring

```console
$ mongostat

insert query update delete getmore command flushes mapped  vsize   res faults qr|qw ar|aw netIn netOut conn                      time
    *0    *0     *0     *0       0     1|0       0 240.0M 682.0M 85.0M      0   0|0   0|0   79b    12k    1 2020-06-08T15:47:26-03:00
    *0    *0     *0     *0       0     1|0       0 240.0M 682.0M 85.0M      0   0|0   0|0   79b    12k    1 2020-06-08T15:47:27-03:00
    *0    *0     *0     *0       0     1|0       0 240.0M 682.0M 85.0M      0   0|0   0|0   79b    12k    1 2020-06-08T15:47:28-03:00
    *0    *0     *0     *0       0     1|0       0 240.0M 682.0M 85.0M      0   0|0   0|0   79b    12k    1 2020-06-08T15:47:29-03:00
```

```console
$ mongotop

ns    total    read    write    2020-06-08T15:49:25-03:00
admin.system.roles      0ms     0ms      0ms                             
admin.system.version      0ms     0ms      0ms                             
db_01.persons      0ms     0ms      0ms                             
db_01.system.indexes      0ms     0ms      0ms                             
db_01.system.namespaces      0ms     0ms      0ms                             
db_test_bk.persons      0ms     0ms      0ms                             
db_test_bk.system.indexes      0ms     0ms      0ms                             
db_test_bk.system.namespaces      0ms     0ms      0ms                             
local.startup_log      0ms     0ms      0ms                             
local.system.indexes      0ms     0ms      0ms
```
## Logging

/etc/mongod.conf

```console
verbosity: 5```

## Version History

https://stackoverflow.com/questions/3507624/mongodb-nosql-keeping-document-change-history

# References

https://api.mongodb.com/python/current/tutorial.html

https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
