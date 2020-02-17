# Выведите таблицу размером n×n,
# заполненную числами от 1 до n^2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке
n = int(input())
a = []
s = 0
m = 0
for i in range(n):
    a.append([0]*n)
while n > n // 2:
    for i in range(m, n, 1):
        for j in range(m, n, 1):
            if i > m:
                break
            else:
                s += 1
            a[i][j] = s
    for j in range(n - 1, m - 1, -1):
        for i in range(m + 1, n, 1):
            if j < n - 1:
                break
            else:
                s += 1
            a[i][j] = s 
    for i in range(n - 1, m - 1, -1):
        for j in range(n - 2, m - 1, -1):
            if i < n - 1:
                break
            else:
                s += 1
            a[i][j] = s
    for j in range(m, n - 1, 1):
        for i in range(n - 2, m, -1):
            if j > m:
                break
            else:
                  s += 1
            a[i][j] = s
    m += 1
    n -= 1       
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()