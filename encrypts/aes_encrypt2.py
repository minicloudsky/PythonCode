from Crypto import Random
from Crypto.Cipher import AES
import random

def get_encryption():
    try:
        strmsg = "This is input string"

        key = 'abcdefghijklmnop'
        key1 = str.encode(key)

        iv = Random.new().read(AES.block_size)

        obj = AES.new(key1, AES.MODE_CBC, iv)
        encrypted = obj.encrypt(str.encode(strmsg))
        print(encrypted)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    get_encryption()