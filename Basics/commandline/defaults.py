import argparse

parser = argparse.ArgumentParser(description="Using defaults in args")
parser.add_argument("-b", action='store') # action ='store' is the default
parser.add_argument('-n', action='store_const', const="PYpy") # not expecting value
parser.add_argument('-j', default="Jack")
parser.add_argument('-v', '--verbose', default=False, action='store_const', const=True)

parser.add_argument('-v2', action='store_const', const=True)
parser.add_argument('-q', '--quiet', action='store_false')
parser.add_argument('-q2', action='store_const', const=False, default=True)
parser.add_argument('-t', action='store_true')
args = parser.parse_args()
print(args)