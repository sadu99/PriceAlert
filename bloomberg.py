import boto3
from boto3.dynamodb.conditions import Key

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.
_db = boto3.resource('dynamodb', region_name='us-east-1')
_table = _db.Table('2012')

def getIndexData(ticker, start, end):
    data = _table.query(KeyConditionExpression=Key('Ticker').eq(ticker) & Key('Date').between(start, end))
    return data['Items']
