from twilio.rest import Client 
 

# removed authorisation
client = Client(account_sid, auth_token) 


def send_message(sentence):

  message = client.messages.create( 
#                               from_= removed phone number,  
                              body=sentence,      
#                               to='whatsapp removed phone number' 
                          ) 
 
