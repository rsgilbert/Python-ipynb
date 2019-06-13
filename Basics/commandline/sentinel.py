_sentinel = object() # you create an object in memory, no other object can go to that same memory address

# def validate(a=_sentinel):
#     print(validate.__defaults__)
#     if a is not _sentinel: # compare memory addresses
#         print("arg was provided")
#     else:
#         print("arg NOT provided")


# def validate(a=object()):
#     if a is not validate.__defaults__[0]: # compare memory addresses
#         print("arg was provided")
#     else:
#         print("arg NOT provided")


# validate()
# validate(3)
# validate(None)


def validate(a=object(), b=object(), *, kword=object()):
    a_default = validate.__defaults__[0]
    b_default = validate.__defaults__[1]
    kword_default = validate.__kwdefaults__['kword']

    if(a_default is a):
        print("A default NOT provided")
    else: 
        print("A default provided")

    if(b_default is b):
        print("B default NOT provided")
    else: 
        print("B default provided")
   
    if(kword_default is kword):
        print("kword default NOT provided")
    else: 
        print("kword default provided")


# validate(3, kword=8)
# validate(8, 2)
# validate()


# using sentinel value, less advisable
sentinel = '-x99'
def sent_validate(a=sentinel):
    if a == sentinel: # compare memory addresses
        print("arg NOT provided")
    else:
        print("arg provided")

sent_validate(33)
sent_validate()