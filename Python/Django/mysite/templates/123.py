s = input()

odds, evens = [], []

# for i in list(s.replace(' ', '')):
#     if int(i) % 2 != 0:
#         odds.append(i)
#     else:
#         evens.append(i)

# print(*(odds + evens[::-1]))

sorted_arr = list(map(lambda x : odds.append(x) if int(x) % 2 !=0 else evens.extend(x), list(s.replace(' ', ''))))
print(*(odds + evens[::-1]))
