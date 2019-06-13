import argparse

parser = argparse.ArgumentParser(description="Print square and cubes")
parser.add_argument('--sq', help='list of numbers ot square', nargs='*', type=float) # nargs= * means 0 or more args
parser.add_argument("--cu", help='list of numbers to cube', nargs='+', type=float, required=True) # nargs= + means atleast 1 arg

args = parser.parse_args()

if args.sq:
    squares = [x ** 2 for x in args.sq]
    print(squares)

cubes = [y ** 3 for y in args.cu]
print(cubes)