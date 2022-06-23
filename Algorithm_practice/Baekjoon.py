from sys import stdin

a = list(stdin.readline().split(" "))

for i in a:
    if int(i) % 5 == 0:
        print(i)
        break
