import sys

keys = sys.argv[1::2] # means start at 1, go to the end, go in steps of 2

li = [x for x in range(30)][1::3]
# print(li)

values = sys.argv[2::2]

# print(tuple(zip(keys,values)))

args = {k: v for (k, v) in zip(keys, values)}
print(args)

first_name = args.get('-fn')
sec_name = args.get('-sn')