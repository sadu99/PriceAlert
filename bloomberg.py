import boto3
from boto3.dynamodb.conditions import Key
import pprint
from sets import Set

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.
_db = boto3.resource('dynamodb', region_name='us-east-1')
_table = _db.Table('2014')

def getIndexData(ticker, start, end):
    data = _table.query(KeyConditionExpression=Key('Ticker').eq(ticker) & Key('Date').between(start, end))
    return data['Items']

def getTickers():

	item_list = _table.scan()['Items']
	tickerSet = Set()
	#Populate tickerSet with existing ticker values
	for triple in item_list:
		tickerSet.add(str(triple['Ticker']))

	return sorted(list(tickerSet))                           
