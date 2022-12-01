# def findPrime(x):
#     nums = list(range(2,x))
#     primes = []
#     for prime in nums:
#         if all(prime%i!=0 for i in range(2,prime)):
#             primes.append(prime)
#     return primes

# print(findPrime(101))

for num in range(2,101):
    prime = True
    for i in range(2,num):
        if num%i==0:
            prime = False
    if prime:
        print(num,end=' ')



# for n in range(2, 10):
#      for x in range(2, n):
#          if n % x == 0:
#              print(n, 'equ  als', x, '*', n//x)
#              break
#      else:
#          # loop fell through without finding a factor
#          print(n, 'is a prime number')


