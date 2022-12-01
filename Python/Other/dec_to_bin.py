def decimal_to_binary(num):
    bin_arr = []

    while num != 0:
        bin_arr.append(str(num%2))
        num = num//2

    return ''.join(bin_arr[::-1]) if len(bin_arr) > 0 else 0

print(decimal_to_binary(510))

def binary_to_decimal(n):
    x = []
    
    for i in range(len(n)):
        if int(n[::-1][i]) == 1:
            x.append(2 ** i)
    
    return sum(x)


print(binary_to_decimal('1001001101'))

