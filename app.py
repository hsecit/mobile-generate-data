from flask import Flask,request
from gen_fake_data import generate_account_info
from firebase import store_account,store_BlockChain_Transaction,store_Bank_Transaction,verify_account
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    return generate_account_info()


@app.route('/api/gen/<uid>',methods=['GET','POST'] )
def store_fire_base(uid):
    store_account(uid,generate_account_info())
    return "succeed"


@app.route('/api/blockchain/transaction',methods=['POST'])
def get_blockchain_transaction():
    store_BlockChain_Transaction(request.get_json())
    return "succes"



@app.route('/api/bank/transaction',methods=['POST'])
def get_bank_transaction():
    store_Bank_Transaction(request.get_json())
    return "succes"
@app.route('/api/bank/check_card',methods=['post'])
def get_data_bank_to_check():
    data = request.get_data()
    print(verify_account(data))
    return verify_account(data)


if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
