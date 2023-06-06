# This is a sample Python script.

import sys, getopt

argumentList = sys.argv[1:]

# Opcoes que tu podera passar na hora de rodar o script. eg: python3 main.py -a
options = "hmka:"

long_options = ["Help", "File", "Key", "Action"]

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-h", "--Help"):
            print("Welcome stranger!\n")
            print("to run this script you need to run: \n")
            print("# python3 main.py <arquivo de texto> <chave de cifragem> <decrypt ou incrypt>")

        elif currentArgument in ("-m", "--File"):
            print("Displaying file_name:", sys.argv[0])

        elif currentArgument in ("-o", "--Output"):
            print(("Enabling special output mode (% s)") % (currentValue))

        elif currentArgument in ("-k", "--Key"):
            if len(currentValue) == 0:
                raise ValueError("Chave nao pode estar vazia!")

        elif currentArgument in ("-a", "--Action"):
            if currentValue != "decrypt" or currentValue != "encrypt":
                raise ValueError("Valores de acao invalidos")

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
