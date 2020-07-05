from flask import Flask
from gen_fake_data import generate_account_info
from firebase import store_account
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def hello_world():
    return generate_account_info()


@app.route('/api/gen/<uid>',methods=['GET','POST'] )
def store_fire_base(uid):
    store_account(uid,generate_account_info())
    return "succeed"

if __name__ == '__main__':
    app.run(debug=True)
