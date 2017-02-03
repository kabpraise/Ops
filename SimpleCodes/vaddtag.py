'''
Supply region-name (e.g. ap-southeast-2), vpcid itself and tag value 
(will be set into EnvType tag key) as three arguments
e.g. $python vaddtag.py ap-southeast-2 vpc-xxxxxxx TEST
will create tag EnvType with value "TEST" for all volumes associated
with the instances in that particular vpc with vpcid supplied as argument
N.B. need to have access credentials (aws_access_key_id and 
aws_secret_access_key) present in .aws/credentials file.
'''

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
