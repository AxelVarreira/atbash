import argparse, blowfish

from validators import validate_arguments


parser = argparse.ArgumentParser()

parser.add_argument("--a", "--Action", help="Actions: decrypt or encrypt file")
parser.add_argument("--k", "--Key", help="Actions: key to encrypt or decrypt file")
parser.add_argument("--f", "--File", help="Actions: File to be encrypt or decrypt")

args = parser.parse_args()

validate_arguments.validate_arguments(args.k, args.a, args.f)



cipher = blowfish.Cipher(b"{args.k}")

match args.a:
    case "decrypt":
        with open(args.f, 'rb') as fb:
            linesBytes = fb.read()
        decryptedText = cipher.decrypt_block(linesBytes)
        print(decryptedText.decode("utf-8"))

    case "encrypt":
        with open(args.f) as f:
            lines = f.read()

        encondedText = lines.encode('utf-8')
        cipherText = cipher.encrypt_block(encondedText)

        path = args.f.split(".txt")
        with open(f"{path[0]}_crypto.txt","xb") as fw:
            fw.write(cipherText)
