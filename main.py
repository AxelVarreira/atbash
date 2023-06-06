#!/usr/bin/python3

import base64;

from Crypto.Cipher import Blowfish;
from Crypto.Random import get_random_bytes;

# Tentando entender Python e Blowfish
class BlowfishHelper():
    def __init__(self, key=None):
        if key == None:
            self.key = get_random_bytes(32)
        else:
            self.key = key
    def encrypt(self, message):
        message = message.encode("utf-8")
        cipher = Blowfish.net(self.key, Blowfish.MODE_CBC);