# d = {'a': 2, 'z': 4, 'r': 3 }
# # print(d)

# def fun(**kvpairs):
#     for pair in kvpairs.items():
#         print(pair)

# fun(x=3, a=8, z=2)


# d = 1_00_0000
# e = 3_1
# print(d, e)
# print(int('0xf_fff', 16))
# print(0xfc_a)
# print("{:_}".format(20000000))

# print("{:,}".format(20000000))

# print("{:X}".format(14))
# print("{:_X}".format(28787871))

# # f string
# word = 'Gloria'
# count = 12.234
# print(f'{word} shines {count:.2f}')

import random
random.seed(0)
for _ in range(10):
    print(random.randint(10, 20))