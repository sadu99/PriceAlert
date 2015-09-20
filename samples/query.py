#!/usr/bin/env python

import boto3
from boto3.dynamodb.conditions import Key
from datetime import date, datetime, timedelta

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.
AWS_REGION = 'us-east-1'
db = boto3.client('dynamodb', region_name = AWS_REGION)

print "Printing all Tables..."
tables = db.list_tables()
print tables['TableNames']
print ""

print "Describing a Table..."
table = db.describe_table(TableName = '2012')
print table['Table']['KeySchema']
print ""

AWS_REGION = 'us-east-1'
db = boto3.resource('dynamodb', region_name = AWS_REGION)

print "Requesting Data from Table..."    
y = list()
data = dict()
tuples = {}
for x in range (2005, 2015):           
	table = db.Table(str(x))
	temp_data = table.query(KeyConditionExpression = Key('Ticker').eq('UKRPI Index'))
	y.extend(temp_data['Items'])
	print "Printing once..."
	print y
print ""
print "Printing Big Table..."
data['Items'] = y
print data
print ""






