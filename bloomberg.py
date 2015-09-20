import boto3
from boto3.dynamodb.conditions import Key
import pprint
from sets import Set
import datetime

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.
_db = boto3.resource('dynamodb', region_name='us-east-1')
_table = _db.Table('2014')
START_TIME = "2012-01-01"

def getIndexData(ticker, end):
    data = _table.query(KeyConditionExpression=Key('Ticker').eq(ticker) & Key('Date').between(START_TIME, end))
    return data['Items']

def getTickers():

	item_list = _table.scan()['Items']
	tickerSet = Set()
	#Populate tickerSet with existing ticker values
	for triple in item_list:
		tickerSet.add(str(triple['Ticker']))

	return sorted(list(tickerSet))                           

def buildDateValueList(data):
	date_list = [triple['Date'] for triple in data['Items']]
	value_list = [float(triple['Value']) for triple in data['Items']]

	return zip(date_list,value_list)

def getValueAtDate(date):
	timeValueList = buildDateValueList(date)
	for tuple in timeValueList:
		if str(tuple[0]) == str(date):
			return str(tuple[1])


def getCurrentTimeData(end_time):
	current_date = datetime.today()
	# future_date = end_time
	future_date = current_date + timedelta(days=10)
	date_diff = abs((future_date - current_date).days)

	start_time = "2012-01-01"

	timeModel = {}
	for x in range(0, date_diff):
		timeModel[current_date] = getValueAtDate(start_time)
		current_date + timedelta(days=1)
		start_time + timedelta(days=1)

	return timeModel








