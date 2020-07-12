import pyrebase
import requests
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

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
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=data,
                  headers={'Content-type': 'application/json'})

    db= fire.database()
    ref = db.child("BlockChain").child("transactions")
    ref.push(data)

# db = fire.database()

# ref = db.child("accounts").child("B4id8gbVZIapozFPKUye972iSEm2").get()
# t= ref.val()

# t1 = t.items()

# key,value=list(t1)
# print(key)