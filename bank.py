import json
from firebase import get_account_cvv
def verify_account(data):
    account = json.loads(data)
    acc= account['cc_number']
    check_account(acc)

def check_account(acc):
   res = get_account_cvv(acc)
   print(res)
   if res['stat'] =='exist':
       print("ready to send data")

