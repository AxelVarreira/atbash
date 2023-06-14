import argparse

from services.atbash_cipher import AtbashCipher
from validators import validate_arguments

# Adiciona os parametros necessarios pro Script
parser = argparse.ArgumentParser()
parser.add_argument("--a", "--Action", help="Actions: decrypt or encrypt file")
parser.add_argument("--f", "--File", help="Actions: File to be encrypt or decrypt")

# Faz o parse dos parametros inserios
args = parser.parse_args()

# Valida os parametros inserios
validate_arguments.validate_arguments(args.a, args.f)

# Instancia o atbash cipher
cipher = AtbashCipher()

# Verifica o parametro passado no script se é pra Criptografar ou descriptografar
match args.a:
    case "decrypt":
        # Lê o arquivo passado como parametro
        with open(args.f, 'r') as fb:
            linesBytes = fb.read()

        #Faz a descriptografia
        decryptedText = cipher.execute(linesBytes)

        # Escreve de volta no arquivo passado
        with open(args.f, "w", encoding="utf-8") as fw:
            fw.write(decryptedText)

    case "encrypt":
        # Lê o arquivo passado como parametro
        with open(args.f, "r", encoding="utf-8") as f:
            lines = f.read()

        #Faz a criptografia
        cipherText = cipher.execute(lines)

        # Cria um arquivo novo com o nome passado no "script+_crypto" e grava a cifra
        path = args.f.split(".txt")
        with open(f"{path[0]}_crypto.txt", "w") as fw:
            fw.write(str(cipherText))
