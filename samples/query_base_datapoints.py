#!/usr/bin/env python

import boto3
import pprint
from boto3.dynamodb.conditions import Key, Attr
from sets import Set
# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.

AWS_REGION = 'us-east-1'

db = boto3.resource('dynamodb',
                    region_name = AWS_REGION)
                                        
item_list = []

TABLE_NAME = '2014'
START_YEAR = '2005'
END_YEAR = '2014' #End of the year
TICKER = 'LMEXZS Index'

temp_table = db.Table(TABLE_NAME)
item_list.extend(temp_table.scan()['Items'])

#Initialize set of tickers
tickerSet = Set()
#Populate tickerSet with existing ticker values
for triple in item_list:
	tickerSet.add(triple['Ticker'])

tickerList = sorted(list(tickerSet))

#Print the list of tickers
pprint.pprint(tickerList)

#How we query shit
data = temp_table.query(KeyConditionExpression = Key('Ticker').eq(TICKER) & Key('Date').between(START_YEAR + '-01-01', END_YEAR + '-06-30'))
pprint.pprint(data['Items'])




