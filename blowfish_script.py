import argparse, blowfish
from os import urandom

from validators import validate_arguments

parser = argparse.ArgumentParser()

parser.add_argument("--a", "--Action", help="Actions: decrypt or encrypt file")
parser.add_argument("--k", "--Key", help="Actions: key to encrypt or decrypt file")
parser.add_argument("--f", "--File", help="Actions: File to be encrypt or decrypt")

args = parser.parse_args()
vector = b'c\xab\xeb\xc7\xdd\xff.\xa4'

validate_arguments.validate_arguments(args.k, args.a, args.f)

cipher = blowfish.Cipher(args.k.encode('utf-8'))

match args.a:
    case "decrypt":
        with open(args.f, 'rb') as fb:
            linesBytes = fb.read()
        decryptedText = b"".join(cipher.decrypt_ofb(linesBytes, vector))

        with open(args.f, "w") as fw:
            fw.write(decryptedText.decode('utf-8'))

    case "encrypt":
        with open(args.f) as f:
            lines = f.read()

        encondedText = (lines.encode('utf-8'))
        cipherText = b"".join(cipher.decrypt_ofb(encondedText, vector))

        path = args.f.split(".txt")
        with open(f"{path[0]}_crypto.txt", "wb") as fw:
            fw.write((cipherText))
