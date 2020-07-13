import json
import random

from faker import Faker
from hashlib import sha256
from wallet_blockchain import blockchain_address


def random_digits(number):
    """
    generate a number with length given in parameter
    :param number:
    :return:
    """
    start = 10 ** (number - 1)
    end = (10 ** number) - 1
    return random.randint(start, end)


# the result function
def generate_account_info():
    """
    generate some random data for virtual account
    :return:
    """
    f = Faker()
    data = {
        "nom": f.name(),
        "phone": f.phone_number(),
        "address": f.address(),
        "bank_account_number": str(random_digits(24)),
        "wallet": blockchain_address()
    }
    #return json.dumps(data)
    return data

def generate_one_time_password():
    digit = str(random_digits(8)).encode('utf8')
    hash_ = sha256(digit).hexdigest()
    return hash_

