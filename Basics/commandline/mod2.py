import sys

# numbers = [int(a) for a in sys.argv[1:]]

for i in range(1, len(sys.argv), 2):
    print(sys.argv[i], sys.argv[i+1])