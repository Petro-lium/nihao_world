#По данному целому числу N распечатайте все квадраты натуральных (целых, положительных) чисел,
#не превосходящие N, в порядке возрастания. Обратите внимание, что если N является полным квадратом,
#то его тоже нужно печатать.
n = int(input())
s = 1
k = 0
while k < n:
    if k > 0:
        print(k)
    k = s*s
    s = s + 1
