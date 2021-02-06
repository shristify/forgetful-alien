from twilio.rest import Client 
from credentials import *

twi=sender      #twilio sandbox
me=receiver   #receiving contact number
account_sid = accountsid
auth_token = authtoken
client = Client(account_sid, auth_token)
        
def send_mess(text1):    
    message = client.messages.create( 
                          from_=twi,  
                          to=me,
                          body=text1
                          )
    print(message.sid)
