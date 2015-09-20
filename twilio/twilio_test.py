from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACdc7d2a4a98d67f7782feb96c317666e7" 
AUTH_TOKEN = "8f7e2fb53338185baa8309ee1fb8cadc" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="+16476099168", 
	from_="+15817004128", 
	body="You need to buy index NOWWWW",  
)

