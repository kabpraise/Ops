#!/usr/bin/python
import sys
import boto3

regionname = str(sys.argv[1])
vpcid = str(sys.argv[2])
tagvalue = str(sys.argv[3])

ec2client = boto3.client("ec2", regionname)
ec2 = boto3.resource('ec2', region_name=regionname)
vpc = ec2.Vpc(vpcid)
j = 0

print ("Please wait while tagging is completed for all volumes!!!\n")

for i in vpc.instances.all():
	volumes = i.volumes.all()
	for v in volumes:
		#print(v.id)
		v.create_tags(
                Tags=[
                	{
                        	'Key': 'EnvType',
                        	'Value': tagvalue
                        },
                ]
        	)
		j = j+1

print (str(j) + " volumes were tagged as EnvType: " + tagvalue)
