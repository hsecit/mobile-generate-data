import pyrebase
import requests
import json
import requests
from gen_fake_data import generate_one_time_password
CONNECTED_NODE_ADDRESS = 'http://192.168.1.5:8000'

# init firebase
conf = {
    "apiKey": "AIzaSyDi8BQjZHM0l2n1tEX5DukmyE0jQ2kctEQ",
    "authDomain": "cryptography-project-12233.firebaseapp.com",
    "databaseURL": "https://cryptography-project-12233.firebaseio.com",
    "projectId": "cryptography-project-12233",
    "storageBucket": "cryptography-project-12233.appspot.com",
    "messagingSenderId": "801611067749",
    "appId": "1:801611067749:web:19e03a535319b18cb7718c",
    "measurementId": "G-LSEMCCBFPT"
}
fire = pyrebase.initialize_app(conf)


def store_account(uid, account_info):
    db = fire.database()
    ref = db.child("accounts").child(uid)
    ref.push(account_info)



def store_Bank_Transaction(data):
    db= fire.database()
    ref = db.child("Bank").child("transactions")
    ref.push(data)

def store_BlockChain_Transaction(data):
    new_tx_address = "{}/new_transaction".format("http://192.168.1.5:8000")
    requests.post(new_tx_address,
                  json=data,
                  headers={'Content-type': 'application/json'})

    db= fire.database()
    ref = db.child("BlockChain").child("transactions")
    ref.push(data)

def database():
    return fire
# db = fire.database()

# ref = db.child("accounts").child("B4id8gbVZIapozFPKUye972iSEm2").get()
# t= ref.val()

# t1 = t.items()

# key,value=list(t1)
# print(key)

def get_account_cvv(cc):
    db = fire.database()
    ref = db.child("accounts").get()
    keys_uid = []
    obj_id = []
    for uid in ref.each():
        keys_uid.append(uid.key())
    for ui in keys_uid:
        ref2 = db.child("accounts").child(ui).get()
        for h in ref2.each():
            obj_id.append(h.key())

    for ui in keys_uid:
        for h in obj_id:
            r = db.child("accounts").child(ui).child(h).child("bank_account_number").get()
            if r.val() == cc:
                return {"stat":"exist"}




def verify_account(data):
    account = json.loads(data)
    acc= account['cc_number']
    return check_account(acc)

def check_account(acc):
   db = fire.database()
   ref = db.child("2fact-auth")
   res = get_account_cvv(acc)
   genn = generate_one_time_password()
   print(res)
   if res['stat'] =='exist':
       ref.push({'one_time-code': genn})
       return {'one_time-code': genn}