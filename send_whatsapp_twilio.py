from twilio.rest import Client 
from secrets import * 

client = Client(account_sid, auth_token) 


def send_message(sentence):

  message = client.messages.create( 
                              from_= phone_number_1,  
                              body=sentence,      
                              to= phone_number_2 
                          ) 
 
