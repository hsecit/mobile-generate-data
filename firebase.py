import pyrebase

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
    

# db = fire.database()

# ref = db.child("accounts").child("B4id8gbVZIapozFPKUye972iSEm2").get()
# t= ref.val()

# t1 = t.items()

# key,value=list(t1)
# print(key)