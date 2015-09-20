import boto3
from boto3.dynamodb.conditions import Key
import pprint
from sets import Set
from datetime import date, datetime, timedelta

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.
_db = boto3.resource('dynamodb', region_name='us-east-1')
_table = _db.Table('2014')
START_TIME = "2009-01-01"
END_TIME = "2015-06-17"

def getIndexData(ticker, start, end_time):
    data = _table.query(KeyConditionExpression=Key('Ticker').eq(ticker) & Key('Date').between(START_TIME, END_TIME))
    remappedData = remapData(data, end_time)
    return remappedData

def remapData(data, end_time):
	remappedData = []
	remappedTempDict = {}
	(date_list, date_diff) = getDateList(end_time)

	x = 0
	print date_list
	for dictionary in data['Items']:
		remappedTempDict = dictionary
		print remappedTempDict['Date'] 
		if x < date_diff-1:
			x = x + 1
		else:
			break	
		remappedTempDict['Date'] = date_list[x]
		print x
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
	# future_date = end_time
	future_date = current_date + timedelta(days=10)
	date_diff = abs((future_date - current_date).days)

	# timeModel = }
	for x in range(0, date_diff):
		# timeModel[current_date] = getValueAtDate(start_time)
		date_list.append(str(current_date.year) + "-" + str(current_date.month) + "-" + str(current_date.day))
		current_date = current_date + timedelta(days=1)
	return (date_list, date_diff)








