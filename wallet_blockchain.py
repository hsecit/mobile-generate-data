import json

from bitcoinaddress import Address, Key, Wallet


def blockchain_address():
    """
    this function generate the wallet address
    :return:
    """
    key = Key()
    key_dict = key.generate()
    address = Address(key)
    address_dict = address.generate()
    return {
        "private_key": key_dict,
        "pair_pub_addr": address_dict
    }


def blockchain_wallet():
    wallet = Wallet()
    return wallet
