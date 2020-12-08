from flask import Flask, render_template, request, redirect
import json
import requests
from twilio.twiml.messaging_response import MessagingResponse
from submit_to_dialog_flow import *
from send_whatsapp import * 

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
  incoming_msg = request.values.get('Body', '').lower()
#   resp = MessagingResponse()
#   msg = resp.message()
  response = submit(incoming_msg)
  send_message(response['result']['fulfillment']['speech'])
  return 'none'
  
@app.route('/home', methods=['GET'])
def home():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)


 