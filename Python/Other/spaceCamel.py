import time

# # my solution

# def spaceCamel(s):
#     for i in s:
#         if i.isupper():
#             s = s.replace(i, ' '+i)
#     return ''.join(s.split('  '))

# print(spaceCamel('helloMyFuckingNiger'))

# # correct solution

# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

start = time.time()

def combination(x):
    return len(set(x)) ** len(x)
    
print(combination('AAB'))
print("--- {0} seconds ---".format(time.time() - start))
