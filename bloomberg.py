import boto3
from boto3.dynamodb.conditions import Key
import pprint
from sets import Set
from datetime import date, datetime, timedelta
import time

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.
db = boto3.resource('dynamodb', region_name='us-east-1')
_table = db.Table('2014')
START_TIME = "2009-01-01"
END_TIME = "2015-06-17"

def getIndexData(ticker, start, end_time):
	y = list()
	data = dict()
	for x in range (2014, 2015):           
		table = db.Table(str(x))
    	temp_data = table.query(KeyConditionExpression=Key('Ticker').eq(ticker) & Key('Date').between(START_TIME, END_TIME))
    	y.extend(temp_data['Items'])
	data['Items'] = y
	remappedData = remapData(data, end_time)
	return remappedData

def remapData(data, end_time):
	remappedData = []
	remappedTempDict = {}
	(date_list, date_diff) = getDateList(end_time)

	x = 0
	for dictionary in data['Items']:
		remappedTempDict = dictionary
		print date_diff
		if x < date_diff-1:
			x = x + 1
		else:
			break	
		remappedTempDict['Date'] = date_list[x]
		remappedData.append(remappedTempDict)
		remappedTempDict = {}
	return remappedData		

def getTickers():
	item_list = _table.scan()['Items']
	tickerSet = Set()
	#Populate tickerSet with existing ticker values
	for triple in item_list:
		tickerSet.add(str(triple['Ticker']))

	return sorted(list(tickerSet))                           

def getModelIndexValues(data, date_diff):
	modelIndexValues = []
	count = 0
	timeValueList = buildDateValueList(data)

	for tuple in timeValueList:
		while date_diff > count:
			modelIndexValues.add(str(tuple[1]))
			date_diff = date_diff -1
	return modelIndexValues


def buildDateValueList(data):
	date_list = [triple['Date'] for triple in data['Items']]
	value_list = [float(triple['Value']) for triple in data['Items']]
	return zip(date_list,value_list)


def getDateList(end_time):
	current_date = datetime.today()
	date_list=[]
	end_time = datetime.strptime(str(end_time), "%Y-%m-%d")
	future_date = end_time
	date_diff = abs((future_date - current_date).days)

	for x in range(0, date_diff):
		date_list.append(str(current_date.year) + "-" + str(current_date.month) + "-" + str(current_date.day))
		current_date = current_date + timedelta(days=1)
	return (date_list, date_diff)








