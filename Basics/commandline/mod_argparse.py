import argparse

parser = argparse.ArgumentParser(description="Testing argparse")
parser.add_argument("subject", help="the subject to learn", type=str)
parser.add_argument("teacher", help="teacher of the subject", type=str)
parser.add_argument("code", help="subject code", type=int)


args = parser.parse_args(['29', '33', '88'])
print(args.subject)
print(args.teacher)
print(args.code)

args = parser.parse_args()
print(args, type(args))

a = args.subject