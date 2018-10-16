import json
import argparse

def convertType(type):
        if type=="long":
                return "bigint"
        else:
                return type

def gen_columns(schema):
        ret = "(" + "\n,".join(['%s %s' % (field['name'],convertType(field['type'])) for (field) in schema['fields']]) + ")"
        return ret

def gen_tblprops(schema):
        ret = "tblproperties ("+"\n"
        if schema["comment"] != "":
            ret += '  "comment"="'+schema["comment"]+'"'+"\n"
        else:
            ret += '  "comment"="' + schema["name"]+'"'+"\n"

        if schema["header"]=="yes":
            ret += '  ,"skip.header.line.count"="1"'+"\n"

        if schema["classification"] != "":
            ret += '  ,"classification"="'+schema["classification"]+'"'+"\n"

        if schema["pii"] != "":
            ret += '  ,"pii"="'+schema["pii"]+'"'+"\n"

        if schema["source"] != "":
                ret += '  ,"source"="'+schema["source"]+'"'+"\n"

        if schema["steward"] != "":
                ret += '  ,"steward"="'+schema["steward"]+'"'+"\n"

        return ret+")"


parser = argparse.ArgumentParser(description='Generate a create external table DDL that includes column definitions from a given Avro schema')
parser.add_argument('table_name',help='Name of Hive table');
parser.add_argument('location',help='HDFS path that contains table data');
parser.add_argument('--partitions',help='If creating a partitioned table, specify the partitions');

args = parser.parse_args();

with open('Data/'+args.table_name+'.schema','r') as schema_file:
    schema_obj = json.load(schema_file)

if args.partitions:
        partitions = "partitioned by (" + args.partitions + " string)"
else:
        partitions = ""

print("""create external table %s
%s
%s --table parition specification if paritition
row format delimited fields terminated by ','
stored as textfile
location '%s'
%s
;""" % (args.table_name,gen_columns(schema_obj),partitions,args.location,gen_tblprops(schema_obj)))