import boto3, json

session = boto3.Session(profile_name='development')
east = 'us-east-1'
west = 'us-west-2'

ec2Client = session.client('ec2', region_name = east)

ec2Resource = session.resource('ec2', region_name = region)
