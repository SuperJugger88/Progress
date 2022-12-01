from distutils.spawn import spawn


def romanToInt(roman):
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    last, total = 0, 0
    for i in roman[::-1]:
        if last > values[i]:
            total -= values[i]
        else:
            total += values[i]
        last = values[i]
    return total   

def readFromFile():
    with open('123.txt') as file:
        return file.read()

print(readFromFile())