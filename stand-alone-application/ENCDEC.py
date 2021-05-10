# import crypto
# import sys
# sys.modules['Crypto'] = crypto
import binascii
import os
import time
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from secretsharing import PlaintextToHexSecretSharer
from secretsharing import SecretSharer


BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]


def shamirs_split(file_object):
	text = file_object.read()
	list = PlaintextToHexSecretSharer.split_secret(text,2,2)
	hexcode = SecretSharer.split_secret(list[0][2:],2,2);
	return hexcode,list[1]


def shamirs_join(list,str):
	temp = []
	msg_alpha =  SecretSharer.recover_secret(list[0:2])
	msg_alpha = '1-'+msg_alpha
	temp.append(msg_alpha)
	temp.append(str)
	text = PlaintextToHexSecretSharer.recover_secret(temp[0:2])
	return text


def iv():
    
    return chr(0) * 16

class AESCipher(object):

    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, iv())
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')
