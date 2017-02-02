'''

Supply region-name (e.g. ap-southeast-2), vpcid itself and tag value 
(will be set into EnvType tag key) to be set as three arguments
It will replace new line with comma
And output will be in filelocation/filename-out
e.g. $python addtag.py ap-southeast-2 vpc-xxxxxxx TEST
will create tag EnvType with value "TEST" for all EC2 instances
which are in the vpc with vpcid supplied as argument

N.B. need to have access credentials (aws_access_key_id and 
aws_secret_access_key) present in .aws/credentials file.

'''


#!/usr/bin/python
import sys
import boto3

def tagresources(resourceID, tagValue):
	response = ec2client.create_tags(
		Resources=[
			resourceID,
		],
		Tags=[
	  		{
				'Key': 'EnvType',
				'Value': tagValue
			},
		]
	)

regionname = str(sys.argv[1])
vpcid = str(sys.argv[2])
tagvalue = str(sys.argv[3])

ec2client = boto3.client("ec2", regionname)
ec2 = boto3.resource('ec2', region_name=regionname)
vpc = ec2.Vpc(vpcid)
j = 0


print ("Please wait while tagging is completed for all instances!!!\n")

for i in vpc.instances.all():
	tagresources(str(i.id),tagvalue)
	j = j+1

print (str(j) + " instances were tagged as EnvType: " + tagvalue)
