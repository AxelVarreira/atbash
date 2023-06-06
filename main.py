# This is a sample Python script.

import sys, getopt, argparse

from validators import validate_arguments


parser = argparse.ArgumentParser()

parser.add_argument("--a", "--Action", help="Actions: decrypt or encrypt file")
parser.add_argument("--k", "--Key", help="Actions: key to encrypt or decrypt file")
parser.add_argument("--f", "--File", help="Actions: File to be encrypt or decrypt")

args = parser.parse_args()

validate_arguments.validate_arguments(args.k, args.a, args.f)

