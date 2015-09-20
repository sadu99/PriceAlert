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
table = db.Table('2012')
data = table.query(KeyConditionExpression = Key('Ticker').eq('UKRPI Index') & Key('Date').eq('2012-06-30'))
print data['Items']
print ""
for items in data['Items']:
	print items.Date


# def days_between(future_date, current_date):
#     future_date = datetime.strptime(future_date, "%Y-%m-%d")
#     current_date = datetime.strptime(current_date, "%Y-%m-%d")
#     return abs((future_date - current_date).days)

current_date = datetime.today()
# date_1 = datetime.strptime(current_date, "%Y-%m-%d")
future_date = current_date + timedelta(days=10)
print future_date

diff = abs((future_date - current_date).days)
print diff

print str(current_date.year) + "-" + str(current_date.month) + "-" + str(current_date.day) 




