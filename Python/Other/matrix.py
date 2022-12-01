def foo(N):
    matrix = []
    for i in range(N):
        row = []
        cnt = i
        for j in range(N):
            if i <= j:
                row.append(cnt)
                cnt += 1
                
            else:
                row.append(0)
        matrix.append(row)
    return matrix


for row in foo(6):
    print(*row)