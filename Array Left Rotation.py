def array_left_rotation(a, n, k):
    b=[0]*n
    for i in range(n):
        b[i-k]=a[i]
    return(b)

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
