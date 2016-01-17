from p59message import *

# print msg

words = set(['the', 'and'])



def decrypt(key, msg):
    result = 0
    idx = 0
    for letter in msg:
        # print key[idx]
        result += (key[idx] ^ letter)
        if idx == len(key) - 1:
            idx = 0
        else:
            idx += 1
    return result

# print decrypt([103, 111, 100], msg)

# def solver():
#     for letter1 in range(97, 123):
#         for letter2 in range(97, 123):
#             for letter3 in range(97, 123):
#                 message = decrypt([letter1, letter2, letter3], msg)
#                 if ' and ' in message or ' the ' in message:
#                     print letter1, letter2, letter3, message






# print solver()


