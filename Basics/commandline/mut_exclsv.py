import argparse

parser = argparse.ArgumentParser(description="mutually exclusive")

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true')
group.add_argument('-q', '--quiet', action='store_true')


parser.add_argument('-n', type=complex, required=True)

# args = parser.parse_args()
# print(args)

d= {'a': 3, 1:8, 2:2}
l = [3, 3]

parser2 = argparse.ArgumentParser(description="You are dead or alive")
group2 = parser2.add_mutually_exclusive_group()
group2.add_argument("--alive", action='store_true')
group2.add_argument("--dead",action='store_true')

parser2.add_argument('-d', const=d.pop('a'), nargs="?")
parser2.add_argument('-d2', action='store_const', const=l.append(4))
print(d)
print(l)
args2 = parser2.parse_args()

print(args2)