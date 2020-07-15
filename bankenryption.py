#######################################################################################################
#       This code for encrypt the bank reuests data
#######################################################################################################

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import requests

BANK_URL =  ''

def generate_keys():
    modulus_length = 1024

    key = RSA.generate(modulus_length)
    #print (key.exportKey())

    pub_key = key.publickey()
    #print (pub_key.exportKey())

    return key, pub_key

def encrypt_private_key(a_message, private_key):
    encryptor = PKCS1_OAEP.new(private_key)
    encrypted_msg = encryptor.encrypt(a_message)
    print(encrypted_msg)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    print(encoded_encrypted_msg)
    return encoded_encrypted_msg

def decrypt_public_key(encoded_encrypted_msg, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    print(decoded_encrypted_msg)
    decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
    print(decoded_decrypted_msg)
    #return decoded_decrypted_msg



def share_my_public_key(site_public_key):
    private, public = generate_keys()
    write_private_key(private)
    write_site_pub_key(site_public_key)
    return public


###################################################3
#   FOR THE SITE PRIVATE KEY
###################################################
def write_private_key(p):
    p.export_key()

def read_private_key():
    f = open('private_key','r')
    p= f.read()
    f.close()
    return p


###################################################3
#   FOR THE SITE BANK PUBLIC KEY
###################################################
def write_site_pub_key(p):
    p.exportKey()

def read_site_pub_key():
    f = open('site_public_key','r')
    p= f.read()
    f.close()
    return p
