#!/usr/bin/python
import sys
import boto3

regionname = "us-west-2"
vpcid = "vpc-46a9a023"

ec2client = boto3.client("ec2", regionname)
ec2 = boto3.resource('ec2', region_name=regionname)
vpc = ec2.Vpc(vpcid)



for i in vpc.instances.all():
        ec2instance = ec2.Instance(str(i.id))
        print ec2instance.tags
        for tags in ec2instance.tags:
                if tags['Key'] == "solr" or tags['Key'] == "zk":
                        ec2client.stop_instances(InstanceIds=[str(i.id),])
