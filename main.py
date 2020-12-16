from submit_to_dialog_flow import *
from chatdaddy import *
from process_response import *
from time import sleep
from new_flow import *
from chat_manager import *
from kol import *
import json
from use_google_sheet import *
from secrets import *

if __name__ == '__main__':
  new_covid_chat_manager = NewCovidChatManager()
  new_covid_chat_manager.run()